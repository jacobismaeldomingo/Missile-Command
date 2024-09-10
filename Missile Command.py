# Missile Command - Jacob Domingo

import os  # winsound - windows
import random
import time
import turtle

mywindow = turtle.Screen()
mywindow.setup(800, 800)
mywindow.bgcolor("#2b2b2b")
mywindow.title("Missile Command")

mywindow.tracer(0, 0)  # turn off screen drawing

# -------------------------------------------------Instructions Screen--------------------------------------------------

# Instructions
instruction_writer = turtle.Turtle()
instruction_writer.speed(0)
instruction_writer.penup()
instruction_writer.color("white")
instruction_writer.goto(0, 250)
instruction_writer.hideturtle()
instruction_writer.write("Missile Command", align="center", font=("Arial", 40, "underline"))
instruction_writer.goto(0, 170)
instruction_writer.write("Instructions", align="center", font=("Arial", 30, "normal"))
instruction_writer.goto(0, 90)
instruction_writer.write("Use your mouse to defend your cities and silos", align="center", font=("Arial", 25, "normal"))
instruction_writer.goto(0, 40)
instruction_writer.write("against an endless hail of enemy missiles", align="center", font=("Arial", 25, "normal"))
instruction_writer.goto(-50, -60)
instruction_writer.write("Cities", align="center", font=("Arial", 30, "normal"))
instruction_writer.goto(-50, -110)
cityStamp = "./cityStamp.gif"
mywindow.addshape(cityStamp)
instruction_writer.shape(cityStamp)
instruction_writer.stamp()
instruction_writer.goto(50, -60)
instruction_writer.write("Silos", align="center", font=("Arial", 30, "normal"))
instruction_writer.goto(50, -110)
siloStamp = "./siloStamp.gif"
mywindow.addshape(siloStamp)
instruction_writer.shape(siloStamp)
instruction_writer.stamp()
instruction_writer.goto(0, -190)
instruction_writer.write("Enemy Missiles", align="center", font=("Arial", 30, "normal"))
instruction_writer.goto(-100, -235)
enemyStamp = "./enemyStamp.gif"
mywindow.addshape(enemyStamp)
instruction_writer.shape(enemyStamp)
instruction_writer.stamp()
instruction_writer.goto(0, -235)
invaderStamp = "./invaderStamp.gif"
mywindow.addshape(invaderStamp)
instruction_writer.shape(invaderStamp)
instruction_writer.stamp()
instruction_writer.goto(100, -235)
sideStamp = "./sideStamp.gif"
mywindow.addshape(sideStamp)
instruction_writer.shape(sideStamp)
instruction_writer.stamp()
instruction_writer.goto(0, -300)
instruction_writer.write("", align="center", font=("Arial", 30, "normal"))

time.sleep(5)
mywindow.clearscreen()

mywindow.bgcolor("#2b2b2b")
mywindow.tracer(0, 0)  # turn off screen drawing

# ---------------------------------------------Turtle Creation and Lists------------------------------------------------

# Border
edgeBoard = turtle.Turtle()  # this is the turtle drawer that will be use to make the border of the game
edgeBoard.speed(0)
edgeBoard.penup()
edgeBoard.turtlesize(1, 1)
edgeBoard.pensize(2)
edgeBoard.pencolor("white")
edgeBoard.goto(-300, -300)
edgeBoard.pendown()
for sides in range(4):
    edgeBoard.fd(600)
    edgeBoard.left(90)
edgeBoard.hideturtle()

# Timer
timer = turtle.Turtle()
timer.color("white")
timer.penup()
timer.speed(0)
timer.hideturtle()
timer.goto(290, 320)

# Sounds
#winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

# Game
gameLevel = 1
invader_count = 1
side_count = 1
game_count = 1

# Cities
cities = []
city_index = -1

# Silos
silos = []
silo_index = -1

# Player Missiles
player_missiles = []  # Hold all the active player missiles
player_storage = []  # Hold all the player missiles
player_index = -1

# Enemy Missiles
enemy_missiles = []  # Hold all the active enemy missiles
enemy_storage = []  # Hold all the enemy missiles
enemy_index = -1

# Invaders Missile
invader_missiles = []  # Hold all the active invader missiles
invader_storage = []  # Hold all the invader missiles
invader_index = -1

