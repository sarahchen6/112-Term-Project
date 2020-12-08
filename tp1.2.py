########################################
#   Santa Maze Game
#   Sarah Chen (sarahc2)
########################################
#   Combine to App
########################################
from gameScreens import *
from mazeModes import *

class MyApp(ModalApp):
    def appStarted(app):
        # from main
        app.titleScreen = TitleScreen()
        app.storyScreen = StoryScreen()
        app.avatarScreen = AvatarScreen()
        app.sledsScreen = SledsScreen()
        app.gameModeScreen = GameModeScreen()
        app.finalScreen = FinalScreen()
        app.setActiveMode(app.titleScreen)

        # from mazeModes
        app.maze = Maze()
        app.radiusMode = RadiusMode()
        app.grinchMode = GrinchMode()
        app.presents = 100
        app.timeSec = 0
        app.timeMin = 0

        app.timerMode = False
        app.timerDelay = 1000

    def timerFired(app):
        if (app.timerMode == True):
            app.timeSec += 1
            if (app.timeSec >= 60):
                app.timeMin += 1
                if (app.presents >= 10):
                    app.presents -= 1
            app.timeSec %= 60

MyApp(width=1000, height=800)

########################################
#   Santa Maze Game
#   Sarah Chen (sarahc2)
########################################
#   Maze Modes
########################################
from mazeGenerationAndSolution import *
from cmu_112_graphics import *
# from gameScreens import *

# class MyApp(ModalApp):
#     def appStarted(app):
#         app.maze = Maze()
#         app.radiusMode = RadiusMode()
#         app.grinchMode = GrinchMode()
#         app.setActiveMode(app.maze)
#         app.n = 10 
#         app.presents = 100

