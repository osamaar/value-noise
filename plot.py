#!/usr/bin/env python-32

import pygame

RESOLUTION = (800, 600)
FPS = 10
CAPTION = 'Value Noise'
BGCOLOR = (200, 200, 200)

def normalize(bitmap, start, end):
    size = len(bitmap)
    peak = 1.0 * max(max(x) for x in bitmap)
    valley = 1.0 * min(min(x) for x in bitmap)
    scale = end - start
    for i in xrange(size):
        for j in xrange(size):
            bitmap[i][j] = start + scale*(bitmap[i][j] - valley)/(peak - valley)
            
def load(fn):
    m = []
    f = open(fn, 'r')
    for line in f:
        m.append(map(int, line.split()))
    return m
    
def mainloop():
    # init stuff
    m = load('land.dat')
    msz = len(m)
    normalize(m, 0, 255)
    #print '\n'.join(str(x) for x in m)

    # init pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)
    screen.fill(BGCOLOR)
    
    done = False
    while not done:
        # events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
            elif (event.type==pygame.KEYUP and
                  event.key==pygame.K_ESCAPE):
                done = True
            elif (event.type==pygame.KEYUP and
                  event.key==pygame.K_SPACE):
                pass
        
        # update

        # draw
        screen.fill(BGCOLOR)
        for i in xrange(msz):
            for j in xrange(msz):
                clr = [int(m[i][j])] *3
                #cell = (20 + i*2), (20 + j*2), 2, 2
                #pygame.draw.rect(screen, clr, cell)
                screen.set_at((20+i, 20+j), clr)
                
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__=='__main__':
    mainloop()
