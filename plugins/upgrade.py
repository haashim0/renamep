"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """<b>**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1** 
	Upload  limit 20GB/per day
	Price ð®ð³ 40â¹/ð 0.52$  per Month
	
	**VIP 2**
	Upload limit 50GB/per day
	Price ð®ð³ 80â¹/ð 1.00$  per Month
	
	**VIP 3**
	Unlimited Daily Upload â/per day
	Price ð®ð³ 150â¹/ð 1.85$  per Month
	
	
	Pay Using Upi I'd ```655365838@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN ð",url = "https://t.me/haashim_999")], 
        			[InlineKeyboardButton("Paytmð°",url = "https://p.paytm.me/xCTH/dtvlquzy")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """<b>**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Upload  limit 20GB/per day
	Price ð®ð³ 40â¹/ð 0.52$  per Month
	
	**VIP 2**
	Upload limit 50GB/per day
	Price ð®ð³ 80â¹/ð 1.00$  per Month
	
	**VIP 3**
	Unlimited Daily Upload â/per day
	Price ð®ð³ 150â¹/ð 1.85$  per Month
	
	
	Pay Using Upi I'd ```655365838@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN ð",url = "https://t.me/haashim_999")], 
        			[InlineKeyboardButton("Paytmð°",url = "https://p.paytm.me/xCTH/dtvlquzy")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
