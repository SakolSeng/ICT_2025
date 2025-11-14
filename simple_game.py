import random

def number_guessing_game():
    """A simple number guessing game."""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    
    # Set difficulty
    print("\nChoose difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        max_number = 50
        difficulty = "Easy"
    elif choice == "2":
        max_number = 100
        difficulty = "Medium"
    elif choice == "3":
        max_number = 500
        difficulty = "Hard"
    else:
        print("Invalid choice! Setting to Medium.")
        max_number = 100
        difficulty = "Medium"
    
    # Generate random number
    secret_number = random.randint(1, max_number)
    attempts = 0
    max_attempts = 10
    
    print(f"\nDifficulty: {difficulty}")
    print(f"I'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}!")
                attempts -= 1
                continue
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempt(s)!")
                break
            elif guess < secret_number:
                print(f"❌ Too low! Try a higher number. ({max_attempts - attempts} attempts left)")
            else:
                print(f"❌ Too high! Try a lower number. ({max_attempts - attempts} attempts left)")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            attempts -= 1
    else:
        print(f"\n😢 Game Over! The number was {secret_number}.")
    
    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        print("\n")
        number_guessing_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    number_guessing_game()