class Maze(Mode):
    def appStarted(mode):
        # maze display
        mode.n = 10 # 38+ has MVC Violation
        mode.mazeDict, mode.solution, mode.connDict, mode.grinchSolution = getMazeSolutionConnections(mode.n, (0,0), (mode.n-1,mode.n-1))
        mode.cellWidth = mode.width / mode.n
        mode.cellHeight = mode.height / mode.n
        mode.lineWidth = mode.height / (mode.n * 10)
        mode.lineMargin = mode.lineWidth * 2 / 5
        mode.showSolution = False
        mode.visibilityR = 5
        mode.mazeFontSize = int(min(mode.cellWidth, mode.cellHeight) / 3)

        # sled
        mode.dotX = mode.cellWidth + mode.cellWidth / 2
        mode.dotY = mode.cellHeight / 2
        mode.dotR = min(mode.cellWidth, mode.cellHeight) / 3
        mode.dotStepSize = mode.dotR / 2
        sledURL = 'https://www.pngarts.com/files/3/Santa-Sleigh-PNG-Background-Image.png'
        mode.sled = mode.loadImage(sledURL)
        mode.sledResized = mode.scaleImage(mode.sled, mode.cellWidth / 1000)

        # grinch
        mode.grinchX = mode.width - mode.cellWidth / 2
        mode.grinchY = mode.cellHeight / 2
        mode.grinchR = min(mode.cellWidth, mode.cellHeight) / 3
        grinchURL = 'https://i.dlpng.com/static/png/6827226_preview.png'
        mode.grinch = mode.loadImage(grinchURL)
        mode.grinchResized = mode.scaleImage(mode.grinch, mode.cellWidth / 1000)

        # north pole and chimney
        northPoleURL = 'https://assets.stickpng.com/thumbs/5843097ca6515b1e0ad75b4c.png'
        mode.northPole = mode.loadImage(northPoleURL)
        mode.northPoleResized = mode.scaleImage(mode.northPole, mode.cellWidth / 500)
        chimneyURL = 'https://images.vexels.com/media/users/3/145859/isolated/lists/cc57359f1f0208919bbe3330dc482d43-snowy-chimney.png'
        mode.chimney = mode.loadImage(chimneyURL)
        mode.chimneyResized = mode.scaleImage(mode.chimney, mode.cellWidth / 500)
        
    def restartMaze(mode):
        # maze display
        mode.mazeDict, mode.solution, mode.connDict, mode.grinchSolution = getMazeSolutionConnections(mode.n, (0,0), (mode.n-1,mode.n-1))
        mode.cellWidth = mode.width / mode.n
        mode.cellHeight = mode.height / mode.n
        mode.lineWidth = mode.height / (mode.n * 10)
        mode.lineMargin = mode.lineWidth * 2 / 5
        mode.showSolution = False
        mode.visibilityR = 5
        mode.mazeFontSize = int(min(mode.cellWidth, mode.cellHeight) / 3)
        mode.app.timeMin = 0
        mode.app.timeSec = 0
        mode.app.presents = 100

        # sled
        mode.dotX = mode.cellWidth + mode.cellWidth / 2
        mode.dotY = mode.cellHeight / 2
        mode.dotR = min(mode.cellWidth, mode.cellHeight) / 3
        mode.dotStepSize = mode.dotR / 2
        mode.sledResized = mode.scaleImage(mode.sled, mode.cellWidth / 1000)

        # grinch
        mode.grinchX = mode.width - mode.cellWidth / 2
        mode.grinchY = mode.cellHeight / 2
        mode.grinchR = min(mode.cellWidth, mode.cellHeight) / 3
        mode.grinchResized = mode.scaleImage(mode.grinch, mode.cellWidth / 1000)

        # north pole and home
        mode.northPoleResized = mode.scaleImage(mode.northPole, mode.cellWidth / 500)

    def keyPressed(mode, event):
        if (event.key == 'Space'):
            mode.showSolution = not mode.showSolution
        elif (event.key == 'r'):
            Maze.restartMaze(mode)
        elif (event.key == 'Up'):
            possibleMoves = Maze.getPossibleMoves(mode)
            if (mode.dotY > mode.dotStepSize) and ('Up' in possibleMoves):
                mode.dotY -= mode.dotStepSize
                Maze.checkIfMazeSolved(mode)
        elif (event.key == 'Down'):
            possibleMoves = Maze.getPossibleMoves(mode)
            if ((mode.dotY < mode.height - mode.dotStepSize) 
                and ('Down' in possibleMoves)):
                mode.dotY += mode.dotStepSize
                Maze.checkIfMazeSolved(mode)
        elif (event.key == 'Left'):
            possibleMoves = Maze.getPossibleMoves(mode)
            if (mode.dotX > mode.dotStepSize) and ('Left' in possibleMoves):
                mode.dotX -= mode.dotStepSize
                Maze.checkIfMazeSolved(mode)
        elif (event.key == 'Right'):
            possibleMoves = Maze.getPossibleMoves(mode)
            if ((mode.dotX < mode.width - mode.dotStepSize) 
                and ('Right' in possibleMoves)):
                mode.dotX += mode.dotStepSize
                Maze.checkIfMazeSolved(mode)
        elif (event.key == 'b'):
            mode.visibilityR += 1
        elif (event.key == 's'):
            if (mode.visibilityR > 0):
                mode.visibilityR -= 1
        elif (event.key == '1'):
            mode.n = 5
            Maze.restartMaze(mode)
        elif (event.key == '2'):
            mode.n = 10
            Maze.restartMaze(mode)
        elif (event.key == '3'):
            mode.n = 15
            Maze.restartMaze(mode)
        elif (event.key == '4'):
            mode.n = 20
            Maze.restartMaze(mode)
        elif (event.key == '5'):
            mode.n = 25
            Maze.restartMaze(mode)
        elif (event.key == '6'):
            mode.n = 30
            Maze.restartMaze(mode)
        elif (event.key == '7'):
            mode.n = 35
            Maze.restartMaze(mode)
        elif (event.key == '8'):
            Maze.restartMaze(mode)
            mode.app.setActiveMode(mode.app.maze)
        elif (event.key == '9'):
            Maze.restartMaze(mode)
            mode.app.timerMode = True
            mode.app.setActiveMode(mode.app.radiusMode)
        elif (event.key == '0'):
            Maze.restartMaze(mode)
            mode.app.timerMode = True
            mode.app.setActiveMode(mode.app.grinchMode)

    def checkIfMazeSolved(mode):
        cellX, cellY = Maze.getCell(mode, mode.dotX, mode.dotY)
        if ((cellX, cellY) == (mode.n - 1, mode.n - 1)):
            Maze.resetTimerAndPresents(mode)
            mode.app.setActiveMode(mode.app.finalScreen)

    def resetTimerAndPresents(mode):
        mode.app.timerMode = False
        mode.app.timeSec = 0
        mode.app.timeMin = 0
        mode.app.presents = 0
    
    def getPossibleMoves(mode):
        # center and radius of dot
        cx, cy, r = mode.dotX, mode.dotY, mode.dotR
        
        # left, right, top, and bottom of dot
        dotx0, dotx1, doty0, doty1 = cx-r, cx+r, cy-r, cy+r
        midX = (dotx0 + dotx1) / 2
        midY = (doty0 + doty1) / 2

        # cell that center, top, bottom, left, and right of dot is in
        centerX, centerY = Maze.getCell(mode, cx, cy)
        cellOfCenter = (centerX, centerY)
        aboveX, aboveY = Maze.getCell(mode, midX, doty0)
        cellOfTop = (aboveX, aboveY)
        belowX, belowY = Maze.getCell(mode, midX, doty1)
        cellOfBottom = (belowX, belowY)
        leftX, leftY = Maze.getCell(mode, dotx0, midY)
        cellOfLeft = (leftX, leftY)
        rightX, rightY = Maze.getCell(mode, dotx1, midY)
        cellOfRight = (rightX, rightY)

        # bounds of cell that center of dot is in
        centerx0, centerx1, centery0, centery1 = Maze.getCellBounds(mode, 
                                                                    centerX, 
                                                                    centerY)

        possibleMoves = set()

        # check if dot can move within cell
        if (doty0 - mode.dotStepSize > centery0 + (mode.lineWidth * 2 / 3)):
            possibleMoves.add('Up')
        if (doty1 + mode.dotStepSize < centery1 - (mode.lineWidth * 2 / 3)):
            possibleMoves.add('Down')
        if (dotx0 - mode.dotStepSize > centerx0 + (mode.lineWidth * 2 / 3)):
            possibleMoves.add('Left')
        if (dotx1 + mode.dotStepSize < centerx1 - (mode.lineWidth * 2 / 3)):
            possibleMoves.add('Right')

        # cells above, below, left, and right of center cell
        cellAbove = (centerX, centerY-1)
        cellBelow = (centerX, centerY+1)
        cellLeft = (centerX-1, centerY)
        cellRight = (centerX+1, centerY)

        # check if dot can move to next cell
        if ((cellAbove in mode.connDict[cellOfLeft]) 
            and (cellAbove in mode.connDict[cellOfRight])):
            possibleMoves.add('Up')
        if ((cellBelow in mode.connDict[cellOfLeft]) 
            and (cellBelow in mode.connDict[cellOfRight])):
            possibleMoves.add('Down')
        if ((cellLeft in mode.connDict[cellOfTop]) 
            and (cellLeft in mode.connDict[cellOfBottom])):
            possibleMoves.add('Left')
        if ((cellRight in mode.connDict[cellOfTop]) 
            and (cellRight in mode.connDict[cellOfBottom])):
            possibleMoves.add('Right')

        return possibleMoves

    def getCell(mode, cx, cy):
        cellX = cx // mode.cellWidth
        cellY = cy // mode.cellHeight
        return int(cellX), int(cellY)

    def getCellBounds(mode, x, y):
        x0 = x * mode.cellWidth
        x1 = x * mode.cellWidth + mode.cellWidth
        y0 = y * mode.cellHeight
        y1 = y * mode.cellHeight + mode.cellHeight
        return x0, x1, y0, y1

    def drawAboveLine(mode, canvas, point):
        x, y = point
        x1 = x * mode.cellWidth - mode.lineMargin
        x2 = x * mode.cellWidth + mode.cellWidth + mode.lineMargin
        y1 = y * mode.cellHeight
        canvas.create_line(x1, y1, x2, y1, width=mode.lineWidth)

    def drawBelowLine(mode, canvas, point):
        x, y = point
        x1 = x * mode.cellWidth - mode.lineMargin
        x2 = x * mode.cellWidth + mode.cellWidth + mode.lineMargin
        y1 = y * mode.cellHeight + mode.cellHeight
        canvas.create_line(x1, y1, x2, y1, width=mode.lineWidth)

    def drawLeftLine(mode, canvas, point):
        x, y = point
        x1 = x * mode.cellWidth
        y1 = y * mode.cellHeight - mode.lineMargin
        y2 = y * mode.cellHeight + mode.cellHeight + mode.lineMargin
        canvas.create_line(x1, y1, x1, y2, width=mode.lineWidth)

    def drawRightLine(mode, canvas, point):
        x, y = point
        x1 = x * mode.cellWidth + mode.cellWidth
        y1 = y * mode.cellHeight - mode.lineMargin
        y2 = y * mode.cellHeight + mode.cellHeight + mode.lineMargin
        canvas.create_line(x1, y1, x1, y2, width=mode.lineWidth)

    def indicateSolution(mode, canvas, point):
        x, y = point        
        cx = x * mode.cellWidth + mode.cellWidth / 2
        cy = y * mode.cellHeight + mode.cellHeight / 2
        r = min(mode.cellWidth, mode.cellHeight) / 10
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='black')

    def highlight(mode, canvas, point):
        x, y = point
        x1 = x * mode.cellWidth
        x2 = x * mode.cellWidth + mode.cellWidth
        y1 = y * mode.cellHeight
        y2 = y * mode.cellHeight + mode.cellHeight
        canvas.create_rectangle(x1, y1, x2, y2, fill='yellow', outline='')

    def redrawAll(mode, canvas):
        if (mode.showSolution == True):
            for point in mode.solution:
                Maze.indicateSolution(mode, canvas, point)

        for point in mode.grinchSolution:
            Maze.highlight(mode, canvas, point)

        for point in mode.connDict:
            x, y = point
            abovePoint = (x, y-1)
            belowPoint = (x, y+1)
            leftPoint = (x-1, y)
            rightPoint = (x+1, y)
            if abovePoint not in mode.connDict[point]:
                Maze.drawAboveLine(mode, canvas, point)
            if belowPoint not in mode.connDict[point]:
                Maze.drawBelowLine(mode, canvas, point)
            if leftPoint not in mode.connDict[point]:
                Maze.drawLeftLine(mode, canvas, point)
            if rightPoint not in mode.connDict[point]:
                Maze.drawRightLine(mode, canvas, point)

        # sled
        canvas.create_oval(mode.dotX - mode.dotR, mode.dotY - mode.dotR,
                        mode.dotX + mode.dotR, mode.dotY + mode.dotR, 
                        fill='white', outline='')
        canvas.create_image(mode.dotX, mode.dotY, 
                        image=ImageTk.PhotoImage(mode.sledResized))

        # north pole, chimney
        canvas.create_image(mode.cellWidth / 2, mode.cellHeight / 2, 
                        image=ImageTk.PhotoImage(mode.northPoleResized))
        canvas.create_image(mode.width - mode.cellWidth / 2, 
                        mode.height - mode.cellHeight / 2,
                        image=ImageTk.PhotoImage(mode.chimneyResized))

