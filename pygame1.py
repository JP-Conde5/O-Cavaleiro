import pygame as pg
import sys 


pg.init()
#Cores do jogo
colors = {
    "gray": (71,71,71), 
    "light_gray": (211,211,211), 
    "green": (138,179,100),
    "black": (0,0,0),
    "white": (255,255,255)
}
#Tela
size = (720, 720)
screen = pg.display.set_mode(size)
pg.display.set_caption("Cavaleiro")
#Button
pos_button = (size[0]/2-70, size[1]/2-15)
size_button = (140, 30)
#Texto
font_title = pg.font.SysFont('arial', 40, True, True)
font_text = pg.font.SysFont('arial', 20, False, True)
#Personagem
pos_person = [size[0]/2-7, size[1]/2-7]
size_person = (14, 14)
#Variáveis de Estado
running = True
start = False
relogio = pg.time.Clock()
while running:
    relogio.tick(30)
    mouse = pg.mouse.get_pos()
    cond_button = pos_button[0] <= mouse[0] <= size[1]/2 + 70 and pos_button[1] <= mouse[1] <= size[1]/2 + 15
    for ev in pg.event.get(): 
        if ev.type == pg.QUIT: 
            pg.quit() 
        if ev.type == pg.MOUSEBUTTONDOWN:
            if not start and cond_button:
                start = True
                screen.fill(colors["green"])
        if True in pg.key.get_pressed():
            if pg.key.get_pressed()[pg.K_w]:
                pos_person[1] -= 10
            if pg.key.get_pressed()[pg.K_s]:
                pos_person[1] += 10
            if pg.key.get_pressed()[pg.K_a]:
                pos_person[0] -= 10
            if pg.key.get_pressed()[pg.K_d]:
                pos_person[0] += 10
    #Menu inicial
    if not start:
        title = "O CAVALEIRO"
        title = font_title.render(title, True, colors["light_gray"])
        options = ["Start", "Quit"]
        if cond_button:
            for i in range(1):
                options[i] = font_text.render(options[i], True, colors["black"])  
            pg.draw.rect(screen, colors["light_gray"], [pos_button[0], pos_button[1], size_button[0], size_button[1]], 0, 10)
        else:
            for i in range(1):
                options[i] = font_text.render(options[i], True, colors["white"])  
            pg.draw.rect(screen, colors["gray"], [pos_button[0], pos_button[1], size_button[0], size_button[1]], 0, 10)
        screen.blit(title, (size[0]/2 - 50, 200))
        screen.blit(options[0], (pos_button[0] + 20, pos_button[1] + 5))
    #Jogo
    else:
        screen.fill(colors["green"])
        pg.draw.rect(screen, colors["light_gray"], [pos_person[0], pos_person[1], size_person[0], size_person[1]], 0, 5)
    pg.display.update()
    
        