"""
Module: comp110_lab04

Practice with writing functions, sounds, conditionals, and functional
composition.
"""
import sound


def get_max_in_range(my_sound, start,end):
    """
    Returns the maximum left channel value between the start and end indices.
    The end index is non-inclusive (just like the range function).

    Note that this maximum is the absolute value maximum, so -10 is consider
    larger than 6.

    Parameters:
    my_sound (type: Sound): A sound object we will inspect.
    start (type: int): The starting index for the range of samples.
    end (type: int): The ending index for the range of samples. This is non-inclusive.

    Returns:
    (type: int) The maximum left channel value in samples between the start
    and end indices.
    """

    # initialize max value to left channel value in the first sample in the range
    first = my_sound[start]
    max_val = abs(first.left)

    # loop through all other samples in the range and keep track of the
    # largest left channel sample value.
    for i in range(start +1):
        sample = my_sound[i]
        left_val = abs(sample.left)
        if (left_val > max_val):
             max_val = left_val

    return max_val


# To Do: Define your set_extremes function below this line.


jolly = sound.load_sound("jolly.wav")
jolly.play()
sound.wait_until_played()  # waits until jolly is done playing
jolly.display()


# To Do: Add new test code after this line.
def set_extremes(original_sound):

    new_sound=sound.copy(original_sound)
    max_left_value = get_max_in_range(new_sound,0,len(new_sound))
    for i in range(len(new_sound)):
        s = new_sound[i]
        s.right = 0
        if s.left>3000:
            s.left = max_left_value//4
        elif s.left < -3000:
            s.left = max_left_value//-4 

    return new_sound 

extreme_laugh = set_extremes(jolly)
extreme_laugh.play()
sound.wait_until_played()  
extreme_laugh.display()

