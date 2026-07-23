import telebot

TOKEN = 8239578701
ADMIN_ID = 123456789  # 5962242471

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! Zakaz berish uchun /zakaz ni bosing."
    )

@bot.message_handler(commands=['zakaz'])
def zakaz(message):
    bot.send_message(message.chat.id, "Nima zakaz qilmoqchisiz?")
    bot.register_next_step_handler(message, get_product)

def get_product(message):
    product = message.text
    bot.send_message(message.chat.id, "Ismingizni yozing:")
    bot.register_next_step_handler(message, lambda m: get_name(m, product))

def get_name(message, product):
    name = message.text
    bot.send_message(message.chat.id, "Telefon raqamingizni yozing:")
    bot.register_next_step_handler(
        message,
        lambda m: get_phone(m, product, name)
    )

def get_phone(message, product, name):
    phone = message.text
    bot.send_message(message.chat.id, "Manzilingizni yozing:")
    bot.register_next_step_handler(
        message,
        lambda m: send_order(m, product, name, phone)
    )

def send_order(message, product, name, phone):
    address = message.text

    order = f"""
Yangi zakaz:
Mahsulot: {product}
Ism: {name}
Telefon: {phone}
Manzil: {address}
"""

    bot.send_message(ADMIN_ID, order)
    bot.send_message(message.chat.id, "Zakazingiz qabul qilindi ✅")

bot.infinity_polling()