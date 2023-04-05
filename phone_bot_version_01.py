from functools import wraps

contacts = {
    'Igor': '+38068123123689',
    'Vitalia': '+21394819032489'
}


def input_error(func):
    @wraps(func)
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError) as exc:
            result = f"An error occurred: {str(exc)}"
            return result
    return wrapper


def help(*args):
    return """"hello", відповідає у консоль "How can I help you?"
"add ...". За цією командою бот зберігає у пам'яті новий контакт.
"change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту.
"phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
"show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!"."""


def hello(*args):
    return 'Hello, how can I help you?'


@input_error
def add_func(*args):
    name = args[0].split()[0]
    number = args[0].split()[1]
    contacts[name] = number
    return f'U add contact with name : {name.title()} and his number is : {number}'


@input_error
def change_contacts_dict(*args):
    name = args[0].split()[0]
    number = args[0].split()[1]
    if name in contacts:
        contacts[name] = number
        return f'you have changed the number to this one: {number} in the contact with the name: {name.title()}'
    return f"Contact with this {name} doesn't exists"


@input_error
def phone_func(*args):
    name = args[0].split()[0]
    return contacts[name]


def show_all_func(*args):
    return "\n".join([f"{name.title()}: {phone}" for name, phone in contacts.items()])


def no_command(*args):
    return "Unknown command, try again."


OPERATION = {
    'hello': hello,
    'add': add_func,
    'change': change_contacts_dict,
    'phone': phone_func,
    'show': show_all_func
}

END_WORDS = ['good bye', 'close', 'exit']


def handle_command(user_input):
    for word, command in OPERATION.items():
        if user_input.startswith(word):
            return command, user_input.replace(word, '').strip()
    return no_command, None


def main():
    print(help())
    while True:
        user_input = input("Write what u wont from bot >>> ").lower()
        if user_input in END_WORDS:
            print("Good bye!")
            break
        command, data = handle_command(user_input)
        print(command(data))


if __name__ == '__main__':
    main()
