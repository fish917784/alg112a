import random

def display_message(message):
    print(message)

def main():
    answer = [random.randint(0, 9) for _ in range(4)]
    guess = [None] * 4
    length = 0

    while True:
        if length < 4:
            print("Enter Number:", end=" ")

            try:
                number = int(input())
            except ValueError:
                print("Invalid input. Please enter a digit.")
                continue

            if number not in range(10):
                print("Invalid input. Please enter a digit between 0 and 9.")
                continue

            if number in guess[:length]:
                print("You have already guessed that number. Try again.")
                continue

            guess[length] = number
            length += 1

        else:
            a, b = 0, 0

            for i in range(4):
                for j in range(4):
                    if i == j and answer[i] == guess[j]:
                        a += 1

                    if i != j and answer[i] == guess[j]:
                        b += 1

            if a == 4:
                display_message("YOU WIN!")
                break
            else:
                display_message(f"{a}A {b}B")
                length = 0

if __name__ == "__main__":
    main()
