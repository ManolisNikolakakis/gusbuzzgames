import pygame
import time
from assets import settings
from text import Text

# many of these functions can (and should) potentially go to their own class

def game_bootloader():
    # pygame.display.set_icon(surface) // add some sort of icon to the game
    pygame.display.set_caption("Project Jacob")

def load_splash_screen(screen, font):

    screen.fill(settings.BLACK)

    text = font.render("Presented by...", True, settings.WHITE)
    screen.blit(text, [350, 270])

    text = font.render("GusBuzzGames", True, settings.WHITE)
    screen.blit(text, [350, 300])

    pygame.display.flip()

    time.sleep(1)

def game_over(screen, font):
    screen.fill(settings.BLACK)

    text = font.render(settings.text_game_over, True, settings.RED)
    screen.blit(text, [270, 270])

    pygame.display.flip() 

    time.sleep(2)

    text = font.render(settings.text_retry, True, settings.WHITE)
    screen.blit(text, [270, 320])  
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                ready_to_start(screen, font)
                return

def ready_to_start(screen, font):

    screen.fill(settings.BLACK)

    start_message = Text(settings.text_start, 310, 270, settings.RED)
    start_message.print_on_screen(font, screen)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                return

def refill_screen(screen, backGround, font, score, current_letter, difficulty, savefile, counter):

    screen.fill(settings.BLACK)
    screen.blit(backGround.image, backGround.rect)

    text = font.render("High Score", True, settings.WHITE)
    screen.blit(text, [settings.WIDTH - 150, 10])

    text = font.render(str(savefile.high_score), True, settings.WHITE)
    screen.blit(text, [settings.WIDTH - 150, 40])

    text = font.render("Current Score", True, settings.WHITE)
    screen.blit(text, [10, 10])

    text = font.render(str(score), True, settings.WHITE)
    screen.blit(text, [10, 40])

    text = font.render("Random Letter", True, settings.WHITE)
    screen.blit(text, [10, 70])
 
    text = font.render(current_letter.value, True, settings.WHITE)
    screen.blit(text, [10, 100])

    text = font.render("Countdown", True, settings.WHITE)
    screen.blit(text, [10, 150])

    text = font.render(str(counter), True, settings.WHITE)
    screen.blit(text, [10, 180])

    if difficulty.mode == 'EASY':
        screen.blit(difficulty.letter_sprite[current_letter.value],(current_letter.width, current_letter.height))
    
    pygame.display.flip()

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
