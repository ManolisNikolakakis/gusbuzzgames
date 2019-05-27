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


# DIFFICULTY #

LETTERS_EASY = ['D', 'F', 'J', 'K']

DIFFICULTY = {
    'easy': (
        pygame.K_d,
        pygame.K_f,
        pygame.K_j,
        pygame.K_k
    ),
    'medium': (
        pygame.K_a,
        pygame.K_s,
        pygame.K_d,
        pygame.K_f,
        pygame.K_h,
        pygame.K_j,
        pygame.K_k,
        pygame.K_l
    ),
    'hard': (
        pygame.K_q,
        pygame.K_w,
        pygame.K_a,
        pygame.K_s,
        pygame.K_p,
        pygame.K_o,
        pygame.K_l,
        pygame.K_k,
        pygame.K_c,
        pygame.K_v,
        pygame.K_n,
        pygame.K_m,
        pygame.K_g,
        pygame.K_h,
        pygame.K_t,
        pygame.K_b
    )
}

MATCHING_EVENTS_TO_LETTERS = {
    'D': pygame.K_d,
    'F': pygame.K_f,
    'J': pygame.K_j,
    'K': pygame.K_k
}
