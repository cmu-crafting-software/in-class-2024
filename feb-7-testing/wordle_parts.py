def is_five_letters(word):
    if(len(word)==5):
       return True
    return False

def is_yellow(guessword, actualword, guess_position):
    position_in_actualworld = actualword.find(guessword[guess_position])
    if position_in_actualworld > -1:
        if(position_in_actualworld == guess_position):
            return False
        #handle case where letter has already appeared
        #eeabc   eabcd  pos 1
        #xeabe   xxabe
        if guessword[0:guess_position].find(guessword[guess_position]) > -1:
            return False
        return True
    else:
        return False

def is_green(guessword, actualword, guess_position):
    position_in_actualword = actualword.find(guessword[guess_position])
    if position_in_actualword == guess_position:
        return True
    return False
 