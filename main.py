import pygame
import sys
from games.tic_tac_toe.tic_tac_toe import TicTacToe
from games.chess.main import  main as chess
from games.mine_sweeper.mine_sweeper import main as mine_sweeper
from games.sudoku.sudoku import main as sudoku
from games.sokoban.sokoban import main as sokoban

class Menu:
    def __init__(self, menu_items=None, menu_games=None):
        if menu_games is None:
            menu_games = [[(41, "data\\images\\test.png"), 127]]
        if menu_items is None:
            menu_items = [(396, 319), (305, 93), "Item", (0, 0, 0), (18, 0, 255), 0]
        self.menu_items = menu_items
        self.menu_games = menu_games

    # рендер каждого пункта
    def render_items(self, scr, font, active_item):
        for i in self.menu_items:
            if i[5] == active_item:
                scr.blit(font.render(i[2], 1, i[4]), i[0])
            else:
                scr.blit(font.render(i[2], 1, i[3]), i[0])

    def render_games(self, scr):
        screen.blit(pygame.image.load("data\\images\\background_fl.jpg"), (0, 0))
        for i in self.menu_games:
            for f in range(len(i) - 1):
                pygame.draw.rect(scr, (0, 0, 153), (i[f][0], i[-1], 272, 179), border_radius=25)
                screen.blit(pygame.image.load(i[f][1]), (i[f][0] + 22, i[-1] + 15))

    # цикл меню
    def menu_cyc(self):
        run = True
        menu_font = pygame.font.Font("data\\fonts\\Arial.otf", 80)
        menu_section = "items"
        pygame.mixer.music.load("data\\sounds\\bgmusic.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        mus = True
        while run:
            if not mus:
                mus = True
                pygame.mixer.music.play(-1)
            screen.fill((0, 0, 0))
            screen.blit(pygame.image.load("data\\images\\background.jpg"), (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            if menu_section == "items":
                item = -1
                for i in self.menu_items:
                    if i[0][0] + i[1][0] > mouse_pos[0] > i[0][0] and i[0][1] + i[1][1] > mouse_pos[1] > i[0][1]:
                        item = i[5]
                self.render_items(screen, menu_font, item)
                for menu_event in pygame.event.get():
                    if menu_event.type == pygame.QUIT:
                        sys.exit()
                    if menu_event.type == pygame.MOUSEBUTTONDOWN and menu_event.button == 1:
                        if item == 0:
                            menu_section = "games"
                        elif item == 1:
                            sys.exit()
            if menu_section == "games":
                self.render_games(screen)
                game = 0
                for i in self.menu_games:
                    for f in range(len(i) - 1):
                        if i[f][0] + 272 > mouse_pos[0] > i[f][0] and i[-1] + 179 > mouse_pos[1] > i[-1]:
                            game = i[f][2]
                for games_event in pygame.event.get():
                    if games_event.type == pygame.QUIT:
                        sys.exit()
                    if games_event.type == pygame.MOUSEBUTTONDOWN and games_event.button == 1:
                        if game == 0:
                            pygame.mixer.music.pause()
                            mus = False
                            TicTacToe(screen)
                        if game == 1:
                            pygame.mixer.music.pause()
                            mus = False
                            chess(screen)
                        if game == 2:
                            pygame.mixer.music.pause()
                            mus = False
                            mine_sweeper(screen)
                        if game == 3:
                            pygame.mixer.music.pause()
                            mus = False
                            pygame.display.set_mode((500, 600))
                            sudoku(screen)
                            pygame.display.set_mode((1280, 720))
                        if game == 4:
                            pygame.mixer.music.pause()
                            mus = False
                            pygame.display.set_mode((512, 512))
                            sokoban(screen)
                            pygame.display.set_mode((1280, 720))
                    if games_event.type == pygame.KEYDOWN and games_event.key == pygame.K_ESCAPE:
                        menu_section = "items"

            pygame.display.flip()


items = [((483, 215), (305, 93), "Играть", (0, 0, 0), (18, 0, 255), 0),
         ((488, 360), (289, 93), "Выйти", (0, 0, 0), (18, 0, 255), 1)]

games = [[(41, "data\\images\\game_ttt.png", 0), (350, "data\\images\\game_chess.png", 1), (659, "data\\images\\game_mine_sweeper.png", 2),
          (968, "data\\images\\sudoku.png", 3), 127], [(41, "data\\images\\game_sokoban.png", 4), 413]]

pygame.init()
size = width, height = 1280, 720
pygame.display.set_caption("PyGames")
screen = pygame.display.set_mode(size)
menu = Menu(items, games)
menu.menu_cyc()
pygame.quit()
