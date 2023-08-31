from tkinter import *
import random
import time



WIDTH = 1500
HEIGHT = 1000
SPEED = 150
GRAFIC_SIZE = 50 #50, 25, , 5, , 1
PYTHON_SIZE = 4
PYTHON_COLOR = "#008000"
APPLE_COLOR = "#FF0000"
BACKGROUND_COLOR = "#672828"

SPEED_APPLE = "FFF0F0" #increases speed for a short time
POWER_APPLE = "FFF00F" #increases score and python size by 5
POWER2_APPLE = "FF0000" #increases score and python size by 10
apple = None
level = 0
canvas = None
update_executed = False
levelOneScore = 15
levelTwoScore = 30
levelThreeScore = 45
levelFourScore = 50
levelFiveScore = 60
levelSixScore = 100
intro_snake_position = (0, 0)
python = None
isRunning = True
visible = True


def initStock():
    global score, SPEED, PYTHON_COLOR, BACKGROUND_COLOR, WIDTH, HEIGHT, GRAFIC_SIZE, PYTHON_SIZE, APPLE_COLOR, intro_snake_position
    global apple, level, canvas, update_executed, python, isRunning
    WIDTH = 1500
    HEIGHT = 1000
    SPEED = 150
    GRAFIC_SIZE = 50 #50, 25, 20, 10, 5, 2, 1
    PYTHON_SIZE = 4
    python.decrease_length(3)

    python.coordinates = python.coordinates[:3]
    python.squares = python.squares[:3]
    python.current_color = "#008000"
    updateColor(python)

    APPLE_COLOR = "#FF0000"
    BACKGROUND_COLOR = "#672828"
    canvas.config(bg=BACKGROUND_COLOR)
    apple = None
    level = 0
    score = 0
    update_executed = False
    intro_snake_position = (0, 0)
    isRunning = True


#snake class, an object of snake is created when calling the class#
class Snake:
    def __init__(self):
        self.body_size = PYTHON_SIZE
        self.coordinates = []
        self.squares = []
        self.current_color = PYTHON_COLOR

        for i in range(0, PYTHON_SIZE):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + GRAFIC_SIZE, y + GRAFIC_SIZE, fill=self.current_color, tag="python")
            self.squares.append(square)

    def increase_length(self, number_of_segments):
        tail_x, tail_y = self.coordinates[-1]

        for _ in range(number_of_segments):
            # Add new segment to the coordinates list
            self.coordinates.append([tail_x, tail_y])
            # Create the corresponding rectangle on the canvas
            square = canvas.create_rectangle(tail_x, tail_y, tail_x + GRAFIC_SIZE, tail_y + GRAFIC_SIZE, fill=self.current_color, tag="python")
            # Append the square to the squares list
            self.squares.append(square)

    def decrease_length(self, decrease):
        # Remove all segments of the Python body except the first three
        for segment in python.squares[decrease:]:
            canvas.delete(segment)

    def toggle_visibility(self, visible):
        # Toggle the visibility of the snake squares
        for square in self.squares:
            if visible:
                canvas.itemconfig(square, state='normal')
            else:
                canvas.itemconfig(square, state='hidden')

        visible = False



