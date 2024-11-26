import pygame
import logging

from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from paths import LOGS


def run_game():
	"""Initializes the game and creates a screen object"""
	logger = logging.getLogger('main')
	logger.setLevel(logging.INFO)
	console_handler = logging.FileHandler(LOGS, mode='w')
	console_handler.setLevel(logging.INFO)
	format = '%(levelname)s | %(module)s | %(funcName)s | %(message)s'
	formatter = logging.Formatter(format)
	console_handler.setFormatter(formatter)
	logger.addHandler(console_handler)
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
								   		 ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(screen, "Play")
	stats = GameStats(ai_settings, logger)
	scoreboard = Scoreboard(screen, ai_settings, stats)
	ship = Ship(screen, ai_settings)
	bullets = Group()
	aliens = Group()
	stars = Group()
	gf.create_stars(screen, ai_settings, stars)
	gf.create_fleet(screen, ai_settings, aliens, ship)
	logger.info('The creation and configuration of the game is completed')
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, stats, play_button,
				  		 aliens, scoreboard, logger)
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, screen, ai_settings, ship, scoreboard, 
					 			stats, logger)
			gf.update_aliens(aliens, ai_settings, ship, stats, screen, bullets, scoreboard,
								 logger)
		gf.update_screen(ai_settings, screen, ship, bullets, aliens, stars, stats,
				   			 play_button, scoreboard)

if __name__ == '__main__':
	run_game()
 