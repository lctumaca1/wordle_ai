import random, pygame, sys
from pygame.locals import *
pygame.init()
import time

white = (255, 255, 255)
yellow = (201, 180, 88)
grey = (120, 124, 126)
black = (0, 0, 0)
green = (106, 170, 100)
light_green = (153, 255, 204)
font = pygame.font.SysFont('Helvetica neue', 40)
big_font = pygame.font.SysFont('Helvetica neue', 80)

you_win = big_font.render('You Win!', True, light_green)
you_lose = big_font.render('You Lose!', True, light_green)
play_again = big_font.render('Play Again?', True, light_green)


win_word_list = []
word_list = []

def check_word(word, user_guess):

    list = [grey, grey, grey, grey, grey]

    for x in range(0, 5):
        if user_guess[x] in word:
            list[x] = yellow

        if word[x] == user_guess[x]:
            list[x] = green

    return list

def check_condi(type_list, user_word):
    return_list = []
    no_letter_list = []
    contain_letter_list = []
    correct_letter_list = [None, None, None, None, None]

    for i, type in enumerate(type_list):
        if type == grey:
            no_letter_list.append(user_word[i])
        
        if type == yellow:
            contain_letter_list.append(user_word[i])

        if type == green:
            correct_letter_list[i] = user_word[i]

    contain_letter_list = list(set(contain_letter_list))

    global word_list

    list1 = []
    list2 = []
    list3 = []

    print(f'CONTAIN LETTER LIST {contain_letter_list}')

    for x, word in enumerate(word_list):
        for no_letter in no_letter_list:
            if no_letter not in word:
                list1.append(word)

        for contain_letter in contain_letter_list:
            all_count = len(contain_letter_list)
            local_count = 0

            if contain_letter in word.upper():
                local_count += 1
            
            if all_count == local_count:
                list2.append(word)
        
        for y, correct_letter in enumerate(correct_letter_list):
            if correct_letter != None:
                if word[y].upper() == correct_letter:
                    list3.append(word)

    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    print(set1 & set2 & set3)
    



    exit()

    # for word in word_list:
    #     if correct_letter_list != [None, None, None, None, None]:
    #         count = 0
    #         for x, correct_letter in enumerate(correct_letter_list):
    #             if correct_letter == None:
    #                 continue
    #             else:
    #                 if word[x] == correct_letter:
    #                     count += 1
    #         print(f'asdasd {count}')

        
    # return_list.append(user_word)
    return word_list

def find_correct_word(word, user_guess):
    result = check_word(word, user_guess)
    print(user_guess)
    if result == [grey, grey, grey, grey, grey]: # 새로운 단어 넣어줘야함
        new_word = word_list[random.randint(0, len(word_list)-1)].upper()[:5]
        return find_correct_word(word, new_word)
    else:
        a = check_condi(result, user_guess)[0]
        print(a)



def check_guess(turns, word, user_guess, window):
    render_list = [None, None, None, None, None]
    spacing = 0
    guess_colour_code = [grey ,grey, grey, grey, grey]

    for x in range(0, 5):
        if user_guess[x] in word:
            guess_colour_code[x] = yellow

        if word[x] == user_guess[x]:
            guess_colour_code[x] = green

    list(user_guess)

    for x in range(0,5):
        render_list[x] = font.render(user_guess[x], True, white)
        pygame.draw.rect(window, guess_colour_code[x], pygame.Rect(60 + spacing, 50 + (turns * 80), 50, 50))
        window.blit(render_list[x], (75.8 + spacing, 62 + (turns * 80)))
        spacing += 80

    if guess_colour_code == [green, green, green, green, green]:
        return True

# function main
def main():
    file = open('./wordList.txt', 'r', encoding = 'utf-8') # read word list 
    global word_list
    word_list = file.readlines()
    word = word_list[random.randint(0, len(word_list)-1)].upper()
    
    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = None
    # 원래라면 문자마다 분석해서 효율적인 단어쓰는 것이 일반적.

    print(f'current word is {word}')

    for x in range(0,5):
        for y in range(0,5):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (x * 80), 50 + (y * 80), 50, 50),2)

    pygame.display.set_caption('WORDLE')

    turns = 0
    win = False

    while True:

        for event in pygame.event.get():

            ai_guess = word_list[random.randint(0, len(word_list)-1)].upper()[:5] # 초기에는 랜덤 단어로 세팅
            guess = find_correct_word(word, ai_guess)
            
            if event.type == QUIT:
                pygame.exit()
                sys.exit()

            if win == True:
                main()

            if turns == 6:
                main()

            if len(guess) > 4:
                win = check_guess(turns, word, guess, window)
                turns += 1

                window.fill(black, (0, 500, 500, 200))

        window.fill(black, (0, 500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.blit(you_win, (90, 200))
            window.blit(play_again, (60, 300))

        if turns == 6 and win != True:
            window.blit(you_lose, (90, 200))
            window.blit(play_again, (60, 300))
        pygame.display.update()
        clock.tick(FPS)

main()