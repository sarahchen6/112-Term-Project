########################################
#   Santa Maze Game
#   Coded by: Sarah Chen (sarahc2)
########################################
#
#   Citations: 
#   1)  incorporated subclassing ModalApp and Mode idea from
#       https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
#
########################################
from cmu_112_graphics import *

class MyApp(ModalApp):
    def appStarted(app):
        app.titleScreen = TitleScreen()
        app.storyScreen = StoryScreen()
        app.avatarScreen = AvatarScreen()
        app.sledsScreen = SledsScreen()
        app.gameModeScreen = GameModeScreen()
        app.finalScreen = FinalScreen()
        app.setActiveMode(app.titleScreen)

class TitleScreen(Mode):
    def appStarted(mode):
        mode.buttonColor = 'sea green'
        mode.buttonTextColor = 'white'

    def mousePressed(mode, event):
        if ((mode.width/2-150 <= event.x <= mode.width/2+150) 
            and (mode.height*2/3-50 <= event.y <= mode.height*2/3+50)
            and (mode.buttonColor != 'dark green')):
            mode.buttonColor = 'dark green'
            mode.buttonTextColor = 'white'
        elif ((mode.width/2-150 <= event.x <= mode.width/2+150) 
            and (mode.height*2/3-50 <= event.y <= mode.height*2/3+50)
            and (mode.buttonColor == 'dark green')):
            mode.app.setActiveMode(mode.app.storyScreen)
    
    def mouseMoved(mode, event):
        if ((mode.width/2-150 <= event.x <= mode.width/2+150) 
            and (mode.height*2/3-50 <= event.y <= mode.height*2/3+50)
            and (mode.buttonColor != 'dark green')):
            mode.buttonColor = 'white'
            mode.buttonTextColor = 'sea green'
        elif (((event.x < mode.width/2-150) 
            or (event.x > mode.width/2+150) 
            or (event.y < mode.height*2/3-50) 
            or (event.y > mode.height*2/3+50))
            and (mode.buttonColor != 'dark green')):
            mode.buttonColor = 'sea green'
            mode.buttonTextColor = 'white'

    def redrawAll(mode, canvas):
        ### title
        canvas.create_text(mode.width/2, mode.height/3,
                            fill='firebrick4',
                            text='Yay Christmas!!', 
                            font='PlayfairDisplay 120 bold')
        ### "Let's Begin" button
        canvas.create_rectangle(mode.width/2-150, mode.height*2/3-50,
                            mode.width/2+150, mode.height*2/3+50,
                            fill=mode.buttonColor)
        canvas.create_text(mode.width/2, mode.height*2/3,
                            fill=mode.buttonTextColor,
                            text='Let\'s Begin', 
                            font='PlayfairDisplay 40 bold')

