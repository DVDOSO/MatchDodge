
##############################################################
# I RECOMMEND THAT YOU DOWNLOAD THE CODE, REPL.IT LAGS A LOT #
#    MAKE SURE YOU HAVE PYGAME AND DOWNLOAD ALL THE ASSETS   #
##############################################################

import pygame
import random

pygame.init()

#Window Settings
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Match Dodge")

#Fonts
CALIBRI_GAME = pygame.font.SysFont("Calibri", 20, False, False)

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 227, 47)
YELLOW = (252, 252, 0)
RED = (250, 53, 27)
BLUE = (66, 176, 245)
PINK = (245, 66, 243)
ORANGE = (252, 182, 3)
TURQUOISE = (3, 252, 240)
PURPLE = (165, 3, 252)
DARK_GREEN = (10, 145, 30)
DARK_BLUE = (10, 48, 145)
LIGHT_RED = (255, 140, 125)
LIGHT_GREEN = (125, 255, 140)
GRAY = (190, 190, 190)
DARK_RED = (168, 50, 50)

#UI
game_UI_easy = pygame.image.load('Game_Easy.png').convert_alpha()
game_UI_medium = pygame.image.load('Game_Medium.png').convert_alpha()
game_UI_hard = pygame.image.load('Game_Hard.png').convert_alpha()
lose_UI = pygame.image.load('Lose.png').convert_alpha()
win_UI = pygame.image.load('Win.png').convert_alpha()
menu_UI = pygame.image.load('Menu.png').convert_alpha()
menu_UI_easy = pygame.image.load('Menu_Easy.png').convert_alpha()
menu_UI_medium = pygame.image.load('Menu_Medium.png').convert_alpha()
menu_UI_hard = pygame.image.load('Menu_Hard.png').convert_alpha()
instructions_UI = pygame.image.load('Instructions.png').convert_alpha()

#Music & Sounds
pygame.mixer.music.load('game_music.ogg')
game_over = pygame.mixer.Sound('game_over.wav')
damage_taken = pygame.mixer.Sound('damage_taken.wav')
matched = pygame.mixer.Sound('matched.wav')

clock = pygame.time.Clock()

#Window displays after the player matches all cards
def win():
    done = False

    #Stop the music and play the game over sound
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(game_over)

    while not done:
        #Background
        screen.blit(win_UI, (0, 0))

        #Mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Return Button        
        return_button_collision = pygame.Rect(275, 362, 250, 50)

        #Event loop
        for event in pygame.event.get():
            click = False
            
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN: #Detects if mouse is clicked
                click = True

            #Detects if button is clicked
            if return_button_collision.collidepoint((mouse_x, mouse_y)):
                if click:
                    menu()
                    pygame.quit()
                    return
        
        pygame.display.flip()
        clock.tick(60)


#Window displays after player loses all their health
def lose():
    done = False

    #Stops music and plays game over sound
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(game_over)

    while not done:
        #Background
        screen.blit(lose_UI, (0, 0))

        #Mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Return button        
        return_button_collision = pygame.Rect(275, 362, 250, 50)

        #Event Loop
        for event in pygame.event.get():
            click = False
            
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN: #Detects if mouse is clicked
                click = True

            #Detects if button is clicked
            if return_button_collision.collidepoint((mouse_x, mouse_y)):
                if click:
                    menu()
                    pygame.quit()
                    return
        
        pygame.display.flip()
        clock.tick(60)


