# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Benton Weizenegger
# Last Modified: 10/29
# -------------------------------------------------
# This program starts with a parent class for generic major
# -------------------------------------------------

#------------------------------------------------------------------------
#   Parent class
class Generic_Major:
    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.major = "Generic"
        self.majorT = False     # True or False for major trouble
        self.mathT = False      # True or False for math trouble
        
        
        
        
    def get_first_name(self):
        return self.first
        
    def get_last_name(self):
        return self.last
        
    def get_major(self):
        return self.major
    
    def set_major_troubles(self, majorT):
        self.majorT = majorT
    
    def set_math_troubles(self, mathT):
        self.mathT = mathT
        
    def get_major_troubles(self):
        return self.majorT
        
    def get_math_troubles(self):
        return self.mathT
        
    def major_advising(self):
        self.majorAdvising = "because you are having trouble with your major:\n" + "-->visit your professor during office hours\n" + "-->visit your acedemic advisor" 
        if self.majorT == True:
            print(self.majorAdvising)
        else:
            pass
        
    def math_advising(self):
        self.mathAdvising = "because you are having trouble with math:\n" + "-->visit the Math Learning Center in Willson 1-112"
        if self.mathT == True:
            print(self.mathAdvising)
        else:
            pass
        
    def __str__():
        return str(self.get_major_troubles)
        return str(self.get_math_troubles)
    
    # def __str__(self):
        # return "Because you are having trouble with your major: \n" + str(self.major_advising)
        # return "Because you are having trouble with math:\n" + str(self.math_advising)
        
        
#------------------------------------------------------------------------
class CLS_Major(Generic_Major):
    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.major = "College of Letters and Science"
        self.majorT = False
        self.mathT = False
#------------------------------------------------------------------------

class COE_Major(Generic_Major):
    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.major = "College of Engineering"
        self.majorT = False
        self.mathT = False
    
    def major_advising(self):
        self.majorAdvising = "because you are having trouble with your major:\n" + "-->visit the EMPower Student Center in Roberts 313\n" + "-->visit your professor during office hours\n" + "-->visit your acedemic advisor"

        if self.majorT == True:
            print(self.majorAdvising)
#------------------------------------------------------------------------

class Computer_Engineering_Major(COE_Major):
    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.major = "Computer Engineering"
        self.majorT = False
        self.mathT = False

#------------------------------------------------------------------------
    
class Physics_Major(COE_Major):
    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.major = "Physics"
        self.majorT = False
        self.mathT = False
        
    def major_advising(self):
        self.majorAdvising = "because you are having trouble with your major:\n" + "-->visit the Physics Learning Center in Barnard Hall 230\n" + "-->visit your professor during office hours\n" + "-->visit your acedemic advisor"
        if self.majorT == True:
            print(self.majorAdvising)
    
#------------------------------------------------------------------------
class Computer_Science_Major(COE_Major):
    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.major = "Computer Science"
        self.majorT = False
        self.mathT = False
        
    def major_advising(self):
        self.majorAdvising = "because you are having trouble with your major:\n" + "-->visit the CS Student Success Center in Barnard Hall 259\n" + "-->visit a CS professional advisor in Barnard Hall 357\n" + "-->visit the EMPower Student Center in Roberts 313\n" + "-->visit your professor during office hours\n" + "-->visit your acedemic advisor"
        if self.majorT == True:
            print(self.majorAdvising)
    
#------------------------------------------------------------------------
# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------

def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    #Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

   #   # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

  #   #   # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

  #   #   # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

  #   #   # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

  #   #   # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

#-------------------------------------------------

main()


