def main():
    while True:
        name = input("What's your first name? ")
        surname = input("What's your surname? ")
        if name.isalpha():  # Check if the input consists only of alphabetic characters
            name = name.capitalize()  # Capitalize the first letter of the first name
            surname = surname.capitalize()
            hello(name, surname)  # Passes the name (input from user) to the hello function.
            break
        else:
            print("Please enter a valid name.")

def hello(first_name, last_name):  # hello accepts two parameters.
    print("hello,",first_name, last_name)

main()  # Calls the main function to start the program