#Easy difficulty
def easy():
    done = False

    #Play music
    pygame.mixer.music.play(-1)

    #Initialize card properties
    card_colours = [[GRAY] * 3 for i in range(2)] #Current colour of the card
    card_colour_master = [[None] * 3 for i in range(2)] #Intended colour of the card
    card_flip_master = [[False] * 3 for i in range(2)] #Whether the card is flipped
    cards_flipped = [] #Cards that are flipped at the moment

    #Generates a random permutation for the cards
    colours = [RED, RED, YELLOW, YELLOW, PINK, PINK] #Available colours for the difficulty
    for i in range(2):
        for j in range(3):
            random_value = random.randint(0, len(colours)-1)
            card_colour_master[i][j] = colours[random_value]
            del colours[random_value]

    #In game variables
    pairs_matched = 0

    time_delay = 0
    bullet_time_1 = 0
    bullet_time_2 = 0
    bullet_time_3 = 0
    bullet_time_4 = 0

    bullets_1 = []
    bullets_2 = []
    bullets_3 = []
    bullets_4 = []
    
    player_health = 100
    player_colour = GREEN
    player_x = 390
    player_y = 240
    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False

    while not done:
        
        #Card collisions
        card_1_1_collision = pygame.Rect(125, 80, 150, 150)
        card_1_1 = pygame.draw.rect(screen, card_colours[0][0], card_1_1_collision)

        card_1_2_collision = pygame.Rect(325, 80, 150, 150)
        card_1_2 = pygame.draw.rect(screen, card_colours[0][1], card_1_2_collision)


        card_1_3_collision = pygame.Rect(525, 80, 150, 150)
        card_1_3 = pygame.draw.rect(screen, card_colours[0][2], card_1_3_collision)

        card_2_1_collision = pygame.Rect(125, 270, 150, 150)
        card_2_1 = pygame.draw.rect(screen, card_colours[1][0], card_2_1_collision)

        card_2_2_collision = pygame.Rect(325, 270, 150, 150)
        card_2_2 = pygame.draw.rect(screen, card_colours[1][1], card_2_2_collision)

        card_2_3_collision = pygame.Rect(525, 270, 150, 150)
        card_2_3 = pygame.draw.rect(screen, card_colours[1][2], card_2_3_collision)

        screen.blit(game_UI_easy, (0, 0))

        #Draw player and collision
        player_collision = pygame.Rect(player_x, player_y, 20, 20)
        player = pygame.draw.rect(screen, player_colour, player_collision)

        player_colour = GREEN

        #Computes bullets from the TOP LEFT on the screen
        if bullet_time_1 >= 30:
            bullet_time_1 = 0
            bullets_1.append([0, 0, pygame.Rect(0, 0, 12, 12), random.randint(0,4)])
            #Bullets are given a random slope to travel

        delete_bullets_1 = [] #Bullets are going to be deleted if they fall off the screen

        #Draws the bullets onto the screen
        for i in range(len(bullets_1)):
            pygame.draw.rect(screen, DARK_RED, bullets_1[i][2])
            if bullets_1[i][3] == 0:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 4
            elif bullets_1[i][3] == 1:
                new_x = bullets_1[i][0] + 2
                new_y = bullets_1[i][1] + 4
            elif bullets_1[i][3] == 2:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 2
            elif bullets_1[i][3] == 3:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 1
            elif bullets_1[i][3] == 4:
                new_x = bullets_1[i][0] + 1
                new_y = bullets_1[i][1] + 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0: #If bullet falls off the screen
                delete_bullets_1.append(i)                          #delete the bullet
            bullets_1[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_1[i][3]]

        for i in range(len(delete_bullets_1)):
            del bullets_1[delete_bullets_1[i]]

        #Delete bullets if they hit the player
        delete_bullets_1 = []

        for i in range(len(bullets_1)):
            if player_collision.colliderect(bullets_1[i][2]):
                pygame.mixer.Sound.play(damage_taken) #Play damage taken sound
                player_health -= random.randint(1, 10) #Player's health will deduct a random amount
                delete_bullets_1.append(i)
                player_colour = RED #Player's colour will change to indicate damage taken
                if player_health <= 0: #If player dies, end game
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_1)):
            del bullets_1[delete_bullets_1[i]]

        #Computes bullets from TOP RIGHT--Same code as above
        if bullet_time_2 >= 30:
            bullet_time_2 = 0
            bullets_2.append([788, 0, pygame.Rect(788, 0, 12, 12), random.randint(0,4)])

        delete_bullets_2 = []

        for i in range(len(bullets_2)):
            pygame.draw.rect(screen, DARK_RED, bullets_2[i][2])
            if bullets_2[i][3] == 0:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 4
            elif bullets_2[i][3] == 1:
                new_x = bullets_2[i][0] - 2
                new_y = bullets_2[i][1] + 4
            elif bullets_2[i][3] == 2:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 2
            elif bullets_2[i][3] == 3:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 1
            elif bullets_2[i][3] == 4:
                new_x = bullets_2[i][0] - 1
                new_y = bullets_2[i][1] + 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_2.append(i)
            bullets_2[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_2[i][3]]

        for i in range(len(delete_bullets_2)):
            del bullets_2[delete_bullets_2[i]]

        delete_bullets_2 = []

        for i in range(len(bullets_2)):
            if player_collision.colliderect(bullets_2[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_2.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_2)):
            del bullets_2[delete_bullets_2[i]]

        #Computes bullets from BOTTOM LEFT--Same code as above
        if bullet_time_3 >= 30:
            bullet_time_3 = 0
            bullets_3.append([0, 488, pygame.Rect(0, 488, 12, 12), random.randint(0,4)])

        delete_bullets_3 = []

        for i in range(len(bullets_3)):
            pygame.draw.rect(screen, DARK_RED, bullets_3[i][2])
            if bullets_3[i][3] == 0:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 4
            elif bullets_3[i][3] == 1:
                new_x = bullets_3[i][0] + 2
                new_y = bullets_3[i][1] - 4
            elif bullets_3[i][3] == 2:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 2
            elif bullets_3[i][3] == 3:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 1
            elif bullets_3[i][3] == 4:
                new_x = bullets_3[i][0] + 1
                new_y = bullets_3[i][1] - 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_3.append(i)
            bullets_3[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_3[i][3]]

        for i in range(len(delete_bullets_3)):
            del bullets_3[delete_bullets_3[i]]

        delete_bullets_3 = []

        for i in range(len(bullets_3)):
            if player_collision.colliderect(bullets_3[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_3.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_3)):
            del bullets_3[delete_bullets_3[i]]

        #Computes bullets from BOTTOM RIGHT--Same code as above
        if bullet_time_4 >= 30:
            bullet_time_4 = 0
            bullets_4.append([788, 488, pygame.Rect(788, 488, 12, 12), random.randint(0,4)])

        delete_bullets_4 = []

        for i in range(len(bullets_4)):
            pygame.draw.rect(screen, DARK_RED, bullets_4[i][2])
            if bullets_4[i][3] == 0:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 4
            elif bullets_4[i][3] == 1:
                new_x = bullets_4[i][0] - 2
                new_y = bullets_4[i][1] - 4
            elif bullets_4[i][3] == 2:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 2
            elif bullets_4[i][3] == 3:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 1
            elif bullets_4[i][3] == 4:
                new_x = bullets_4[i][0] - 1
                new_y = bullets_4[i][1] - 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_4.append(i)
            bullets_4[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_4[i][3]]

        for i in range(len(delete_bullets_4)):
            del bullets_4[delete_bullets_4[i]]

        delete_bullets_4 = []

        for i in range(len(bullets_4)):
            if player_collision.colliderect(bullets_4[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_4.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_4)):
            del bullets_4[delete_bullets_4[i]]

        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                #Detects if an arrow key is pressed
                if event.key == pygame.K_RIGHT:
                    pressed_right = True
                elif event.key == pygame.K_LEFT:
                    pressed_left = True
                elif event.key == pygame.K_UP:
                    pressed_up = True
                elif event.key == pygame.K_DOWN:
                    pressed_down = True

                #Detects if the player flips the card
                if player_collision.colliderect(card_1_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or (0, 0) in cards_flipped or card_flip_master[0][0]:
                            pass #If card is already flipped, two cards are already flipped
                                #Or card is already matched, do nothing
                        else:
                            cards_flipped.append((0, 0)) #Flip card
                        card_colours[0][0] = card_colour_master[0][0]
                elif player_collision.colliderect(card_1_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or (0, 1) in cards_flipped or card_flip_master[0][1]:
                            pass
                        else:
                            cards_flipped.append((0, 1))
                        card_colours[0][1] = card_colour_master[0][1]
                elif player_collision.colliderect(card_1_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or (0, 2) in cards_flipped or card_flip_master[0][2]:
                            pass
                        else:
                            cards_flipped.append((0, 2))
                        card_colours[0][2] = card_colour_master[0][2]
                elif player_collision.colliderect(card_2_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or (1, 0) in cards_flipped or card_flip_master[1][0]:
                            pass
                        else:
                            cards_flipped.append((1, 0))
                        card_colours[1][0] = card_colour_master[1][0]
                elif player_collision.colliderect(card_2_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or (1, 1) in cards_flipped or card_flip_master[1][1]:
                            pass
                        else:
                            cards_flipped.append((1, 1))
                        card_colours[1][1] = card_colour_master[1][1]
                elif player_collision.colliderect(card_2_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or (1, 2) in cards_flipped or card_flip_master[1][2]:
                            pass
                        else:
                            cards_flipped.append((1, 2))
                        card_colours[1][2] = card_colour_master[1][2]

            #If user lets go of the arrow key, stop moving the player
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pressed_right = False
                elif event.key == pygame.K_LEFT:
                    pressed_left = False
                elif event.key == pygame.K_UP:
                    pressed_up = False
                elif event.key == pygame.K_DOWN:
                    pressed_down = False

        #If the two cards flipped are not the same, display it for some time for the player
        #to memorize
        if len(cards_flipped) >= 2:
            time_delay += 1

        if time_delay >= 20:
            time_delay = 0
            #Checks if player's card is correct
            if card_colour_master[cards_flipped[0][0]][cards_flipped[0][1]] == card_colour_master[cards_flipped[1][0]][cards_flipped[1][1]]:
                pygame.mixer.Sound.play(matched) #Plays matched sound
                card_flip_master[cards_flipped[0][0]][cards_flipped[0][1]] = True
                card_flip_master[cards_flipped[1][0]][cards_flipped[1][1]] = True
                pairs_matched += 1
            #If they are not correct, change them back to gray
            for i in range(2):
                for j in range(3):
                    if not card_flip_master[i][j]:
                        card_colours[i][j] = GRAY
            cards_flipped = []

        #If arrow key is pressed, move the player
        if pressed_right and player_x + 4 <= 780:
            player_x += 4
        if pressed_left and player_x - 4 >= 0:
            player_x -= 4
        if pressed_up and player_y - 4 >= 0:
            player_y -= 4
        if pressed_down and player_y + 4 <= 480:
            player_y += 4

        #Text
        pairs_matched_text = CALIBRI_GAME.render("Pairs Matched: " + str(pairs_matched), True, BLACK)
        screen.blit(pairs_matched_text, [40, 460])

        player_health_text = CALIBRI_GAME.render("Health: " + str(player_health), True, BLACK)
        screen.blit(player_health_text, [250, 460])

        #If all cards are matched, end game
        if pairs_matched >= 3:
            win()
            pygame.quit()
            return

        #Update time variables
        bullet_time_1 += 1
        bullet_time_2 += 1
        bullet_time_3 += 1
        bullet_time_4 += 1
        
        pygame.display.flip()
        clock.tick(60)
        

#Displays if player selects medium difficulty, same code as easy() except with more cards,
#therefore more variables
def medium():
    done = False

    pygame.mixer.music.play(-1)

    card_colours = [[GRAY] * 4 for i in range(3)]
    card_colour_master = [[None] * 4 for i in range(3)]
    card_flip_master = [[False] * 4 for i in range(3)]
    cards_flipped = []
    colours = [RED, RED, YELLOW, YELLOW, PINK, PINK, PURPLE, PURPLE, TURQUOISE, TURQUOISE, ORANGE, ORANGE]

    for i in range(3):
        for j in range(4):
            random_value = random.randint(0, len(colours)-1)
            card_colour_master[i][j] = colours[random_value]
            del colours[random_value]

    pairs_matched = 0

    time_delay = 0
    bullet_time_1 = 0
    bullet_time_2 = 0
    bullet_time_3 = 0
    bullet_time_4 = 0

    bullets_1 = []
    bullets_2 = []
    bullets_3 = []
    bullets_4 = []
    
    player_health = 100
    player_colour = GREEN
    player_x = 390
    player_y = 240
    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False

    while not done:
        card_1_1_collision = pygame.Rect(110, 60, 100, 100)
        card_1_1 = pygame.draw.rect(screen, card_colours[0][0], card_1_1_collision)

        card_1_2_collision = pygame.Rect(270, 60, 100, 100)
        card_1_2 = pygame.draw.rect(screen, card_colours[0][1], card_1_2_collision)


        card_1_3_collision = pygame.Rect(430, 60, 100, 100)
        card_1_3 = pygame.draw.rect(screen, card_colours[0][2], card_1_3_collision)

        card_1_4_collision = pygame.Rect(590, 60, 100, 100)
        card_1_4 = pygame.draw.rect(screen, card_colours[0][3], card_1_4_collision)

        card_2_1_collision = pygame.Rect(110, 200, 100, 100)
        card_2_1 = pygame.draw.rect(screen, card_colours[1][0], card_2_1_collision)

        card_2_2_collision = pygame.Rect(270, 200, 100, 100)
        card_2_2 = pygame.draw.rect(screen, card_colours[1][1], card_2_2_collision)

        card_2_3_collision = pygame.Rect(430, 200, 100, 100)
        card_2_3 = pygame.draw.rect(screen, card_colours[1][2], card_2_3_collision)

        card_2_4_collision = pygame.Rect(590, 200, 100, 100)
        card_2_4 = pygame.draw.rect(screen, card_colours[1][3], card_2_4_collision)

        card_3_1_collision = pygame.Rect(110, 340, 100, 100)
        card_3_1 = pygame.draw.rect(screen, card_colours[2][0], card_3_1_collision)

        card_3_2_collision = pygame.Rect(270, 340, 100, 100)
        card_3_2 = pygame.draw.rect(screen, card_colours[2][1], card_3_2_collision)

        card_3_3_collision = pygame.Rect(430, 340, 100, 100)
        card_3_3 = pygame.draw.rect(screen, card_colours[2][2], card_3_3_collision)

        card_3_4_collision = pygame.Rect(590, 340, 100, 100)
        card_3_4 = pygame.draw.rect(screen, card_colours[2][3], card_3_4_collision)

        screen.blit(game_UI_medium, (0, 0))

        player_collision = pygame.Rect(player_x, player_y, 20, 20)
        player = pygame.draw.rect(screen, player_colour, player_collision)

        player_colour = GREEN

        if bullet_time_1 >= 30:
            bullet_time_1 = 0
            bullets_1.append([0, 0, pygame.Rect(0, 0, 12, 12), random.randint(0,4)])

        delete_bullets_1 = []

        for i in range(len(bullets_1)):
            pygame.draw.rect(screen, DARK_RED, bullets_1[i][2])
            if bullets_1[i][3] == 0:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 4
            elif bullets_1[i][3] == 1:
                new_x = bullets_1[i][0] + 2
                new_y = bullets_1[i][1] + 4
            elif bullets_1[i][3] == 2:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 2
            elif bullets_1[i][3] == 3:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 1
            elif bullets_1[i][3] == 4:
                new_x = bullets_1[i][0] + 1
                new_y = bullets_1[i][1] + 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_1.append(i)
            bullets_1[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_1[i][3]]

        for i in range(len(delete_bullets_1)):
            del bullets_1[delete_bullets_1[i]]

        delete_bullets_1 = []

        for i in range(len(bullets_1)):
            if player_collision.colliderect(bullets_1[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_1.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_1)):
            del bullets_1[delete_bullets_1[i]]

        if bullet_time_2 >= 30:
            bullet_time_2 = 0
            bullets_2.append([788, 0, pygame.Rect(788, 0, 12, 12), random.randint(0,4)])

        delete_bullets_2 = []

        for i in range(len(bullets_2)):
            pygame.draw.rect(screen, DARK_RED, bullets_2[i][2])
            if bullets_2[i][3] == 0:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 4
            elif bullets_2[i][3] == 1:
                new_x = bullets_2[i][0] - 2
                new_y = bullets_2[i][1] + 4
            elif bullets_2[i][3] == 2:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 2
            elif bullets_2[i][3] == 3:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 1
            elif bullets_2[i][3] == 4:
                new_x = bullets_2[i][0] - 1
                new_y = bullets_2[i][1] + 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_2.append(i)
            bullets_2[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_2[i][3]]

        for i in range(len(delete_bullets_2)):
            del bullets_2[delete_bullets_2[i]]

        delete_bullets_2 = []

        for i in range(len(bullets_2)):
            if player_collision.colliderect(bullets_2[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_2.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_2)):
            del bullets_2[delete_bullets_2[i]]

        if bullet_time_3 >= 30:
            bullet_time_3 = 0
            bullets_3.append([0, 488, pygame.Rect(0, 488, 12, 12), random.randint(0,4)])

        delete_bullets_3 = []

        for i in range(len(bullets_3)):
            pygame.draw.rect(screen, DARK_RED, bullets_3[i][2])
            if bullets_3[i][3] == 0:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 4
            elif bullets_3[i][3] == 1:
                new_x = bullets_3[i][0] + 2
                new_y = bullets_3[i][1] - 4
            elif bullets_3[i][3] == 2:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 2
            elif bullets_3[i][3] == 3:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 1
            elif bullets_3[i][3] == 4:
                new_x = bullets_3[i][0] + 1
                new_y = bullets_3[i][1] - 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_3.append(i)
            bullets_3[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_3[i][3]]

        for i in range(len(delete_bullets_3)):
            del bullets_3[delete_bullets_3[i]]

        delete_bullets_3 = []

        for i in range(len(bullets_3)):
            if player_collision.colliderect(bullets_3[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_3.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_3)):
            del bullets_3[delete_bullets_3[i]]

        if bullet_time_4 >= 30:
            bullet_time_4 = 0
            bullets_4.append([788, 488, pygame.Rect(788, 488, 12, 12), random.randint(0,4)])

        delete_bullets_4 = []

        for i in range(len(bullets_4)):
            pygame.draw.rect(screen, DARK_RED, bullets_4[i][2])
            if bullets_4[i][3] == 0:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 4
            elif bullets_4[i][3] == 1:
                new_x = bullets_4[i][0] - 2
                new_y = bullets_4[i][1] - 4
            elif bullets_4[i][3] == 2:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 2
            elif bullets_4[i][3] == 3:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 1
            elif bullets_4[i][3] == 4:
                new_x = bullets_4[i][0] - 1
                new_y = bullets_4[i][1] - 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_4.append(i)
            bullets_4[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_4[i][3]]

        for i in range(len(delete_bullets_4)):
            del bullets_4[delete_bullets_4[i]]

        delete_bullets_4 = []

        for i in range(len(bullets_4)):
            if player_collision.colliderect(bullets_4[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_4.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_4)):
            del bullets_4[delete_bullets_4[i]]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pressed_right = True
                elif event.key == pygame.K_LEFT:
                    pressed_left = True
                elif event.key == pygame.K_UP:
                    pressed_up = True
                elif event.key == pygame.K_DOWN:
                    pressed_down = True
                
                if player_collision.colliderect(card_1_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][0] or (0, 0) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 0))
                        card_colours[0][0] = card_colour_master[0][0]
                elif player_collision.colliderect(card_1_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][1] or (0, 1) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 1))
                        card_colours[0][1] = card_colour_master[0][1]
                elif player_collision.colliderect(card_1_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][2] or (0, 2) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 2))
                        card_colours[0][2] = card_colour_master[0][2]
                elif player_collision.colliderect(card_1_4_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][3] or (0, 3) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 3))
                        card_colours[0][3] = card_colour_master[0][3]
                elif player_collision.colliderect(card_2_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][0] or (1, 0) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 0))
                        card_colours[1][0] = card_colour_master[1][0]
                elif player_collision.colliderect(card_2_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][1] or (1, 1) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 1))
                        card_colours[1][1] = card_colour_master[1][1]
                elif player_collision.colliderect(card_2_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][2] or (1, 2) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 2))
                        card_colours[1][2] = card_colour_master[1][2]
                elif player_collision.colliderect(card_2_4_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][3] or (1, 3) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 3))
                        card_colours[1][3] = card_colour_master[1][3]
                elif player_collision.colliderect(card_3_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][0] or (2, 0) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 0))
                        card_colours[2][0] = card_colour_master[2][0]
                elif player_collision.colliderect(card_3_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][1] or (2, 1) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 1))
                        card_colours[2][1] = card_colour_master[2][1]
                elif player_collision.colliderect(card_3_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][2] or (2, 2) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 2))
                        card_colours[2][2] = card_colour_master[2][2]
                elif player_collision.colliderect(card_3_4_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][3] or (2, 3) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 3))
                        card_colours[2][3] = card_colour_master[2][3]
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pressed_right = False
                elif event.key == pygame.K_LEFT:
                    pressed_left = False
                elif event.key == pygame.K_UP:
                    pressed_up = False
                elif event.key == pygame.K_DOWN:
                    pressed_down = False

        if len(cards_flipped) >= 2:
            time_delay += 1

        if time_delay >= 20:
            time_delay = 0
            if card_colour_master[cards_flipped[0][0]][cards_flipped[0][1]] == card_colour_master[cards_flipped[1][0]][cards_flipped[1][1]]:
                pygame.mixer.Sound.play(matched)
                card_flip_master[cards_flipped[0][0]][cards_flipped[0][1]] = True
                card_flip_master[cards_flipped[1][0]][cards_flipped[1][1]] = True
                pairs_matched += 1
            for i in range(3):
                for j in range(4):
                    if not card_flip_master[i][j]:
                        card_colours[i][j] = GRAY
            cards_flipped = []
    
        if pressed_right and player_x + 4 <= 780:
            player_x += 4
        if pressed_left and player_x - 4 >= 0:
            player_x -= 4
        if pressed_up and player_y - 4 >= 0:
            player_y -= 4
        if pressed_down and player_y + 4 <= 480:
            player_y += 4

        pairs_matched_text = CALIBRI_GAME.render("Pairs Matched: " + str(pairs_matched), True, BLACK)
        screen.blit(pairs_matched_text, [40, 460])

        player_health_text = CALIBRI_GAME.render("Health: " + str(player_health), True, BLACK)
        screen.blit(player_health_text, [250, 460])

        if pairs_matched >= 6:
            win()
            pygame.quit()
            return

        bullet_time_1 += 1
        bullet_time_2 += 1
        bullet_time_3 += 1
        bullet_time_4 += 1
        
        pygame.display.flip()
        clock.tick(60)

        
