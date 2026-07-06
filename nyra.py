def create_journal_entry():
     print()
     print("📖 New Journal Entry")
     print()
     entry = input("Write today's journal entry: ")
     with open("journal.txt", "a") as file:
          file.write(entry + "\n")
    
          print("✅ Journal saved.")

shift_over = False
while shift_over == False:
    print("══════════════════════════════")
    print("            NYRA")
    print("══════════════════════════════")
    print("")
    print("Welcome back, Dej.")
    print("")
    print("1. ✒️New Journal Entry")
    print("2. 📖View Journal")
    print("3. 🌿Herbs")
    print("4. 🃏Tarot")
    print("5. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        create_journal_entry()
    elif choice == "2":
        print()
        print("📚 Your Journal")
        print()

        with open("journal.txt", "r") as file:
             journal_contents = file.read()

        print(journal_contents)     
    elif choice == "3":
        print(" 🌿Opening Herb...")
    elif choice == "4":
        print(" 🃏Opening Tarot...")
    elif choice == "5":
        print("Goodbye, Dej.")
        shift_over = True
    else:
        print("I don't recognize that option.")


