def main():
    num_elements = int(input("Enter the number of elements: "))

    num_list = []
    for i in range(num_elements):
        num = int(input(f"Enter element {i + 1}: "))
        num_list.append(num)

    even_list = []
    odd_list = []

    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    merged_list = even_list + odd_list
    sorted_list = sorted(merged_list)

    print("Even Numbers List:", even_list)
    print("Odd Numbers List:", odd_list)
    print("Merged and Sorted List:", sorted_list)

    # student
    student_info = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        roll_no = int(input(f"Enter Roll No. for student {i + 1}: "))
        student_name = input(f"Enter Name for student {i + 1}: ")
        
        # Asking for marks in subject 1 and subject 2
        subject1 = float(input(f"Enter marks for Subject 1 for student {i + 1}: "))
        subject2 = float(input(f"Enter marks for Subject 2 for student {i + 1}: "))
        marks = (subject1, subject2)
        
        student_info.append((roll_no, student_name, marks))

    for student in student_info:
        roll_no, name, marks = student
        average = sum(marks) / len(marks)
        total_marks = sum(marks)
        print(f"Student {name} (Roll No. {roll_no}): Average = {average}, Total Marks = {total_marks}")

    search_string = input("Enter a string to search in student names: ")
    if any(search_string.lower() in name.lower() for _, name, _ in student_info):
        print(f"The string '{search_string}' is present in the student names.")
    else:
        print(f"The string '{search_string}' is not present in the student names.")

    def sortByName(student):
        return student[1].lower()
    sorted_student_info = sorted(student_info, key=sortByName)
    print("Sorted Student Info by Names:", sorted_student_info)

    student_dict = {name: {'Roll No.': roll_no, 'Marks': marks} for roll_no, name, marks in student_info}
    print("Student Dictionary:", student_dict)

main()


