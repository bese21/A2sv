
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    _grade_result=[]
    for grade in grades:
        five_multiple=40
        if grade>=40:
            if grade%5>=3:
             _grade_result.append(grade+5-grade%5)
            else:
             _grade_result.append(grade)
        elif grade<38:
               _grade_result.append(grade)
        else:
               _grade_result.append(40)
    return _grade_result
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
