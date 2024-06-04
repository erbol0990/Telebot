import telebot
import random

# Инициализация бота
bot = telebot.TeleBot('6992045021:AAFIC-Xme5Wv-8LvRb_RXIDi5VDZ5i2zTt0')

# Словарь для хранения загаданных чисел для каждого пользователя
secret_numbers = {}

# Словарь для хранения количества попыток для каждого пользователя
attempts = {}

# Функция, которая будет вызываться при запуске команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Генерируем случайное число от 1 до 100 для текущего пользователя
    secret_numbers[message.chat.id] = random.randint(1, 100)
    attempts[message.chat.id] = 0  # Сброс счетчика попыток при начале игры
    bot.reply_to(message, "Привет! Я загадал число от 1 до 100. Попробуй угадать!")

# Функция, которая будет вызываться при получении текстового сообщения
@bot.message_handler(func=lambda message: True)
def guess_number(message):
    try:
        guess = int(message.text)
        secret_number = secret_numbers[message.chat.id]
        attempts[message.chat.id] += 1  # Увеличиваем счетчик попыток
        if guess < secret_number:
            bot.reply_to(message, "Загаданное число больше.")
        elif guess > secret_number:
            bot.reply_to(message, "Загаданное число меньше.")
        else:
            bot.reply_to(message, f"Поздравляю! Ты угадал число {secret_number} за {attempts[message.chat.id]} попыток.")
            attempts[message.chat.id] = 0  # Сброс счетчика попыток
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите целое число.")

# Главная функция
def main():
    bot.polling()

if __name__ == '__main__':
    main()
