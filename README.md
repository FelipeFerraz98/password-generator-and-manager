# Password Generator and Manager

This is a Python program that allows you to generate custom passwords based on user preferences and also manage these passwords by saving them in a JSON file.

The program has two main features:

1 Password Generator: Allows the user to generate passwords based on their preferences for length and type. Password type options include:

* just letters
* Numeric
* alphanumeric
* Letters + special characters
* Numeric + special characters
* Alphanumeric + special characters

The user can choose the minimum password length and the desired type. After generating a password, you can save the password to a list for later use or discard it. The program allows you to generate multiple passwords and, when finished, all saved passwords can be stored in a JSON file.

2 Password Manager: Allows the user to manually save passwords to a JSON file, search for passwords in existing files, and view saved passwords. The user can choose from the following options:

* Manually Save Passwords: The user can manually enter the passwords they want to save and provide a name for the file where they will be stored.
* Search a password: User can select an existing file and view all passwords saved in it.
* Exit Manager: Closes the password management program.

## Requirements

Python 3.x

## How to use
1 Download or clone the program repository.

2 Make sure you have Python 3.x installed on your system.

3 Run the main.py file using the following command:

    python main.py

4 Follow the instructions provided by the program to generate and manage passwords.

## Files

* main.py: Contains the main function of the program, where the user can choose between the Password Generator and the Password Manager.
* algorithm.py: Contains logic to generate passwords based on user preferences.
* manager.py: Contains the functions to save, search and read passwords in JSON files.

## Contribution
Contributions are welcome! If you encounter a problem, have a suggestion, or want to improve the code, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

