def calculateAverage(s1, s2, s3):
    # Add them up and divide by 3
    avg = (s1 + s2 + s3) / 3
    # Round to 2 decimal places as required
    return round(avg, 2)


def getLetterGrade(average):
    # Standard grading scale logic
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def getAcademicStanding(letter):
    # Match the letter to the standing description
    if letter == "A":
        return "Excellent"
    elif letter == "B":
        return "Good"
    elif letter == "C":
        return "Satisfactory"
    elif letter == "D":
        return "Needs Improvement"
    else:
        return "Failing"


def main():
    print("--- Test Score Calculator ---")

    # Getting inputs one by one
    score1 = float(input("Enter first test score: "))
    score2 = float(input("Enter second test score: "))
    score3 = float(input("Enter third test score: "))

    # Basic validation check
    if (score1 < 0 or score1 > 100) or (score2 < 0 or score2 > 100) or (score3 < 0 or score3 > 100):
        print("Error: All scores must be between 0 and 100.")
    else:
        # Call the functions and store results
        final_avg = calculateAverage(score1, score2, score3)
        final_letter = getLetterGrade(final_avg)
        final_standing = getAcademicStanding(final_letter)

        # Display results to the user
        print("\n--- Results ---")
        print("Average score:", final_avg)
        print("Letter grade:", final_letter)
        print("Academic Standing:", final_standing)


# Run the program
main()