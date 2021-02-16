class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def registration(line):
    try:
        name, email, age = line.split(' ')
    except ValueError:
        raise ValueError('Недостаточно данных')
    else:
        age = int(age)
        if not name.isalpha():
            raise NotNameError('Невозможное имя')
        elif '@' not in email or '.' not in email:
            raise NotEmailError('Невозможный email')
        elif age < 10 or age > 99:
            raise ValueError('Неправильный возраст')


with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            registration(line=line)
            with open('registrations_good.log', mode='a', encoding='utf8') as file:
                file.write(f'{line}\n')
        except (ValueError, NotNameError, NotEmailError) as exp:
            with open('registrations_bad.log', mode='a', encoding='utf8') as file:
                file.write(f'Ошибка {exp} в строке {line}\n')