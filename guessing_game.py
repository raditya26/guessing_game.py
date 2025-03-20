import random
import sys

def main():
    while True:
        try:
            level = int(input('Level: '))
            if level < 0:
                raise ValueError
            guess_game(level)
            break
        except ValueError:
            pass
        except EOFError:
            print()
            break

def guess_game(n):
    answer = random.randint(1, n)
    while True:
        try:
            user_answer = int(input("Guess: "))
            if user_answer < answer:
                print("Too small!")
                pass
            elif user_answer > answer:
                print("Too large!")
                pass
            else:
                sys.exit("Just right!")
                return
        except ValueError:
            pass

main()
