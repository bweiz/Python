#
#--------------------
# CSCI 127, GPA Calculator
# Sept 19, 2017
# Ben Weizenegger
#--------------------
#
def translate(grade):
    
    if grade == 'A':
        return 4.00
    
    elif grade == 'A-':
        return 3.70
    
    elif grade == 'B+':
        return 3.30
    
    elif grade == 'B':
        return 3.00
    
    elif grade == 'B-':
        return 2.70
    
    elif grade == 'C+':
        return 2.30
   
    elif grade == 'C':
        return 2.00
    
    elif grade == 'C-':
        return 1.70
    
    elif grade == 'D+':
        return 1.30
    
    elif grade == 'D':
        return 1.00
    
    elif grade == 'F':
        return 0.0
    

num_courses = int(input("Enter the number of courses you are taking: "))
print("\n")
coursenum = 1

credit_list = []    #list of all the credits to be added together for final                                  calculation
first_list = []     #list of grade multiplied by number of credits for one class

while(coursenum <= num_courses):
    grades = input("Enter grade for course " + str(coursenum) + ": ").upper()
    num_grade = translate(grades)       #Translate grade to number
    credit = int(input("Enter credits for course " + str(coursenum) + ": "))
    credit_list.append(float(credit))
    first = num_grade * credit
    first_list.append(first)
    print("\n")
    coursenum = coursenum + 1
    
def Calculate():
    a = sum(first_list)
    b = sum(credit_list)
    GPA = a / b
    round(GPA, 2)
    return GPA
    

print("Your GPA is "  + str(Calculate()))
    

    