#Food class, an object of food is created when calling the class#
class SpeedBoost:
    def __init__(self):
        adHeight = HEIGHT - 50
        x = random.randint(0, (WIDTH / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        y = random.randint(0, (adHeight / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        self.coordinates = [x, y]
        self.sApple_obj = canvas.create_oval(x, y, x + GRAFIC_SIZE, y + GRAFIC_SIZE, fill=SPEED_APPLE, tag="sApple")

    def update_position(self):
        global sApple
        adHeight = HEIGHT - 50
        x = random.randint(0, (WIDTH / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        y = random.randint(0, (adHeight / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        self.coordinates = [x, y]
        canvas.coords(self.sApple_obj, x, y, x + GRAFIC_SIZE, y + GRAFIC_SIZE)
        sApple = SpeedBoost()



class Food:
    def __init__(self):
        adHeight = HEIGHT - 50
        x = random.randint(0, (WIDTH / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        y = random.randint(0, (adHeight / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        self.coordinates = [x, y]
        self.apple_obj = canvas.create_oval(x, y, x + GRAFIC_SIZE, y + GRAFIC_SIZE, fill=APPLE_COLOR, tag="apple")

    def update_position(self):
        global apple
        adHeight = HEIGHT - 50
        x = random.randint(0, (WIDTH / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        y = random.randint(0, (adHeight / GRAFIC_SIZE) - 1) * GRAFIC_SIZE
        self.coordinates = [x, y]
        canvas.coords(self.apple_obj, x, y, x + GRAFIC_SIZE, y + GRAFIC_SIZE)
        apple = Food()


class Boss():
    def __init__(self):
        print("hello")
        
#Background = #666666, speed = 150, size = 50, snake = #008000, score<=50#
#place of the dead#
def levelOne():
    pass



def levelTwo():
    pass




def levelThree():
    pass



def levelFour():
    pass



def levelFive():
    pass



def levelSix():
    pass




def updateColor(python):
        for i, square in enumerate(python.squares):
            canvas.itemconfig(square, fill=python.current_color)
        

def updateSize(size):
    global GRAFIC_SIZE, apple
    #python.decrease_length(3)
    GRAFIC_SIZE = size
    canvas.delete("apple")
    #python.toggle_visibility(False)
    apple.update_position()

#calling specific level function depending on score#
def updateGame(score, python):
    global SPEED, levelName, level, update_executed, BACKGROUND_COLOR, canvas, apple, sApple


    levelName = "Place Of Death  -  "
    text_label.config(text=levelName)

    if score == levelOneScore and not update_executed:
        updateSize(25)
        #python.increase_length(score)
        #sApple = SpeedBoost()
        python.current_color = "#FFFF0F"
        level += 1
        print(level)
        python.increase_length(score)
        SPEED = 125
        update_executed = True
    elif score == levelTwoScore and not update_executed:
        python.current_color = "#FF0F0F"
        #BACKGROUND_COLOR = "#FF0220"
        #canvas.config(bg=BACKGROUND_COLOR)
        level += 1
        print(level)
        SPEED = 80
        update_executed = True
    elif score == levelThreeScore and not update_executed:
        python.current_color = "#F7770F"
        updateSize(5)
        BACKGROUND_COLOR = "#FF00FF"
        canvas.config(bg=BACKGROUND_COLOR)
        level += 1
        print(level)
        SPEED = 90
        update_executed = True
    elif score == levelFourScore and not update_executed:
        python.current_color = "#0F0077"
        #BACKGROUND_COLOR = "#000F00"
        #canvas.config(bg=BACKGROUND_COLOR)
        level += 1
        print(level)        
        SPEED = 50
        update_executed = True
    elif score == levelFiveScore and not update_executed:
        python.current_color = "#0FF077"
        updateSize(1)
        BACKGROUND_COLOR = "#000077"
        canvas.config(bg=BACKGROUND_COLOR)
        level += 1
        print(level)        
        SPEED = 80
        update_executed = True
    elif score == levelSixScore and not update_executed:
        python.current_color = "#FFFFFF"
        BACKGROUND_COLOR = "#000000"
        canvas.config(bg=BACKGROUND_COLOR)
        level += 1
        print(level)        
        SPEED = 40
        update_executed = True
    if score != levelOneScore and score != levelTwoScore and score != levelThreeScore and score != levelFourScore and score != levelFiveScore and score != levelSixScore: 
        update_executed = False

    updateColor(python)
        

def runSnake(python, x, y):
        
        python.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + GRAFIC_SIZE, y + GRAFIC_SIZE, fill=PYTHON_COLOR)
        python.squares.insert(0, square)


#basically the game, makes the python move#
def nextTurn(python):
    global PYTHON_COLOR, apple, score, sApple
    
    if not is_paused:
        x, y = python.coordinates[0]
        if direction == "up":
            y -= GRAFIC_SIZE
        elif direction == "down":
            y += GRAFIC_SIZE
        elif direction == "right":
            x += GRAFIC_SIZE
        elif direction == "left":
            x -= GRAFIC_SIZE

        runSnake(python, x, y)


        if x == apple.coordinates[0] and y == apple.coordinates[1]:
            global score
            score += 1
            label.config(text="Score:{}".format(score))
            canvas.delete("apple")
            apple.update_position()
        else:
            del python.coordinates[-1]
            canvas.delete(python.squares[-1])
            del python.squares[-1]


        if checkCollision(python):
            gameOver()
        else:
            updateGame(score, python)
            game.after(SPEED, nextTurn, python)

            
        
#so you can not move from up to down, right to left, visa verca#
def changeDirection(update_direction):
    global direction
    if not is_paused:
        if update_direction == 'left':
            if direction != 'right':
                direction = update_direction
        elif update_direction == 'right':
            if direction != 'left':
                direction = update_direction
        elif update_direction == 'up':
            if direction != 'down':
                direction = update_direction
        elif update_direction == 'down':
            if direction != 'up':
                direction = update_direction

                
#checks if franklin is hitting border or himself#
def checkCollision(python):
    x, y = python.coordinates[0]

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True

    for body in python.coordinates[1:]:
        if x == body[0] and y == body[1]:
            return True

    return False




#game over, user is able to restart the game#
def gameOver():
    canvas.delete(ALL)
    game.unbind('<Escape>')
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('Arial', 70), text='F', fill="red", tag="f")
    global begin_button
    begin_button = Button(game, text="Restart", font=('Arial', 30), command=restartGame)
    begin_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    global is_paused
    is_paused = False


#when pausing the user is able to continue#
def continueGame():
    global is_paused, continue_button, exit_button, apple
    is_paused = False
    continue_button.destroy()
    exit_button.destroy()
    canvas.delete("paused")
    # Call nextTurn to continue the game loop
    global python
    nextTurn(python)
    game.bind('<Escape>', lambda event: pauseGame())



#pause function, when pausing the user is able to press on continue or exit#
def pauseGame():
    global is_paused, continue_button, exit_button
    is_paused = not is_paused
    if is_paused:
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text='PAUSED', font=('Arial', 40), fill="white", tag="paused")
        exit_button = Button(game, text="Exit", font=('Arial', 30), command=exitGame)
        exit_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        continue_button = Button(game, text="Continue", font=('Arial', 30), command=continueGame)
        continue_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        game.unbind('<Escape>')
    else:
        canvas.delete("paused")
        exit_button.destroy()


#this function enables the restart, all values are back to stock#
def restartGame():

    #label.config(text="Score:{}".format(score))
    canvas.delete("all")
    global is_paused, direction
    direction = 'right'
    is_paused = False
    text_label.destroy()
    label.destroy()
    initStock()
    beginGame()


#this function start the game and binds the used keys after the user presses begin#
def beginGame():
    global begin_button, isRunning, levelName, label, text_label, HEIGHT

    levelName = ""  
    isRunning = False
    canvas.delete(ALL)
    begin_button.destroy()
    customize_button.destroy()


    text_label = Label(top_frame, text=levelName, font=('Arial', 40))
    text_label.pack(side=LEFT)

    label = Label(top_frame, text="Score:{}".format(score), font=('Arial', 40))
    label.pack(side=LEFT)

    game.bind('<Up>', lambda event: changeDirection('up'))
    game.bind('<Down>', lambda event: changeDirection('down'))
    game.bind('<Left>', lambda event: changeDirection('left'))
    game.bind('<Right>', lambda event: changeDirection('right'))
    game.bind('<Escape>', lambda event: pauseGame())

    global python, apple, intro_snake_position
    python.coordinates[0] = intro_snake_position
    apple = Food()
    tempHeight = HEIGHT-50
    if python.coordinates[0][1] >= tempHeight:
        python.coordinates[0] = (python.coordinates[0][0], tempHeight - GRAFIC_SIZE)
    nextTurn(python)




#if pressing exit, the game closes#
def exitGame():
    game.destroy()



def startIntro():
    global isRunning, python
    python = Snake()
    if isRunning:
        startScreenIntro(python)
    else:
        beginGame()

    
def startScreenIntro(python):
    global PYTHON_COLOR, direction, x, y, intro_snake_position

    if isRunning and not is_paused:
        x, y = python.coordinates[0]
        if direction == "up":
            y -= GRAFIC_SIZE
        elif direction == "down":
            y += GRAFIC_SIZE
        elif direction == "right":
            x += GRAFIC_SIZE
        elif direction == "left":
            x -= GRAFIC_SIZE

        if x >= WIDTH - GRAFIC_SIZE and direction == "right":
            direction = "down"
        elif y >= HEIGHT - GRAFIC_SIZE and direction == "down":
            direction = "left"
        elif x <= 0 and direction == "left":
            direction = "up"
        elif y <= 0 and direction == "up":
            direction = "right"
        
        runSnake(python, x, y)
        intro_snake_position = (x, y)

        del python.coordinates[-1]
        canvas.delete(python.squares[-1])
        del python.squares[-1]

    game.after(SPEED, startScreenIntro, python)
    
        


#basically the "main class", setting up the gui#
game = Tk()
game.title("FRANKLIN THE Python")
#game.resizable(False, False)

score = 0
direction = 'right'
is_paused = False
levelName = ""

top_frame = Frame(game)
top_frame.pack(fill=BOTH)

canvas = Canvas(game, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

begin_button = Button(game, text="Begin", font=('Arial', 30), command=beginGame)
begin_button.place(relx=0.5, rely=0.5, anchor=CENTER)

customize_button = Button(game, text="Customize", font=('Arial', 20))
customize_button.place(relx=0.5, rely=0.6, anchor=CENTER)

startIntro()

game.update()

#center windows
game_width = game.winfo_width()
game_height = game.winfo_height()
screen_width = game.winfo_screenwidth()
screen_height = game.winfo_screenheight()

x = int((screen_width / 2) - (game_width / 2))
y = int((screen_height / 2) - (game_height / 2))

game.geometry(f"{game_width}x{game_height}+{x}+{y}")

game.mainloop()