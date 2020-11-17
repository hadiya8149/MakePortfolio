# a program that takes user data as input by filling a form and then creates a html portfolio
import string
from tkinter import *
root = Tk()
root.title("Portfolio form")
canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH)
canvas["bg"] = "white"
canvas.configure(canvas, highlightcolor="white", bd=0, width=550, height=420)

txt = Label(canvas, height=3, text="All fields are required\nType 'none' instead\nSeparate multiple values with comma", background="white", foreground="brown")
txt.place(x=115, y=1)


list_Lower_ascii = []
list_digits = []
for i in string.digits:
    list_digits.append(i)
for i in string.ascii_lowercase:
    list_Lower_ascii.append(i)



    def create_variables():  # function to create global variables
      global nameinfo, highest_education_level_info, occupation_name_info, school_name_info, college_name_info, university_name_info, job_post_info, salary_info


# variable that will be referenced to change the background colors of the label widgets
bgcoloroflabel = "white"
# label text widgets
nametitle = Label(text="Name: ", bg=bgcoloroflabel).place(x=5, y=54)
highest_education_level_title = Label(canvas, text="Highest education level:", bg=bgcoloroflabel).place(x=5, y=81)
college_name_title = Label(canvas, text="College Name: ", bg=bgcoloroflabel).place(x=5, y=108)
school_name_title = Label(canvas, text="School Name: ", bg=bgcoloroflabel).place(x=5, y=135)
university_name_title = Label(canvas, text="University name:", bg=bgcoloroflabel).place(x=5, y=164)
occupation_name_title = Label(canvas, text="Occupation:", bg=bgcoloroflabel).place(x=5, y=191)
job_post_title = Label(canvas, text="Position in the company: ", bg=bgcoloroflabel).place(x=5, y=219)
salary_title = Label(canvas, text="Salary per month:", bg=bgcoloroflabel).place(x=5, y=247)
Project_title = Label(canvas, text="Projects:", bg=bgcoloroflabel).place(x=5, y=275)
skill_title = Label(canvas, text="Skills:", bg=bgcoloroflabel).place(x=5, y=304)
ContactDetails_title = Label(canvas, text="Provide Contact details:", bg=bgcoloroflabel).place(x=5, y=332)
# entry widgets
name = Entry(canvas, text="name", width=36, bd=2, font="Saira 8", relief="groove")
highest_education_level = Entry(canvas, width=36, bd=2, font="Saira 8", relief="groove" , highlightbackground="#001D73")
college_name = Entry(canvas, width=36, bd=2, font="Saira 8", relief="groove")
school_name = Entry(canvas, width=36, bd=2, font="Saira 8", relief="groove")
university_name = Entry(canvas, width=36, bd=2, font="Saira 8", relief="groove")
occupation_name = Entry(canvas, width=36, bd=2, font="Saira 8", relief="groove")
job_post = Entry(canvas, width=36, bd=2, font="Saira 8", relief="groove")
salary = Entry(canvas, width=36, bd=2, font="Saira 8", relief="groove")
projects = Entry(canvas, width=36, bd=2,font="Arial 9", relief="groove")
skills = Entry(canvas, width=36, bd=2,font="Arial 9", relief="groove")
contact = Entry(canvas, width=36, bd=2,font="Arial 9", relief="groove", highlightbackground="black")
salary_instruction = Label(root, background="white", fg="#73005B", height=3, text="Type digits without comma\nand then the unit of your\nsalary separated by space")
# entry widgets managed by place geometry
name.place(x=154, y=51)
highest_education_level.place(x=154, y=79)
college_name.place(x=154, y=107)
school_name.place(x=154, y=135)
university_name.place(x=154, y=163)
occupation_name.place(x=154, y=191)
job_post.place(x=154, y=219)
salary.place(x=154, y=247)
projects.place(x=154, y=275)
skills.place(x=154, y=303)
contact.place(x=154, y=331)
name.focus_set()  # sets focus to name entry widget
create_variables()   # invokes the function that creates variable
nameForFunc = name
EduLevelNameForFunc = highest_education_level
collegeNameForFunc = college_name
schoolNameForFunc = school_name
uni_NameForFunc = university_name
occupationNameForFunc = occupation_name
jobNameForFunc = job_post
salaryNameForFunc = salary
ProjectNameForFunc = projects
skillNameForFunc = skills
contactNameForFunc = contact
invalidInput_name = Label(root, background="white", foreground="blue", font="Helvetica")
invalidInput_eduLevel = Label(root, bg="white", fg="red", font="Saira 7")
invalidInput_college = Label(root, background="white", foreground="red", font="Saira 7")
invalidInput_school = Label(root, background="white", fg="red", font="Saira 7")
invalidInput_university = Label(root, background="white", fg="red", font="Saira 7")
invalidInput_occupation = Label(root, background="white", fg="red", font="Saira 7")
invalidInput_job = Label(root, background="white", fg="red", font="Saira 7")
invalidInput_salary = Label(root, background="white", fg="red", font="Saira 7")
invalidInput_project = Label(root, background="white", fg="red", font="Saira 7")
invalidInput_skill = Label(root, background="white", fg="red", font="Saira 7")
invalidInput_contact = Label(root, background="white", fg="red", font="Saira 7")
checkmark = "\u2611"
validInput_name = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_eduLevel = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_college = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_school = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_university= Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_occupation = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_job = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_salary = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_project = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_skills = Label(root, background="white", foreground="blue", text=checkmark, font="8")
validInput_contact = Label(root, background="white", foreground="blue", text=checkmark, font="8")

