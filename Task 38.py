def readall(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                print(line.rstrip())
    except FileNotFoundError as e:
        print(f"Error: {e}")

def get_input_data():
    last_name = input('Last name: ')
    first_name = input('First_name: ')
    middle_name = input('Middle_name: ')
    phone_number = input('Phone_number: ')
    return f'{last_name}, {first_name}, {middle_name}, {phone_number}\n'

def write_record(file_name, data):
    try:
        if data is not None:
            with open(file_name, 'a', encoding='utf8') as txt_file:
                txt_file.write(data)
            print("Entry successfully added.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def find_item(file_name):
    item = input('Characterization: ')
    try:
        with open(file_name, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                if item.lower() in line.lower():
                    print(line.strip())
    except FileNotFoundError as e:
        print(f"Error: {e}")


def update_record(file_name):
    item = input('Enter the first or last name to update: ')
    try:
        with open(file_name, 'r', encoding='utf8') as txt_file:
            lines = [line.strip() for line in txt_file]
        
        found = False
        updated_records = []

        for i, line in enumerate(lines):
            line_parts = line.split(', ')
            if item.lower() in line_parts[0].lower() or item.lower() in line_parts[1].lower():
                found = True
                new_data = get_input_data()
                updated_records.append(new_data)
            else:
                updated_records.append(line)

        if found:
            with open(file_name, 'w', encoding='utf8') as txt_file:
                for updated_record in updated_records:
                    txt_file.write(f"{updated_record}\n")

            print("This entry has been successfully updated.")
        else:
            print(f"First or last name record '{item}' not found.")

    except FileNotFoundError as e:
        print(f"Error: {e}")

def delete_record(file_name):
    item = input('Enter the first or last name to be deleted: ')
    try:
        with open(file_name, 'r', encoding='utf8') as txt_file:
            lines = [line.strip() for line in txt_file]
        
        found = False
        updated_records = []

        for i, line in enumerate(lines):
            line_parts = line.split(', ')
            if item.lower() in line_parts[0].lower() or item.lower() in line_parts[1].lower():
                found = True
            else:
                updated_records.append(line)

        if found:
            with open(file_name, 'w', encoding='utf8') as txt_file:
                for updated_record in updated_records:
                    txt_file.write(f"{updated_record}\n")

            print(f"First or last name record '{item}' successfully deleted.")
        else:
            print(f"First or last name record '{item}' not found.")

    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    file_path = "d:/GeekBrains/Знакомство с языком Python/Lesson 08/Data.txt"
    while True:
        print("1. Print all records")
        print("2. Add an entry")
        print("3. Update the record")
        print("4. Delete record")
        print("5. Get out")
        
        choice = input("Select an action: ")

        if choice == "1":
            readall(file_path)
        elif choice == "2":
            data = get_input_data()
            write_record(file_path, data)
        elif choice == "3":
            update_record(file_path)
        elif choice == "4":
            delete_record(file_path)
        elif choice == "5":
            break
        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    main()