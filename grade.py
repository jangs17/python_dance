def get_score():
    while True:
        score_input = input("Enter the score (0-100): ")
        try:
            score = float(score_input)
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Additional check to prevent arrow keys and other non-numeric inputs
        if any(char.isalpha() for char in score_input):
            print("Non-numeric characters are not allowed.")
        elif score_input.strip() == "":
            print("Empty input is not allowed.")

def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 50 <= score < 60:  # Adjusted passing grade to 50%
        return "Pass"
    else:
        return "Fail"

def main():
    score = get_score()
    grade = calculate_grade(score)
    print(f"Grade: {grade} ({score:.2f})")

if __name__ == "__main__":
    main()








