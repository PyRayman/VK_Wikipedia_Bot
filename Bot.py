import vk_api
import wikipediaapi
import json
import time
import random
from Token import token

bot = vk_api.VkApi(token = token)

while True:

	message = bot.method('messages.getConversations',{'offset':0,'count':20,'filter':'unread'})
	
	if message['count'] >= 1:
		id = message['items'][0]['last_message']['from_id']
		#bot.method('messages.send',{'peer_id':id,'message':'Input a page name',"random_id":random.randint(1,9223372036854775807)})
		user_page = message['items'][0]['last_message']['text']
		
		wiki_object = wikipediaapi.Wikipedia(
			language = 'ru', # Your Language 
			extract_format = wikipediaapi.ExtractFormat.WIKI
		)
		page = wiki_object.page(user_page.replace(' ','_'))
		

		if page.exists() == True:
			bot.method('messages.send',{'peer_id':id,'message':str(page.title),"random_id":random.randint(1,9223372036854775807)})
			bot.method('messages.send',{'peer_id':id,'message':str(page.text[0:4001]),"random_id":random.randint(1,9223372036854775807)})
			if len(page.text) > 4000:
				bot.method('messages.send',{'peer_id':id,'message':page.text[4001:8000],"random_id":random.randint(1,9223372036854775807)})
			bot.method('messages.send',{'peer_id':id,'message':'Link to the full page: ' + page.fullurl,"random_id":random.randint(1,9223372036854775807)})
			
		else:
			bot.method('messages.send',{'peer_id':id,'message':'The name is incorrect!',"random_id":random.randint(1,9223372036854775807)})
