
#Realisation of Mastermind game. 
#In the game of Mastermind, one player, the codemaker (in this case the computer)
#chooses four colored “pegs” in a particular order. The codebreaker (the human 
#player) tries to guess the chosen colors by placing four pegs in the guessed order.
#For each guess, the codemaker provides a clue about how well the codebreaker
#guessed. The codebreaker has 10 guesses to break the code.
#The program allows computer be codebreaker first and try to geuss players colors.
#Then switch and let the human be the codebreaker, and the computer be the codebreaker.
#Then compute how many guesses it takes for human and computer and deside who win.
#Codebreaker with less guesses wins.

import random

#This function checks if the player's guess is correct. Otherwise it gives a clue.
#If player guesses the color and the position of color, function adds to clue 2 and delete this colors from guess and hidden_color. If player doesn't guess position,  
#algorithm comperes amout of "guess" in "hidden_colors" and adds ones to clue that equal minimum amount of color in "guess" or "hidden_colors".
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

#Function reads players guess and give it to player_check function.
def player_codebreaker(all_colors,game_rounds = 10):
    current_round = 1
    hidden_colors = []
    clue = []
    for i in range(4):
        c = random.randint(0,len(all_colors)-1)
        hidden_colors.append(all_colors[c])
    while(current_round <= game_rounds):
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
        current_round = current_round + 1
    else:
        print("You lose!")
        print("Correct answers are:\n",hidden_colors)
        return

#Function switch cloros in color array for computer_solution functions
def switch_colors(colors_array,first_position,second_position):
    color = colors_array[first_position]
    colors_array[first_position] = colors_array[second_position]
    colors_array[second_position] = color
    return colors_array

#Function finds guessed by player colors. On the first stage it finds all colors in "guessed_colors".
#On the second stage it find position of colors by replacing each color with next color and compere best clue
#with clue that recived on current step.
def computer_solution(guessed_colors,all_colors):
    game_round = 0
    itr_color = 0
    color_position = 0
    computer_colors =  []
    computer_colors.append(all_colors[itr_color])
    computer_colors = computer_colors * 4
    current_position = 0
    next_position = 1
    best_clue = []
    while(True):
        game_round = game_round + 1 
        clue = player_check(guessed_colors, computer_colors, all_colors)
        print("Guess: ", computer_colors)
        print("Clue: ", clue)
        if(clue == [0]):
            print("I found your colors:\n", computer_colors)
            return game_round
        if(len(clue) == 4):
            if(clue.count(2) > best_clue.count(2) and best_clue != []):
                next_position = next_position + 1
                best_clue = clue.copy()
            elif(clue.count(2) <= best_clue.count(2)):
                computer_colors = switch_colors(computer_colors, current_position, next_position)
                next_position = next_position + 1
            elif(prev_clue == []):
                best_clue = clue.copy()
            if (next_position == 4):
                current_position = current_position + 1
                next_position = current_position + 1
            computer_colors = switch_colors(computer_colors, current_position, next_position)
        else:
            itr_color = itr_color + 1
            for i in range(len(clue)- len(guessed_colors),0):
                computer_colors[i] = all_colors[itr_color]
                
    return game_round


#Function reads chosen by player colors and run computer_solution function to guess player`s colors.
def computer_codebreaker(all_colors):
    guessed_colors = []
    itr = 0
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
    game_rounds = computer_solution(guessed_colors,all_colors)
    print("Your turn. You have {0} tries.".format(game_rounds))
    player_codebreaker(all_colors,game_rounds)
    return

#Main menu
def main():
    all_colors = {0:'red',1:'orange',2:'yellow',3:'green',4:'blue',5:'purple'}
    game_options = {1: "Player", 2: "Computer vs Player", 3:"Exit"}
    while(True):
        print("Choose who will be codebreaker.")
        for key, value in game_options.items():
            print("{0} - {1}".format(key,value))    
        while(True):
            try:
                game_mode = game_options[int(input("Option: "))]
                break
            except ValueError:
                print("Use numbers to choose color.")
            except KeyError:
                print("Enter option from list.")
        if (game_mode == "Player"):
            player_codebreaker(all_colors)
        elif(game_mode == "Computer vs Player"):
            computer_codebreaker(all_colors)
        elif (game_mode == "Exit"):
            return

main()