class StoryScreen(Mode):
    def appStarted(mode):
        mode.titleColor = 'black'
        mode.backButtonColor = mode.nextButtonColor = 'sea green'
        mode.backButtonTextColor = mode.nextButtonTextColor = 'white'

    def mousePressed(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.titleScreen)
            mode.backButtonColor = 'sea green'
            mode.backButtonTextColor = 'white'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.avatarScreen)
            mode.nextButtonColor = 'sea green'
            mode.nextButtonTextColor = 'white'
    
    def mouseMoved(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.backButtonColor = 'white'
            mode.backButtonTextColor = 'sea green'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.nextButtonColor = 'white'
            mode.nextButtonTextColor = 'sea green'
        elif (((event.x < 50) or ((event.x > 150) 
            and (event.x < mode.width-150)) or (event.x > mode.width-50))
            or ((event.y < 50) or (event.y > 100))):
            mode.backButtonColor = mode.nextButtonColor = 'sea green'
            mode.backButtonTextColor = mode.nextButtonTextColor = 'white'

    def redrawAll(mode, canvas):
        ### title
        canvas.create_text(mode.width/2, mode.height/10,
                            fill=mode.titleColor,
                            text='Story', 
                            font='PlayfairDisplay 64 bold')
        ### 'Back' button
        canvas.create_rectangle(50, 50, 150, 100,
                            fill=mode.backButtonColor)
        canvas.create_text(100, 75,
                            fill=mode.backButtonTextColor,
                            text='Back', 
                            font='PlayfairDisplay 16 bold')
        ### 'Next' button
        canvas.create_rectangle(mode.width-50, 50, mode.width-150, 100,
                            fill=mode.nextButtonColor)
        canvas.create_text(mode.width-100, 75,
                            fill=mode.nextButtonTextColor,
                            text='Next', 
                            font='PlayfairDisplay 16 bold')

class AvatarScreen(StoryScreen):
    def appStarted(mode):
        mode.titleColor = 'black'
        mode.backButtonColor = mode.nextButtonColor = 'sea green'
        mode.backButtonTextColor = mode.nextButtonTextColor = 'white'
        mode.infoButtonColor = 'gray'
        mode.infoButtonTextColor = 'black'
        mode.startButtonColor = 'sea green'
        mode.startButtonTextColor = 'white'

    def mouseMoved(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.backButtonColor = 'white'
            mode.backButtonTextColor = 'sea green'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.nextButtonColor = 'white'
            mode.nextButtonTextColor = 'sea green'
        elif ((mode.width/2-100 <= event.x <= mode.width/2+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.startButtonColor = 'white'
            mode.startButtonTextColor = 'sea green'
        elif (((event.x < 50) or ((event.x > 150) 
            and (event.x < mode.width-150)) or (event.x > mode.width-50)
            or ((event.y < 50) or (event.y > 100)))
            or ((event.x < mode.width/2-100) or (event.x > mode.width/2+100)
            or (event.y < mode.height*9/10-50) 
            or (event.y < mode.height*9/10+50))):
            mode.backButtonColor = mode.nextButtonColor = 'sea green'
            mode.backButtonTextColor = mode.nextButtonTextColor = 'white'
            mode.startButtonColor = 'sea green'
            mode.startButtonTextColor = 'white'
        # add info button toggling after location is set?

    def mousePressed(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.storyScreen)
            mode.backButtonColor = 'sea green'
            mode.backButtonTextColor = 'white'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.titleScreen)
            mode.nextButtonColor = 'sea green'
            mode.nextButtonTextColor = 'white'
        elif ((mode.width/2-50 <= event.x <= mode.width/2+50) 
            and (mode.height/2-50 <= event.y <= mode.height/2+50)):
            mode.app.setActiveMode(mode.app.sledsScreen)
        elif ((mode.width/2-100 <= event.x <= mode.width/2+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.app.setActiveMode(mode.app.gameModeScreen)
            mode.startButtonColor = 'sea green'
            mode.startButtonTextColor = 'white'

    def redrawAll(mode, canvas):
        ### title
        canvas.create_text(mode.width/2, mode.height/10,
                            fill=mode.titleColor,
                            text='Customize Your Avatar', 
                            font='PlayfairDisplay 64 bold')
        ### 'Back' button
        canvas.create_rectangle(50, 50, 150, 100,
                            fill=mode.backButtonColor)
        canvas.create_text(100, 75,
                            fill=mode.backButtonTextColor,
                            text='Back', 
                            font='PlayfairDisplay 16 bold')
        ### 'Home' button
        canvas.create_rectangle(mode.width-50, 50, mode.width-150, 100,
                            fill=mode.nextButtonColor)
        canvas.create_text(mode.width-100, 75,
                            fill=mode.nextButtonTextColor,
                            text='Home', 
                            font='PlayfairDisplay 16 bold')
        ### 'More Info' Button
        canvas.create_rectangle(mode.width/2-50, mode.height/2-50, 
                            mode.width/2+50, mode.height/2+50,
                            fill=mode.infoButtonColor)
        canvas.create_text(mode.width/2, mode.height/2,
                            fill=mode.infoButtonTextColor,
                            text='More Info', 
                            font='PlayfairDisplay 16 bold')
        ### 'Start' Button
        canvas.create_rectangle(mode.width/2-100, mode.height*9/10-50, 
                            mode.width/2+100, mode.height*9/10+50,
                            fill=mode.startButtonColor)
        canvas.create_text(mode.width/2, mode.height*9/10,
                            fill=mode.startButtonTextColor,
                            text='Start!', 
                            font='PlayfairDisplay 40 bold')

class SledsScreen(AvatarScreen):
    def mousePressed(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.avatarScreen)
            mode.backButtonColor = 'sea green'
            mode.backButtonTextColor = 'white'

    def redrawAll(mode, canvas):
        ### title
        canvas.create_text(mode.width/2, mode.height/10,
                            fill=mode.titleColor,
                            text='Sleds', 
                            font='PlayfairDisplay 64 bold')
        ### 'Back' button
        canvas.create_rectangle(50, 50, 150, 100,
                            fill=mode.backButtonColor)
        canvas.create_text(100, 75,
                            fill=mode.backButtonTextColor,
                            text='Back', 
                            font='PlayfairDisplay 16 bold')

class GameModeScreen(AvatarScreen):
    def mousePressed(mode, event):
        if ((mode.width/2-100 <= event.x <= mode.width/2+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.app.setActiveMode(mode.app.finalScreen)

    def redrawAll(mode, canvas):
        ### title
        canvas.create_text(mode.width/2, mode.height/2,
                            fill=mode.titleColor,
                            text='Game Mode', 
                            font='PlayfairDisplay 64 bold')
        ### 'Exit' Button
        canvas.create_rectangle(mode.width/2-100, mode.height*9/10-50, 
                            mode.width/2+100, mode.height*9/10+50,
                            fill='black')
        canvas.create_text(mode.width/2, mode.height*9/10,
                            fill='white',
                            text='Exit', 
                            font='PlayfairDisplay 40 bold')

class FinalScreen(GameModeScreen):
    def appStarted(mode):
        mode.titleColor = 'black'
        mode.playAgainButtonColor = 'sea green'
        mode.playAgainButtonTextColor = 'white'
        mode.homeButtonColor = 'gray'
        mode.homeButtonTextColor = 'black'

    def mouseMoved(mode, event):
        if ((mode.width/2-200 <= event.x <= mode.width/2+200) 
            and (mode.height*7/10-50 <= event.y <= mode.height*7/10+50)):
            mode.playAgainButtonColor = 'white'
            mode.playAgainButtonTextColor = 'sea green'
        elif ((mode.width/2-50 <= event.x <= mode.width/2+50) 
            and (mode.height*9/10-25 <= event.y <= mode.height*9/10+25)):
            mode.homeButtonColor = 'black'
            mode.homeButtonTextColor = 'gray'
        elif ((event.x < mode.width/2-200) or (event.x > mode.width/2+200)
            or (event.y < mode.height*7/10-50) 
            or (event.y > mode.height*7/10+50)):
            mode.playAgainButtonColor = 'sea green'
            mode.playAgainButtonTextColor = 'white'
        elif ((event.x < mode.width/2-50) or (event.x > mode.width/2+50)
            or (event.y < mode.height*9/10-25) 
            or (event.y > mode.height*9/10+25)):
            mode.homeButtonColor = 'gray'
            mode.homeButtonTextColor = 'black'

    def mousePressed(mode, event):
        if ((mode.width/2-200 <= event.x <= mode.width/2+200) 
            and (mode.height*7/10-50 <= event.y <= mode.height*7/10+50)):
            mode.app.setActiveMode(mode.app.avatarScreen)
            mode.playAgainButtonColor = 'sea green'
            mode.playAgainButtonTextColor = 'white'
        elif ((mode.width/2-50 <= event.x <= mode.width/2+50) 
            and (mode.height*9/10-25 <= event.y <= mode.height*9/10+25)):
            mode.app.setActiveMode(mode.app.titleScreen)
            mode.homeButtonColor = 'gray'
            mode.homeButtonTextColor = 'black'

    def redrawAll(mode, canvas):
        ### title
        canvas.create_text(mode.width/2, mode.height*3/10,
                            fill=mode.titleColor,
                            text='Congrats!', 
                            font='PlayfairDisplay 64 bold')
        canvas.create_text(mode.width/2, mode.height*4/10,
                            fill=mode.titleColor,
                            text='You successfully delivered __ presents', 
                            font='PlayfairDisplay 40 bold')
        ### 'Play Again' Button
        canvas.create_rectangle(mode.width/2-200, mode.height*7/10-50, 
                            mode.width/2+200, mode.height*7/10+50,
                            fill=mode.playAgainButtonColor)
        canvas.create_text(mode.width/2, mode.height*7/10,
                            fill=mode.playAgainButtonTextColor,
                            text='Play Again', 
                            font='PlayfairDisplay 40 bold')
        ### 'Exit' Button
        canvas.create_rectangle(mode.width/2-50, mode.height*9/10-25, 
                            mode.width/2+50, mode.height*9/10+25,
                            fill=mode.homeButtonColor)
        canvas.create_text(mode.width/2, mode.height*9/10,
                            fill=mode.homeButtonTextColor,
                            text='Home', 
                            font='PlayfairDisplay 20 bold')

MyApp(width=1000, height=800)



########################################
#   Santa Maze Game
#   Sarah Chen (sarahc2)
########################################
#   Maze Generation & Solution
########################################
import random

def generateMazeDict(n):
    mazeDict = {}
    lastPoint = (0,0)
    newPoint = (1,0)
    generateMazeDictHelper(n, mazeDict, lastPoint, newPoint, 0)
    return mazeDict

def generateMazeDictHelper(n, mazeDict, lastPoint, newPoint, index):
    # check if newPoint valid
    newX, newY = newPoint
    if ((newX < 0) or (newX > n-1) or (newY < 0) or (newY > n-1)
        or (isPointInDict(mazeDict, newPoint) == True) 
        or (newPoint == (0,0))):
        return False

    # set new point
    if lastPoint in mazeDict:
        mazeDict[lastPoint].append(newPoint)
    else:
        mazeDict[lastPoint] = [newPoint]

    # check if maze complete
    if (index == (n**2 - 2)):
        return True

    # run through moves & continue w recursion
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    random.shuffle(moves)
    for move in moves:
        dx, dy = move
        nextX = newX + dx
        nextY = newY + dy
        nextPoint = (nextX, nextY)
        if (generateMazeDictHelper(n, mazeDict, newPoint, 
                                    nextPoint, index+1) == True):
            return True
    
    # if recursion doesn't work, undo move
    return generateMazeDictHelper(n, mazeDict, lastPoint, newPoint, index)

def isPointInDict(mazeDict, point):
    for coordinate in mazeDict:
        if point in mazeDict[coordinate]:
            return True
    return False

def mazeSolver(n):
    mazeDict = generateMazeDict(n)
    solution = [(0,0)]
    lastPoint = (1,0)
    mazeSolverHelper(n, mazeDict, solution, lastPoint)
    return mazeDict, solution

def mazeSolverHelper(n, mazeDict, solution, lastPoint):
    lastX, lastY = lastPoint

    # set lastPoint
    solution.append(lastPoint)

    # check if reached bottom right coordinate
    if (lastPoint == (n-1, n-1)):
        return True

    # check if lastPoint valid
    if (lastPoint not in mazeDict):
        solution.pop()
        return False
    
    # recurse 
    for connection in mazeDict[lastPoint]:
        if mazeSolverHelper(n, mazeDict, solution, connection) == True:
            return True

    # if recursion doesn't work
    solution.pop()
    return False

def getMazeSolutionConnections(n):
    mazeDict, solution = mazeSolver(n)
    connDict = dict()

    # create dictionary of all coordinates
    for x in range(n):
        for y in range(n):
            connDict[(x,y)] = []
    
    # map all coordinates to every point each is connected to
    for key in mazeDict:
        connDict[key] += mazeDict[key]
        for point in mazeDict[key]:
            connDict[point].append((key))

    print(f'Dict: {mazeDict} \n Sol: {solution} \n Conn: {connDict}')
    return mazeDict, solution, connDict

# getMazeSolutionConnections(2)



########################################
#   Santa Maze Game
#   Sarah Chen (sarahc2)
########################################
#   Maze & Solution Display
########################################
from mazeGenerationAndSolution import *
from cmu_112_graphics import *

def appStarted(app):
    app.n = 15
    app.cellWidth = app.width / app.n
    app.cellHeight = app.height / app.n
    app.lineWidth = app.height / (app.n * 10)
    app.lineMargin = app.lineWidth * 2 / 5
    app.lines = set()
    app.dotX = app.cellWidth / 2
    app.dotY = app.cellHeight / 2
    app.dotR = min(app.cellWidth, app.cellHeight) / 3
    app.mazeDict, app.solution, app.connDict = getMazeSolutionConnections(app.n)
    app.showSolution = False

def keyPressed(app, event):
    if (event.key == 'Space'):
        app.showSolution = not app.showSolution
    elif (event.key == 'Up'):
        app.dotY -= 10
    elif (event.key == 'Down'):
        app.dotY += 10
    elif (event.key == 'Left'):
        app.dotX -= 10
    elif (event.key == 'Right'):
        app.dotX += 10
 
def redrawAll(app, canvas):
    if (app.showSolution == True):
        for point in app.solution:
            highlight(app, canvas, point)

    for point in app.connDict:
        x, y = point
        abovePoint = (x, y-1)
        belowPoint = (x, y+1)
        leftPoint = (x-1, y)
        rightPoint = (x+1, y)
        if abovePoint not in app.connDict[point]:
            drawAboveLine(app, canvas, point)
        if belowPoint not in app.connDict[point]:
            drawBelowLine(app, canvas, point)
        if leftPoint not in app.connDict[point]:
            drawLeftLine(app, canvas, point)
        if rightPoint not in app.connDict[point]:
            drawRightLine(app, canvas, point)

    canvas.create_oval(app.dotX - app.dotR, app.dotY - app.dotR,
                    app.dotX + app.dotR, app.dotY + app.dotR,
                    fill='red')

def drawAboveLine(app, canvas, point):
    x, y = point
    x1 = x * app.cellWidth - app.lineMargin
    x2 = x * app.cellWidth + app.cellWidth + app.lineMargin
    y1 = y * app.cellHeight
    canvas.create_line(x1, y1, x2, y1, width=app.lineWidth)

def drawBelowLine(app, canvas, point):
    x, y = point
    x1 = x * app.cellWidth - app.lineMargin
    x2 = x * app.cellWidth + app.cellWidth + app.lineMargin
    y1 = y * app.cellHeight + app.cellHeight
    canvas.create_line(x1, y1, x2, y1, width=app.lineWidth)

def drawLeftLine(app, canvas, point):
    x, y = point
    x1 = x * app.cellWidth
    y1 = y * app.cellHeight - app.lineMargin
    y2 = y * app.cellHeight + app.cellHeight + app.lineMargin
    canvas.create_line(x1, y1, x1, y2, width=app.lineWidth)

def drawRightLine(app, canvas, point):
    x, y = point
    x1 = x * app.cellWidth + app.cellWidth
    y1 = y * app.cellHeight - app.lineMargin
    y2 = y * app.cellHeight + app.cellHeight + app.lineMargin
    canvas.create_line(x1, y1, x1, y2, width=app.lineWidth)

def highlight(app, canvas, point):
    x, y = point
    x1 = x * app.cellWidth
    x2 = x * app.cellWidth + app.cellWidth
    y1 = y * app.cellHeight
    y2 = y * app.cellHeight + app.cellHeight
    canvas.create_rectangle(x1, y1, x2, y2, fill='yellow', outline='')

runApp(width=1000, height=800)
