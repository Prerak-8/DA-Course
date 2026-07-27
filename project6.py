print("Welcome to Personal Journal Manager!")
print()

class JournalManager:
    def __init__(self):
        self.__file = "journal.txt"

    def add_entry(self):
        timestamp = input("Enter timestamp (YYYY-MM-DD HH:MM:SS): ")
        journal_ent = input("Enter your journal entry: ")
        print()
                            
        if journal_ent == "":
            print("Entry cannot be empty.\n")
        else:
            try:
                with open(self.__file, "a") as write_jour:
                    write_jour.write(f"[{timestamp}] {journal_ent}\n")
                print("Entry added successfully!\n")
            except PermissionError:
                print("Permission denied.\n")
        
        print("Select another option.\n")

    def view_entries(self):
        try:
            with open(self.__file, "r") as read_jour:
                content = read_jour.read()

                if content.strip() == "":
                    print("No journal entries found.\n")
                else:
                    print("***************************")
                    print(content, end="")
                    print("***************************\n")
            
        except FileNotFoundError:
            print("Error: The file does not exist.\n")
        
        print("Select another option.\n")

    def search_entry(self):
        search = input("Enter a keyword or date to search: ")
        print()

        try:        
            found = False

            with open(self.__file, "r") as f:
                for line in f:
                    if search.lower() in line.lower():
                        if not found:
                            print("Matching entries:\n")
                            print("****************************")
                        print(line, end="")
                        found = True

            if found:
                print("****************************\n")
            else:
                print(f"No entries found for keyword or date: {search}\n")

        except FileNotFoundError:
            print("Error: The file does not exist.\n")

        print("Select another option.")

    def delete_entries(self):
        del_all = input("Are you sure you want to delete all entries? (yes/no): ")
        print()

        if del_all == "yes":
            open(self.__file, "w").close()
            print("All journal entries have been deleted.\n")
        elif del_all == "no":
            print("No entries will be deleted.\n")
        else:
            print("Invalid input.\n")

        print("Select another option.\n")

manager = JournalManager()

while True:

    print("Select an option:")
    print("1. Add a New Entry")
    print("2. View all Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit\n")

    choice = int(input("Enter an option: "))
    print()

    match choice:

        case 1:
            manager.add_entry()

        case 2:
            manager.view_entries()

        case 3:
            manager.search_entry()

        case 4:
            manager.delete_entries()

        case 5:
            break

        case _:
            print("Invalid option. Select valid option.\n")

print("Thank you for using Personal Journal Manager.\n Goodbye!")