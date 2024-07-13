import pygame
from sys import exit
import random

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

def colorMaker(r,g,b):
    return (r*255,g*255,b*255)

a_note = pygame.mixer.Sound('A.wav')
b_note = pygame.mixer.Sound('B.wav')
c_note = pygame.mixer.Sound('C.wav')
c2_note = pygame.mixer.Sound('C2.wav')
d_note = pygame.mixer.Sound('D.wav')
e_note = pygame.mixer.Sound('E.wav')
f_note = pygame.mixer.Sound('F.wav')
g_note = pygame.mixer.Sound('G.wav')
g_flat_note = pygame.mixer.Sound('Gb.wav')




soundList = [d_note,f_note,a_note,c2_note,
             d_note,f_note,g_note,b_note,
             c_note,e_note,g_note,b_note,
             c_note,e_note,g_note,a_note]
soundLen = len(soundList)


font = pygame.font.SysFont(pygame.font.get_fonts()[101],100)
font_title = font.render('Running',False,colorMaker(0,0,0))

font2 = pygame.font.SysFont(pygame.font.get_fonts()[1],40)



screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Never ending run')


sprite_sheet_image = pygame.image.load('spritesheet.png').convert_alpha()
sprite_sheet_image.set_colorkey((153,217,234))

def get_imageR1(sheet, frame, width, height, scale, colorKey):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet,(0,0),((frame * width),0,width,height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colorKey)

    return image
def get_imageR2(sheet, frame, width, height, scale, colorKey):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet,(0,0),((frame * width),130,width,height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colorKey)

    return image

frame_0 = get_imageR1(sprite_sheet_image, 0,
                    130,130,2,(colorMaker(0,0,0)))
frame_1 = get_imageR1(sprite_sheet_image, 1,
                    130,130,2,(colorMaker(0,0,0)))
frame_2 = get_imageR2(sprite_sheet_image, 0,
                    130,130,2,(colorMaker(0,0,0)))
frame_3 = get_imageR2(sprite_sheet_image, 1,
                    130,130,2,(colorMaker(0,0,0)))

frames = [frame_0,frame_1,frame_2,frame_3,50]


run = True

count = 0
x_pos = -200
x_end = 800
rate = 0
lapCount = 0

sound_pos = 0

r = 0
g = 0
b = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(colorMaker(.1,.5,.5))
    if count > 4:
        count = 0
        
    
    if x_pos > x_end:
        x_pos = -200
        lapCount += 1
        if rate < 120:
            rate += 4
        else:
            rate = 0
        if sound_pos < soundLen:
            soundList[sound_pos].play()
            sound_pos += 1
        else:
            sound_pos = 0
            soundList[sound_pos].play()
            sound_pos += 1

    screen.blit(frames[int(count)],(x_pos,130))
    
    screen.blit(font_title,(250,30))
    pygame.draw.line(screen, (colorMaker(0,.9,.5)),(0,390),(800,390),10)
    pygame.draw.rect(screen,colorMaker(0,.9,.5),(0,390,800,800),0)
    rate_text = font2.render(f"The Speed up rate is +{rate} per run",False,(colorMaker(r,g,b)))


    if r <= .96 and g <= .96 and b <= 0:
        r += .02
        g += .02


    lap_text = font2.render(f"Lap count = {lapCount}",False,(colorMaker(0,0,0)))
    screen.blit(rate_text,(50,600))
    screen.blit(lap_text,(50,700))
    
    x_pos += 11 + rate 
    count += .26
    

    pygame.display.update()
    clock.tick(60)
