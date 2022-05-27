import os
import logging
from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Chat import ChatPresence
from TwitchChannelPointsMiner.classes.Discord import Discord
from TwitchChannelPointsMiner.classes.Telegram import Telegram
from TwitchChannelPointsMiner.classes.Settings import Priority, Events, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Bet import Strategy, BetSettings, Condition, OutcomeKeys, FilterCondition, DelayMode
from TwitchChannelPointsMiner.classes.entities.Streamer import Streamer, StreamerSettings

twitch_miner = TwitchChannelPointsMiner(
    username="",
    password="",           
    claim_drops_startup=False,                  
    priority=[                                  
        Priority.STREAK,                        
        Priority.DROPS,                         
        Priority.ORDER                          
    ],
    logger_settings=LoggerSettings(
        save=True,                              
        console_level=logging.INFO,             
        file_level=logging.DEBUG,               
        emoji=True,                             
        less=False,                             
        colored=True,                           
        color_palette=ColorPalette(             
            STREAMER_online="GREEN",            
            streamer_offline="red",             
            BET_wiN=Fore.MAGENTA                
        ),
        telegram=Telegram(                                                          
            chat_id=123456789,                                                      
            token="123456789:shfuihreuifheuifhiu34578347",                          
            events=[Events.STREAMER_ONLINE, Events.STREAMER_OFFLINE, "BET_LOSE"],   
            disable_notification=True,                                              
        ),
        discord=Discord(
            webhook_api="https://discord.com/api/webhooks/0123456789/0a1B2c3D4e5F6g7H8i9J",  
            events=[Events.STREAMER_ONLINE, Events.STREAMER_OFFLINE, Events.BET_LOSE],       
        )
    ),
    streamer_settings=StreamerSettings(
        make_predictions=True,                  
        follow_raid=True,                       
        claim_drops=True,                       
        watch_streak=True,                      
        chat=ChatPresence.ONLINE,               
        bet=BetSettings(
            strategy=Strategy.SMART,            
            percentage=5,                       
            percentage_gap=20,                  
            max_points=50000,                   
            stealth_mode=True,                  
            delay_mode=DelayMode.FROM_END,      
            delay=6,
            minimum_points=20000,               
            filter_condition=FilterCondition(
                by=OutcomeKeys.TOTAL_USERS,     
                where=Condition.LTE,            
                value=800
            )
        )
    )
)

port = int(os.environ.get('PORT', 5000))
twitch_miner.analytics(host="0.0.0.0", port=port, refresh=5)   # Analytics web-server
twitch_miner.mine(
    [
        Streamer("sashizinha", settings=StreamerSettings(make_predictions=False  , follow_raid=True , claim_drops=True  , watch_streak=True , bet=BetSettings(strategy=Strategy.SMART      , percentage=5 , stealth_mode=True,  percentage_gap=20 , max_points=234   , filter_condition=FilterCondition(by=OutcomeKeys.TOTAL_USERS,      where=Condition.LTE, value=800 ) ) )),
        Streamer("scrubnoob", settings=StreamerSettings(make_predictions=False  , follow_raid=True , claim_drops=True  , watch_streak=True , bet=BetSettings(strategy=Strategy.SMART      , percentage=5 , stealth_mode=True,  percentage_gap=20 , max_points=234   , filter_condition=FilterCondition(by=OutcomeKeys.TOTAL_USERS,      where=Condition.LTE, value=800 ) ) )),
    ],                                  
    followers=False,                    
    followers_order=FollowersOrder.ASC  
)
