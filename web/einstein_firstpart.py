from typing import Any
import telebot, requests, re, os

token = '1151315588:AAEM1I6Go3NGKzcyBxW3plj1kgft_jpVZZ0'

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start', 'help', 'info'])
def get_text_messages(message):
  if message.text == '/start':
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True, True)
    keyboard.row('info', 'help')
    bot.send_message(message.chat.id, 'Привет! Я — Альберт Эйнштейн. Ты можешь задать мне любой вопрос, а я постараюсь на него ответить! Надеюсь, что мы подружимся!', reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def answer_to_text(message):
  user = message.from_user.id
  if message.text.lower() == 'start':
    bot.send_message(message.chat.id, 'Привет! Я — Альберт Эйнштейн. Ты можешь задать мне любой вопрос, а я постараюсь на него ответить! Надеюсь, что мы подружимся!') 
  elif message.text.lower() == 'info':
    bot.send_message(message.chat.id, 'Обожаю GEEK PICNIC, но я на нём лишь гость! Если у тебя возникли вопросы по поводу организации мероприятия, ты можешь найти ответы здесь: https://www.online.geekpicnic.me/faq')
  elif message.text.lower() == 'help':
    bot.send_message(message.chat.id, 'Когда будешь задавать свой вопрос, не забудь поставить "?", надеюсь, что тебе понравится общаться со мной!')


def main():
    new_offset = 0
    print('launching...')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    bot.polling(none_stop=True, interval=0)

