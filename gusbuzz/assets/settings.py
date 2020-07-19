import pygame

# SCREEN #

SIZE = WIDTH, HEIGHT = 900, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0

# MUSIC #

INFINITE_MUSIC_LOOP = -1
MAIN_TUNE = 'resources/sounds/Tune1.mp3'

# BACKGROUND #

BACKGROUND_IMAGE = 'resources/images/game_image.jpg'
BACKGROUND_IMAGE_STARTING_POINT = (0, 0)  # Always start from the top

# SAVEFILES #

SAVE_LOCATION = {
    'EASY': 'resources/saveslots/savefileEasy.txt',
    'MEDIUM': 'resources/saveslots/savefileMedium.txt',
    'HARD': 'resources/saveslots/savefileHard.txt'
}

# PRINT TEXTS #

text_game_over = "GAME OVER, mofo"
text_escape = "PRESS ESCAPE TO QUIT THE GAME"
text_retry = "PRESS R TO RETRY"
text_start = "PRESS F TO START"

text_easy_mode = "PRESS E FOR EASY (4 letters)"
text_medium_mode = "PRESS M FOR MEDIUM (8 letters)"
text_hard_mode = "PRESS H FOR HARD (19 letters)"

# SPRITES #

sprites_directory =  "resources/sprites/"
sprites_format = ".png"

# DIFFICULTY # 

# TO BE CHECKED BECAUSE THE LETTERS AT THE MOMENT ARE COMPLETELY RANDOM

LETTERS_EASY = ['D', 'S', 'J', 'K']
LETTERS_MEDIUM = ['A', 'S', 'D', 'F', 'H', 'J', 'K', 'L']
LETTERS_HARD = ['A', 'S', 'D', 'F', 'H', 'J', 'K', 'L', 'Q', 'W', 'P', 'O', 'C', 'V', 'N', 'M', 'G', 'T', 'B']

MODE = {
    'EASY': LETTERS_EASY,
    'MEDIUM': LETTERS_MEDIUM,
    'HARD': LETTERS_HARD
}

MATCHING_EVENTS_TO_LETTERS = {
    'A': pygame.K_a,
    'S': pygame.K_s,
    'D': pygame.K_d,
    'F': pygame.K_f,
    'H': pygame.K_h,
    'J': pygame.K_j,
    'K': pygame.K_k,
    'L': pygame.K_l,
    'Q': pygame.K_q,
    'W': pygame.K_w,
    'P': pygame.K_p,
    'O': pygame.K_o,
    'C': pygame.K_c,
    'V': pygame.K_v,
    'N': pygame.K_n,
    'M': pygame.K_m,
    'G': pygame.K_g,
    'T': pygame.K_t,
    'B': pygame.K_b
}
