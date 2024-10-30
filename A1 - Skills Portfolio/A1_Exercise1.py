import random  # Import the random module to generate random numbers

def displayMenu():
    # Display the difficulty level menu for the user to choose
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

def randomInt(difficulty):
    # Generate a random integer based on the chosen difficulty level
    if difficulty == 1:  # Easy level, single-digit numbers
        return random.randint(1, 9)
    elif difficulty == 2:  # Moderate level, double-digit numbers
        return random.randint(10, 99)
    elif difficulty == 3:  # Advanced level, four-digit numbers
        return random.randint(1000, 9999)

def decideOperation():
    # Randomly select either addition or subtraction operation
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    # Display the problem to the user and return the correct answer
    answer = eval(f"{num1} {operation} {num2}")  # Calculate the correct answer
    print(f"{num1} {operation} {num2} = ", end='')  # Show the problem
    return answer  # Return the correct answer

def isCorrect(user_answer, correct_answer):
    # Check if the user's answer is correct
    return user_answer == correct_answer

def displayResults(score):
    # Display the user's final score and grade based on their score
    print("\nQuiz Complete!")
    print(f"Your final score: {score} / 100")  # Display score out of 100
    if score >= 90:  # Grade assignment
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"Your grade: {grade}")  # Display the assigned grade

def main():
    # Main function to control the quiz flow
    while True:  # Loop to allow replaying the quiz
        displayMenu()  # Show the difficulty menu
        difficulty = int(input("Choose your difficulty level (1-3): "))  # Get difficulty level
        
        score = 0  # Initialize score to 0
        for i in range(10):  # Loop for 10 questions in the quiz
            num1 = randomInt(difficulty)  # Generate first random number
            num2 = randomInt(difficulty)  # Generate second random number
            operation = decideOperation()  # Decide if it's addition or subtraction
            correct_answer = displayProblem(num1, num2, operation)  # Display the question and get the answer
            
            user_answer = int(input())  # Get user answer
            if isCorrect(user_answer, correct_answer):  # Check if the answer is correct
                print("Correct!")  # Inform the user of the correct answer
                score += 10  # Award 10 points for a first attempt correct answer
            else:
                print("Incorrect. Try again.")  # Give the user a second attempt
                user_answer = int(input())  # Get the second attempt answer
                if isCorrect(user_answer, correct_answer):  # Check second attempt
                    print("Correct!")  # Inform the user of the correct answer
                    score += 5  # Award 5 points for a second attempt correct answer
                else:
                    print("Wrong answer.")  # Inform the user if the answer is wrong again

        displayResults(score)  # Display the final score and grade
        
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()  # Ask if the user wants to play again
        if play_again != 'yes':  # Exit loop if the answer is not 'yes'
            break  # End the quiz if the user does not want to play again

if __name__ == "__main__":
    main()  # Start the quiz by calling the main function
