from telebot import TeleBot
from content import number8

bot = TeleBot("7000706075:AAHcBlYKrkDR1eUCIiMOstJa-vSOMX7b8Xk")
data = {}

@bot.message_handler(commands=["start"])
def wellcome(message):
    data[message.chat.id] = ""
    bot.send_message(message.chat.id, "Халоо, это бот на проверку знаний по №8 ОГЭ по русскому\n/test чтобы начать")


@bot.message_handler(commands=["test"])
def handler(massage):
    try:
        data[massage.chat.id] = {"chance" : 0}
        process(massage)

    except:
        bot.send_message(massage.chat.id, "Почему то не получилось тебя добавить в базу...")


def process(message):
    try:
        _, answer = number8[data[message.chat.id]["chance"]]
        proposal, _ = number8[data[message.chat.id]["chance"] + 1]
        if message.text.lower() == answer.lower():
            bot.send_message(message.chat.id, "✅правильно")
        else:
            bot.send_message(message.chat.id, f"☠{answer}")
        data[message.chat.id]["chance"] += 1
        bot.send_message(message.chat.id, proposal)
        bot.register_next_step_handler(message, process)

    except:
        bot.send_message(message.chat.id, "Всё.")


bot.polling()
