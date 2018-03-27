computational_thinking = input("what is your grade in this class.")

creative_writting = input("what is your grade in this class.")

algebra = input("what is your grade in this class.")

biology = input("what is your grade in this class.")

computer_hardware_software = input("what is your grade in this class.")


grade = [computational_thinking,creative_writting,algebra,biology,computer_hardware_software]

grade_average = (computational_thinking + creative_writting + algebra + biology + computer_hardware_software)
grade.append ("grade average:" + str(grade_average))
print grade


if grade_average >= 60:
        print ("you get U")
elif grade_average >= 90 and grade <= 100:
       print ("you get A")
elif grade_average >= 80 and grade <= 90:
        print ("you get B")
elif grade_average >= 70 and grade <= 80:
        print ("you get C")
elif grade_average >= 60 and grade <= 70:
    print (" you get D")

