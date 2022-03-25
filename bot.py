TOKEN = '5231657153:AAGeSuyB8NMVrDu2euevoIlQuP2Vej6qcwM'
from telegram import Update,Bot
from telegram.ext import CallbackContext
from telegram.ext import (Updater,CommandHandler,MessageHandler,MessageFilter,
Filters)
from telegram.utils.request import Request

import requests

from bs4 import BeautifulSoup




def dictio(word):
  
  try:
      working_word = word
      base_url = 'https://www.merriam-webster.com/dictionary/'
      url = base_url+word
      r = requests.get(url)
      soup = BeautifulSoup(r.content, 'html.parser')
      match = soup.find('span',class_='dtText')
      meaning = match.text.replace(":",'')
      # print(f'** Meaning of the { word}')
      # print('')
      phrase = ''
      phrases = soup.find_all('div',class_="related-phrases-list-item")
      for index,items in enumerate(phrases) :
        phrase+=(f'{index+1}-{items.text}')
        phrase+='\n'

      etymo =soup.find('p',class_="et")
      return (f'✅{word}:\n\n {meaning}\n\n\n✅history of {word} : \n\n{etymo.text.strip()}\n\n✅with {word} :\n\n---------------\n{phrase}\n\nmade by ❤️@atmilad')
    
  except:
    return (f'the word ( {word} ) Not fonud in my dictionary')
      
  






def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="hi ! just give me a word and i will give you meaning , ethymology and callocations of the word")

start_handler = CommandHandler('start', start)


def message_handler(update,context):
  text= update.message.text
 
  update.message.reply_text(dictio(text))


def main():
  req = Request(connect_timeout = 0.5)
  t_bot = Bot(request=req,token = TOKEN)
  updater = Updater(bot = t_bot ,use_context = True)    
  dp = updater.dispatcher
  dp.add_handler(start_handler)
  dp.add_handler(MessageHandler(filters = Filters.all,callback =     
  message_handler))  
  updater.start_polling()
  updater.idle()





if __name__=='__main__':
   main()
  