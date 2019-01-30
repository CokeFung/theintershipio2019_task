import random

def string2list(str):
    """ Coonvert string to list"""
    return str.replace("\n", "").split(", ")

def readCategoryNWord():
    """ Read categories and words from file """
    with open("./resource/category_list.txt", "r") as category_list_file:  #read category from "category.txt"
        category_list = category_list_file.read()[3:]
        category_list = string2list(category_list)

    word_list = {}
    for category_name in category_list:   #read all words in category
        with open("./resource/"+category_name+".txt", "r") as temp_category:
            temp_category = temp_category.read()[3:]
            word_list[category_name] = string2list(temp_category)

    return category_list, word_list

def chooseCategory(category_list):
    """ Menu : user must a category """
    while(True):
        print("\nSelect a number of category :")
        for i in range(len(category_list)):
            print("\t%d. %s" % (i+1, category_list[i]))
        print("\nSelect : ", end="")
        selected_index = input()
        if (checkNumber(selected_index)):
            selected_index = int(selected_index)
            if selected_index-1 in range(len(category_list)):
                return selected_index-1
            else:
                print("!! Number is out of range !!", end="\n\n")
                continue
        else:
            print("!! Type only a Number !!", end="\n\n")
            continue

def checkNumber(number):
    """ Check type of input (int)"""
    try:
        number = int(number)
        return True
    except ValueError:
        return False

def checkChar(char):
    """ Check tye of input (char)"""
    if char.isalpha() and len(char) == 1:
        return True
    else:
        return False

def createHiddenAnswer(hidden_word):
    """ Convert word to hidden answer """
    tmp = ""
    for i in hidden_word:
        if i.isalpha():
            tmp += "_"
        else:
            tmp += i
    return tmp

def calculateScore(score, current_answer, hidden_word, char_answer):
    """ Calculate score from user's guessing character """
    if char_answer in hidden_word and (not char_answer in current_answer):
        temp = ""
        for i in range(len(hidden_word)):
            if hidden_word[i] == char_answer and  not char_answer == current_answer[i]:
                temp += char_answer
                score += 10
            else:
                temp += current_answer[i]
    elif char_answer in hidden_word and char_answer in current_answer:
        temp = current_answer
    else:
        temp = current_answer
        score -= 1
    return  temp == hidden_word,score, temp, char_answer


def guessAnswer(score, current_answer, hidden_word):
    """ User must guess a character a-z """
    while True:
        print("\nGuess a character : ", end="")
        char_answer = input().lower()
        if checkChar(char_answer):
            return calculateScore(score, current_answer, hidden_word, char_answer)
        else:
            print("\n!! Type only a character a-z !!")
            continue

def playAgain():
    """ Wanna play again? """
    temp = "x"
    while not (temp == "y" or temp == "n"):
        print("Wanna play again?(y/n)\n>", end="")
        temp = input().lower()
    return temp

def main():

    category_list, word_list = readCategoryNWord()
    while(True):
        selected_category = chooseCategory(category_list)
        word_index = random.randint(0, len(word_list[category_list[selected_category]])-1)
        hidden_word, hint = word_list[category_list[selected_category]][word_index].split("::")
        print("\nHint : \"%s\"" % hint.capitalize())
        score = 0
        guessed_times = 0
        guessed_char = {}
        current_answer = createHiddenAnswer(hidden_word)
        while(True):
            guessed_times += 1
            print("\n\t", end="")
            for i in current_answer:
                print(i, end=" ")
            print()
            isEnd, score, current_answer, last_guess = guessAnswer(score, current_answer, hidden_word)
            if not last_guess in guessed_char:
                guessed_char[last_guess] = 1

            if isEnd == True:
                print("\nExcellent,answer is " + hidden_word + ".")
                print("Guessed character :", *guessed_char.keys())
                print("Guessed %d times.\n" % guessed_times)
                show_score = "Your score is %d." % score
                print("-"*(len(show_score)+4))
                print("| " + show_score + " |")
                print("-"*(len(show_score)+4))
                break
            print("Guessed character :", *guessed_char.keys())
            print("Guessed %d times.\n" % guessed_times)
        play_again = playAgain()
        if play_again == "n":
            break
    print("\n  T - T Good bye T - T ")
main()


