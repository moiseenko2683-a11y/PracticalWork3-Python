# Practical work 3
# Working with dictionary
# Robotics club students

students = {
    1: ("Petrenko", "Oleksandr", "Shevchenka St. 10", 1, 10),
    2: ("Ivanenko", "Andrii", "Kharkivska St. 25", 2, 11),
    3: ("Sydorenko", "Maksym", "Soborna St. 15", 1, 9),
    4: ("Kovalenko", "Dmytro", "Nezalezhnosti St. 8", 3, 10),
    5: ("Melnyk", "Artem", "Kyivska St. 32", 2, 10),
    6: ("Bondarenko", "Illia", "Peremohy St. 14", 3, 11),
    7: ("Shevchenko", "Danylo", "Haharina St. 21", 1, 11),
    8: ("Tkachenko", "Roman", "Lesi Ukrainky St. 5", 2, 9),
    9: ("Kravchenko", "Nazar", "Sumska St. 18", 3, 10),
    10: ("Moroz", "Vladyslav", "Tsentralna St. 7", 2, 11)
}


# Display all dictionary records
def show_all():
    print("\n--- ALL STUDENTS ---")

    for key, data in students.items():
        print(
            key, ":",
            data[0], data[1],
            "| Address:", data[2],
            "| School:", data[3],
            "| Grade:", data[4]
        )


# Add a new student
def add_student():
    try:
        key = int(input("Enter record number: "))

        if key in students:
            print("Error: this key already exists!")
            return

        surname = input("Enter surname: ")
        name = input("Enter name: ")
        address = input("Enter address: ")
        school = int(input("Enter school number: "))
        grade = int(input("Enter grade (1-11): "))

        if school <= 0:
            print("Error: school number must be positive!")
            return

        if grade < 1 or grade > 11:
            print("Error: grade must be from 1 to 11!")
            return

        students[key] = (
            surname,
            name,
            address,
            school,
            grade
        )

        print("Student added successfully!")

    except ValueError:
        print("Error: incorrect data entered!")


# Delete a student
def delete_student():
    try:
        key = int(input("Enter key to delete: "))

        if key not in students:
            print("Error: this key does not exist!")
            return

        del students[key]

        print("Record deleted successfully!")

    except ValueError:
        print("Error: key must be a number!")


# Display records sorted by keys
def show_sorted():
    print("\n--- SORTED RECORDS ---")

    for key in sorted(students):
        data = students[key]

        print(
            key, ":",
            data[0], data[1],
            "| Address:", data[2],
            "| School:", data[3],
            "| Grade:", data[4]
        )


# Find students from selected school
# who study in grades 10 or 11
def find_students():
    try:
        school = int(input("Enter school number: "))

        result = []

        for key, data in students.items():

            surname = data[0]
            name = data[1]
            address = data[2]
            student_school = data[3]
            grade = data[4]

            if student_school == school and grade in (10, 11):

                result.append(
                    (key, (surname, name, address))
                )

        print("\n--- SEARCH RESULT ---")

        if len(result) == 0:
            print("No students found.")
        else:
            for key, data in result:
                print(
                    key, ":",
                    data[0], data[1],
                    "| Address:", data[2]
                )

        return result

    except ValueError:
        print("Error: school number must be a number!")
        return []


# Main menu
def main():

    while True:

        print("\n==============================")
        print("       MAIN MENU")
        print("==============================")
        print("1 - Show all students")
        print("2 - Add student")
        print("3 - Delete student")
        print("4 - Show sorted records")
        print("5 - Find students")
        print("0 - Exit")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":
            show_all()

        elif choice == "2":
            add_student()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            show_sorted()

        elif choice == "5":

            result = find_students()

            print("\n--- RESULT LIST ---")
            print(result)

        elif choice == "0":
            print("Program finished.")
            break

        else:
            print("Error: invalid menu option!")


main()