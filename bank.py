def check_greeting():
    greeting = input("Enter your greeting: ").strip().lower()
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

def main():
    result = check_greeting()
    print(f"Output: {result}")

if __name__ == "__main__":
    main()


