import unittest
from unittest import TestCase
from unittest.mock import MagicMock

import logic
import pygame
from coverage import coverage
from logic.Computer_checkers import Computer_checkers
from logic.Game import Game
from logic.Main import main
from logic.Player_checkers import Player_checkers
from logic.client_game import Client_game
from logic.game_object import GameObject


class Tests(TestCase):

    def test_game_object_init(self):
        game_obj = GameObject(5, 5, 10, 10)
        self.assertTrue(True)

    def test_game_object_center(self):
        game_obj = GameObject(5, 5, 10, 10)
        self.assertEqual((10, 10), game_obj.center)

    def test_game_object_move(self):
        game_obj = GameObject(5, 5, 10, 10)
        game_obj.move(1, 1)
        self.assertEqual((11, 11), game_obj.center)

    def test_game_object_update(self):
        game_obj = GameObject(5, 5, 10, 10)
        game_obj.update()
        game_obj.speed = (1, 1)
        game_obj.update()
        self.assertEqual((11, 11), game_obj.center)

    def test_Player_checkers_init(self):
        checker = Player_checkers(0, 0, 10, (0, 0, 0))
        self.assertTrue(True)

    def test_Player_checkers_draw(self):
        checker = Player_checkers(0, 0, 10, (0, 0, 0))
        checker.draw(pygame.display.set_mode((775, 800)))
        self.assertTrue(True)

    def test_Computer_checkers_init(self):
        checker = Computer_checkers(0, 0, 10, (0, 0, 0))
        self.assertTrue(True)

    def test_Computer_checkers_draw(self):
        checker = Computer_checkers(0, 0, 10, (0, 0, 0))
        checker.draw(pygame.display.set_mode((775, 800)))
        self.assertTrue(True)

    def test_game_init(self):
        x_size = 775
        y_size = 800
        game = Game("Checkers 100", x_size, y_size, "1.png", 120)
        self.assertTrue(True)

    def test_game_draw_hexagons(self):
        x_size = 775
        y_size = 800
        game = Game("Checkers 100", x_size, y_size, "1.png", 120)
        game.draw_hexagons()
        self.assertTrue(True)

if __name__ == '__main__':
    cover = coverage()
    cover.erase()
    try:
        cover.start()
        unittest.main()
    finally:
        cover.stop()
        cover.report([logic.Game, logic.game_object, logic.Player_checkers,
                      logic.Computer_checkers])
