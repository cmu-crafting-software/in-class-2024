#Select Random word

#Read in guess from command line

#check correctness of guess

def guess_word_checker(guess_word,target_word):
    #for loop to check each character
    #if guess is correct
    answer = ""
    if guess_word == target_word:
        return "*****"
    #for loop to check each character
    for position in range(0,5,1):
        # print(position)
        # print(guess_word[position])
        # print(target_word[position])
        if guess_word[position] == target_word[position]:
            # print("before"+answer)
            answer += "*"
            # print("after"+answer)
        elif guess_word[position] in target_word:
            # print("Found in target word")
            answer += "!"
        else:
            answer += "_"
    return answer    

#is a character in the word but not in the right place
# print(guess_word_checker("piano","piano"))
# **!__
print(guess_word_checker("piano","pizza"))
    #is guess a real word
    #are letters correct?
    #are letters in the wrong spot?
    # return <data>
#if correct, print win

#if not, give feedback, expect next guess
