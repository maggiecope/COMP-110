"""
Module: comp110_lab09

Starter code for COMP110 Lab 09.
"""

import matplotlib.pyplot as pp


def get_grade_frequencies(filename):
    """
    Creates a dictionary mapping letter grade to the number of students with
    that grade for the midterm exam #1.
    """
    f = open(filename, 'r')
    line = f.readline()
    

    grade_frequency = {}
   
    for ch in "ABCDF":
        grade_frequency[ch] = 0 
    
    for line in f:
        line = line.split(",")
        if 90<=int(line[5])<=100:
            grade_frequency['A'] = grade_frequency['A'] + 1
        elif 80<= int(line[5]) <= 89:
            grade_frequency["B"] = grade_frequency["B"] + 1
        elif 70<= int(line[5]) <= 79:
            grade_frequency["C"] = grade_frequency["C"] + 1
        elif 60<= int(line[5]) <= 69:
            grade_frequency["D"] = grade_frequency["D"] + 1
        else:
            grade_frequency["F"] = grade_frequency["F"] + 1
    
    return grade_frequency


def test_get_grade_frequencies():
    actual = get_grade_frequencies("students.txt")

    # To Do: update the next line so it is a dictionary with the correct,
    # expected values.
    expected = {"A": 3, "B": 6, "C": 8, "D": 2, "F": 1}

    if actual == expected:
        print("Test PASSED")
    else:
        print("Test FAILED!")
        print("Expected:", expected)
        print("Actual:", actual)


def main():
    """
    Creates a bar chart showing grade distribution on midterm exam #1.
    """

    dictionary = get_grade_frequencies("students.txt")

    x_vals, y_vals = list(dictionary.keys()), list(dictionary.values())
 

    pp.bar(x_vals, y_vals)


    # To Do: Step 3: Update the labels for the x and y axis as well as the
    # title of the chart.
    pp.xlabel("Grades")
    pp.ylabel("# of students")
    pp.title("Grade Distribution for Midterm 1")
    pp.show()


if __name__ == "__main__":
    main()
