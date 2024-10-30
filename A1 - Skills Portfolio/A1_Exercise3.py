#imports tkinter to python
from tkinter import*

#makes it possible to make images using tkinter
from PIL import ImageTk, Image

from tkinter import filedialog

from tkinter import ttk



root = Tk()
#sets the title of the program window
root.title("Formative Assessment")

container = Frame(root)
container.pack()

#sets the window size when running the code
root.geometry('550x400')

#makes the window not resizable 
root.resizable(False,False)

#Changes background color
root.configure(bg="#EEF4F8")




#Texts that's written in the assessment
l = Label(root, text="Student Manager",
      	fg="black",
      	bg="#FFFFFF",
      	font=('Calibri',20))
l.pack()






def fileOpen():
    txtarea.delete("1.0", "end")
    
    # Searches for the file that contains the data and reads it
    with open(r"C:\Users\m1kee\OneDrive\Documents\CODELAB-2--A1\A1 - Skills Portfolio\A1 - Resources\studentMarks.txt", "r") as file_handler:
        lines = file_handler.readlines()
        
    # Start formatting each student's data
    formatted_content = ""
    for line in lines[1:]:  # Skip the first line as it's just the header count
        data = line.strip().split(",")
        if len(data) == 6:
            student_id, name, coursework, exam, overall, grade = data
            formatted_content += (
                f"Name: {name}\n"
                f"Number: {student_id}\n"
                f"Coursework Total: {coursework}\n"
                f"Exam Mark: {exam}\n"
                f"Overall Percentage: {overall}\n"
                f"Grade: {grade}\n\n"
            )
    
    # Insert the formatted content into the text area
    txtarea.insert("end", formatted_content)
    print(formatted_content)

#highest score function
def showHighestScore():
    txtarea.delete("1.0", "end")

    with open(r"C:\Users\m1kee\OneDrive\Documents\CODELAB-2--A1\A1 - Skills Portfolio\A1 - Resources\studentMarks.txt", "r") as file_handler:
        lines = file_handler.readlines()

    highest_score = 0
    highest_student = ""

    # Start processing each student's data
    for line in lines[1:]:  # Skip the first line as it's just the header count
        data = line.strip().split(",")
        if len(data) == 6:
            student_id, name, coursework, exam, overall, grade = data
            if int(overall) > highest_score:
                highest_score = int(overall)
                highest_student = (
                    f"Name: {name}\n"
                    f"Number: {student_id}\n"
                    f"Coursework Total: {coursework}\n"
                    f"Exam Mark: {exam}\n"
                    f"Overall Percentage: {overall}\n"
                    f"Grade: {grade}\n"
                )
    
    # Display the highest-scoring student's data
    txtarea.insert("end", highest_student)
    print(highest_student)


#lowest score function
def showLowestScore():
    txtarea.delete("1.0", "end")

    with open(r"C:\Users\m1kee\OneDrive\Documents\CODELAB-2--A1\A1 - Skills Portfolio\A1 - Resources\studentMarks.txt", "r") as file_handler:
        lines = file_handler.readlines()

    lowest_score = float('inf')
    lowest_student = ""

    # Start processing each student's data
    for line in lines[1:]:  # Skip the first line as it's just the header count
        data = line.strip().split(",")
        if len(data) == 6:
            student_id, name, coursework, exam, overall, grade = data
            if int(overall) < lowest_score:
                lowest_score = int(overall)
                lowest_student = (
                    f"Name: {name}\n"
                    f"Number: {student_id}\n"
                    f"Coursework Total: {coursework}\n"
                    f"Exam Mark: {exam}\n"
                    f"Overall Percentage: {overall}\n"
                    f"Grade: {grade}\n"
                )
    
    # Display the lowest-scoring student's data
    txtarea.insert("end", lowest_student)
    print(lowest_student)


def showStudentRecord():
    selected_student = student_combobox.get()
    txtarea.delete("1.0", "end")

    with open(r"C:\Users\m1kee\OneDrive\Documents\CODELAB-2--A1\A1 - Skills Portfolio\A1 - Resources\studentMarks.txt", "r") as file_handler:
        lines = file_handler.readlines()

    for line in lines[1:]:
        data = line.strip().split(",")
        if len(data) == 6:
            student_id, name, coursework, exam, overall, grade = data
            if name == selected_student:
                student_info = (
                    f"Name: {name}\n"
                    f"Number: {student_id}\n"
                    f"Coursework Total: {coursework}\n"
                    f"Exam Mark: {exam}\n"
                    f"Overall Percentage: {overall}\n"
                    f"Grade: {grade}\n"
                )
                txtarea.insert("end", student_info)
                break

# Load student names into the combobox
def loadStudentNames():
    with open(r"C:\Users\m1kee\OneDrive\Documents\CODELAB-2--A1\A1 - Skills Portfolio\A1 - Resources\studentMarks.txt", "r") as file_handler:
        lines = file_handler.readlines()

    student_names = [line.strip().split(",")[1] for line in lines[1:] if len(line.strip().split(",")) == 6]
    student_combobox['values'] = student_names






#creates a variable so it can be called to be placed
txtarea = Text(root)  # Capitalized Text

#places the text in a specific area
txtarea.place(x=50, y=175, height=175, width=450)



#Button to view all student records
btn = Button(root, text="View All Student Records", command=fileOpen)
btn.place(x=50, y=75, height=25, width=150)

#Button to view the highest score
btn_highest = Button(root, text="Show Highest Score", command=showHighestScore)
btn_highest.place(x=205, y=75, height=25, width=140)

#Button to view the lowest score
btn_lowest = Button(root, text="Show Lowest Score", command=showLowestScore)
btn_lowest.place(x=350, y=75, height=25, width=150)

#labels the text and be visible
l1 = Label(root, text="View Individual Student Record:",
      	fg="black",
      	bg="#FFFFFF",
      	font=('Calibri',13))
l1.place(x=50, y=125)

# Combobox to select a student
student_combobox = ttk.Combobox(root, state="readonly")
student_combobox.place(x=280, y=129, width=115)

# Load student names into the combobox
loadStudentNames()

view_record_button = Button(root, text="View Record", command=showStudentRecord)
view_record_button.place(x=400, y=125, height=25, width=100)

root.mainloop()