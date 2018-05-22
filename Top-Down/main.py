import os
import pygame as pg
import settings as s
import sprites
import mobs


class Game:
    def __init__(self):
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((s.WIDTH, s.HEIGHT), s.FLAGS | pg.FULLSCREEN)
        pg.display.set_caption(s.TITLE)
        self.clock = pg.time.Clock()
        self.playing = True
        self.all_events = pg.event.get()
        pg.event.set_allowed(s.ALLOWED_EVENTS)

        self.all_sprites = pg.sprite.OrderedUpdates()
        self.map = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = None

    def new(self):
        self.all_sprites = pg.sprite.OrderedUpdates()
        self.map = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.enemies = pg.sprite.Group()

        l = sprites.Level(self, os.path.join(s.map_folder, "level.txt"), 60, 34)
        l.build()
        mobs.Enemy.seeing_player = False

        pistol1 = sprites.Pistol(self, False)
        pistol3 = sprites.Pistol(self, True)

        e1 = mobs.Enemy(self, (400, 150), pistol1)
        e2 = mobs.Enemy(self, (1200, 700))
        self.player = mobs.Player(self, (500, 700))
        pistol3.rect.x = 200
        pistol3.rect.y = 800

        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(s.FPS)
            self.handle_events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def handle_events(self):
        self.all_events = pg.event.get()
        for event in self.all_events:
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
                elif event.key == pg.K_F11:
                    if self.screen.get_flags() & pg.FULLSCREEN:
                        pg.display.set_mode((s.WIDTH, s.HEIGHT), s.FLAGS)
                    else:
                        pg.display.set_mode((s.WIDTH, s.HEIGHT), s.FLAGS | pg.FULLSCREEN)
                elif event.key == pg.K_t:
                    print(str(self.clock.get_fps()))

    def draw(self):
        pg.display.set_caption(s.TITLE + str(self.clock.get_fps()))
        # game loop - draw/ render
        self.screen.fill(s.BLACK)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
