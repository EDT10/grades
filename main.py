print("#### GET YOUR LETTER GRADE ####")

#ask for user name
name = input("Please enter your name: ")

#function to output grade values
def gradeLetters ():
    grade = int(input("Please enter your grade: "))

    if grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    elif grade >= 60:
        print("Grade: D")
    else:
        print("Grade: E")
    
    #while loop that ask the user for more grades.
while True:
    hasGrade = input(f"Hi {name}, do you have a grade you want check? Yes or No. ")

    if hasGrade == "yes" or hasGrade == "Yes":
        gradeLetters()
    elif hasGrade =="no" or hasGrade == "No":
        print("Thank you, Goodbye")
        break
    else:
        print("Erro: Please enter a valid response.")
