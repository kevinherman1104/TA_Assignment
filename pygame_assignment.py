import sys 
from settings_for_alien_invasion import Settings
from ship import Ship
import pygame
from pygame.sprite import Group
import game_function_alien as gf

def run_game():   
     # Initialize game and create a screen object.     
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode(        
        (ai_settings.screen_width, ai_settings.screen_height))    
    pygame.display.set_caption("Alien Invasion")

    #make SHip
    ship = Ship(ai_settings, screen) 
    # Make a group to store bullets in.     
    bullets = Group()
 
 
 
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

    # Watch for keyboard and mouse events.
        for event in pygame.event.get():             
            if event.type == pygame.QUIT:                
                sys.exit()  
    # Redraw the screen during each pass through the loop. v        
        screen.fill(ai_settings.bg_color)
        ship.blitme() 
                      
    # Make the most recently drawn screen visible. z         
        pygame.display.flip()
run_game()