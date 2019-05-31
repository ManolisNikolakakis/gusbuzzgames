import pygame
from assets import settings

# many of these functions can (and should) potentially go to their own class

def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load(settings.MAIN_TUNE)
    pygame.mixer.music.play(settings.INFINITE_MUSIC_LOOP)

def increase_score(score, high_score):
    score = score + 10
    if score > high_score:
        high_score = score
    return score, high_score

def decrease_score(score):
    score = score - 10
    return score

def set_score_to_zero(score):
    score = 0;
    return score

def load_images(difficulty, letter_sprite):
    for letter in difficulty:
        letter_sprite[letter] = pygame.image.load(settings.sprites_directory + letter.lower()+ settings.sprites_format)

def difficulty_selection(difficulty, screen, font, letter_sprite):
    text = font.render(settings.text_easy_mode, True, settings.RED)
    screen.blit(text, [310, 380])   

    text = font.render(settings.text_medium_mode, True, settings.RED)
    screen.blit(text, [310, 410])   

    text = font.render(settings.text_hard_mode, True, settings.RED)
    screen.blit(text, [310, 440])    

    pygame.display.flip()

    difficulty = False

    while not difficulty:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                difficulty = settings.LETTERS_EASY
                load_images(difficulty, letter_sprite)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                difficulty = settings.LETTERS_MEDIUM
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                difficulty = settings.LETTERS_HARD
    return difficulty