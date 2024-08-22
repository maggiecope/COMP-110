"""
Module: song_generator

Module with functions for PSA #4 of COMP 110 (Fall 2019).

Authors:
1) Maggie Cope - mcope@sandiego.edu
2) Sophia Zaboukos - szaboukos@sandiego.edu
"""

import sound

# Do NOT modify the scale_volume function
def scale_volume(original_sound, factor):
    """
    Decreases the volume of a sound object by a specified factor.

    Paramters:
    original_sound (type; Sound): The sound object whose volume is to be decreased.
    factor (type: float): The factor by which the volume is to be decreased.

    Returns:
    (type: Sound) A new sound object that is a copy of original_sound, but with volumes
    scaled by factor.
    """

    scaled_sound = sound.copy(original_sound)

    for smpl in scaled_sound:
        # Scale left channel of smpl
        current_left = smpl.left
        scaled_left = round(current_left * factor)
        smpl.left = scaled_left

        # Scale right channel of smpl
        current_right = smpl.right
        scaled_right = round(current_right * factor)
        smpl.right = scaled_right

    return scaled_sound


def mix_sounds(snd1, snd2):
    """
    Mixes together two sounds (snd1 and snd2) into a single sound.
    If the sounds are of different length, the mixed sound will be the length
    of the longer sound.

    This returns a new sound: it does not modify either of the original
    sounds.

    Parameters:
    snd1 (type: Sound) - The first sound to mix
    snd2 (type: Sound) - The second sound to mix

    Returns:
    (type: Sound) A Sound object that combines the two parameter sounds into a
    single, overlapping sound.
    """
    s1 = sound.copy(snd1)
    s2 = sound.copy(snd2)

    #looks at two sounds and makes a copy of the longer sound, longer_sound, 
    #  and a copy of the shorter sound,  shorter_sound
    if len(s1) > len(s2):
        longer_sound = s1
        shorter_sound = s2
    else:
        longer_sound = s2
        shorter_sound = s1

    #loops through the samples of the shorter sound, and adds
    # the shorter sound’s channel values to the longer sound’s channel values.

    for i in range(len(shorter_sound)):
        short_sample = shorter_sound[i]
        long_sample = longer_sound[i]
        long_sample.left = long_sample.left + short_sample.left
        long_sample.right = long_sample.right + short_sample.right
    
    #returns a new sound object which is a mix of two sounds 
    return longer_sound
    
       



        






def song_generator(notestring):
    """
    Generates a sound object containing a song specified by the notestring.

    Parameter:
    notestring (type: string) - A string of musical notes and characters to
    change the volume and/or octave of the song.

    Returns:
    (type: Sound) A song generated from the notestring given as a paramter.
    """
    song1 = sound.create_silent_sound(1)
    song2 = sound.create_silent_sound(1)
    sound_1 = ""
    sound_2 = ""
    upper_notestring = ""
    default = 1.0
    vol = 1.0 
    sound_length = 14700
    pause = sound.create_silent_sound(sound_length)
    split = False
    x=0
    
    #makes all of the characters upper-case
    for note in notestring:
        note_upper = note.upper()
        upper_notestring = upper_notestring + note_upper

    #makes it so mutliple parts that are mixed together in the final sound 
    for i in upper_notestring:
        if i == "|":
            split = True 
        if split ==True:
            sound_2 = sound_2 + i 
        else:
            sound_1 = sound_1 + i
            

    for n in sound_1:
        #checks note length
        if n in ["0","1","2","3","4","5","6","7","8","9"]:
            sound_length = 14700 * int(n)  
        
        #checks octave
        elif n == "<":
            x = x - 1
        elif n ==">":
            x = x + 1   

         #checks volume     
        elif n == "+":
            vol = vol + 0.2
        elif n == "-":
            vol = vol - 0.2 

        #checks for which note to make 
        elif n in ["A", "B", "C", "D", "E", "F", "G" ]:
            new_note = sound.Note(n,sound_length, octave = x)
            new_note_volume = scale_volume(new_note,vol)
            song1 = song1 + new_note_volume
            sound_length = 14700
        
        #checks for pause 
        elif n == "P":
            new_note = pause
            new_note_volume = scale_volume(new_note,vol)
            song1 = song1 + new_note_volume
            
            sound_length = 14700

    for n in sound_2:
        #checks note length
        if n in ["0","1","2","3","4","5","6","7","8","9"]:
            sound_length = 14700 * int(n) 

        #checks octave 
        elif n == "<":
            x = x - 1
        elif n ==">":
            x = x + 1  

        #checks volume       
        elif n == "+":
            vol = vol + 0.2
        elif n == "-":
            vol = vol - 0.2 
        
        #checks which note to play 
        elif n in ["A", "B", "C", "D", "E", "F", "G" ]:
            new_note = sound.Note(n,sound_length, octave = x)
            new_note_volume = scale_volume(new_note,vol)
            song2 = song2 + new_note_volume
            sound_length = 14700
        
        #checks for pause 
        elif n == "P":
            new_note = pause
            new_note_volume = scale_volume(new_note,vol)
            song2 = song2 + new_note_volume
            sound_length = 14700
        
        
    #returns a new sound object
    return mix_sounds(song1, song2)




"""
Don't modify anything below this point.
"""

def main():
    """
    Asks the user for a notestring, generates the song from that
    notestring, then plays the resulting song.
    """
    import sounddevice
    print("Enter a notestring (without quotes):")
    ns = input()
    song = song_generator(ns)
    song.play()
    sounddevice.wait()

if __name__ == "__main__":
    main()