class RadiusMode(Maze):
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill='black')
        canvas.create_oval(mode.dotX - mode.dotR * mode.visibilityR, 
                        mode.dotY - mode.dotR * mode.visibilityR,
                        mode.dotX + mode.dotR * mode.visibilityR, 
                        mode.dotY + mode.dotR * mode.visibilityR, 
                        fill='white')

        if (mode.showSolution == True):
            for point in mode.solution:
                Maze.indicateSolution(mode, canvas, point)

        for point in mode.connDict:
            x, y = point
            abovePoint = (x, y-1)
            belowPoint = (x, y+1)
            leftPoint = (x-1, y)
            rightPoint = (x+1, y)
            if abovePoint not in mode.connDict[point]:
                Maze.drawAboveLine(mode, canvas, point)
            if belowPoint not in mode.connDict[point]:
                Maze.drawBelowLine(mode, canvas, point)
            if leftPoint not in mode.connDict[point]:
                Maze.drawLeftLine(mode, canvas, point)
            if rightPoint not in mode.connDict[point]:
                Maze.drawRightLine(mode, canvas, point)

        # sled
        canvas.create_oval(mode.dotX - mode.dotR, mode.dotY - mode.dotR,
                        mode.dotX + mode.dotR, mode.dotY + mode.dotR, 
                        fill='white', outline='')
        canvas.create_image(mode.dotX, mode.dotY, 
                        image=ImageTk.PhotoImage(mode.sledResized))

        # time, presents label
        canvas.create_text(mode.width - 20, 20, fill='green', 
                        text=f'Time: {mode.app.timeMin}m {mode.app.timeSec}s',
                        anchor='ne',
                        font='PlayfairDisplay 40 bold')
        canvas.create_text(mode.width - 20, 60, fill='green', 
                        text=f'Presents: {mode.app.presents}',
                        anchor='ne',
                        font='PlayfairDisplay 40 bold')

        # north pole, chimney
        canvas.create_image(mode.cellWidth / 2, mode.cellHeight / 2, 
                        image=ImageTk.PhotoImage(mode.northPoleResized))
        canvas.create_image(mode.width - mode.cellWidth / 2, 
                        mode.height - mode.cellHeight / 2,
                        image=ImageTk.PhotoImage(mode.chimneyResized))

