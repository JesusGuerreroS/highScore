#######################################################################
#               checks the highest score in a list of student scores  #
#######################################################################

#get student scores
student_scores = input("Input a list of student scores ").split()

#add all scores
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high = 0

#calculate highest score
for score in student_scores:

    if score > high:
        high = score

print(f"The highest score in the class is: {high}")