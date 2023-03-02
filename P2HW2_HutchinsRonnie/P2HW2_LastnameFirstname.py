 # CTI-110
 # P2HW2 - List
 # Ronnie Hutchins
 # Date 03/02/2023

# Create List


grade_list = []

grade = float(input("Enter grade for Module 1: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 2: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 3: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 4: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 5: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 6: "))
grade_list.append(grade)

#print(grade_list)
print('-'*12, 'Results', '-'*12)

print('Lowest Grade:   ', min(grade_list))
print('Highest Grade:  ', max(grade_list))
print('Sum Grade:       ',     sum(grade_list))
print('Average:            ', format(sum(grade_list)/ len(grade_list), ',.2f'))

print('-'*40)




