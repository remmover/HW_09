# Contacts Management Program

This program is a simple contacts management system implemented in Python. It allows users to interact with a bot to perform various operations on a contacts dictionary, such as adding contacts, changing contact numbers, retrieving phone numbers, and displaying all contacts.

## Getting Started

To run the program, follow these steps:

1. Make sure you have Python installed on your system (version 3.6 or above).
2. Clone this repository or download the Python script file.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the following command to execute the program:

```shell
python contacts_management.py
```

## Usage

Once the program is running, you can interact with the bot by entering commands. The following commands are available:

- `hello`: Displays a greeting message from the bot.
- `add <name> <phone_number>`: Adds a new contact with the specified name and phone number to the contacts dictionary.
- `change <name> <new_phone_number>`: Changes the phone number of an existing contact with the specified name.
- `phone <name>`: Retrieves and displays the phone number of the contact with the specified name.
- `show all`: Displays all contacts and their phone numbers.
- `good bye`, `close`, `exit`: Exits the program and displays a goodbye message.

Please note that the name and phone number arguments should be provided without angle brackets (`<>`).

## Error Handling

The program includes error handling for common exceptions such as `KeyError`, `ValueError`, and `IndexError`. If any of these exceptions occur during the execution of a command, an error message will be displayed.

## Example

Here's an example interaction with the program:

```
Write what u want from the bot >>> hello
Hello, how can I help you?

Write what u want from the bot >>> add John +123456789
You added a contact with the name: John and his number is: +123456789

Write what u want from the bot >>> change John +987654321
You have changed the number to: +987654321 in the contact with the name: John

Write what u want from the bot >>> phone John
+987654321

Write what u want from the bot >>> show all
John: +987654321

Write what u want from the bot >>> good bye
Good bye!
```

## Contributing

Contributions to this project are welcome. If you find any issues or would like to suggest improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This program is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it according to your needs.
