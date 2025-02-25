import telebot
from openai import OpenAI
TOKEN = '7813587250:AAHAKzLEUBAB8wEO3hSsUkFXQK5AaeFvTqw'
bot = telebot.TeleBot(TOKEN)
base_url = 'https://api.aimlapi.com/v1'

api_key = '31b33472c40d42e0a90aa12f31c5f17c'
system_prompt = 'You are simple chat gpt. Just answer questions of user'
api = OpenAI(api_key = api_key, base_url = base_url)
def get_ai_response(prompt):
  completion = api.chat.completions.create(
    model = 'mistralai/Mistral-7B-Instruct-v0.2',
    messages = [
      {"role" : "system", "content" : system_prompt},
      {"role" : "user", "content" : prompt},
    ],
    temperature = 0.7,
    max_tokens = 256,
  )
  response = completion.choices[0].message.content
  return response

@bot.message_handler()
def start_message(message):
  response = get_ai_response(message.text)
  bot.send_message(message.chat.id, response)

bot.polling()
