import telepot
import time
from torrent_finder import FINDLINKS

bot = telepot.Bot('your token')

requests = {}
fiter ={}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id,"Hi! \nThis is torrent finder.\ntype what you want after that i will give you link for get that torrent.")

        elif msg['text'] == '/seemore':
            try:
                page = int(requests[chat_id][requests[chat_id].find("////")+4:])
                page=page+1
                requests[chat_id] = requests[chat_id][:requests[chat_id].find("////")+4]+str(page)
                FINDLINKS(requests[chat_id][:requests[chat_id].find("////")-1],0,page,chat_id)
            except:
                bot.sendMessage(chat_id,"what do you want to see more?")
        elif msg['text'] == '/filter':
            bot.sendMessage(chat_id,'what do you want to see?\nall\naudio\nvideo\napp\ngames\nporn\nother')
            bot.sendMessage(chat_id,'example: audio')
        elif msg['text'] == 'all':
            fiter[chat_id] = 0
            bot.sendMessage(chat_id, f'you filtered {msg["text"]}')
        elif msg['text'] == 'audio':
            fiter[chat_id] = 100
            bot.sendMessage(chat_id, f'you filtered {msg["text"]}')
        elif msg['text'] == 'video':
            fiter[chat_id] = 200
            bot.sendMessage(chat_id, f'you filtered {msg["text"]}')
        elif msg['text'] == 'app':
            fiter[chat_id] = 300
            bot.sendMessage(chat_id, f'you filtered {msg["text"]}')
        elif msg['text'] == 'games':
            fiter[chat_id] = 400
            bot.sendMessage(chat_id, f'you filtered {msg["text"]}')
        elif msg['text'] == 'porn':
            fiter[chat_id] = 500
            bot.sendMessage(chat_id, f'you filtered {msg["text"]}')
        elif msg['text'] == 'other':
            fiter[chat_id] = 600
            bot.sendMessage(chat_id,f'you filtered {msg["text"]}')
        else:
            requests[chat_id] = msg['text'] + '////' + "1"
            try:
                FINDLINKS(msg['text'],fiter[chat_id],1,chat_id)
            except:
                FINDLINKS(msg['text'], 0, 1, chat_id)


bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)