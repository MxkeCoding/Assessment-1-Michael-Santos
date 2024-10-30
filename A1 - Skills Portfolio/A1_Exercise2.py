import random  # Import random module to select a random joke

def load_jokes(filename=r"C:\Users\m1kee\OneDrive\Documents\CODELAB-2--A1\A1 - Skills Portfolio\A1 - Resources\randomJokes.txt"):
    # Load jokes from the specified file and return a list of jokes
    jokes = []
    with open(filename, "r") as file:  # Open the jokes file in read mode
        for line in file:
            setup, punchline = line.strip().split('?')  # Split each line by the question mark
            jokes.append((setup + '?', punchline))  # Store the setup and punchline as a tuple
    return jokes  # Return the list of jokes

def tell_joke(jokes):
    # Select and present a random joke
    joke = random.choice(jokes)  # Choose a random joke from the list
    print("\n" + joke[0])  # Display the setup part
    input("Press Enter to hear the punchline...")  # Wait for user input
    print(joke[1] + "\n")  # Display the punchline

def main():
    # Main function to run the joke-telling program
    jokes = load_jokes()  # Load the jokes from the file
    while True:  # Loop to allow repeated requests for jokes
        user_input = input("Type 'Alexa tell me a Joke' or 'quit' to exit: ").strip().lower()
        if user_input == "alexa tell me a joke":  # Check if user requested a joke
            tell_joke(jokes)  # Call function to tell a random joke
        elif user_input == "quit":  # Check if user wants to quit
            print("Goodbye!")  # Say goodbye
            break  # Exit the loop to end the program
        else:
            print("Invalid command. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Run the main function
