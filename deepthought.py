import re

def get_answer():
    while True:
        answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower()
        answer = re.sub(r'[^a-z0-9]', '', answer)  # Remove non-alphanumeric characters
        if answer == "42" or answer == "fortytwo":
            return "Yes"
        else:
            return "No"

def main():
    result = get_answer()
    print(result)

if __name__ == "__main__":
    main()