class GrinchMode(Maze):
    def timerFired(mode):
        # automatically changes time & presents
        if (mode.app.timerMode == True):
            mode.app.timeSec += 1
            if (mode.app.timeSec >= 60):
                mode.app.timeMin += 1
                if (mode.app.presents >= 10):
                    mode.app.presents -= 1
            mode.app.timeSec %= 60

        print(mode.grinchSolution)

        # -10 presents if sled intersects grinch
        GrinchMode.checkSledGrinchIntersect(mode)

        GrinchMode.moveGrinch(mode, mode.grinchSolution)

    def checkSledGrinchIntersect(mode):
        sledX, sledY = mode.getCell(mode, mode.dotX, mode.dotY)
        grinchX, grinchY = mode.getCell(mode, mode.grinchX, mode.grinchY)
        if (sledX, sledY) == (grinchX, grinchY):
            mode.app.presents -= 5

    def moveGrinch(mode, grinchSolList):
        print(grinchSolList)

    def redrawAll(mode, canvas):
        if (mode.showSolution == True):
            for point in mode.solution:
                Maze.indicateSolution(mode, canvas, point)

        for point in mode.connDict:
            x, y = point
            abovePoint = (x, y-1)
            belowPoint = (x, y+1)
            leftPoint = (x-1, y)
            rightPoint = (x+1, y)
            if abovePoint not in mode.connDict[point]:
                Maze.drawAboveLine(mode, canvas, point)
            if belowPoint not in mode.connDict[point]:
                Maze.drawBelowLine(mode, canvas, point)
            if leftPoint not in mode.connDict[point]:
                Maze.drawLeftLine(mode, canvas, point)
            if rightPoint not in mode.connDict[point]:
                Maze.drawRightLine(mode, canvas, point)

        # sled
        canvas.create_oval(mode.dotX - mode.dotR, mode.dotY - mode.dotR,
                        mode.dotX + mode.dotR, mode.dotY + mode.dotR, 
                        fill='white', outline='')
        canvas.create_image(mode.dotX, mode.dotY, 
                        image=ImageTk.PhotoImage(mode.sledResized))

        # grinch
        canvas.create_oval(mode.grinchX - mode.grinchR, mode.grinchY - mode.grinchR,
                        mode.grinchX + mode.grinchR, mode.grinchY + mode.grinchR,
                        fill='white', outline='')
        canvas.create_image(mode.grinchX, mode.grinchY, 
                        image=ImageTk.PhotoImage(mode.grinchResized))

        # time, presents label
        canvas.create_text(mode.width - 20, 20, fill='green', 
                        text=f'Time: {mode.app.timeMin}m {mode.app.timeSec}s',
                        anchor='ne',
                        font='PlayfairDisplay 40 bold')
        canvas.create_text(mode.width - 20, 60, fill='green', 
                        text=f'Presents: {mode.app.presents}',
                        anchor='ne',
                        font='PlayfairDisplay 40 bold')

        # north pole, chimney
        canvas.create_image(mode.cellWidth / 2, mode.cellHeight / 2, 
                        image=ImageTk.PhotoImage(mode.northPoleResized))
        canvas.create_image(mode.width - mode.cellWidth / 2, 
                        mode.height - mode.cellHeight / 2,
                        image=ImageTk.PhotoImage(mode.chimneyResized))

