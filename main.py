import telebot

# Halkaan geli token-ka botkaaga
TOKEN = "7790991731:AAF4NHGm0BJCf08JTdBaUWKzwfs82_Y9Ecw"
bot = telebot.TeleBot(TOKEN)

# Tir dhammaan commands-ka
bot.delete_my_commands()

print("✅ Dhamaan commands-ka waa la tirtiray!")
