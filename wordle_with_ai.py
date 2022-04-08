import random, pygame, sys
from pygame.locals import *
pygame.init()
import time

white = (255, 255, 255)
yellow = (201, 180, 88)
grey = (120, 124, 126)
black = (0, 0, 0)
green = (106, 170, 100)
all_green = [green, green, green, green, green]
all_grey = [grey, grey, grey, grey, grey]
light_green = (153, 255, 204)
font = pygame.font.SysFont('Helvetica neue', 40)
big_font = pygame.font.SysFont('Helvetica neue', 80)

you_win = big_font.render('You Win!', True, light_green)
you_lose = big_font.render('You Lose!', True, light_green)
play_again = big_font.render('Play Again?', True, light_green)


win_word_list = []
word_list = []

def get_random_word():
    # 실제 wordle 게임은 한 단어를 입력할때 존재하는 단어로 입력해야 다음 단어를 입력할 수가 있기 때문에 word_list에서 한 단어 가져옴.
    return word_list[random.randint(0, len(word_list)-1)].upper()[:5]

def check_word(word, user_guess):

    list = all_grey

    for x in range(0, 5):
        if user_guess[x] in word:
            list[x] = yellow

        if word[x] == user_guess[x]:
            list[x] = green

    return list

def check_condi(type_list, user_word):
    print(f'FUNC: check_condi(type_list={type_list}, user_word={user_word})')
    
    for word, x in enumerate(word_list):
        for type, y in enumerate(type_list):
            if type == grey and word[y]: # grey check
                pass
    exit()
    # return_list.append(user_word)
    # return word_list

def find_correct_word(winning_word, ai_guess):
    if ai_guess == "": # 비어있으면 그냥 빈 공백 리턴
        return ""
    else:
        result = check_word(winning_word, ai_guess)
        print(ai_guess)
        if result == all_grey: # 새로운 단어 넣어줘야함
            new_word = get_random_word()
            return find_correct_word(winning_word, new_word)
        else:
            a = check_condi(result, ai_guess)[0]
            print(a)



def check_guess(turns, word, user_guess, window):
    render_list = [None, None, None, None, None]
    spacing = 0
    guess_colour_code = all_grey

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

    if guess_colour_code == all_green:
        return True

# function main
def main():
    word_list_file = open('./wordList.txt', 'r', encoding = 'utf-8') # read word list 
    global word_list # word_list를 전역 변수로 선언하고 이곳저곳에서 사용할 수있도록 global 사용
    word_list = word_list_file.readlines() # word_list에 행을 기준으로 배열로 저장
    winning_word = get_random_word() # 정답 단어 세팅.
    
    window_height = 600 # pygame window height
    window_width = 500 # pygame window width

    game_fps = 60 # game_fps 세팅
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((window_width, window_height))
    window.fill(black)

    guess = None
    # 원래라면 문자마다 분석해서 효율적인 단어쓰는 것이 일반적.

    print(f'The winning word is {winning_word}')

    # visual setting
    for x in range(0,5): 
        for y in range(0,5):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (x * 80), 50 + (y * 80), 50, 50),2)

    pygame.display.set_caption('WORDLE WITH AI')

    turns = 0 # 턴 수 (normal: 5, 5글자 단어들이기때문에 5)
    win = False # 정답 여부

    while True:
        for event in pygame.event.get():

            # ai_guess는 초기에 랜덤한 값으로 초기화
            # 어떤 단어가 나오는지는 처음부터 예상이 안되기때문에 힌트를 얻기위한 사전작업
            ai_guess = "" # word_list에서 실제로 존재하는 단어 중 하나의 단어 가져옴.
            if not turns > 5:
                ai_guess = get_random_word()
            guess = find_correct_word(winning_word, ai_guess)
            
            if event.type == QUIT:
                pygame.exit()
                sys.exit()


            if win == True: # 정답 맞출 시에 재시작하지않고 게임 종료
                pass
                # main()

            if turns == 6: # 6행 모두 입력 시 재시작 하지않고 pass
                guess = "qwewqe"
                pass
                # main()

            if len(guess) > 4:
                win = check_guess(turns, winning_word, guess, window)
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
        clock.tick(game_fps)

main()