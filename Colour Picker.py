import pygame
pygame.init()

#Render display window
screen = pygame.display.set_mode((800, 600))

#sets titles for displays icon and program head aswell as pulls files from fold
pygame.display.set_caption("RGB Colour Pick")
icon = pygame.image.load('world.png')
dot1 = pygame.image.load('dot.png')
backdropGUI = pygame.image.load('Colour gui.png')
pygame.display.set_icon(icon)

#resizes the gui
SizeGUI = (500, 500)
backdropGUI = pygame.transform.scale(backdropGUI, SizeGUI)

#gui render
def GUI():
    screen.blit(backdropGUI, (175, 80))
    screen.blit(dot1, (298, redChange))
    screen.blit(dot2, (393, greenChange))
    screen.blit(dot3, (484, blueChange))

#pre set valuse
red = 100
green = 100
blue = 100
dot2 = dot1
dot3 = dot1
redChange = 310
greenChange = 310
blueChange = 310

#game loop
isRunning = True
while isRunning:
    screen.fill((red, green, blue))
    GUI() # calls on GUI

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
#checks when keys are pressed and move dot
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                print("Pressed 7")
                redChange = redChange - 5
            elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                print("Pressed 4")
                redChange = redChange + 5
            elif event.key == pygame.K_KP8 or event.key == pygame.K_8:
                print("Pressed 8")
                greenChange = greenChange - 5
            elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                print("Pressed 5")
                greenChange = greenChange + 5
            elif event.key == pygame.K_KP9 or event.key == pygame.K_9:
                print("Pressed 9")
                blueChange = blueChange - 5
            elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
                print("Pressed 6")
                blueChange = blueChange + 5
#check when keys released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                print("Released 7")
            elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                print("Released 4")
            elif event.key == pygame.K_KP8 or event.key == pygame.K_8:
                print("Released 8")
            elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                print("Released 5")
            elif event.key == pygame.K_KP9 or event.key == pygame.K_9:
                print("Released 9")
            elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
                print("Released 6")
#the max and min high limit for the dots            
        if redChange > 420:
            redChange = 420
        elif redChange < 165:
            redChange = 165
            
        if greenChange > 420:
            greenChange = 420
        elif greenChange < 165:
            greenChange = 165

        if blueChange > 420:
            blueChange = 420
        elif blueChange < 165:
            blueChange = 165  

#- 165 to turn from x to 255 colour value
        red = redChange - 165  
        green = greenChange - 165
        blue = blueChange - 165

#inverting values from 0 to 255
        red = 255 - red
        green = 255 - green
        blue = 255 - blue
        PrintRGB = (red, green, blue)
        print("RGB:", PrintRGB)
    pygame.display.update()