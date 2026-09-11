import sys

inventory = 0
rejectedEntryCount = 0

user_input = input("Enter the stock quantity in inventory: ")

while user_input != "quit":
    if user_input.isdigit() == False or int(user_input) < 0: 
        rejectedEntryCount += 1
        print("Error! Please enter a valid integer.")
        user_input = input("Enter the stock quantity in inventory: ")
    elif user_input=="quit":
        sys.exit()
    else:
        inventory += int(user_input)

        if inventory < 500:
            print(f"Current inventory: {inventory}")
            user_input = input("Enter the stock quantity in inventory: ")
        elif inventory > 500:
            print("Inventory count exceeds 500.")
            print(f"Total Units Processed: {inventory}")
            print(f"Total Rejected Entries: {rejectedEntryCount}")
            break;
    