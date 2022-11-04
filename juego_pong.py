import os
import pygame
pygame.init()

#colores
gris=(128,128,128)
rosado=(204,0,202)
amarillo=(255,255,0)
azul=(0,0,204)
rojo=(153,0,0)
negro=(0,0,0)
blanco=(255,255,255)
verde=(0,102,0)
verde_oscuro=(0,52,0)
ventanaTamaño=(800,600)
jugadorAncho=15
jugadorAlto=90
centro=150

ventana=pygame.display.set_mode(ventanaTamaño)
reloj=pygame.time.Clock()


#jugador 1
jugador1_x_coor=50
jugador1_y_coor=300-45
jugador1_y_velocidad=0

#jugador 2
jugador2_x_coor=750-jugadorAncho
jugador2_y_coor=300-45
jugador2_y_velocidad=0

#pelota
pelota_x=400
pelota_y=300
pelota_velocidad_X=3
pelota_velocidad_y=3

#obstaculo
obstaculo1_x=400
obstaculo1_y=0
obstaculo1_velocidad_y=1
obstaculo1_velocidad_x=1

obstaculo2_x=400
obstaculo2_y=530
obstaculo2_velocidad_y=1
obstaculo2_velocidad_x=1
#contador de puntos
contador1=0
contador2=0
inicio_tiempo = pygame.time.get_ticks()
fin_tiempo = inicio_tiempo + 120000
tiempo=70

#texto
#mifuente=pygame.font.Font(None,30)
#mitexto=mifuente.render(contador1,25,(128,108,40))

game_over=False

while not game_over: 
    mifuente=pygame.font.Font(None,100)
    mitexto=mifuente.render(str(contador1),25,(blanco))   
    mifuente=pygame.font.Font(None,100)
    mitexto2=mifuente.render(str(contador2),25,(blanco)) 
    mifuente=pygame.font.Font(None,200) 
    ganar1=mifuente.render("gano el jugador 1",25,(blanco))
    mifuente=pygame.font.Font(None,100) 
    #tiempo_pantalla=mifuente.render(str(tiempo),25,(blanco))
    #tiempo_pantalla=mifuente.render(str(int(fin_tiempo / 1000)),25,(blanco))
    #tiempo2=pygame.time.get_ticks()/1000
    #fin_tiempo-=100



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            #jugador1
            if event.key==pygame.K_w:
                jugador1_y_velocidad=-3
            if event.key==pygame.K_s:
                jugador1_y_velocidad=3
          #jugador2
            if event.key==pygame.K_UP:
                jugador2_y_velocidad=-3
            if event.key==pygame.K_DOWN:
                jugador2_y_velocidad=3

        if event.type==pygame.KEYUP:
            #jugador1
            if event.key==pygame.K_w:
                jugador1_y_velocidad=0
            if event.key==pygame.K_s:
                jugador1_y_velocidad=0
          #jugador2
            if event.key==pygame.K_UP:
                jugador2_y_velocidad=0
            if event.key==pygame.K_DOWN:
                jugador2_y_velocidad=0

    if pelota_y>590 or pelota_y<10:
       pelota_velocidad_y*=-1

    if obstaculo1_y>229 or obstaculo1_y<0:
        obstaculo1_velocidad_y*=-1

    if obstaculo2_y>530 or obstaculo2_y<301:
        obstaculo2_velocidad_y*=-1

    if tiempo>5050:
        ventana

        
        break

    #revisa si la pelota sale lado derecho
    if pelota_x>800:
        pelota_x=400
        pelota_y=300
        contador1+=1
        #si se sale de la pantalla,inviente direccion
        pelota_velocidad_X*=-1
        pelota_velocidad_y*=-1

        #revisa si la pelota sale lado izquierdo
    if pelota_x<0:
        pelota_x=400
        pelota_y=300
        contador2+=1
        #si se sale de la pantalla,inviente direccion
        pelota_velocidad_X*=-1
        pelota_velocidad_y*=-1

    """
    if contador1==3:
        pygame.cdrom.pause()
        ventana.blit(ganar1,(400,300))
    """

    #MODIFICAR LAS CORDENADAS POR MOVIMIENTOS
    jugador1_y_coor+=jugador1_y_velocidad
    jugador2_y_coor+=jugador2_y_velocidad

    pelota_x+=pelota_velocidad_X
    pelota_y+=pelota_velocidad_y

    obstaculo1_y+=obstaculo1_velocidad_y
    obstaculo2_y-=obstaculo2_velocidad_y

     

    ventana.fill(verde)
    #zona de dibujo
    #fondo
    linea_horizontal=pygame.draw.rect(ventana,verde_oscuro,(0,50,800,50))
    linea_horizontal=pygame.draw.rect(ventana,verde_oscuro,(0,150,800,50))
    linea_horizontal=pygame.draw.rect(ventana,verde_oscuro,(0,250,800,50))
    linea_horizontal=pygame.draw.rect(ventana,verde_oscuro,(0,350,800,50))
    linea_horizontal=pygame.draw.rect(ventana,verde_oscuro,(0,450,800,50))
    linea_horizontal=pygame.draw.rect(ventana,verde_oscuro,(0,550,800,50))
    linea_horizontal=pygame.draw.rect(ventana,verde_oscuro,(0,650,800,50))
    

    linea_horizontal=pygame.draw.rect(ventana,blanco,(0,0,800,10))
    linea_horizontal=pygame.draw.rect(ventana,blanco,(0,590,800,10))


    linea_centro=pygame.draw.ellipse(ventana,blanco,(300,200,200,200),15)
    linea_central=pygame.draw.rect(ventana,blanco,(400,0,10,600))

    #lo demas
    obstaculo1=pygame.draw.rect(ventana,amarillo,(obstaculo1_x,obstaculo1_y,15,70))
    obstaculo2=pygame.draw.rect(ventana,rosado,(obstaculo1_x,obstaculo2_y,15,70))
    jugador1=pygame.draw.rect(ventana,amarillo,(jugador1_x_coor,jugador1_y_coor,jugadorAncho,jugadorAlto))
    jugador2=pygame.draw.rect(ventana,rosado,(jugador2_x_coor,jugador2_y_coor,jugadorAncho,jugadorAlto))
    pelota=pygame.draw.circle(ventana,gris,(pelota_x,pelota_y),10)

    
    

    #colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2) or pelota.colliderect(obstaculo2) or pelota.colliderect(obstaculo1):
        pelota_velocidad_X*=-1

    if obstaculo1.colliderect(obstaculo2) or obstaculo2.colliderect(obstaculo1):
        obstaculo1_velocidad_y*=-1
        obstaculo2_velocidad_y*=-1

    ventana.blit(mitexto,(200,10))
    ventana.blit(mitexto2,(600,10))
    #ventana.blit(tiempo_pantalla,(350,10))
    pygame.display.flip()
    
    print("puntajes",contador1,contador2)
    
    reloj.tick(60)
pygame.quit()
