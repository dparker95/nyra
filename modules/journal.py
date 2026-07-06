def create_journal_entry():
    print()
    print("📖 New Journal Entry")
    print()

    entry = input("Write today's journal entry: ")

    with open("data/journal.txt", "a") as file:
        file.write(entry + "\n")

    print("✅ Journal saved.")


def view_journal():
    print()
    print("📚 Your Journal")
    print()

    with open("data/journal.txt", "r") as file:
        journal_contents = file.read()

    print(journal_contents)