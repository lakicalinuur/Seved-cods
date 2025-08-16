


import telebot
from flask import Flask, request

# Halkan ku qor token-kaaga toos
TOKEN = "7790991731:AAF4NHGm0BJCf08JTdBaUWKzwfs82_Y9Ecw"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Tir dhammaan commands-ka marka app la bilaabo
bot.delete_my_commands()
print("✅ Dhamaan commands-ka waa la tirtiray!")

# Endpoint webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    # render service URL halkan ku qor adiga
    bot.set_webhook(url=f"https://seved-cods.onrender.com/{TOKEN}")
    return "Webhook set", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
