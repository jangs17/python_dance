def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

x = get_integer_input("What's x? ")
y = get_integer_input("What's y? ")

if x < y: # Boolean Expression
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
