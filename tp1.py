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
        elif (((event.x < 50) or ((event.x > 150) 
            and (event.x < mode.width-150)) or (event.x > mode.width-50)
            or ((event.y < 50) or (event.y > 100)))):
            mode.backButtonColor = mode.nextButtonColor = 'sea green'
            mode.backButtonTextColor = mode.nextButtonTextColor = 'white'
        if ((mode.width/2-100 <= event.x <= mode.width/2+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.startButtonColor = 'white'
            mode.startButtonTextColor = 'sea green'
        elif ((event.x < mode.width/2-100) or (event.x > mode.width/2+100)
            or (event.y < mode.height*9/10-50) 
            or (event.y < mode.height*9/10+50)):
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
        elif ((event.x < mode.width/2-50) or (event.x > mode.width/2+50)
            or (event.y < mode.height*9/10-25) 
            or (event.y > mode.height*9/10+25)):
            mode.homeButtonColor = 'gray'
            mode.homeButtonTextColor = 'black'
        if ((event.x < mode.width/2-200) or (event.x > mode.width/2+200)
            or (event.y < mode.height*7/10-50) 
            or (event.y > mode.height*7/10+50)):
            mode.playAgainButtonColor = 'sea green'
            mode.playAgainButtonTextColor = 'white'

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
#   Buttons
########################################

class Buttons(object):
    def __init__(self, label):
        self.label = label

    def startButton(self, canvas):
        canvas.create_rectangle(self.width/2-150, self.height*2/3-50,
                            self.width/2+150, self.height*2/3+50,
                            fill='dark sea green')
        canvas.create_text(self.width/2, self.height*2/3,
                            fill='white',
                            text=self.label, 
                            font='PlayfairDisplay 40 bold')
        
        
        
########################################
#   Maze Game
#   Coded by: Sarah Chen (sarahc2)
########################################
#
#   Citations: 
#   1)  http://weblog.jamisbuck.org/2011/1/12/
#       maze-generation-recursive-division-algorithm
#
########################################
from cmu_112_graphics import *
import random

# experimenting with drawing random lines one at a time
def chooseOrientation(width, height):
    if (width < height):
        return 'horizontal'
    elif (height > width):
        return 'vertical'
    else:
        return random.choice(['horizontal', 'vertical'])

def appStarted(app):
    app.yValues = list()
    app.xValues = list()
    app.dimension = 5

def defineYValues(app, width, height, dimension):
    orientation = chooseOrientation(width, height)
    if (orientation == 'horizontal') or (orientation == 'vertical'):
        yValue = random.randint(1, app.dimension)
        app.yValues.append(yValue)
    print('yValues: ', app.yValues)

def defineXValues(app, width, height, dimension):
    orientation = chooseOrientation(width, height)
    if (orientation == 'horizontal') or (orientation == 'vertical'):
        xValue = random.randint(1, app.dimension)
        app.xValues.append(xValue)
    print('xValues: ', app.xValues)

def keyPressed(app, event):
    if (event.key == 'y'):
        defineYValues(app, app.width, app.height, app.dimension)
    elif (event.key == 'x'):
        defineXValues(app, app.width, app.height, app.dimension)

def drawMaze(app, canvas):
    for yValue in app.yValues:
        yValue = yValue*(app.height/app.dimension)
        canvas.create_line(0, yValue, app.width, yValue)
    for xValue in app.xValues:
        xValue = xValue*(app.width/app.dimension)
        canvas.create_line(xValue, 0, xValue, app.height)

def redrawAll(app, canvas):
    drawMaze(app, canvas)

runApp(width=400, height=400)



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

    # print(f'Dict: {mazeDict} \n Sol: {solution} \n Conn: {connDict}')
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
    app.n = 35 # 38+ has MVC Violation
    app.cellWidth = app.width / app.n
    app.cellHeight = app.height / app.n
    app.lineWidth = app.height / (app.n * 10)
    app.lineMargin = app.lineWidth * 2 / 5
    app.dotX = app.cellWidth / 2
    app.dotY = app.cellHeight / 2
    app.dotR = min(app.cellWidth, app.cellHeight) / 3
    app.dotStepSize = app.dotR / 2
    app.mazeDict, app.solution, app.connDict = getMazeSolutionConnections(app.n)
    app.showSolution = False

def keyPressed(app, event):
    if (event.key == 'Space'):
        app.showSolution = not app.showSolution
    elif (event.key == 'r'):
        appStarted(app)
    elif (event.key == 'Up'):
        possibleMoves = getPossibleMoves(app)
        print(possibleMoves)
        if (app.dotY > app.dotStepSize) and ('Up' in possibleMoves):
            app.dotY -= app.dotStepSize
    elif (event.key == 'Down'):
        possibleMoves = getPossibleMoves(app)
        print(possibleMoves)
        if ((app.dotY < app.height - app.dotStepSize) 
            and ('Down' in possibleMoves)):
            app.dotY += app.dotStepSize
    elif (event.key == 'Left'):
        possibleMoves = getPossibleMoves(app)
        print(possibleMoves)
        if (app.dotX > app.dotStepSize) and ('Left' in possibleMoves):
            app.dotX -= app.dotStepSize
    elif (event.key == 'Right'):
        possibleMoves = getPossibleMoves(app)
        print(possibleMoves)
        if ((app.dotX < app.width - app.dotStepSize) 
            and ('Right' in possibleMoves)):
            app.dotX += app.dotStepSize
 
def getPossibleMoves(app):
    # center and radius of dot
    cx, cy, r = app.dotX, app.dotY, app.dotR
    # bounds of cell that center of dot is in
    centerx0, centerx1, centery0, centery1 = getCellBounds(app,centerX,centerY)
    # left, right, top, and bottom of dot
    dotx0, dotx1, doty0, doty1 = cx-r, cx+r, cy-r, cy+r
    midX = (dotx0 + dotx1) / 2
    midY = (doty0 + doty1) / 2

    # cell that center, top, bottom, left, and right of dot is in
    centerX, centerY = getCell(app, cx, cy)
    cellOfCenter = (centerX, centerY)
    aboveX, aboveY = getCell(app, midX, doty0)
    cellOfTop = (aboveX, aboveY)
    belowX, belowY = getCell(app, midX, doty1)
    cellOfBottom = (belowX, belowY)
    leftX, leftY = getCell(app, dotx0, midY)
    cellOfLeft = (leftX, leftY)
    rightX, rightY = getCell(app, dotx1, midY)
    cellOfRight = (rightX, rightY)

    possibleMoves = set()

    # check if dot can move within cell
    if (doty0 - app.dotStepSize > centery0 + (app.lineWidth * 2 / 3)):
        possibleMoves.add('Up')
    if (doty1 + app.dotStepSize < centery1 - (app.lineWidth * 2 / 3)):
        possibleMoves.add('Down')
    if (dotx0 - app.dotStepSize > centerx0 + (app.lineWidth * 2 / 3)):
        possibleMoves.add('Left')
    if (dotx1 + app.dotStepSize < centerx1 - (app.lineWidth * 2 / 3)):
        possibleMoves.add('Right')

    # cells above, below, left, and right of center cell
    cellAbove = (centerX, centerY-1)
    cellBelow = (centerX, centerY+1)
    cellLeft = (centerX-1, centerY)
    cellRight = (centerX+1, centerY)

    # check if dot can move to next cell
    if ((cellAbove in app.connDict[cellOfLeft]) 
        and (cellAbove in app.connDict[cellOfRight])):
        possibleMoves.add('Up')
    if ((cellBelow in app.connDict[cellOfLeft]) 
        and (cellBelow in app.connDict[cellOfRight])):
        possibleMoves.add('Down')
    if ((cellLeft in app.connDict[cellOfTop]) 
        and (cellLeft in app.connDict[cellOfBottom])):
        possibleMoves.add('Left')
    if ((cellRight in app.connDict[cellOfTop]) 
        and (cellRight in app.connDict[cellOfBottom])):
        possibleMoves.add('Right')

    return possibleMoves

def getCell(app, cx, cy):
    cellX = cx // app.cellWidth
    cellY = cy // app.cellHeight
    return int(cellX), int(cellY)

def getCellBounds(app, x, y):
    x0 = x * app.cellWidth
    x1 = x * app.cellWidth + app.cellWidth
    y0 = y * app.cellHeight
    y1 = y * app.cellHeight + app.cellHeight
    return x0, x1, y0, y1

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
                    app.dotX + app.dotR, app.dotY + app.dotR, fill='red')

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