# MyApp(width=1000, height=800)

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
# from mazeModes import *

# class MyApp(ModalApp):
#     def appStarted(app):
#         app.titleScreen = TitleScreen()
#         app.storyScreen = StoryScreen()
#         app.avatarScreen = AvatarScreen()
#         app.sledsScreen = SledsScreen()
#         app.gameModeScreen = GameModeScreen()
#         app.finalScreen = FinalScreen()
#         app.setActiveMode(app.titleScreen)

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
        canvas.create_text(mode.width/2, mode.height/3-50,
                            fill='firebrick4',
                            text='Ho Ho Home', 
                            font='PlayfairDisplay 120 bold')
        canvas.create_text(mode.width/2, mode.height/3+50,
                            fill='firebrick4',
                            text='the Santa Maze Game', 
                            font='PlayfairDisplay 50 bold')
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
                            text='Background', 
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
            mode.app.setActiveMode(mode.app.maze) 
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
                            text=f'You successfully delivered {mode.app.presents} presents', 
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

# MyApp(width=1000, height=800)

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

# def mazeSolver(n, startCell, endCell):
#     mazeDict = generateMazeDict(n)
#     flippedDict = flipMazeDict(mazeDict)
#     solution = [startCell]
#     grinchSolution = [(n-1, 0)]
#     lastPoint = mazeDict[startCell][0]
#     if (((n-1, 0) in mazeDict) and ((n-1, 1) in mazeDict[(n-1, 0)])\
#         or (((n-1, 1) in mazeDict) and ((n-1, 0) in mazeDict[(n-1, 1)]))):
#         grinchLastPoint = (n-1, 1)
#     else:
#         grinchLastPoint = (n-2, 0)
#     mazeSolverHelper(n, mazeDict, solution, lastPoint, endCell)
#     if (len(solution) == 1):
#         mazeSolverHelper(n, flippedDict, solution, lastPoint, endCell)
#     mazeSolverHelper(n, mazeDict, grinchSolution, grinchLastPoint, endCell)
#     if (len(grinchSolution) == 1):
#         grinchSolverHelper(n, flippedDict, grinchSolution, grinchLastPoint, solution, endCell)
#     return mazeDict, flippedDict, solution

