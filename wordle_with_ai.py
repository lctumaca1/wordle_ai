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


used_word_list = []
word_list = []

def check_word(word, user_guess):

    list = [grey, grey, grey, grey, grey]

    for x in range(0, 5):
        if user_guess[x] in word:
            list[x] = yellow

        if word[x] == user_guess[x]:
            list[x] = green

    return list

def find_correct_word(word, user_guess):
    result = check_word(word, user_guess)
    print(user_guess)
    if result == [grey, grey, grey, grey, grey]: # 새로운 단어 넣어줘야함
        new_word = word_list[random.randint(0, len(word_list)-1)].upper()[:5]
        return find_correct_word(word, new_word)
    else:
        print("hi");


def check_guess(turns, word, user_guess, window):
    render_list = ['', '', '', '', '']
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
    list = find_correct_word('APPLE', 'YYYYY')
    exit()
    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ''
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
            guess = ai_guess

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
                if win == False:
                    ai_guess = word_list[random.randint(0, len(word_list)-1)].upper()[:5] # 초기에는 랜z덤 단어로 세팅
                    # 분석 필요
                    guess = ai_guess
                    time.sleep(2000)

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