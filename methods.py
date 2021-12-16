from googletrans import Translator


def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salom, hush kelibsiz, marxamat matn kiriting!")

def translate(matn):
    translator = Translator()
    natija = translator.translate(matn, src='auto', dest='en')
    return natija.text
    

def xabar(update,context):
    matn=update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=translate(matn))