def mazeSolver(n, startCell, endCell):
    mazeDict = generateMazeDict(n)
    flippedDict = flipMazeDict(mazeDict)
    solution = [startCell]
    lastPoint = mazeDict[startCell][0]
    mazeSolverHelper(n, mazeDict, solution, lastPoint, endCell)
    if (len(solution) == 1):
        mazeSolverHelper(n, flippedDict, solution, lastPoint, endCell)
    return mazeDict, flippedDict, solution

def mazeSolverInTwoParts(n, startCell, endCell):
    # get maze dictionary, flipped maze dictionary, and solution list from UL to BR
    mazeDict, flippedDict, solution = mazeSolver(n, (0,0), (n-1,n-1))

    # get BL cell
    intermediateCell = (n-1, n-1)

    # firstSol gets from startCell to BR
    firstSol = [startCell]
    try:
        firstLastPoint = mazeDict[startCell][0]
    except:
        for point in mazeDict:
            if startCell in mazeDict[point]:
                firstLastPoint = point
    mazeSolverGivenSol(n, mazeDict, firstSol, firstLastPoint, intermediateCell, solution)
    if (len(firstSol) == 1):
        try:
            firstLastPoint = flippedDict[startCell][0]
        except:
            for point in flippedDict:
                if startCell in flippedDict[point]:
                    firstLastPoint = point
        mazeSolverGivenSol(n, flippedDict, firstSol, firstLastPoint, intermediateCell, solution)

    # gets rid of firstSol duplicate tuples
    fullFirstSol = firstSol
    for point in fullFirstSol:
        if firstSol.count(point) > 1:
            firstSol.remove(point)

    # secondSol gets from endCell to BR
    secondSol = [endCell]
    try:
        secondLastPoint = mazeDict[endCell][0]
    except:
        for point in mazeDict:
            if endCell in mazeDict[point]:
                secondLastPoint = point
    mazeSolverGivenSol(n, mazeDict, secondSol, secondLastPoint, intermediateCell, solution)
    if (len(secondSol) == 1):
        try:
            secondLastPoint = flippedDict[endCell][0]
        except:
            for point in flippedDict:
                if endCell in flippedDict[point]:
                    secondLastPoint = point
        mazeSolverGivenSol(n, flippedDict, secondSol, secondLastPoint, intermediateCell, solution)
    
    # gets rid of secondSol duplicate tuples
    fullSecondSol = secondSol
    for point in fullSecondSol:
        if secondSol.count(point) > 1:
            secondSol.remove(point)

    secondSol.reverse()
    finalSol = firstSol
    finalSol.extend(secondSol)
    fullFinalSol = finalSol
    for point in fullFinalSol:
        if finalSol.count(point) > 1:
            finalSol.remove(point)

    # fullFinalSol = finalSol
    # for i in range(1, len(fullFinalSol)):
    #     x, y = finalSol[i]
    #     poss1 = (x-1, y)
    #     poss2 = (x+1, y)
    #     poss3 = (x, y-1)
    #     poss4 = (x, y+1)
    #     if ((poss1 != finalSol[i-1]) and (poss2 != finalSol[i-1]) 
    #         and (poss3 != finalSol[i-1]) and (poss4 != finalSol[i-1])):
    #         finalSol.remove(finalSol[i])

    # i = 0
    # while (i < len(finalSol)-1):
    #     x, y = finalSol[i]
    #     poss1 = (x-1, y)
    #     poss2 = (x+1, y)
    #     poss3 = (x, y-1)
    #     poss4 = (x, y+1)
    #     if ((poss1 == finalSol[i+1]) or (poss2 == finalSol[i+1]) 
    #         or (poss3 == finalSol[i+1]) or (poss4 == finalSol[i+1])):
    #         i += 1
    #     else:
    #         finalSol.pop(i+1)

    print(finalSol)
    return mazeDict, finalSol

