# Basic Chatbot

def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()   # take input and convert to lowercase
        
        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()  guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print("❌ Wrong guess! Attempts left:", attempts)

        print("Word:", display(word, guessed_letters))

        if "_" not in display(word, guessed_letters):
            print("🏆 You win! The word was:", word)
            break
    else:
        print("💀 Game over! The word was:", word)

# Run the game
hangman()