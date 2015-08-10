#!/usr/bin/env python-32

import sys
import pygame
import vn

RESOLUTION = (800, 600)
FPS = 10
CAPTION = 'Value Noise | exact map size'
BGCOLOR = (200, 200, 200)

def mainloop():
    # init stuff
    msz = 512
    maxit = -1
    lvls = 255
    m = vn.generate(msz, maxit, map_seed='hello')
    vn.normalize(m, 0, lvls)
    m = [map(int, x) for x in m]
    vn.normalize(m, 0, 255)
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
                m = vn.generate(msz, maxit)
                vn.normalize(m, 0, lvls)
                m = [map(int, x) for x in m]
                vn.normalize(m, 0, 255)
        
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