def mazeSolverHelper(n, mazeDict, solution, lastPoint, endCell):
    lastX, lastY = lastPoint

    # set lastPoint
    solution.append(lastPoint)

    # check if reached bottom right coordinate
    if (lastPoint == endCell):
        return True

    # check if lastPoint valid
    if (lastPoint not in mazeDict):
        solution.pop()
        return False
    
    # recurse 
    for connection in mazeDict[lastPoint]:
        if mazeSolverHelper(n, mazeDict, solution, connection, endCell) == True:
            return True

    # if recursion doesn't work
    solution.pop()
    return False

def mazeSolverGivenSol(n, dictionary, solution, lastPoint, endCell, givenSol):
    lastX, lastY = lastPoint

    # set lastPoint
    solution.append(lastPoint)

    # check if reached solution
    for i in range(len(givenSol)):
        if (lastPoint == givenSol[i]):
            solution.extend(givenSol[i:])
            return True

    # check if lastPoint valid
    if (lastPoint not in dictionary):
        solution.pop()
        return False
    
    # recurse 
    for connection in dictionary[lastPoint]:
        if mazeSolverGivenSol(n, dictionary, solution, connection, givenSol, endCell) == True:
            return True

    # if recursion doesn't work
    solution.pop()
    return False

def getMazeSolutionConnections(n, startCell, endCell):
    mazeDict, solution = mazeSolverInTwoParts(n, startCell, endCell)
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

    # print(f'''
    #     Dict: {mazeDict}
    #     Sol: {solution}
    #     Conn: {connDict} 
    #     ''')
    # print(f'''
    #     Dict: {mazeDict}
    #     Sol: {solution}
    #     ''')

    return mazeDict, solution, connDict

