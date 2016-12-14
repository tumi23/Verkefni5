import math, pygame, sys, os, pygame.mixer
import random
import euclid
from pygame import *

#Thar sem thetta er nu adeins prototypa tha er ekki vodaleg dypt i leikinum en tho eru main "game logic"-id tharna
#Og her thad ad faera sig um platforma, med thvi ad hoppa og skoppa um svaedid og finna lykilinn til thess ad opna
#hurdina sem er stadsett til haegri a skjanum, lenti i vandraedum med ad lata lykilinn hverfa thegar madur hefur nad
#honum en eins og sest hverfur hann ekki og er thvi bara solid objective tharna.

DISPLAY = (1280, 850)
DEPTH = 32
FLAGS = 0
KEY = 0
GO = 0
DED = 0
DEATHS = 0

background = pygame.image.load("images/background/area1.png")
character = pygame.image.load("images/character/spritefeis.png")
background2 = pygame.image.load("images/character/gudniminn.png")
item = pygame.image.load("images/character/KEY.png")
background2 = pygame.transform.scale(background2,(1280, 850))
character = pygame.transform.scale(character,(32,32))
item = pygame.transform.scale(item,(64,32))

def main():
    pygame.init()
    screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("PlatformerLokaverkefni")
    timer = time.Clock()
    screen.blit(background,(0,0))
    up = down = left = right = False
    bg = Surface((1280, 800))
    bg.blit(background,(0,0))
    bg.convert()
    entities = pygame.sprite.Group()
    player = Player(32, 256)
    platforms = []
    
    x = y = 0
    level = [
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                                      P",
    "P                                      P",
    "P                                      P",
    "PPP     PPPPPPPPPP    PPPPPPPPPP     PPP",
    "PPP     PPPPPPPPPP    PPPPPPPPPP     PPP",
    "P                                      D",
    "P                                      D",
    "PPPPP       PPPPPPPPPPPPPPPP       PPPPP",
    "P   P       PP PPPP     PPPP       PPPPP",
    "P  P         PP   P  PPP            PPPP",
    "P P                PPP               P P",
    "P P                                  P P", 
    "P P                                  P P",
    "P PPPPPPPPP                  PPPPPPPP  P",
    "P PPPPPPPPP     PPP  PPP     PPPPPPPPP P",
    "P PP            P P  P P            P   ",
    "P PP        PPPPPP   P PPPPP         P  ",
    "P P  PP     PPPPPP    PPPPPP     PP  P  ",
    "P P  PPPPP      PP    PP      PPP P  P  ",
    "P P  PPPPP      PP    PP      P  PP  P  ",
    "P P    PP                      PP    P  ",
    "P P                                  P  ",
    "P P                K                 P  ",
    "PPPPPPPPPPP     PPPPPPPP     PPPPPPPPPPP",
    "           FFFFF        FFFFF           ",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "K":
                k = KeyBlock(x, y)
                platforms.append(k)
                entities.add(k)
            if col == "D":
                d = Door(x, y)
                platforms.append(d)
                entities.add(d)
            if col == "F":
                f = Fallpit(x, y)
                platforms.append(f)
                entities.add(f)
            x += 32
        y += 32
        x = 0
    
    entities.add(player)
    
    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE: 
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
        
        # Byr til bakgruninn i theim formum sem passa
        if GO == 1:
           screen.fill((0,0,0))
           myfont2 = pygame.font.SysFont("monospace", 50)
           label2 = myfont2.render("Thu hefur unnid til verdlauna!", 100, (255,0,0))
           screen.blit(background2,(0,0))
           screen.blit(label2, (220, 600))
           
        elif GO == 0:
            for y in range(1):
                for x in range(1):
                    screen.blit(bg, (x * 1280, y * 800))
                    myfont = pygame.font.SysFont("monospace", 15)
                    label = myfont.render("Keys Acquired: "+str(KEY-1), 30, (0,0,0))
                    screen.blit(label, (32, 825))
                    label = myfont.render("Keys Acquired: "+str(KEY), 30, (255,255,255))
                    screen.blit(label, (32, 825))
                    myfont = pygame.font.SysFont("monospace", 15)
                    label = myfont.render("Deaths: "+str(DEATHS-1), 30, (0,0,0))
                    screen.blit(label, (1150, 825))
                    label = myfont.render("Deaths: "+str(DEATHS), 30, (255,255,255))
                    screen.blit(label, (1150, 825))
                    
        if DED == 1:
            global DED
            player = Player(64, 256)
            entities.add(player)
            DED = 0
            myfont = pygame.font.SysFont("monospace", 15)
            label = myfont.render("Keys Acquired: "+str(KEY+1), 30, (0,0,0))
            screen.blit(label, (32, 825))
            label = myfont.render("Keys Acquired: "+str(KEY), 30, (255,255,255))
            screen.blit(label, (32, 825))
        # Uppfaerir player-inn og teiknar allt annad
        player.update(up, down, left, right, platforms)
        entities.draw(screen)
        
        pygame.display.flip()

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.image.blit(character,(0, 0))
        self.rect = Rect(x, y, 32, 32)
    def update(self, up, down, left, right, platforms):
        if GO == 0:
            if up:
                # Getur adeins hoppad ef hann er a jordinni
                if self.onGround: self.yvel -= 11
            if down:
                pass
            if left:
                self.xvel = -5
            if right:
                self.xvel = 5
            if not self.onGround:
                # Hreyfist med thyngdaraflinu adeins ef hann er i loftinu
                self.yvel += 0.3
                # max falling speed
                if self.yvel > 30: self.yvel = 30
            if not(left or right):
                self.xvel = 0
            
            self.rect.left += self.xvel
           
            self.collide(self.xvel, 0, platforms)
            
            self.rect.top += self.yvel
           
            self.onGround = False;
            
            self.collide(0, self.yvel, platforms)
        
        elif GO == 1:
            self.image.fill((255,0,255))
    
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                if isinstance(p, KeyBlock):
                    global KEY
                    KEY = 1
                if isinstance(p, Door):
                    global KEY
                    if KEY == 1:
                        global GO
                        GO = 1
                if isinstance(p, Fallpit):
                    global DED, DEATHS, KEY
                    DED = 1
                    DEATHS += 1
                    KEY = 0
                if yvel < 0: self.rect.top = p.rect.bottom
                if xvel > 0: self.rect.right = p.rect.left
                if xvel < 0: self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0: self.rect.top = p.rect.bottom

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.rect = Rect(x, y, 32, 32)
    
    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

class KeyBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = Surface((64,32))
        self.image.blit(item,(0, 0))
        self.rect = Rect(x,y, 64, 32)
        if KEY == 1:
            self.rect = Rect(x,y, 0,0)
        
class Door(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color(255,0,255))

class Fallpit(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color(0,0,255))
        self.image.set_colorkey((0, 0, 255))




if(__name__ == "__main__"):
    main()