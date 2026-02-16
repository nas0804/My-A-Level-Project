import pygame
import time
import random

pygame.init()

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (224, 17, 95)#(255, 0, 0)
green = (0, 168, 107)#(0, 255, 0)
blue = (0, 105, 225)#(0, 0, 255)
yellow = (228, 208, 10)#(255, 255, 0)
orange = (204, 119, 34)#(255, 165, 0)
grey = (141, 144, 147) #for title
bgBlue = (42,168,223) #for buttons
inactiveBlue = (54,138,175) #for buttons

# Game class
class Game:
    def __init__(self):
        self.title = "Connect The Dots"
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu_started = False
        self.game_started = False
        self.level_solved = False
        self.moves = -1
        self.squareFilled = 0
        self.gridSize = 5
        self.cellSize = 100
        self.pathWidth = 20
        self.bgColour = (0, 0, 0)
        self.gridColour = (255, 255, 255)
        self.windowWidth = 1102.5
        self.windowHeight = 735
        #loads the background image and scales bg image to fit the window
        self.morph = pygame.image.load("background6.png")
        self.bgImage = pygame.transform.scale(self.morph, (self.windowWidth, self.windowHeight))

        self.display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        pygame.display.set_caption(self.title)

    def main(self): #creates menu class and displays menu
        self.menu = Menu()
        self.menu.displayMenu()

    def quit(self): #quits the game
        pygame.quit()
        quit()

