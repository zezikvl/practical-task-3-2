def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    while 1 > 0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if '@' not in recipient and '@' not in sender:
                print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
                break
        else:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
            break
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
            break
        elif sender == 'university.help@gmail.com':
            print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
            break
        else:
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
            break

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')