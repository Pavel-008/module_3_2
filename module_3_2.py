



def send_email(message, recipient, sender = 'university.help@gmail.com'):
    variants = ('com', 'ru', 'net')
    if ('@' in recipient and '@' in sender and recipient.endswith(variants)
            and sender.endswith(variants)) and recipient != sender\
            and sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Писмо отправленно с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно оправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)


send_email(message = input('Введите сообщение: '),
           recipient = input('Введите Е-mail получателя: '),
           sender = input('Введите Е-mail отправителя: '))



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')













