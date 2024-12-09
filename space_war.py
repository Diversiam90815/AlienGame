import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from bullet import Bullet
from alien import Alien
from random import choice
from alien_laser import Alien_Laser
from explosion import Explosion
from audio import Audio


class SpaceWar:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.SCREEN_MENU = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space War")
    
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.sb = Scoreboard(self)
        self.alien = Alien(self)
        self.exp = Explosion()
        self.audio = Audio()

        self.alaser = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        self.create_fleet()
        self.BG_MENU = pygame.image.load("image/Space_Background_Menu.jpg")
        self.ALIENLASER = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ALIENLASER, self.settings.alaser_timer)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.settings.clock.tick(self.settings.fps)
            self.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self.update_bullets()
                self.update_aliens()
                self.exp.update()
                self.alaser.update()            
            self.update_screen()
           

    def check_events(self):
        """Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            if event.type == self.ALIENLASER:
                self.alien_shoot()

    def check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            pygame.mouse.set_visible(True)
            self.main_menu()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        """Create a new bullet and add it to its group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.audio.sfx_bullet()
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def show_explosion(self, position):
        self.exp = Explosion()
        self.exp.rect.center = position
        self.explosions.add(self.exp)

    def update_bullets(self):
        """Updates the position of all bullets and gets rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():                          # removes bullets that are out of sight
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()
      

    def check_bullet_alien_collisions(self):
        """Checks if aliens got hit by a bullet and removes the alien as well as if we got hit by a laser."""
        collisions_alien = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        collisions_player = pygame.sprite.spritecollideany(self.ship, self.alaser)

        if collisions_alien:
            for aliens in collisions_alien.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.audio.sfx_explosion()
            for alien in collisions_alien:          #Display explosion at the alien's position
                self.show_explosion(alien.rect.center)
        if collisions_player:
            self.ship_hit()

        """Destroys bullets and creates a new fleet."""
        if not self.aliens:
            sleep(0.3)
            self.bullets.empty()
            self.alaser.empty()
            self.explosions.empty()
            self.create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def update_aliens(self):
        """Check if the fleet is at an edge, then update the positions of all aliens in the fleet."""
        self.check_fleet_edges()
        self.aliens.update()
        """Checks for collisions between aliens and our ship."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.audio.sfx_ship_hit()
            self.ship_hit()
        self.check_aliens_bottom()

    def create_fleet(self):
        """Create the fleet of aliens."""
        self.alien_width, self.alien_height = self.alien.rect.size
        available_space_x = self.settings.screen_width - (2 * self.alien_width)
        number_aliens_x = available_space_x // (2 * self.alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * self.alien_height) - ship_height)
        number_rows = available_space_y // (2 * self.alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)


    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Alien_Laser(self, random_alien.rect.center)
            self.alaser.add(laser_sprite)
            self.audio.sfx_laser()

    def create_alien(self, alien_number, row_number):
        """Create alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def update_screen(self):
        """Updates the images on the screen and flip to the new screen."""
        self.screen.blit(self.settings.bg_img, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alaser in self.alaser.sprites():
            alaser.draw_laser()
        self.aliens.draw(self.screen)        
        for explosion in self.explosions.sprites():
            explosion.update()
            explosion.draw(self.screen)
        self.sb.show_score()
        pygame.display.flip()

    def check_fleet_edges(self):
        """Respond appropriately if aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Drop the entire fleet and change its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= (-1)

    def ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.alaser.empty()
            self.create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.stats.save_game()
            pygame.mouse.set_visible(True)
            sleep(0.5)
            self.end_screen()

    def check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def get_font(self, size):
        return pygame.font.SysFont(self.settings.font, size)

    def play(self):
        """Starts a new game if the player hits "Play" """
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.aliens.empty()
        self.bullets.empty()
        self.create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)
        self.settings.initialize_dynamic_settings()
        sleep(1)
        self.run_game()
    
    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN_MENU.blit(self.BG_MENU, (0, 0))
            pygame.display.set_caption("Options")

            GAMEPLAY_BUTTON = Button(image = pygame.image.load("image/Options Rect.png"), pos = (640, 250), 
                              text_input = "Gameplay")

            SOUND_BUTTON = Button(image = pygame.image.load("image/Play Rect.png"), pos = (640, 400), 
                                text_input = "Sound")
            
            OPTIONS_BACK = Button(image = pygame.image.load("image/Play Rect.png"), pos = (640, 550), 
                                text_input = "BACK")

            for button in [GAMEPLAY_BUTTON, SOUND_BUTTON, OPTIONS_BACK]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(self.SCREEN_MENU)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.audio.sfx_exit()
                    sleep(0.5)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.audio.sfx_btnclick()
                        self.main_menu()
                    if GAMEPLAY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        self.audio.sfx_btnclick()
                        self.gameplay_info()

            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN_MENU.blit(self.BG_MENU, (0, 0))
            pygame.display.set_caption("Menu")

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, self.settings.menutitle_color)
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image = pygame.image.load("image/Play Rect.png"), pos = (640, 300), 
                                text_input = "PLAY")

            OPTIONS_BUTTON = Button(image = pygame.image.load("image/Options Rect.png"), pos = (640, 450), 
                             text_input = "OPTIONS")

            QUIT_BUTTON = Button(image = pygame.image.load("image/Quit Rect.png"), pos = (640, 600), 
                                text_input = "QUIT")

            self.SCREEN_MENU.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN_MENU)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.audio.sfx_btnclick()
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.audio.sfx_btnclick()
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.audio.sfx_exit()
                        sleep(0.5)
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def end_screen(self):
        while True:
            self.SCREEN_MENU.blit(self.BG_MENU, (0, 0))
            pygame.display.set_caption("End Screen")

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN_TEXT = self.get_font(100).render("END SCREEN", True, self.settings.menutitle_color)
            SCREEN_RECT = SCREEN_TEXT.get_rect(center=(640, 100))
     
            self.sb.high_score = round(self.stats.high_score, -1)
            self.high_score = self.sb.high_score_str = "{:,}".format(self.sb.high_score)


            HSCORE_BUTTON = Button(image = None, pos = (640, 250), 
                                text_input = f'High Score: {self.high_score}')

            NGAME_BUTTON = Button(image = pygame.image.load("image/Options Rect.png"), pos = (640, 400), 
                                text_input = "NEW GAME")

            OPTIONS_BUTTON = Button(image = pygame.image.load("image/Options Rect.png"), pos = (640, 550), 
                                text_input = "OPTIONS")

            QUIT_BUTTON = Button(image = pygame.image.load("image/Quit Rect.png"), pos = (640, 700), 
                                text_input = "QUIT")


            self.SCREEN_MENU.blit(SCREEN_TEXT, SCREEN_RECT)

            for button in [HSCORE_BUTTON, NGAME_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN_MENU)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NGAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.audio.sfx_btnclick()
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.audio.sfx_btnclick()
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.audio.sfx_exit()
                        sleep(0.5)
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def gameplay_info(self):
        while True:
            GAMEPLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN_MENU.blit(self.BG_MENU, (0, 0))
            pygame.display.set_caption("Gameplay Information")

            ## Write mechanics and rules in a text!

            game_string = "You are under attack by multiple waves of alien ships.\n " \
                          "Shoot them before they get to you, but be aware: they will fight back!\n " \
                          "You have 3 lives"
            
            game_text = self.get_font(75).render(game_string, False, (0, 0, 0))
            self.screen.blit(game_text, (0, 0))

            GAMEPLAY_BACK = Button(image = pygame.image.load("image/Play Rect.png"), pos = (640, 550), 
                                text_input = "BACK")

            for button in [GAMEPLAY_BACK]:
                button.changeColor(GAMEPLAY_MOUSE_POS)
                button.update(self.SCREEN_MENU)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.audio.sfx_exit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if GAMEPLAY_BACK.checkForInput(GAMEPLAY_MOUSE_POS):
                        self.audio.sfx_btnclick()
                        self.options()

            pygame.display.update()


if __name__ == '__main__':
    ai = SpaceWar()
    ai.main_menu()