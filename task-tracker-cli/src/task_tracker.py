import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return

    command = sys.argv[1]

    if command == "add":
        print("Add command selected")
    elif command == "list":
        print("List command selected")
    elif command == "delete":
        print("Delete command selected")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()