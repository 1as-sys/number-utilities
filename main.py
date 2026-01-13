def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def check_positive_negative():
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


def largest_of_two():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b:
        print("First number is greater")
    elif b > a:
        print("Second number is greater")
    else:
        print("Both numbers are equal")


def check_leap_year():
    year = int(input("Enter year: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")


while True:
    print("\n--- Number Utilities Menu ---")
    print("1. Check Even or Odd")
    print("2. Check Positive / Negative / Zero")
    print("3. Find Largest of Two Numbers")
    print("4. Check Leap Year")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        check_even_odd()
    elif choice == "2":
        check_positive_negative()
    elif choice == "3":
        largest_of_two()
    elif choice == "4":
        check_leap_year()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