def flipMazeDict(mazeDict):
    flippedDict = dict()

    for key in mazeDict:
        for point in mazeDict[key]:
            flippedDict[point] = [key]

    return flippedDict

# getMazeSolutionConnections(20, (0,0), (19,19))

getMazeSolutionConnections(20, (5,5), (12,9))

########################################
#   Santa Maze Game
#   Sarah Chen (sarahc2)
########################################
#   Maze & Solution Display
########################################
from mazeGenerationAndSolution import *
from cmu_112_graphics import *

def appStarted(app):
    app.n = 8 # 38+ has MVC Violation
    app.cellWidth = app.width / app.n
    app.cellHeight = app.height / app.n
    app.lineWidth = app.height / (app.n * 10)
    app.lineMargin = app.lineWidth * 2 / 5
    app.dotX = app.cellWidth / 2
    app.dotY = app.cellHeight / 2
    app.dotR = min(app.cellWidth, app.cellHeight) / 3
    app.dotStepSize = app.dotR / 2
    app.mazeDict, app.solution, app.connDict = getMazeSolutionConnections(app.n, (1,1), (4,2))
    app.showSolution = False

def keyPressed(app, event):
    if (event.key == 'Space'):
        app.showSolution = not app.showSolution
    elif (event.key == 'r'):
        appStarted(app)
    elif (event.key == 'Up'):
        possibleMoves = getPossibleMoves(app)
        if (app.dotY > app.dotStepSize) and ('Up' in possibleMoves):
            app.dotY -= app.dotStepSize
    elif (event.key == 'Down'):
        possibleMoves = getPossibleMoves(app)
        if ((app.dotY < app.height - app.dotStepSize) 
            and ('Down' in possibleMoves)):
            app.dotY += app.dotStepSize
    elif (event.key == 'Left'):
        possibleMoves = getPossibleMoves(app)
        if (app.dotX > app.dotStepSize) and ('Left' in possibleMoves):
            app.dotX -= app.dotStepSize
    elif (event.key == 'Right'):
        possibleMoves = getPossibleMoves(app)
        if ((app.dotX < app.width - app.dotStepSize) 
            and ('Right' in possibleMoves)):
            app.dotX += app.dotStepSize
 
def getPossibleMoves(app):
    # center and radius of dot
    cx, cy, r = app.dotX, app.dotY, app.dotR
    
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

    # bounds of cell that center of dot is in
    centerx0, centerx1, centery0, centery1 = getCellBounds(app,centerX,centerY)

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

    # for point in app.grinchSol:
    #     highlight(app, canvas, point)

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
