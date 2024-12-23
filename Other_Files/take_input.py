from Other_Files import operation_handler
def taking_input():
    while True: 
        print("\nEnter '+' for Addition")
        print("Enter '-' for Subtraction")
        print("Enter '/' for Division")
        print("Enter '*' for Multiplication")
        print("Enter 'Q' to Exit")

        operation = input("What do you want to do? ").strip()

        if operation.lower() == "q":
            print("Exiting the calculator. Goodbye!")
            break
        a = input("Enter Your First Number: ").strip()
        b = input("Enter Your Second Number: ").strip()
        result=operation_handler(operation,a,b)
        print(f"Output is : {result}")
