def shutdown():
    user_input = input("enter condition")
    if user_input == "yes":
        print("shutting down.")
    elif user_input == "no":
        print("stoping shut down.")
    else:
        print("sorry")
shutdown()