def getinfo():   # portfolio construction work is done here
    nameinfo = name.get()
    highest_education_level_info = highest_education_level.get()
    college_name_info = college_name.get()
    school_name_info = school_name.get()
    university_name_info = university_name.get()
    occupation_name_info = occupation_name.get()
    job_post_info = job_post.get()
    salary_info = salary.get()
    project_info = projects.get()
    skills_info = skills.get()
    contact_info = contact.get()
    length_name = len(nameinfo)
    length_highest_edu_level = len(highest_education_level_info)
    length_school = len(school_name_info)
    length_college = len(college_name_info)
    length_university = len(university_name_info)
    length_occupation = len(occupation_name_info)
    length_job = len(job_post_info)
    length_salary = len(salary_info)
    length_project = len(project_info)
    length_skills  = len(skills_info)
    length_contact = len(contact_info)

    def info_test():   # validation of form is done here
        """
        Sr.1 Rules of name widget's input validation:
        1.User cannot type none or non; The user has to type user's name
        2.Only blank spaces are not allowed
        3.Empty input is not allowed
        4.Numeric characters at the start of the name are not allowed
        5.Especial characters are not allowed
        """
        if nameinfo.lower() == "none" or nameinfo.lower().strip() == "non":  # if the user input of name widget is none or non
            invalidInput_name.configure(text="'none' not accepted\nType your name")
            invalidInput_name.place(x=390, y=50)
            # entry widget of name
            nameForFunc.focus_set()
            nameForFunc.configure(foreground="red", highlightcolor="red", highlightbackground="red", background="white")
            nameForFunc.delete(first=0, last=length_name)
            validInput_name.place_forget()
        elif nameinfo.isspace():  # input of entry widget contain spaces
            invalidInput_name.configure(text="(_spaces_)\nType a name")
            invalidInput_name.place(x=390, y=50)
            # entry widget of name
            nameForFunc.focus_set()
            nameForFunc.configure(foreground="red", highlightcolor="red", highlightbackground="red", background="white")
            nameForFunc.delete(first=0, last=length_name)
            validInput_name.place_forget()
        elif not nameinfo:  # input of entry widget is empty( no characters typed)
            invalidInput_name.configure(text="Field Required")
            invalidInput_name.place(x=390, y=50)
            # entry widget of name
            nameForFunc.focus_set()
            nameForFunc.configure(foreground="red", highlightbackground="red", highlightcolor="red", background="white")
            validInput_name.place_forget()
        elif (re.findall("\d +", nameinfo) or re.findall("\d *", nameinfo)):
            print(nameinfo)
            nameForFunc.delete(first=0, last=length_name)
            invalidInput_name.configure(text="Type your name in alphabets")
            invalidInput_name.place(x=390, y=50)
            validInput_name.place_forget()
        else:
            invalidInput_name.place_forget()
            validInput_name.place(x=390, y=50)

        """
        Sr.2 Rules of Highest education level widget's input validation:
        1.Blank spaces are not allowed
        2.Empty input is not allowed
        """

        if highest_education_level_info.isspace():  # if the input contains only spaces
            # entry widget of highest education level
            EduLevelNameForFunc.configure( highlightbackground="red", highlightcolor="red", background="white")
            EduLevelNameForFunc.delete(first=0, last=length_highest_edu_level)
            invalidInput_eduLevel.configure(text="__spaces__ :(\nType none instead")
            invalidInput_eduLevel.place(x=390, y=78)
            validInput_eduLevel.place_forget()
        elif not highest_education_level_info:  # if the input is empty
            EduLevelNameForFunc.configure(highlightbackground="red", highlightcolor="red", background="white")
            invalidInput_eduLevel.configure(text="(_Field required_) :(\nType none instead")
            invalidInput_eduLevel.place(x=390, y=77)
            validInput_eduLevel.place_forget()  # valid input message
        elif re.findall(r"\d+", highest_education_level_info) or (re.findall(r"\.", highest_education_level_info)) or (re.findall(r"\d*", highest_education_level_info)):
            EduLevelNameForFunc.delete(first=0, last=length_highest_edu_level)
            invalidInput_eduLevel.configure(text="Type your name in alphabets")
            invalidInput_eduLevel.place(x=390, y=77)
            validInput_eduLevel.place_forget()
            print("elif working but not hte block code")
        else:
            invalidInput_eduLevel.place_forget()
            validInput_eduLevel.place(x=390, y=50)
        if college_name_info.lower().strip()  == "none" or college_name_info.lower().strip() == "non":  # if the input value is "none" or "non"
            # entry widget of collegge
            collegeNameForFunc.configure(background="gray", highlightcolor="black", highlightbackground="black")
            invalidInput_college.place_forget()  # invalid input message
            validInput_college.place(x=390, y=105)  # valid input message
        elif college_name_info.isspace():  # if the input contains only spaces
            collegeNameForFunc.configure(highlightbackground="red", fg="black", highlightcolor="red", background="white")
            collegeNameForFunc.delete(first=0, last=length_college)
            invalidInput_college.configure(text="Bad space\nType none instead")  # invalid input message
            invalidInput_college.place(x=390, y=106)
            validInput_college.place_forget()  # valid input message
        elif not college_name_info:  # if the input is empty
            invalidInput_college.configure(text="Field required\nType none instead")
            invalidInput_college.place(x=390, y=106)
            validInput_college.place_forget()
            collegeNameForFunc.configure(highlightbackground="red", highlightcolor="red", background="white")
        else:  # if the input is valid according to the rules in serial no.2
            invalidInput_college.place_forget()
            validInput_college.place(x=390, y=105)
            collegeNameForFunc.configure(fg="black", highlightcolor="black", highlightbackground="black")
        # school input validation
        if school_name_info.lower().strip() == "none" or school_name_info.lower().strip() == "non":  # if the input value is 'none' or 'non'
            schoolNameForFunc.configure(background="gray", highlightbackground="black", highlightcolor="black")
            invalidInput_school.place_forget()
            validInput_school.place(x=390, y=135)
        elif school_name_info.isspace():
            schoolNameForFunc.configure(highlightcolor="red", highlightbackground="red")
            schoolNameForFunc.delete(first=0, last=length_school)
            invalidInput_school.configure(text="Bad spaces\nType \"none\" instead")
            invalidInput_school.place(x=390, y=135)
            validInput_school.place_forget()
        elif not school_name_info:  #  if the input is empty
            invalidInput_school.place(x=390, y=135)
            schoolNameForFunc.configure(highlightcolor="red", highlightbackground="red")
            invalidInput_school.configure(text="Field required\nType 'none' instead")
            validInput_school.place_forget()
        else:  # if the input is valid according to the rules in serial no2
            schoolNameForFunc.configure(highlightbackground="black", highlightcolor="#001D73")
            validInput_school.place(x=390, y=135)
            invalidInput_school.place_forget()
        # university entry widget value validation
        if university_name_info.isspace():  # if the input contains only spaces
            uni_NameForFunc.configure(highlightcolor="red", highlightbackground="red", background="white")
            uni_NameForFunc.delete(first=0, last=length_university)
            invalidInput_university.configure(text="Bad spaces :(\nType none instead")
            invalidInput_university.place(x=390, y=163)
            validInput_university.place_forget()
        elif not university_name_info:  # if the input is empty
            uni_NameForFunc.configure(highlightcolor="red", highlightbackground="red", background="white")
            invalidInput_university.configure(text="Field required:(\nType 'none' instead")
            invalidInput_university.place(x=390, y=163)
            validInput_university.place_forget()
        elif university_name_info.lower().strip() == "none" or university_name_info.lower().strip() == "non":  # if the value of input is 'none' or 'non'
            uni_NameForFunc.configure(bg="gray", highlightcolor="gray", highlightbackground="black", fg="black")
            invalidInput_university.place_forget()
            validInput_university.place(x=390, y=163)
        else:  # if the input is valid according to the rules in serial no.2
            uni_NameForFunc.configure(bg="white", fg="black", highlightcolor="#001D73", highlightbackground="black")
            invalidInput_university.place_forget()
            validInput_university.place(x=390, y=163)
        # entry widget of occupation
        if occupation_name_info.isspace():  # if the input contains only spaces
            occupationNameForFunc.configure(bg="white", highlightbackground="red", highlightcolor="red")
            occupationNameForFunc.delete(first=0, last=length_job)
            invalidInput_occupation.configure(text="Bad spaces\nType none instead")
            invalidInput_occupation.place(x=390, y=191)
            validInput_occupation.place_forget()
        elif not occupation_name_info:  # if the input field is left empty
            occupationNameForFunc.configure(bg="white", highlightbackground="red", highlightcolor="red")
            invalidInput_occupation.configure(text="Field required\nType 'none' instead")
            invalidInput_occupation.place(x=390, y=191)
            validInput_occupation.place_forget()
        elif occupation_name_info.lower().strip() == "none" or occupation_name_info.lower().strip() == "non":  # if the input's value is 'none' or 'non'
            occupationNameForFunc.configure(bg="gray", highlightbackground="gray", highlightcolor="gray", fg="black")
            invalidInput_occupation.place_forget()
            validInput_occupation.place(x=390, y=191)
        else:  # if the input is valid according to the rules in serial no.2
            invalidInput_occupation.place_forget()
            validInput_occupation.place(x=390, y=191)
            occupationNameForFunc.configure(highlightbackground="black", highlightcolor="#001D73", bg="white", fg="black")
        # job entry widget
        if job_post_info.isspace():  # if input contains only spaces
            jobNameForFunc.configure(highlightbackground="red", highlightcolor='red')
            jobNameForFunc.delete(first=0, last=length_job)
            invalidInput_job.configure(text="Bad spaces\nType 'none' instead")
            invalidInput_job.place(x=390, y=219)
            validInput_job.place_forget()
        elif not job_post_info:  # if the input is empty
            jobNameForFunc.configure(highlightbackground="red", highlightcolor='red')
            invalidInput_job.configure(text="Field required\nType none instead")
            invalidInput_job.place(x=390, y=219)
            validInput_job.place_forget()
        elif job_post_info.lower().strip() == "none" or job_post_info.lower().strip() == "non":  # if the input's value is none or non
            jobNameForFunc.configure(highlightbackground="gray", highlightcolor="#001D73", bg="gray", fg="black")
            invalidInput_job.place_forget()
            validInput_job.place(x=390, y=219)
        else:  # if the input is valid according to the rules in serial no.3
            jobNameForFunc.configure(highlightbackground="gray", highlightcolor="#001D73", bg="white", fg="black")
            invalidInput_job.place_forget()
            validInput_job.place(x=390, y=219)
        # salary widget
        """
        Sr.3 Rules of validation

                Rules of validation
                1.It should not contain more than one space
                2.The characters from the right side of the white space must be alphabetic
                3.The chars from the  left side of the white space must be numeric
                4.No special characters are allowed
                5.Empty input is not allowed
                6.Only spaces as characters are not allowed
                Example of correct input:            x unit
                                                234343 Rs

        """
        if salary_info.isspace():
            invalidInput_salary.configure(text="Bad spaces\nType none instead")
            invalidInput_salary.place(x=322, y=247)
    info_test()


def callBack(event):

    def hide():
        salary_instruction.place_forget()

    def display():
        salary_instruction.place(x=322, y=247)
        salary.after(5000, hide)

    salary.after(250, display)


salary.bind("<Button-1>", callBack)

currentch = "12346556**&)($%dlkf"
if any(currentch in string.punctuation for c in string.punctuation):
    print("i dnnnnnnnnt know what it means")







def display_instructions():
    instructions = ".dfglkfdj"
    Label(canvas, text=instructions,  highlightcolor="white", bd=0, width=500, height=420, fg="black")
    Label.pack(canvas, side=BOTTOM, fill=BOTH)
instruction_button = Button(root, text="Instructions", command=display_instructions)
instruction_button.place(x=396, y=391)
submit_button = Button(root, text="Submit", command=getinfo)
submit_button.place(x=309, y=391)


canvas.mainloop()