#Displays if player chooses hard difficulty
#Same code as easy() and medium(), but more variables
def hard():
    done = False

    pygame.mixer.music.play(-1)

    card_colours = [[GRAY] * 5 for i in range(4)]
    card_colour_master = [[None] * 5 for i in range(4)]
    card_flip_master = [[False] * 5 for i in range(4)]
    cards_flipped = []
    colours = [RED, RED, YELLOW, YELLOW, PINK, PINK, PURPLE, PURPLE, TURQUOISE, TURQUOISE, ORANGE, ORANGE,
               DARK_BLUE, DARK_BLUE, DARK_GREEN, DARK_GREEN, LIGHT_RED, LIGHT_RED, LIGHT_GREEN, LIGHT_GREEN]

    for i in range(4):
        for j in range(5):
            random_value = random.randint(0, len(colours)-1)
            card_colour_master[i][j] = colours[random_value]
            del colours[random_value]

    pairs_matched = 0

    time_delay = 0
    bullet_time_1 = 0
    bullet_time_2 = 0
    bullet_time_3 = 0
    bullet_time_4 = 0

    bullets_1 = []
    bullets_2 = []
    bullets_3 = []
    bullets_4 = []
    
    player_health = 100
    player_colour = GREEN
    player_x = 390
    player_y = 240
    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False

    while not done:
        card_1_1_collision = pygame.Rect(93, 40, 80, 80)
        card_1_1 = pygame.draw.rect(screen, card_colours[0][0], card_1_1_collision)

        card_1_2_collision = pygame.Rect(226, 40, 80, 80)
        card_1_2 = pygame.draw.rect(screen, card_colours[0][1], card_1_2_collision)

        card_1_3_collision = pygame.Rect(359, 40, 80, 80)
        card_1_3 = pygame.draw.rect(screen, card_colours[0][2], card_1_3_collision)

        card_1_4_collision = pygame.Rect(492, 40, 80, 80)
        card_1_4 = pygame.draw.rect(screen, card_colours[0][3], card_1_4_collision)

        card_1_5_collision = pygame.Rect(625, 40, 80, 80)
        card_1_5 = pygame.draw.rect(screen, card_colours[0][4], card_1_5_collision)

        card_2_1_collision = pygame.Rect(93, 150, 80, 80)
        card_2_1 = pygame.draw.rect(screen, card_colours[1][0], card_2_1_collision)

        card_2_2_collision = pygame.Rect(226, 150, 80, 80)
        card_2_2 = pygame.draw.rect(screen, card_colours[1][1], card_2_2_collision)

        card_2_3_collision = pygame.Rect(359, 150, 80, 80)
        card_2_3 = pygame.draw.rect(screen, card_colours[1][2], card_2_3_collision)

        card_2_4_collision = pygame.Rect(492, 150, 80, 80)
        card_2_4 = pygame.draw.rect(screen, card_colours[1][3], card_2_4_collision)

        card_2_5_collision = pygame.Rect(625, 150, 80, 80)
        card_2_5 = pygame.draw.rect(screen, card_colours[1][4], card_2_5_collision)

        card_3_1_collision = pygame.Rect(93, 260, 80, 80)
        card_3_1 = pygame.draw.rect(screen, card_colours[2][0], card_3_1_collision)

        card_3_2_collision = pygame.Rect(226, 260, 80, 80)
        card_3_2 = pygame.draw.rect(screen, card_colours[2][1], card_3_2_collision)

        card_3_3_collision = pygame.Rect(359, 260, 80, 80)
        card_3_3 = pygame.draw.rect(screen, card_colours[2][2], card_3_3_collision)

        card_3_4_collision = pygame.Rect(492, 260, 80, 80)
        card_3_4 = pygame.draw.rect(screen, card_colours[2][3], card_3_4_collision)

        card_3_5_collision = pygame.Rect(625, 260, 80, 80)
        card_3_5 = pygame.draw.rect(screen, card_colours[2][4], card_3_5_collision)

        card_4_1_collision = pygame.Rect(93, 370, 80, 80)
        card_4_1 = pygame.draw.rect(screen, card_colours[3][0], card_4_1_collision)

        card_4_2_collision = pygame.Rect(226, 370, 80, 80)
        card_4_2 = pygame.draw.rect(screen, card_colours[3][1], card_4_2_collision)

        card_4_3_collision = pygame.Rect(359, 370, 80, 80)
        card_4_3 = pygame.draw.rect(screen, card_colours[3][2], card_4_3_collision)

        card_4_4_collision = pygame.Rect(492, 370, 80, 80)
        card_4_4 = pygame.draw.rect(screen, card_colours[3][3], card_4_4_collision)

        card_4_5_collision = pygame.Rect(625, 370, 80, 80)
        card_4_5 = pygame.draw.rect(screen, card_colours[3][4], card_4_5_collision)

        screen.blit(game_UI_hard, (0, 0))

        player_collision = pygame.Rect(player_x, player_y, 20, 20)
        player = pygame.draw.rect(screen, player_colour, player_collision)

        player_colour = GREEN

        if bullet_time_1 >= 30:
            bullet_time_1 = 0
            bullets_1.append([0, 0, pygame.Rect(0, 0, 12, 12), random.randint(0,4)])

        delete_bullets_1 = []

        for i in range(len(bullets_1)):
            pygame.draw.rect(screen, DARK_RED, bullets_1[i][2])
            if bullets_1[i][3] == 0:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 4
            elif bullets_1[i][3] == 1:
                new_x = bullets_1[i][0] + 2
                new_y = bullets_1[i][1] + 4
            elif bullets_1[i][3] == 2:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 2
            elif bullets_1[i][3] == 3:
                new_x = bullets_1[i][0] + 4
                new_y = bullets_1[i][1] + 1
            elif bullets_1[i][3] == 4:
                new_x = bullets_1[i][0] + 1
                new_y = bullets_1[i][1] + 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_1.append(i)
            bullets_1[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_1[i][3]]

        for i in range(len(delete_bullets_1)):
            del bullets_1[delete_bullets_1[i]]

        delete_bullets_1 = []

        for i in range(len(bullets_1)):
            if player_collision.colliderect(bullets_1[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_1.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_1)):
            del bullets_1[delete_bullets_1[i]]

        if bullet_time_2 >= 30:
            bullet_time_2 = 0
            bullets_2.append([788, 0, pygame.Rect(788, 0, 12, 12), random.randint(0,4)])

        delete_bullets_2 = []

        for i in range(len(bullets_2)):
            pygame.draw.rect(screen, DARK_RED, bullets_2[i][2])
            if bullets_2[i][3] == 0:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 4
            elif bullets_2[i][3] == 1:
                new_x = bullets_2[i][0] - 2
                new_y = bullets_2[i][1] + 4
            elif bullets_2[i][3] == 2:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 2
            elif bullets_2[i][3] == 3:
                new_x = bullets_2[i][0] - 4
                new_y = bullets_2[i][1] + 1
            elif bullets_2[i][3] == 4:
                new_x = bullets_2[i][0] - 1
                new_y = bullets_2[i][1] + 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_2.append(i)
            bullets_2[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_2[i][3]]

        for i in range(len(delete_bullets_2)):
            del bullets_2[delete_bullets_2[i]]

        delete_bullets_2 = []

        for i in range(len(bullets_2)):
            if player_collision.colliderect(bullets_2[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_2.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_2)):
            del bullets_2[delete_bullets_2[i]]

        if bullet_time_3 >= 30:
            bullet_time_3 = 0
            bullets_3.append([0, 488, pygame.Rect(0, 488, 12, 12), random.randint(0,4)])

        delete_bullets_3 = []

        for i in range(len(bullets_3)):
            pygame.draw.rect(screen, DARK_RED, bullets_3[i][2])
            if bullets_3[i][3] == 0:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 4
            elif bullets_3[i][3] == 1:
                new_x = bullets_3[i][0] + 2
                new_y = bullets_3[i][1] - 4
            elif bullets_3[i][3] == 2:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 2
            elif bullets_3[i][3] == 3:
                new_x = bullets_3[i][0] + 4
                new_y = bullets_3[i][1] - 1
            elif bullets_3[i][3] == 4:
                new_x = bullets_3[i][0] + 1
                new_y = bullets_3[i][1] - 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_3.append(i)
            bullets_3[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_3[i][3]]

        for i in range(len(delete_bullets_3)):
            del bullets_3[delete_bullets_3[i]]

        delete_bullets_3 = []

        for i in range(len(bullets_3)):
            if player_collision.colliderect(bullets_3[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_3.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_3)):
            del bullets_3[delete_bullets_3[i]]

        if bullet_time_4 >= 30:
            bullet_time_4 = 0
            bullets_4.append([788, 488, pygame.Rect(788, 488, 12, 12), random.randint(0,4)])

        delete_bullets_4 = []

        for i in range(len(bullets_4)):
            pygame.draw.rect(screen, DARK_RED, bullets_4[i][2])
            if bullets_4[i][3] == 0:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 4
            elif bullets_4[i][3] == 1:
                new_x = bullets_4[i][0] - 2
                new_y = bullets_4[i][1] - 4
            elif bullets_4[i][3] == 2:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 2
            elif bullets_4[i][3] == 3:
                new_x = bullets_4[i][0] - 4
                new_y = bullets_4[i][1] - 1
            elif bullets_4[i][3] == 4:
                new_x = bullets_4[i][0] - 1
                new_y = bullets_4[i][1] - 4
            if new_x > 788 or new_x < 0 or new_y > 488 or new_y < 0:
                delete_bullets_4.append(i)
            bullets_4[i] = [new_x, new_y, pygame.Rect(new_x, new_y, 12, 12), bullets_4[i][3]]

        for i in range(len(delete_bullets_4)):
            del bullets_4[delete_bullets_4[i]]

        delete_bullets_4 = []

        for i in range(len(bullets_4)):
            if player_collision.colliderect(bullets_4[i][2]):
                pygame.mixer.Sound.play(damage_taken)
                player_health -= random.randint(1, 10)
                delete_bullets_4.append(i)
                player_colour = RED
                if player_health <= 0:
                    lose()
                    pygame.quit()
                    return

        for i in range(len(delete_bullets_4)):
            del bullets_4[delete_bullets_4[i]]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pressed_right = True
                elif event.key == pygame.K_LEFT:
                    pressed_left = True
                elif event.key == pygame.K_UP:
                    pressed_up = True
                elif event.key == pygame.K_DOWN:
                    pressed_down = True
                
                if player_collision.colliderect(card_1_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][0] or (0, 0) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 0))
                        card_colours[0][0] = card_colour_master[0][0]
                elif player_collision.colliderect(card_1_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][1] or (0, 1) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 1))
                        card_colours[0][1] = card_colour_master[0][1]
                elif player_collision.colliderect(card_1_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][2] or (0, 2) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 2))
                        card_colours[0][2] = card_colour_master[0][2]
                elif player_collision.colliderect(card_1_4_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][3] or (0, 3) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 3))
                        card_colours[0][3] = card_colour_master[0][3]
                elif player_collision.colliderect(card_1_5_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[0][4] or (0, 4) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((0, 4))
                        card_colours[0][4] = card_colour_master[0][4]
                elif player_collision.colliderect(card_2_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][0] or (1, 0) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 0))
                        card_colours[1][0] = card_colour_master[1][0]
                elif player_collision.colliderect(card_2_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][1] or (1, 1) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 1))
                        card_colours[1][1] = card_colour_master[1][1]
                elif player_collision.colliderect(card_2_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][2] or (1, 2) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 2))
                        card_colours[1][2] = card_colour_master[1][2]
                elif player_collision.colliderect(card_2_4_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][3] or (1, 3) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 3))
                        card_colours[1][3] = card_colour_master[1][3]
                elif player_collision.colliderect(card_2_5_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[1][4] or (1, 4) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((1, 4))
                        card_colours[1][4] = card_colour_master[1][4]
                elif player_collision.colliderect(card_3_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][0] or (2, 0) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 0))
                        card_colours[2][0] = card_colour_master[2][0]
                elif player_collision.colliderect(card_3_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][1] or (2, 1) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 1))
                        card_colours[2][1] = card_colour_master[2][1]
                elif player_collision.colliderect(card_3_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][2] or (2, 2) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 2))
                        card_colours[2][2] = card_colour_master[2][2]
                elif player_collision.colliderect(card_3_4_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][3] or (2, 3) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 3))
                        card_colours[2][3] = card_colour_master[2][3]
                elif player_collision.colliderect(card_3_5_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[2][4] or (2, 4) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((2, 4))
                        card_colours[2][4] = card_colour_master[2][4]
                elif player_collision.colliderect(card_4_1_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[3][0] or (3, 0) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((3, 0))
                        card_colours[3][0] = card_colour_master[3][0]
                elif player_collision.colliderect(card_4_2_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[3][1] or (3, 1) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((3, 1))
                        card_colours[3][1] = card_colour_master[3][1]
                elif player_collision.colliderect(card_4_3_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[3][2] or (3, 2) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((3, 2))
                        card_colours[3][2] = card_colour_master[3][2]
                elif player_collision.colliderect(card_4_4_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[3][3] or (3, 3) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((3, 3))
                        card_colours[3][3] = card_colour_master[3][3]
                elif player_collision.colliderect(card_4_5_collision):
                    if event.key == pygame.K_z:
                        if len(cards_flipped) >= 2 or card_flip_master[3][4] or (3, 4) in cards_flipped:
                            pass
                        else:
                            cards_flipped.append((3, 4))
                        card_colours[3][4] = card_colour_master[3][4]
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pressed_right = False
                elif event.key == pygame.K_LEFT:
                    pressed_left = False
                elif event.key == pygame.K_UP:
                    pressed_up = False
                elif event.key == pygame.K_DOWN:
                    pressed_down = False

        if len(cards_flipped) >= 2:
            time_delay += 1

        if time_delay >= 20:
            time_delay = 0
            if card_colour_master[cards_flipped[0][0]][cards_flipped[0][1]] == card_colour_master[cards_flipped[1][0]][cards_flipped[1][1]]:
                pygame.mixer.Sound.play(matched)
                card_flip_master[cards_flipped[0][0]][cards_flipped[0][1]] = True
                card_flip_master[cards_flipped[1][0]][cards_flipped[1][1]] = True
                pairs_matched += 1
            for i in range(4):
                for j in range(5):
                    if not card_flip_master[i][j]:
                        card_colours[i][j] = GRAY
            cards_flipped = []
    
        if pressed_right and player_x + 4 <= 780:
            player_x += 4
        if pressed_left and player_x - 4 >= 0:
            player_x -= 4
        if pressed_up and player_y - 4 >= 0:
            player_y -= 4
        if pressed_down and player_y + 4 <= 480:
            player_y += 4

        pairs_matched_text = CALIBRI_GAME.render("Pairs Matched: " + str(pairs_matched), True, BLACK)
        screen.blit(pairs_matched_text, [40, 460])

        player_health_text = CALIBRI_GAME.render("Health: " + str(player_health), True, BLACK)
        screen.blit(player_health_text, [250, 460])

        if pairs_matched >= 10:
            win()
            pygame.quit()
            return

        bullet_time_1 += 1
        bullet_time_2 += 1
        bullet_time_3 += 1
        bullet_time_4 += 1
        
        pygame.display.flip()
        clock.tick(60)
        

#Displays if player presses "Instructions" button
def instructions():
    done = False
    click = False
    
    while not done:
        #Background
        screen.blit(instructions_UI, (0, 0))
        
        mouse_x, mouse_y = pygame.mouse.get_pos() #Mouse positions

        #Return button
        return_button_collision = pygame.Rect(320, 419, 150, 50)

        #Event loops
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN: #Checks if mouse is clicked
                click = True

            if return_button_collision.collidepoint((mouse_x, mouse_y)):
                #Checks if return button is pressed
                if click:
                    menu()
                    pygame.quit()
                    return

        pygame.display.flip()
        clock.tick(60)
        

#Main Menu, default window
def menu():
    done = False
    click = False
    
    while not done:
        #Background
        screen.blit(menu_UI, (0, 0))

        #Mouse positions
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Easy button
        easy_button_collision = pygame.Rect(125, 250, 150, 75)

        #Medium button
        medium_button_collision = pygame.Rect(325, 250, 150, 75)
        
        #Hard button
        hard_button_collision = pygame.Rect(525, 250, 150, 75)

        #Quit button
        quit_button_collision = pygame.Rect(290, 375, 40, 40)

        #Instructions button
        instructions_button_collision = pygame.Rect(370, 375, 150, 40)

        #Checks if button is pressed
        if easy_button_collision.collidepoint((mouse_x, mouse_y)):
            screen.blit(menu_UI_easy, (0, 0))
            if click:
                easy()
                pygame.quit()
                return #Returns the function to prevent function stack overflowing
        if medium_button_collision.collidepoint((mouse_x, mouse_y)):
            screen.blit(menu_UI_medium, (0, 0))
            if click:
                medium()
                pygame.quit()
                return
        if hard_button_collision.collidepoint((mouse_x, mouse_y)):
            screen.blit(menu_UI_hard, (0, 0))
            if click:
                hard()
                pygame.quit()
                return
        if quit_button_collision.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.quit()
                return
        if instructions_button_collision.collidepoint((mouse_x, mouse_y)):
            if click:
                instructions()
                pygame.quit()
                return

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        
        pygame.display.flip()
        clock.tick(60)
        
    return

menu() #Starts the game
pygame.quit() #If player exits all windows, quit








