dog = "@"
dom = [".com", ".ru", ".net"]
def validate_dog(text, smb):
    if smb not in text:
        return True
    else:
        return False

def validate_dom(text, smb):
    if not any(text.endswith(i) for i in smb):
        return True
    else:
        return False



def send_email(message, recipient, sender = "university.help@gmail.com"):
    if validate_dog(recipient, dog) or validate_dog(sender, dog) or validate_dom(recipient, dom) or validate_dom(sender, dom):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

