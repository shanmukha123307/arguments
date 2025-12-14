def shutdown(choice):
    if choice == "Yes":
        print("Shutting down")
    elif choice == "no":
        print("Abort shut down")
    else:
        print("sorry")

user_input = input("Do you want to shut down the system? (Yes/no): ")
shutdown(user_input)
