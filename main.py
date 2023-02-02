import asyncio
import re

from quiz import Quiz

def welcome() -> None:
    """
    Welcome message
    :return: None
    """
    print("\nLet's learn Regex!")

def learn_again() -> bool:
    """
    Ask user if they want to learn again
    :return: bool
    """
    while True:
        run_again = input("Do you want to learn again? (y/n) → ").lower()
        if re.match(r"^(y|yes)$", run_again):
            print()
            return True
        elif re.match(r"^(n|no)$", run_again):
            print()
            return False
        else:
            print("Please enter a valid input.")

async def main() -> None:
    """
    Main function
    :return: None
    """
    welcome()
    while True:
        Quiz().run()
        if not learn_again():
            break


if __name__ == "__main__":
    asyncio.run(main())
