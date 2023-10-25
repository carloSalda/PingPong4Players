# Carlos Saldaña 

#Importar todas las librerías necesarios para el código
from random import choice, random
from turtle import *
from freegames import vector

#Numero random para decidir valores de x y y de las pelotas para que cambie de dirección
def value(): 
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())
ball2 = vector(0,0)
aim2= vector(value(), value())
state = {1: 0, 2: 0, 3: 0, 4: 0}
score = {1: 0, 2: 0}

#Función para mover el rectangulo de cada jugador y limitarlos dentro de la pantalla de juego
def move(player, change): 
    state[player] += change
    if state[player] > 180 or state[player] < -210:
        state[player] -= change

#Función para determinar el tamaño de rectangulos
def rectangle(x, y, width, height, col): 
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    color(col)
    end_fill()

#Mostrar el puntaje de cada equipo en la pantalla
def draw_score():
    up()
    #Mostrar el puntaje del equipo rojo
    goto(-20, 180)
    write("Equipo 1: {}".format(score[1]),align="right",
          font=("Courier", 16, "normal"))
    
    #Mostrar el puntaje del equipo azul
    goto(30, 180)
    write("Equipo 2: {}".format(score[2]),align="left",
          font=("Courier", 16, "normal"))

#Funcion que dibuja el juego y controla colisiones y areas de juego
def draw():   
    clear()
    rectangle(-150, state[1], 10, 50, "blue") #Dibuja el rectangulo del jugador 1 del equipo azul y se encuentra adelante
    rectangle(-190, state[3], 10, 50, "blue") #Dibuja el rectangulo del jugador 2 del equipo azul y se encuentra atrás
    rectangle(140, state[4], 10, 50, "red") #Dibuja el rectangulo del jugador 1 del equipo rojo y se encuentra adelante
    rectangle(180, state[2], 10, 50, "red") #Dibuja el rectangulo del jugador 2 del equipo rojo y se encuentra atrás
    
    rectangle(0,50,10,200,"black")  #Dibuja la barrera que se encuentra en medio superior
    rectangle(0,-50,10,-200, "black")  #Dibuja la barrera que se encuentra en medio inferior
    draw_score()

    #Crea la pelota 1 y le asigna los valores de dirección
    ball.move(aim) 
    x = ball.x
    y = ball.y

    #Color y tamaño de la pelota 1
    up()
    goto(x, y)
    dot(10, "blue")                  
    
    #Crea la pelota 2 y le asigna los valores de dirección
    ball2.move(aim2) 
    x2 = ball2.x
    y2 = ball2.y

    #Color y tamaño de la pelota 2
    up()
    goto(x2, y2)
    dot(10, "red") 
    update()

    #Rebota la pelota azul automáticamente cuando toca a la pared de arriba y abajo
    if y < -200 or y > 200:
        aim.y = -aim.y

    #Rebota la pelota azul si toca a la barrera que se encuentra en medio superior
    if -5 < x < 17 and y > 60:
        aim.y = -aim.y
        aim.x = -aim.x

    #Rebota la pelota azul si toca a la barrera que se encuentra en medio inferior
    if -5 < x < 17 and y < -60:
        aim.y = -aim.y
        aim.x = -aim.x

    #Rebote de la pelota cuando los jugadores logra a catchar la pelota azul
    if x < -175 and state[3] <= y <= state[3] + 50:
        aim.x = -aim.x
        aim.y = -aim.y

    if x < -135 and state[1] <= y <= state[1] + 50:                    
        aim.x = -aim.x
        aim.y = -aim.y

    if x > 135 and state[4] <= y <= state[4] + 50:
        aim.x = -aim.x
        aim.y = -aim.y
        
    if x > 175 and state[2] <= y <= state[2] + 50:
        aim.x = -aim.x
        aim.y = -aim.y

    #Sumar el puntaje para el equipo rojo si el equipo azul no logra catchar la pelota azul
    if x < -210: 
        ball.x, ball.y = 0, 0
        aim.x, aim.y = value(), value()
        score[2] += 1

    #Sumar el puntaje para el equipo azul si el equipo rojo no logra catchar la pelota azul
    if x > 210: 
        ball.x, ball.y = 0, 0                          
        aim.x, aim.y = -value(), -value()
        score[1] += 1

    #Rebota la pelota roja automáticamente cuando toca a la pared de arriba y abajo
    if y2 < -190 or y2 > 190:
        aim2.y = -aim2.y

    #Rebota la pelota roja si toca a las barreras que se encuentra en medio superior
    if -5 < x2 < 17 and y2 > 60:
        aim2.y = -aim2.y
        aim2.x = -aim2.x

    #Rebota la pelota roja si toca a las barreras que se encuentra en medio inferior
    if -5 < x2 < 17 and y2 < -60:
        aim2.y = -aim2.y
        aim2.x = -aim2.x

    #Rebote de la pelota cuando los jugadores logra a catchar la pelota roja
    if x2 < -175 and state[3] <= y2 <= state[3] + 50:        
        aim2.x = -aim2.x
        aim2.y = -aim2.y

    if x2 < -145 and state[1] <= y2 <= state[1] + 50:
        aim2.x = -aim2.x
        aim2.y = -aim2.y

    if x2 > 135 and state[4] <= y2 <= state[4] + 50:
        aim2.x = -aim2.x
        aim2.y = -aim2.y
    
    if x2 > 175 and state[2] <= y2 <= state[2] + 50:
        aim2.x = -aim2.x
        aim2.y = -aim2.y

    #Sumar el puntaje para el equipo rojo si el equipo azul no logra catchar la pelota roja
    if x2 < -210: 
        ball2.x, ball2.y = 0, 0                                    
        aim2.x, aim2.y = value(), value()
        score[2] += 1
    
    #Sumar el puntaje para el equipo azul si el equipo rojo no logra catchar la pelota roja
    if x2 > 210: 
        ball2.x, ball2.y = 0, 0
        aim2.x, aim2.y = -value(), -value()
        score[1] += 1

    #Gana el equipo que anote primero 10 puntos, y se desplpiega qué equipo fue ese en el eje (0,0)
    #Utilizamos return para indicar que una vez que se llegue a los 10 puntos, el juego termina
    if score[1] == 11:
        goto(0, 0)
        write(("Finish, Team blue win!"),align="center", font=("Courier", 16, "normal"))
        return
      
    if score[2] == 11:
        goto(0, 0)
        write(("Finish, Team red win!"),align="center", font=("Courier", 16, "normal"))
        return

    #Indica la velocidad de las pelotas y llama a la función draw una vez que inicia el juego
    ontimer(draw, 40)
    
    
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#Controles jugador 1 Equipo azul
onkey(lambda: move(1, 30), 'w')       
onkey(lambda: move(1, -30), 's')
#Controles jugador 2 Equipo azul
onkey(lambda: move(3, 30), 'a')        
onkey(lambda: move(3, -30), 'd')
#Controles jugador 1 Equipo rojo
onkey(lambda: move(4, 30), 'Up')         
onkey(lambda: move(4, -30), 'Down')
#Controles jugador 2 Equipo rojo
onkey(lambda: move(2, 30), 'Left')  
onkey(lambda: move(2, -30), 'Right')
draw()
done()