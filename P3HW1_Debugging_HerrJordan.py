# debugging a grade calculator
# 6/24/2021
# CTI-110 P3HW1
# Jordan Herr
# 

def main():
# This program takes a number grade and outputs a letter grade.
# system uses 10-point grading scale
    A_score = int(90)
    B_score = int(80)
    C_score = int(70)
    D_score = int(60)
    F_score = int(50)
    
    score = int(input('Enter grade: '))

    if (score >= A_score) and (score <= 100):
        print('Your grade is: A')

    elif (score >= B_score) and (score < A_score):
        print('Your grade is: B')

    elif (score >= C_score)and (score < B_score):
        print('Your grade is: C')

    elif (score >= D_score) and (score < C_score):
        print('Your grade is: D')

    elif (score >= F_score) and (score < D_score) and (score < 0):
        print('Your grade is: F')

    elif (score < 100) and (score < 0):
        print("Please enter a valid grade!")






# program start
main()