# Side Missile
side_missiles = []  # Hold all the active side missiles
side_storage = []  # Hold all the side missiles
side_index = -1
side_xcoordinates = [-300, 300]

# Score
score = 0
score1 = len(cities)
score2 = len(silos)
score3 = len(player_missiles)
level = gameLevel
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.speed(0)
score_pen.goto(-290, 320)
score_pen.color("white")
scores = "Score: %s, Cities: %s, Silos: %s, Missiles: %s, Level: %s" % (score, score1, score2, score3, level)
score_pen.write(scores, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# ------------------------------------------------Function Definitions--------------------------------------------------


def leave():  # Quit Button
    global quitFlag
    quitFlag = True
    return


def calculate_time():  # Score Points
    global oldTime, newTime, elapsedTime
    oldTime = newTime
    newTime = int(time.perf_counter())
    timeDiff = newTime - oldTime
    if timeDiff == 1:
        elapsedTime += 1
        timer.clear()
        timer.write(elapsedTime, font=("Arial", 16, "normal"))
    return


def make_city(x_city, y_city):  # Create Cities
    global city_index, cities
    city_index += 1
    cities.append(turtle.Turtle())
    cities[city_index].speed(0)
    cities[city_index].penup()
    cities[city_index].shape("square")
    cities[city_index].color("gray")
    cities[city_index].goto(x_city, y_city)
    return


def city_destroy():  # Destroy City
    city.clear()
    city.penup()
    city.goto(1000, 1000)


def make_silo(x_silo, y_silo):  # Create Silos
    global silo_index, silos
    silo_index += 1
    silos.append(turtle.Turtle())
    silos[silo_index].speed(0)
    silos[silo_index].penup()
    silos[silo_index].shape("square")
    silos[silo_index].color("blue")
    silos[silo_index].goto(x_silo, y_silo)
    return


def silo_destroy():  # Destroy Silo
    silo.clear()
    silo.penup()
    silo.goto(1000, 1000)


def make_player(x_player, y_player):  # Create Player missiles
    global player_index, player_storage
    player_index += 1
    player_storage.append(turtle.Turtle())
    player_storage[player_index].speed(0)
    player_storage[player_index].penup()
    player_storage[player_index].shape("circle")
    player_storage[player_index].color("white")
    player_storage[player_index].goto(x_player, y_player)
    player_storage[player_index].condition = "set"
    player_storage[player_index].target_x = 0
    player_storage[player_index].target_y = 0
    player_storage[player_index].dx = 0  # Change in x
    player_storage[player_index].dy = 0  # Change in y
    player_storage[player_index].slope = 0
    player_storage[player_index].size = 0.2
    player_storage[player_index].shapesize(player_storage[player_index].size, player_storage[player_index].size)  # 4 pixels
    player_storage[player_index].form = 0  # use for explosion
    player_storage[player_index].moving = 5  # speed
    return


def make_enemy(x_enemy, y_enemy):  # Create Enemy missiles
    global enemy_index, enemy_storage
    enemy_index += 1
    enemy_storage.append(turtle.Turtle())
    enemy_storage[enemy_index].speed(0)
    enemy_storage[enemy_index].penup()
    enemy_storage[enemy_index].shape("circle")
    enemy_storage[enemy_index].color("red")
    enemy_storage[enemy_index].goto(x_enemy, y_enemy)
    enemy_storage[enemy_index].hideturtle()
    enemy_storage[enemy_index].moving = 1.5  # speed
    enemy_storage[enemy_index].size = 0.2
    enemy_storage[enemy_index].shapesize(enemy_storage[enemy_index].size, enemy_storage[enemy_index].size)  # 4 pixels
    enemy_storage[enemy_index].form = 2  # use for the explosion
    enemy_storage[enemy_index].target_x = 0
    enemy_storage[enemy_index].target_y = 0
    enemy_storage[enemy_index].condition = "set"
    enemy_storage[enemy_index].dx = 0  # Change in x
    enemy_storage[enemy_index].dy = 0  # Change in y
    enemy_storage[enemy_index].slope = 0
    return


def make_invader(x_invader, y_invader):  # Create Invader Enemy missiles
    global invader_index, invader_storage
    invader_index += 1
    invader_storage.append(turtle.Turtle())
    invader_storage[invader_index].speed(0)
    invader_storage[invader_index].penup()
    invader_storage[invader_index].shape("circle")
    invader_storage[invader_index].color("yellow")
    invader_storage[invader_index].goto(x_invader, y_invader)
    invader_storage[invader_index].hideturtle()
    invader_storage[invader_index].moving = 2  # speed
    invader_storage[invader_index].size = 0.5
    invader_storage[invader_index].shapesize(invader_storage[invader_index].size, invader_storage[invader_index].size)  # 10 pixels
    invader_storage[invader_index].form = 2  # use for the explosion
    invader_storage[invader_index].target_x = 0
    invader_storage[invader_index].target_y = 0
    invader_storage[invader_index].condition = "set"
    invader_storage[invader_index].dx = 0  # Change in x
    invader_storage[invader_index].dy = 0  # Change in y
    invader_storage[invader_index].slope = 0
    return


def make_side(x_side, y_side):  # Create Side Enemy missiles
    global side_index, side_storage
    side_index += 1
    side_storage.append(turtle.Turtle())
    side_storage[side_index].speed(0)
    side_storage[side_index].penup()
    side_storage[side_index].shape("circle")
    side_storage[side_index].color("green")
    side_storage[side_index].goto(x_side, y_side)
    side_storage[side_index].hideturtle()
    side_storage[side_index].moving = 3  # speed
    side_storage[side_index].size = 0.9
    side_storage[side_index].shapesize(side_storage[side_index].size, side_storage[side_index].size)  # 18 pixels
    side_storage[side_index].form = 2  # use for the explosion
    side_storage[side_index].target_x = 0
    side_storage[side_index].target_y = 0
    side_storage[side_index].condition = "set"
    side_storage[side_index].dx = 0  # Change in x
    side_storage[side_index].dy = 0  # Change in y
    side_storage[side_index].slope = 0
    return


def enemy_target(enemy, target):  # Enemy randomly target a city or silo
    enemy.penup()
    enemy.goto(random.randint(-300, 300), 300)
    enemy.size = 0.2
    enemy.shapesize(enemy.size, enemy.size)
    enemy.pendown()

    enemy.targetx = target.xcor()
    enemy.targety = target.ycor()

    enemy.dx = enemy.xcor() - target.xcor()  # run
    # Avoid dividing it by 0 error
    if enemy.dx == 0:
        enemy.dx = 0.01
    enemy.dy = enemy.ycor() - target.ycor()  # rise
    enemy.slope = enemy.dy / enemy.dx  # rise/run

    enemy.condition = "fire"
    return


def enemy_move(enemy):  # Enemy Movement
    if enemy.condition == "fire":
        enemy.showturtle()
        enemy.setx(enemy.xcor() - (1 / enemy.slope) * enemy.moving)  # going down to target smoothly/equally
        enemy.sety(enemy.ycor() - enemy.moving)  # going down to target

        # Check if reaching target
        distance = enemy.distance(enemy.targetx, enemy.targety)
        if distance < 5:
            enemy.condition = "blow up"

    if enemy.condition == "blow up":
        enemy_explode(enemy)
    return


def enemy_explode(enemy):  # Explode Enemy
    os.system("afplay explosion.wav&") # OS
    enemy.form += 1
    if enemy.form <= 25:
        enemy.size = enemy.form / 10
        enemy.shapesize(enemy.size, enemy.size)  # example 1/10 times 20 = 2 (actual pixel size)
    elif enemy.form <= 50:
        enemy.size = (55 - enemy.form) / 10
        enemy.shapesize(enemy.size, enemy.size)  # Shrinks it down
    else:
        enemy_destroy(enemy)
    return


def enemy_destroy(enemy):  # Destroy Enemy
    enemy.clear()
    enemy.penup()
    enemy.goto(1000, 1000)
    enemy.size = 0.2
    enemy.shapesize(enemy.size, enemy.size)
    enemy.condition = "set"
    enemy.form = 2  # use for the explosion
    enemy_missiles.remove(enemy_missile)  # Remove enemy missiles from the list
    return


def invader_target(invader, target):  # Invader will randomly target a city or silo
    invader.penup()
    invader.goto(random.randint(-300, 300), 300)
    invader.size = 0.5
    invader.shapesize(invader.size, invader.size)
    invader.hideturtle()
    invader.pendown()

    invader.targetx = target.xcor()
    invader.targety = target.ycor()

    invader.dx = invader.xcor() - target.xcor()  # run
    # Avoid dividing it by 0 error
    if invader.dx == 0:
        invader.dx = 0.01
    invader.dy = invader.ycor() - target.ycor()  # rise
    invader.slope = invader.dy / invader.dx  # rise/run

    invader.condition = "fire"
    return


def invader_move(invader):  # Invader Movement
    global invader_count
    if invader.condition == "fire" and invader_count == 5:
        invader.showturtle()
        invader.setx(invader.xcor() - (1 / invader.slope) * invader.moving)  # going down to target
        invader.sety(invader.ycor() - invader.moving)  # going down to target

        # Check if reaching target
        distance = invader.distance(invader.targetx, invader.targety)
        if distance < 5:
            invader.condition = "blow up"

    if invader.condition == "blow up":
        invader_explode(invader)
    return


def invader_explode(invader):  # Explode Invader missile
    os.system("afplay explosion.wav&") # OS
    invader.form += 1
    if invader.form <= 25:
        invader.size = invader.form / 10
        invader.shapesize(invader.size, invader.size)  # example 1/10 times 20 = 2 (actual pixel size)
    elif invader.form <= 50:
        invader.size = (55 - invader.form) / 10
        invader.shapesize(invader.size, invader.size)  # Shrinks it down
    else:
        invader_destroy(invader)
    return


def invader_destroy(invader):  # Destroy Invader missile
    invader.clear()
    invader.penup()
    invader.goto(-1000, 1000)
    invader.size = 0.5
    invader.shapesize(invader.size, invader.size)
    invader.condition = "set"
    invader.form = 2  # use for the explosion
    return


def side_target(side, target):  # Side missile randomly target a city or silo
    side.penup()
    side.goto(random.choice(side_xcoordinates), random.randint(200, 250))
    side.size = 0.9
    side.shapesize(side.size, side.size)
    side.hideturtle()
    side.pendown()

    side.targetx = target.xcor()
    side.targety = target.ycor()

    side.dx = side.xcor() - target.xcor()  # run
    # Avoid dividing it by 0 error
    if side.dx == 0:
        side.dx = 0.01
    side.dy = side.ycor() - target.ycor()  # rise
    side.slope = side.dy / side.dx  # rise/run

    side.condition = "fire"
    return


def side_move(side):  # Side Missile Movement
    global side_count
    if side.condition == "fire" and side_count == 3:
        side.showturtle()
        side.setx(side.xcor() - (1 / side.slope) * side.moving)  # going down to target smoothly
        side.sety(side.ycor() - side.moving)  # going down to target

        # Check if reaching target
        distance = side.distance(side.targetx, side.targety)
        if distance < 5:
            side.condition = "blow up"

    if side.condition == "blow up":
        side_explode(side)
    return


def side_explode(side):  # Explode Side missile
    os.system("afplay explosion.wav&")  # OS
    side.form += 1
    if side.form <= 25:
        side.size = side.form / 10
        side.shapesize(side.size, side.size)  # example 1/10 times 20 = 2 (actual pixel size)
    elif side.form <= 50:
        side.size = (55 - side.form) / 10
        side.shapesize(side.size, side.size)  # Shrinks it down
    else:
        side_destroy(side)
    return


def side_destroy(side):  # Destroy Side missile
    side.clear()
    side.penup()
    side.goto(1000, 1000)
    side.size = 0.9
    side.shapesize(side.size, side.size)
    side.condition = "set"
    side.form = 2  # use for the explosion
    return


def player_target(player, x, y):  # Player Target
    if player.condition == "set":
        player.target_x = x
        player.target_y = y

        player.dx = player.xcor() - player.target_x  # run
        # Avoid dividing it by 0 error
        if player.dx == 0:
            player.dx = 0.01
        player.dy = player.ycor() - player.target_y  # rise
        player.slope = player.dy / player.dx  # rise/run

        player.condition = "fire"
    return


def player_move(player):  # Player Movement
    if player.condition == "fire":
        player.pendown()
        player.setx(player.xcor() + (1 / player.slope) * player.moving)  # it will make the move smoothly
        player.sety(player.ycor() + player.moving)  # going down

        # Check if reaching target
        distance = player.distance(player.target_x, player.target_y)
        if distance < 5:
            player.condition = "blow up"

        # Border Checking
        if player.xcor() <= -320 or player.xcor() >= 320:  # if the missile is outside the border, explode it
            player.condition = "blow up"

    if player.condition == "blow up":
        player_explode(player)
    return


def player_explode(player):  # Explode Player
    player.form += 1
    if player.form <= 25:
        player.size = player.form / 10
        player.shapesize(player.size, player.size)  # example 1/10 times 20 = 2 (actual pixel size)
    elif player.form <= 50:
        player.size = (55 - player.form) / 10
        player.shapesize(player.size, player.size)  # Shrinks it down to a small size
    else:
        player_destroy(player)
    return


def player_destroy(player):  # Destroy Player
    player.clear()
    player.penup()
    player.goto(-1000, -1000)
    player.condition = "set"
    player.form = 2  # use for the explosion
    return


def click(x, y):  # Mouse Click
    # Find the nearest missile to fire
    nearest_distance = 10000
    nearest_missile = None
    for player_missile in player_missiles:
        if player_missile.condition == "set":  # Only deals with missile that haven't been destroyed, explode or fired
            distance = player_missile.distance(x, y)
            if distance < nearest_distance:
                nearest_missile = player_missile
                nearest_distance = distance
    if nearest_missile:  # If there is a near missile set the target
        player_target(nearest_missile, x, y)
    return


def points():  # Score Points
    global score, score1, score2, score3, level
    score1 = len(cities)
    score2 = len(silos)
    score3 = len(player_missiles)
    level = gameLevel
    # Update the scores
    score_pen.clear()
    scores = "Score: %s, Cities: %s, Silos: %s, Missiles: %s, Level: %s" % (score, score1, score2, score3, level)
    score_pen.write(scores, align="left", font=("Arial", 16, "normal"))
    score_pen.hideturtle()
    return


# -------------------------------------------------Keyboard Events------------------------------------------------------

mywindow.listen()
mywindow.onkey(leave, 'q')
mywindow.onscreenclick(click)

# ---------------------------------------------Frame Rate Definition----------------------------------------------------

FPS = 60  # 60 frames per second
refreshInterval = 1 / FPS  # and so this is how long we wait before the next screen draw
startOfInterval = time.perf_counter()

# -----------------------------------Setting Up Data Structures and Initial Conditions----------------------------------

quitFlag = False

newTime = int(time.perf_counter())
elapsedTime = 0
timer.write(newTime, font=("Arial", 16, "normal"))

#-----------------------------------------------Creating the Objects----------------------------------------------------

for i in range(6):  # Cities
    make_city(-225 + (i * 90), -250)  # started at x = -225 then add 90, to get an equal amount of space between cities

for j in range(3):  # Silos
    make_silo(-275 + (j * 275), -225)  # started at x = -275 then add 275, to get an equal amount of space between silos

for k in range(30):  # Player Missiles
    if 0 < k < 10:  # Silo Missile 1
        x = -275
    elif 10 < k < 20:  # Silo Missile 2
        x = 0
    else:  # Silo Missile 3
        x = 275
    make_player(x, -225)

for player_missile in player_storage:  # Store all missiles to list & append to another list to only use active missile
    player_missiles.append(player_missile)

for l in range(30):  # 30 Enemy Missiles
    make_enemy(random.randint(-300, 300), 300)

for enemy_missile in enemy_storage:
    if len(enemy_missiles) < gameLevel:  # Determine the number of enemy missiles per level
        enemy_target(enemy_missile, random.choice(cities + silos))
        enemy_missiles.append(enemy_missile)

for q in range(10):  # at least 10 invaders
    make_invader(random.randint(-300, 300), 300)

for invader_missile in invader_storage:
    if len(invader_missiles) < invader_count:  # the number of invaders missiles per 5th level
        invader_target(invader_missile, random.choice(cities + silos))
        invader_missiles.append(invader_missile)

for p in range(15):  # at least 15 side missiles
    make_side(random.choice(side_xcoordinates), random.randint(200, 250))

for side_missile in side_storage:
    if len(side_missiles) < side_count:  # the number of invaders missiles per 3rd level
        side_target(side_missile, random.choice(cities + silos))
        side_missiles.append(side_missile)

# ----------------------------------------------------Main Game---------------------------------------------------------

while quitFlag == False:
    endOfInterval = time.perf_counter()
    if endOfInterval - startOfInterval >= refreshInterval:

        # moving the player to the target
        for player_missile in player_missiles:
            player_move(player_missile)

        # moving the enemy
        for enemy_missile in enemy_missiles:
            enemy_move(enemy_missile)

        # moving the invader
        for invader_missile in invader_missiles:
            invader_move(invader_missile)

        # moving the side
        for side_missile in side_missiles:
            side_move(side_missile)

        # Player Missile collides with Enemy Missiles
        for player_missile in player_missiles:
            for enemy_missile in enemy_missiles:
                # Check if the player is exploding
                if player_missile.condition == "blow up":  # While exploding enemy can be destroyed
                    radius = (player_missile.size * 20) / 2  # (0.2 * 20) / 2 to get the actual radius
                    distance = player_missile.distance(enemy_missile.xcor(), enemy_missile.ycor())
                    if distance < radius:
                        enemy_destroy(enemy_missile)
                        score += 10
                        os.system("afplay explosion.wav&")  # OS

            for invader_missile in invader_missiles:
                # Check if the player missile is exploding
                if player_missile.condition == "blow up":  # While exploding invader missile can be destroyed
                    radius = (player_missile.size * 20) / 2
                    distance = player_missile.distance(invader_missile.xcor(), invader_missile.ycor())
                    if distance < radius:
                        invader_destroy(invader_missile)
                        invader_missiles.remove(invader_missile)  # remove the invader missiles from the list
                        invader_count = 0
                        score += 20
                        os.system("afplay explosion.wav&")  # OS

            for side_missile in side_missiles:
                # Check if the player missile is exploding
                if player_missile.condition == "blow up":  # While exploding side missile can be destroyed
                    radius = (player_missile.size * 20) / 2
                    distance = player_missile.distance(side_missile.xcor(), side_missile.ycor())
                    if distance < radius:
                        side_destroy(side_missile)
                        side_missiles.remove(side_missile)  # remove the side missiles from the list
                        side_count = 0
                        score += 30
                        os.system("afplay explosion.wav&")  # OS

        # Player Missile collides with cities and silos
        for enemy_missile in enemy_missiles:
            for city in cities:
                if enemy_missile.condition == "blow up":  # While exploding city can be destroyed
                    radius = (enemy_missile.size * 20) / 2
                    distance = enemy_missile.distance(city.xcor(), city.ycor())
                    if distance < radius:
                        city_destroy()
                        cities.remove(city)  # remove the city from the list

            for silo in silos:
                if enemy_missile.condition == "blow up":  # While exploding silo can be destroyed
                    radius = (enemy_missile.size * 20) / 2
                    distance = enemy_missile.distance(silo.xcor(), silo.ycor())
                    if distance < radius:
                        silo_destroy()
                        silos.remove(silo)  # remove the silo from the list

                    for player_missile in player_missiles:  # If silo is destroyed the missiles inside it cant be used
                        distance = enemy_missile.distance(player_missile.xcor(), player_missile.ycor())
                        if distance < radius:
                            player_destroy(player_missile)
                            player_missiles.remove(player_missile)  # remove the player missiles from the list

        for invader_missile in invader_missiles:
            for city in cities:
                if invader_missile.condition == "blow up":  # While exploding city can be destroyed
                    radius = (invader_missile.size * 20) / 2
                    distance = invader_missile.distance(city.xcor(), city.ycor())
                    if distance < radius:
                        city_destroy()
                        cities.remove(city)  # remove the city from the list
                        invader_count = 0

            for silo in silos:
                if invader_missile.condition == "blow up":  # While exploding silo can be destroyed
                    radius = (invader_missile.size * 20) / 2
                    distance = invader_missile.distance(silo.xcor(), silo.ycor())
                    if distance < radius:
                        silo_destroy()
                        silos.remove(silo)  # remove the silo from the list
                        invader_count = 0

                    for player_missile in player_missiles:  # If silo is destroyed the missiles inside it can't be used
                        distance = invader_missile.distance(player_missile.xcor(), player_missile.ycor())
                        if distance < radius:
                            player_destroy(player_missile)
                            player_missiles.remove(player_missile)  # remove the player missiles from the list

        for side_missile in side_missiles:
            for city in cities:
                if side_missile.condition == "blow up":  # While exploding city can be destroyed
                    radius = (side_missile.size * 20) / 2
                    distance = side_missile.distance(city.xcor(), city.ycor())
                    if distance < radius:
                        city_destroy()
                        cities.remove(city)  # remove the city from the list
                        side_count = 0

            for silo in silos:
                if side_missile.condition == "blow up":  # While exploding silo can be destroyed
                    radius = (side_missile.size * 20) / 2
                    distance = side_missile.distance(silo.xcor(), silo.ycor())
                    if distance < radius:
                        silo_destroy()
                        silos.remove(silo)  # remove the silo from the list
                        side_count = 0

                    for player_missile in player_missiles:  # If silo is destroyed the missiles inside it cant be used
                        distance = side_missile.distance(player_missile.xcor(), player_missile.ycor())
                        if distance < radius:
                            player_destroy(player_missile)
                            player_missiles.remove(player_missile)  # remove the player missiles from the list

        # Check to see how many enemy missiles remain in this level
        if len(enemy_missiles) == 0:  # Check if the enemy missiles is = 0

            # Reset enemy, invader, and side missiles
            for enemy_missile in enemy_storage:
                if len(enemy_missiles) < gameLevel:
                    enemy_target(enemy_missile, random.choice(cities + silos))
                    enemy_missiles.append(enemy_missile)

            if invader_count == 2:
                for invader_missile in invader_storage:
                    if len(invader_missiles) < invader_count:
                        invader_target(invader_missile, random.choice(cities + silos))
                        invader_missiles.append(invader_missile)

            if side_count == 1:
                for side_missile in side_storage:
                    if len(side_missiles) < side_count:
                        side_target(side_missile, random.choice(cities + silos))
                        side_missiles.append(side_missile)

            # Reset the player missiles
            for player_missile in player_missiles:  # Clears the list
                player_destroy(player_missile)

            player_missiles = []  # Resets the list

            for player_missile in player_storage:  # Append missiles again
                player_missiles.append(player_missile)

            for k in range(30):  # 30 player missiles
                if 0 < k < 10:  # Silo Missile 1
                    x = -275
                elif 10 < k < 20:  # Silo Missile 2
                    x = 0
                else:  # Silo Missile 3
                    x = 275

                player_missiles[k].clear()
                player_missiles[k].goto(x, -225)
                player_missiles[k].size = 0.2  # to make sure they are back to normal size
                player_missiles[k].shapesize(player_missiles[k].size, player_missiles[k].size)
                player_missiles[k].condition = "set"
                player_missiles[k].clear()  # to make sure all the used missiles are removed

            # Add up scores
            city_bonus = 100 * len(cities)  # 100 points + length of cities left
            silo_bonus = 50 * len(silos)  # 50 points + length of silos left
            missile_bonus = 25 * len(player_missiles)  # 25 points + length of missiles left

            score += (city_bonus + silo_bonus + missile_bonus)

            print("Level %s Complete" % gameLevel)
            print("City Bonus:", city_bonus, "Silos Bonus:", silo_bonus, "Missiles Bonus:", missile_bonus)

            gameLevel += 1

            game_count += 1
            print("Game Count(Increase Speed if equals to 15): %s" % game_count)

            invader_count += 1
            print("Invader Count:%s" % invader_count)

            side_count += 1
            print("Side Count: %s" % side_count)
            print(" ")

            # Added Speed Difficulty
            if game_count == 15:
                for enemy_missile in enemy_missiles:
                    enemy_missile.moving += .5
                for invader_missile in invader_missiles:
                    invader_missile.moving += .5
                for side_missile in side_missiles:
                    side_missile.moving += .5


        # Update the score, number of cities, number of silos, and player's missiles
        points()

        # Timer
        calculate_time()

        # Game Over
        if len(cities) == 0 and len(silos) == 0:
            print("Game Over.....")
            instruction_writer.goto(0, 20)
            instruction_writer.write("Game Over", align="center", font=("Arial", 30, "normal"))
            instruction_writer.goto(0, -20)
            final_score = "Score: %s" % score
            instruction_writer.write(final_score, align="center", font=("Arial", 30, "normal"))
            time.sleep(3)
            mywindow.bye()

        mywindow.update()  # manually draw the screen
        startOfInterval = time.perf_counter()

mywindow.bye()

print("Final Score: %s" % score)
