import random

def player_check(hiden_colors,guess):
    correct_answer_count = 0
    clue = []
    checked_hiden_colors = hiden_colors
    checked_guess = guess
    color_inx = 0
    for color in guess.values():
        clue_variant = 0
        start_inx = -1
        while (True):
            try:    
                inx = hiden_colors.index(color,start_inx+1)
            except:
                break
            else:
                if(inx == color_inx):
                    clue_variant = 2
                    correct_answer_count = correct_answer_count + 1
                    break
                else:
                    clue_variant = 1
                start_inx = inx
        color_inx = color_inx + 1
        if(clue_variant != 0):
            clue.append(clue_variant)
    clue.sort()
    if (correct_answer_count == 4):
        print("The guess is correct. You win!")
        return False
    else:
        print("Clue : " , clue)
        return True

def player_codebreaker(all_colors):
    counter = 0
    hiden_colors = {}
    flag = True
    for i in range(4):
        c = random.randint(0,len(all_colors)-1)
        hiden_colors[i] = all_colors[c]
    while(flag and counter < 10):
        guess = {}
        print ("Make a guess of four colors:")
        print ("----------------")
        for key, value in all_colors.items():
            print("{0} - {1}".format(key,value))
        print ("----------------")
        itr = 0;
        while(itr < 4):
            try:
                guess_color = int(input("Guess color : "))
                guess[itr] = all_colors[guess_color]
                itr = itr + 1
            except ValueError:
                print("Use numbers to choose color.")
            except KeyError:
                print("Your number isn't in list.")
        print ("Your guess:\n",guess)
        flag = player_check(hiden_colors,guess)
        counter = counter + 1
    else:
        print("You lose!")
        print("Correct answers are:\n",hiden_colors)    
    

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