# Menu class
class Menu:
    def __init__(self): #initialise variables
        self.leaderboard = None
        self.gameStart = False
        self.buttons = None
        self.bigButtonHeight = 60
        self.bigButtonWidth = 120
        self.smallButtonHeight = 30
        self.smallButtonWidth = 100

    def text_objects(self, text, font):
        textSurface = font.render(text, True, grey)
        return textSurface, textSurface.get_rect()

    def displayMenu(self):
        newGame.display.blit(newGame.bgImage,(0,0)) #display background image
        self.drawTitle()    #draw title
        self.createButtons() #create buttons
        while not newGame.menu_started: #main loop for menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    newGame.quit()
                    pygame.quit()
                for button in self.buttons:
                    button.drawButton() # draws button and checks if pressed

            pygame.display.update()
            newGame.clock.tick(30)
        self.levelSelection() # starts game when loop ends

    def levelSelection(self): #displays level selection menu
        newGame.display.blit(newGame.bgImage,(0,0))
        self.drawTitle()
        self.createButtons2()
        pygame.display.update()
        time.sleep(0.1)
   
        while not newGame.game_started: #main loop for level selection
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    newGame.quit()
                    pygame.quit()
                for button in self.buttons:
                    button.drawButton() # draws button and checks if pressed

            pygame.display.update()
            newGame.clock.tick(30)
        #THIS IS WHERE TO CALL SOLVED PUZZLE FUNCTION
        self.easyLevel()

    def createButtons(self):
        self.buttons = [] #creates an array for the buttons to be stored in
        #Play button added to the array
        self.buttons.append(Button("Play", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 300, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, self.startMenu))
        #Leaderboard button added to the array
        self.buttons.append(Button("Leaderboard", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 400, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, self.showLeaderboard))
        #Quit button added to the array
        self.buttons.append(Button("Quit", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 500, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, newGame.quit))

    def createButtons2(self):
        self.buttons = [] #sets another an array for the buttons to be stored in
        #Easy level button added to the array
        self.buttons.append(Button("Easy- 5x5", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 300, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, self.startGame))
        #Medium level button added to the array
        self.buttons.append(Button("Medium- 7x7", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 400, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, self.mediumLevel))
        #Hard level button added to the array
        self.buttons.append(Button("Hard- 10x10", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 500, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, self.hardLevel))
        #Back button added to the array
        self.buttons.append(Button("Back", 150, 600, self.bigButtonWidth, self.smallButtonHeight, bgBlue, inactiveBlue, self.backButton))

    def createButtons3(self):
        self.buttons = [] #sets another an array for the buttons to be stored in
        #Undo button added to the array
        self.buttons.append(Button("Undo", (newGame.windowWidth/2) - (75/2) - 160, 650, 75, 30, bgBlue, inactiveBlue, self.undoMove))
        #Hint button added to the array
        self.buttons.append(Button("Hint", (newGame.windowWidth/2) - (75/2) + 160, 650, 75, 30, bgBlue, inactiveBlue, self.giveHint))
        #Reset level button added to the array
        self.buttons.append(Button("Reset", (newGame.windowWidth/2) - (75/2), 650, 75, 30, bgBlue, inactiveBlue, self.resetLevel))
        self.buttons.append(Button("Quit", 900, 200, 75, 75, bgBlue, inactiveBlue, newGame.quit))

    def createButtons4(self):
        self.buttons = []
        #Button the will generate a new level/ problem in a future sprint
        self.buttons.append(Button("Next Level", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 300, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, self.nextLvl))
        #Button that will take the user to the level selection screen
        self.buttons.append(Button("Level Selection", (newGame.windowWidth/2) - (self.bigButtonWidth/2) - 20, 400, 160, self.bigButtonHeight, bgBlue, inactiveBlue, self.levelSelection))
        #Button that will quit the program
        self.buttons.append(Button("Quit", (newGame.windowWidth/2) - (self.bigButtonWidth/2), 500, self.bigButtonWidth, self.bigButtonHeight, bgBlue, inactiveBlue, newGame.quit))

    def giveHint(self): #then this is 34566787889
        print("Hint")

    def resetLevel(self):
        self.easyLevel()  
       
    def undoMove(self):#IT REMOVES THE VALUES FROM THE ARRAY BUT NOT FROM THE ACTUAL GRID
        if self.undo == 1:
            self.total -= self.length #Subtracts the length so that when "Undo" is pressed, the squares covered remains the same
            newGame.moves -= 1 #Subtracts 1 from the "self.moves" variable so that the value of it does not increment when not wanted
            print("Before", self.paths)

            pathRemoved = len(self.paths[-2]) #stores the length of the path that is 2nd to last in the list
            self.total -= pathRemoved
            self.paths.pop() #removes the last 2 elements in the list
            self.paths.pop()

            print("after", self.paths)
            self.undo -= 1
        else:
            self.total -= self.length
            newGame.moves -= 1
            print("No hint")



    def gameStats(self, moves): #displays the number of moves made by the player (value will be able to change in future sprint)
        pygame.draw.rect(newGame.display, bgBlue, (90, 195, 165, 70))
        Font = pygame.font.Font("freesansbold.ttf", 25)
        movesSurf = Font.render("Moves: " + str(moves), True, black)
        pathsSurf = Font.render("Filled: "+ str(newGame.squareFilled) + "%"  , True, black)
        movesRect = movesSurf.get_rect()
        pathsRect = pathsSurf.get_rect()
        movesRect.topleft = (100, 200)
        pathsRect.topleft = (100, 230)
        newGame.display.blit(movesSurf, movesRect)
        newGame.display.blit(pathsSurf, pathsRect)
 
    def drawTitle(self): #draws the title
        titleFont = pygame.font.Font("freesansbold.ttf", 100)
        titleSurf, titleRect = self.text_objects("Connect The Dots", titleFont)
        titleRect.center = ((newGame.windowWidth/2), (newGame.windowHeight/7))
        newGame.display.blit(titleSurf, titleRect)

    def startMenu(self): #breaks out of the initial menu loop
        newGame.menu_started = True

    def startGame(self): #breaks out of the level selection loop
        newGame.game_started = True #sets gameStart to true

    def backButton(self): #sets the program back to the inital menu screen
        newGame.menu_started = False
        self.displayMenu()

    def showLeaderboard(self):
        print("Leaderboard button pressed")

    def nextLvl(self):
        self.easyLevel()

    def easyLevel(self): #the main block of code for the game
        newGame.display.blit(newGame.bgImage,(0,0))
        self.drawTitle()
        self.createButtons3()
        newGrid = Grid(5, 5, 90, 30) #creates a grid object with 5 rows, 5 columns, cell size of 90, path width of 30
        self.drawing = False
        self.currentPath = []
        self.paths = []
        self.total = 0
        self.length = 0
        newGame.moves = -1
        self.undo = 1
        self.level = True


        while self.level:    
            newGrid.createGrid()

            if newGrid.solvePuzzle(newGrid.pathFindPuzzle): #runs the solvePuzzle function on the pathFindPuzzle and checks if it is solvable
                print("Solved")
            else:
                print("Not solved")

            pygame.display.update()
            while newGame.running: #main loop for the game
                self.gameStats(newGame.moves)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        newGame.running = False

                    elif event.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse is clicked
                        self.drawing = True
                        mousePos = pygame.mouse.get_pos() #gets the mouse position and then converts it to a grid position
                        gridPos = newGrid.getCellFromMouse(mousePos)
                        self.currentPath.append(gridPos) #appends the grid position to the current path
                        self.paths.append(self.currentPath)

                    elif event.type == pygame.MOUSEBUTTONUP: #checks if the mouse is released
                        self.drawing = False
                        self.currentPath = []
                        self.total += self.length
                        newGame.moves += 1
                        newGame.squareFilled = ((self.total * 100) // (newGrid.rows * newGrid.cols)) #returns a precentage value on how many squares are filled

                    elif event.type == pygame.MOUSEMOTION and self.drawing: #checks if the mouse is moving
                        mousePos = pygame.mouse.get_pos()
                        gridPos = newGrid.getCellFromMouse(mousePos)
                        if gridPos != self.currentPath[-1]: #if the grid position is not the same as the last grid position
                            self.currentPath.append(gridPos)
                        self.length = len(self.currentPath)
   
                    for button in self.buttons:
                        button.drawButton()

                pygame.display.flip() #updates the display    

                #This will block of code is responsible for drawing the path
                if self.drawing and self.currentPath: #will only draw the path if the player is drawing and there is a path to draw
                    for i in range(len(self.currentPath) - 1): #loops through the current path
                        pathColour = 0 #sets the path colour to 0 initially
                        if gridPos == None:
                            self.drawing = False
                            print("Invalid move")
                            newGame.menu.total -= self.length
                            newGame.moves -= 1
                        else:
                            dotNum = newGrid.getDotColour(gridPos[1], gridPos[0])
                            if dotNum == 2:
                                pathColour = red
                            elif dotNum == 3:
                                pathColour = blue
                            elif dotNum == 4:
                                pathColour = green
                            elif dotNum == 5:
                                pathColour = yellow
                            elif dotNum == 6:
                                pathColour = orange

                            startPos = ((self.currentPath[i][0] * newGrid.cellSize + newGrid.cellSize // 2) + newGrid.xOffset, (self.currentPath[i][1] * newGrid.cellSize + newGrid.cellSize // 2) + newGrid.yOffset)
                            # stores the start position of line
                            endPos = ((self.currentPath[i+1][0] * newGrid.cellSize + newGrid.cellSize // 2) + newGrid.xOffset, (self.currentPath[i+1][1] * newGrid.cellSize + newGrid.cellSize // 2) + newGrid.yOffset)
                            # stores the end position of line
                            pygame.draw.line(newGame.display, pathColour, startPos, endPos, newGrid.pathWidth) # draws the line

                if self.total == (newGrid.rows * newGrid.cols): #if the total is equal to the number of squares in the grid
                    newGame.running = False
                    self.level = False #set the level to false so the player can move on to the next level

                    self.solved()

    def solved(self): #displays the level solved screen
        newGame.display.blit(newGame.bgImage, (0,0))
        self.drawTitle()
        self.createButtons4()
        font = pygame.font.Font(None, 52)
        text = font.render("Level Solved!", True, white)
        newGame.display.blit(text, (450, 200))
        pygame.display.update()
        while not newGame.level_solved:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    newGame.quit()
                    pygame.quit()

                newGame.game_started = False #set these 3 flags as true so the player can go back to previous screens without error
                newGame.running = True
                newGame.menu.level = True

                for button in self.buttons:
                    button.drawButton()

            pygame.display.update()

            self.total = 0
            newGame.moves = -1

    def mediumLevel(self):#this wont work unless puzzle has 7 rows and columns
        print("Medium Level works")

    def hardLevel(self):
        print("Hard Level works")

# Button class
class Button:
    #creates buttons with text, x, y, width, height, colour, action
    def __init__(self,text, x, y, w, h, inactive_colour, active_colour, action):
        self._text = text
        self._x = x                     #coordinates of top left corner of button
        self._y = y        
        self._w = w                     #button dimensions
        self._h = h
        self._inactive_colour = inactive_colour
        self._active_colour = active_colour
        self._action = action           #function to be called when button is clicked

    def drawButton(self):
        mouse = pygame.mouse.get_pos() #gets mouse position
        click = pygame.mouse.get_pressed() #gets mouse click

        if self._x + self._w > mouse[0] > self._x and self._y + self._h > mouse[1] > self._y: #checks if mouse is over button
            pygame.draw.rect(newGame.display, self._active_colour, (self._x, self._y, self._w, self._h)) #draws button in active colour
            if click[0] == 1 and self._action != None: #checks if button is clicked
                self._action() #calls the function associated with the button
        else:
            pygame.draw.rect(newGame.display, self._inactive_colour, (self._x, self._y, self._w, self._h)) #otherwise draws button in inactive colour
           
        smallText = pygame.font.Font("freesansbold.ttf", 20) #creates font, text and shape for button
        textSurf = smallText.render(self._text, True, black)
        textRect = textSurf.get_rect()

        textRect.center = ((self._x + (self._w/2)), (self._y +(self._h/2))) #displays and centers text on button
        newGame.display.blit(textSurf, textRect)

#Grid class
class Grid:
    def __init__(self, rows, cols, cellSize, pathWidth):
        self.rows = rows
        self.cols = cols
        self.cellSize = cellSize
        self.pathWidth = pathWidth
        self.xOffset = (newGame.windowWidth - self.cols * self.cellSize) // 2
        self.yOffset = (newGame.windowHeight - self.rows * self.cellSize) // 2 + 50 # +50 to offset, to account for the change in grid position
       
        self.puzzle = []
        self.startNodes = {} #creates a dictionary for the start nodes
        self.endNodes = {} #creates a dictionary for the end nodes
        self.allNodes = [] #creates an array for all the nodes
        self.distances = {} #creates a dictionary for the distances
        self.sortedNodes = [] #creates an array for the sorted nodes
        self.pathFindPuzzle = [] #creates a path finding puzzle

    def makePuzzle(self):
        self.puzzle = [[0,0,0,0,0]] #creates a puzzle with 5 rows and 5 columns that gets random values assigned to it
        self.puzzle.append([0,0,0,0,0])
        self.puzzle.append([0,0,0,0,0])
        self.puzzle.append([0,0,0,0,0])
        self.puzzle.append([0,0,0,0,0])

        #generates random coordinates for the dots to be draw in from the list of coordinates
        coords = [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4), (3,0), (3,1), (3,2), (3,3), (3,4), (4,0), (4,1), (4,2), (4,3), (4,4)]
        for i in range(2,7):
            coord1 = random.choice(coords) #chooses a random coordinate from "coords" then removes it from the array
            x,y = coord1 # x and y are set to the values of the coordinate
            coords.remove(coord1)

            coord2 = random.choice(coords)
            w,z = coord2
            coords.remove(coord2)

            self.puzzle[y][x] = i #changes the value held at the y,x postion to a sigular value so that the dots can be drawn
            self.puzzle[z][w] = i

            # print(i,":", coord1, coord2)

        self.pathFindPuzzle = [[1,1,1,1,1,1,1]] #creates a path finding puzzle by adding 1's to the puzzle so that the there is a "barrier" around the grid
        self.pathFindPuzzle.append([1, self.puzzle[0], 1])
        self.pathFindPuzzle.append([1, self.puzzle[1], 1])
        self.pathFindPuzzle.append([1, self.puzzle[2], 1])
        self.pathFindPuzzle.append([1, self.puzzle[3], 1])
        self.pathFindPuzzle.append([1, self.puzzle[4], 1])    
        self.pathFindPuzzle.append([1,1,1,1,1,1,1])

        # print("path find puzzle", self.pathFindPuzzle)
        # print("puzzle", self.puzzle)
       

    def returnSolved(self, total): #checks if the puzzle is solved and returns a boolean value
        if total == 25:
            return True
        else:
            return False

    def abs(self, a , b): #returns the absolute value of the difference between two numbers
        if a > b:
            return a - b
        else:
            return b - a
       
    def solvePuzzle(self, grid): #solves the puzzle using a recursive backtracking algorithm
        if self.checkGrid(grid) == False: #checks if the grid is valid
            return False

        if self.returnSolved(grid): #checks if the puzzle is solved
            return True
       
        for dotNum in self.sortedNodes: #loops through the sorted nodes
            start = self.startNodes[dotNum]
            end = self.endNodes[dotNum]
           
            if (abs(end[0], start[0]) + abs(end[1], start[1])) > 1: #checks if the distance between the start and end nodes is greater than 1
                directions = []
                if grid[start[0]][start[1] + 1] == 0: #checks if the value to the right of the start node is 0
                    if end[1] > start[1]: #checks if the end node is to the right of the start node
                        directions.insert(0, "right") #inserts "right" at the start of the directions array
                    else:
                        directions.append("right")  #appends "right" to the end of the directions array

                if grid[start[0]][start[1] - 1] == 0: #checks if the value to the left of the start node is 0
                    if end[1] < start[1]: #checks if the end node is to the left of the start node
                        directions.insert(0, "left") #inserts "left" at the start of the directions array
                    else:
                        directions.append("left") #appends "left" to the end of the directions array

                if grid[start[0] + 1][start[1]] == 0: #checks if the value below the start node is 0
                    if end[0] > start[0]:
                        directions.insert(0, "down")
                    else:
                        directions.append("down")
                       
                if grid[start[0] - 1][start[1]] == 0: #checks if the value above the start node is 0
                    if end[0] < start[0]:
                        directions.insert(0, "up")
                    else:
                        directions.append("up")
               
                if len(directions) == 0: #checks if the length of the directions array is 0
                    return False
       
                for direction in directions:
                    if direction == "right": #checks if the direction is right
                        start[1] += 1 #increments the x value of the start node
                        grid[start[0]][start[1]] = dotNum #sets the value at the start node to the dot number
                        if self.solvePuzzle(grid) == True: #recursively calls the solvePuzzle function
                            return True
                        else:
                            grid[start[0]][start[1]] = 0 #sets the value at the start node to 0
                            start[1] -= 1 #decrements the x value of the start node

                    elif direction == "left": #checks if the direction is left
                        start[1] -= 1 #decrements the x value of the start node
                        grid[start[0]][start[1]] = dotNum #sets the value at the start node to the dot number
                        if self.solvePuzzle(grid) == True: #recursively calls the solvePuzzle function
                            return True
                        else:
                            grid[start[0]][start[1]] = 0 #sets the value at the start node to 0
                            start[1] += 1 #increments the x value of the start node
 
                    elif direction == "up": #checks if the direction is up
                        start[0] -= 1
                        grid[start[0]][start[1]] = dotNum
                        if self.solvePuzzle(grid) == True:
                            return True
                        else:
                            grid[start[0]][start[1]] = 0
                            start[0] += 1

                    elif direction == "down": #checks if the direction is down
                        start[0] += 1
                        grid[start[0]][start[1]] = dotNum
                        if self.solvePuzzle(grid) == True:
                            return True
                        else:
                            grid[start[0]][start[1]] = 0
                            start[0] -= 1
                return False


    def createGrid(self): #will create the grid and draw the dots
        self.makePuzzle() #creates the puzzle

        #sorts the nodes by distance so that the shortest distance is first
        keys = list(self.distances)
        for i in range(0, len(self.distances)):
            min = self.distances[keys[0]]
            for key in self.distances:
                if self.distances[key] < min:
                    min = self.distances[key]
            self.sortedNodes.append(key)
            self.distances.pop(key)
   
        for row in range(self.rows):
            for col in range(self.cols):

                #finds the start and end nodes that need to be connected
                if self.puzzle[row][col] > 0:
                    if self.puzzle[row][col] in self.startNodes:
                        self.endNodes[self.puzzle[row][col]] = (row, col)
                        self.distances[self.puzzle[row][col]] = abs(row - self.startNodes[self.puzzle[row][col]][0]) + abs(col - self.startNodes[self.puzzle[row][col]][1])
                    else:
                        self.startNodes[self.puzzle[row][col]] = (row, col)
                    self.allNodes.append((row, col))


                #draws grid and dots with colours
                rect = pygame.Rect(self.xOffset + col * self.cellSize, (self.yOffset + row * self.cellSize) , self.cellSize, self.cellSize) #creates rectangle for grid
                pygame.draw.rect(newGame.display, white, rect, 1) #draws grid lines
                if self.puzzle[row][col] != 0 or 1: #if the dot label is not 0, draw a dot
                    circle_centre = (self.xOffset + col * self.cellSize + self.cellSize // 2, ((self.yOffset + row * self.cellSize) ) + self.cellSize // 2)
                    circle_radius = 25
                    if self.puzzle[row][col] == 2: #if dot label is 1, draw red dot, if 2 draw blue dot, etc.
                        pygame.draw.circle(newGame.display, red, circle_centre, circle_radius)
                    elif self.puzzle[row][col] == 3:
                        pygame.draw.circle(newGame.display, blue, circle_centre, circle_radius)
                    elif self.puzzle[row][col] == 4:
                        pygame.draw.circle(newGame.display, green, circle_centre, circle_radius)
                    elif self.puzzle[row][col] == 5:
                        pygame.draw.circle(newGame.display, yellow, circle_centre, circle_radius)
                    elif self.puzzle[row][col] == 6:
                        pygame.draw.circle(newGame.display, orange, circle_centre, circle_radius)
       
        # print("sorted nodes",self.sortedNodes)
        # print("start nodes", self.startNodes)
        # print("end nodes", self.endNodes)
        # print("all nodes", self.allNodes)
        # print("distances", self.distances)
                       
   
    def checkGrid(self, grid): #checks if the grid is valid
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] > 0: #checks if the value at the grid position is greater than 0
                    dotNum = grid[row][col]
                    if grid[row + 1][col] > 0 and grid[row + 1][col] != dotNum: #checks if the value below the current grid position is greater than 0 and not equal to the dot number
                        if grid[row - 1][col] > 0 and grid[row - 1][col] != dotNum: #checks if the value above the current grid position is greater than 0 and not equal to the dot number
                            if grid[row][col + 1] > 0 and grid[row][col + 1] != dotNum: #checks if the value to the right of the current grid position is greater than 0 and not equal to the dot number
                                if grid[row][col - 1] > 0 and grid[row][col - 1] != dotNum: #checks if the value to the left of the current grid position is greater than 0 and not equal to the dot number
                                    return False
                    if grid[row + 1][col] == dotNum and grid[row - 1][col] == dotNum and grid[row][col + 1] == dotNum: #checks if the value below, above and to the right of the current grid position is equal to the dot number
                        return False
                    elif grid[row + 1][col] == dotNum and grid[row - 1][col] == dotNum and grid[row][col - 1] == dotNum: #checks if the value below, above and to the left of the current grid position is equal to the dot number
                        return False
                    elif grid[row + 1][col] == dotNum and grid[row][col + 1] == dotNum and grid[row][col - 1] == dotNum: #checks if the value below, to the right and to the left of the current grid position is equal to the dot number
                        return False
                    elif grid[row - 1][col] == dotNum and grid[row][col + 1] == dotNum and grid[row][col - 1] == dotNum: #checks if the value above, to the right and to the left of the current grid position is equal to the dot number
                        return False
        return True


    def getDotColour(self, row, col): #returns the number of the dot when looking at the puzzle
        return self.puzzle[row][col]

    def getCellFromMouse(self, pos): #returns the cell position of the mouse
        x, y = pos
        self.xOffset = int(self.xOffset) #sets xOffset to an integer as the window dimensions are floats
        row = (y - self.yOffset) // self.cellSize
        col = (x - self.xOffset) // self.cellSize
        if row < 0 or col < 0 or row > 4 or col > 4:
            return None
        return (col, row) #returns the cell position





# Create an instance of the Game class and call the main method
newGame = Game()
newGame.main()
