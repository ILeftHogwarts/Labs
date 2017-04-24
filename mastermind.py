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
        clue = [0]
        return clue
    else:
        for color in all_colors.values():
            clue.extend([1]*min(checked_guess.count(color),checked_hidden_colors.count(color)))
        clue.sort()
        return clue

def player_codebreaker(all_colors):
    game_round = 0
    hidden_colors = []
    clue = []
    for i in range(4):
        c = random.randint(0,len(all_colors)-1)
        hidden_colors.append(all_colors[c])
    while(game_round < 10):
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
        clue = player_check(hidden_colors,guess,all_colors)
        if(clue == [0]):
            print("The guess is correct. You win!")
            return
        else:
            print("Clue : " , clue)
        game_round = game_round + 1
    else:
        print("You lose!")
        print("Correct answers are:\n",hidden_colors)
        return
    
def computer_solution(guessed_colors,all_colors):
    game_round = 0
    itr_color = 0
    color_position = 0
    computer_colors = all_colors[itr_color]*4
    current_position = 0
    next_position = 1
    while(True):
        game_round = game_round + 1 
        clue = player_check(guessed_colors,computer_colors)
        if(clue == [0]):
            print("I found your colors:\n",computer_colors)
            return
        else:
            if(len(clue) == 4):
                if(clue == [1,1,1,1]):
                    color = computer_colors[current_color]
                    computer_colors[current_color] = computer_colors[next_color]
                    computer_colors[next_color] = color
                    if(prev_clue == clue):
                        
                else if(clue == [1,1,1,2]):
                    
                else if(clue == [1,1,2,2]):
            else:
                itr_color = itr_color + 1
                for i in range(len(guess_colors)-len(clue),0):
                    computer_color[i] = all_colors[itr_color]
                
    return

def computer_codebreaker(all_colors):
    guessed_colors = []
    print ("Choose four colors for computer guessing:")
    print ("----------------")
    for key, value in all_colors.items():
        print("{0} - {1}".format(key,value))
    print ("----------------")
    while(itr < 4):
        try:
            color = int(input("Your color : "))
            guessed_colors.append(all_colors[color])
            itr = itr + 1
        except ValueError:
            print("Use numbers to choose color.")
        except KeyError:
            print("Your number isn't in list.")
    
    return

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
    return

main()
