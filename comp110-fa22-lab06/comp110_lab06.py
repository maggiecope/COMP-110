"""
Module: comp110_lab06

Exercises from lab 06, dealing with string accumualators.
"""


def create_edited_string(text_with_edit_marks):
    """ Function that returns a sting with editing applied. """

    final_str = ""
    caps_lock_mode = False
    lower_case_mode = False 
    delete_mode = False


    for ch in text_with_edit_marks:
        if ch == '!':
            delete_mode = True 
        elif ch == '^':
            caps_lock_mode = True
        elif ch == '_':
            lower_case_mode=True
        elif delete_mode ==True:
            delete_mode = False 
        elif caps_lock_mode == True:
            final_str = final_str +ch.upper()
        elif lower_case_mode == True:
            final_str = final_str +ch.lower()
        
        else:
            final_str = final_str + ch
   
    return final_str



def test_create_edited_string():
    """
    Function that tests the create_edited_string function.

    Do not modify this function in any way.
    """

    # define a list with our test inputs
    test_cases = []
    test_cases.append("String without edit marks")
    test_cases.append("This was !qwicked awesome")
    test_cases.append("Please do not ^make me yell")
    test_cases.append("This is my ^roar!s")
    test_cases.append("You need to _CALM DOWN")
    test_cases.append("You need to _CALM ^down")
    test_cases.append("Please give me some ^f!lood")
    test_cases.append("Interesting _result")

    # define a list with the expected results based on inputs
    solutions = []
    solutions.append("String without edit marks")
    solutions.append("This was wicked awesome")
    solutions.append("Please do not MAKE ME YELL")
    solutions.append("This is my ROAR")
    solutions.append("You need to calm down")
    solutions.append("You need to calm DOWN")
    solutions.append("Please give me some FOOD")
    solutions.append("Interesting result")

    num_passed = 0
    num_failed = 0

    for i in range(len(test_cases)):
        # get the input and expected result
        current_test = test_cases[i]
        current_solution = solutions[i]

        # call the function and check the result
        result = create_edited_string(current_test)
        if result != current_solution:
            print("Test", i, "(", current_test, ") FAILED. \n\tExpected Result:", current_solution, "\n\tActual Result:", result)
            num_failed = num_failed + 1
        else:
            print("Test", i, "(", current_test, ") PASSED.\n\tResult:", current_solution)
            num_passed = num_passed + 1

    print("\nTest summary:", num_passed, "case(s) passed,", num_failed, "case(s) failed.")

# Do not modify anything after this point.
if __name__ == "__main__":
    test_create_edited_string()
