import random

def player_check(hidden_colors,guess,all_colors):
    correct_answer_count = 0
    clue = []
    checked_hidden_colors = hidden_colors.copy()
    checked_guess = guess.copy()
    color_inx = 0
    while(True):
        try:            
            if(checked_hidden_colors[color_inx] == checked_guess[color_inx]):
                clue.append(2);
                correct_answer_count = correct_answer_count + 1
                checked_hidden_colors.pop(color_inx)
                checked_guess.pop(color_inx)
            else:
                color_inx = color_inx + 1 
        except IndexError:
            break
    if (correct_answer_count == 4):
        print("The guess is correct. You win!")
        return True
    else:
        for color in all_colors.values():
            clue.extend([1]*min(checked_guess.count(color),checked_hidden_colors.count(color)))
        clue.sort()
        print("Clue : " , clue)
        return False

def player_codebreaker(all_colors):
    counter = 0
    hidden_colors = []
    flag = False
    for i in range(4):
        c = random.randint(0,len(all_colors)-1)
        hidden_colors.append(all_colors[c])
    while(counter < 10):
        guess = []
        print ("Make a guess of four colors:")
        print ("----------------")
        for key, value in all_colors.items():
            print("{0} - {1}".format(key,value))
        print ("----------------")
        itr = 0;
        while(itr < 4):
            try:
                guess_color = int(input("Guess color : "))
                guess.append(all_colors[guess_color])
                itr = itr + 1
            except ValueError:
                print("Use numbers to choose color.")
            except KeyError:
                print("Your number isn't in list.")
        print ("Your guess:\n",guess)
        flag = player_check(hidden_colors,guess,all_colors)
        if(flag):
            return
        counter = counter + 1
    else:
        print("You lose!")
        print("Correct answers are:\n",hidden_colors)
        return
    

def computer_codebreaker(all_colors):
    return 0;

def main():
    all_colors = {0:'red',1:'orange',2:'yellow',3:'green',4:'blue',5:'purple'}
    print("Choose who will be codebreaker.")
    print("1 - You")
    print("2 - Computer")
    game_options = {1: True, 2: False}
    while(True):
        try:
            game_mode = game_options[int(input("Option: "))]
            break
        except ValueError:
            print("Use numbers to choose color.")
        except KeyError:
            print("Enter option from list.")
    if (game_mode):
        player_codebreaker(all_colors)
    else:
        computer_codebreaker(all_colors)
    return 0

main()
