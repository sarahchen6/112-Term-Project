########################################
#   Santa Maze Game (main.py)
#   Author: Sarah Chen (sarahc2)
########################################
#   Combine gameScreens and mazeModes
########################################
#
#   Citations: 
#   1)  incorporated subclassing ModalApp and Mode idea from
#       https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
#
########################################
from gameScreens import *
from mazeModes import *

class MyApp(ModalApp):
    def appStarted(app):
        # from gameScreens
        app.titleScreen = TitleScreen()
        app.backgroundScreen = BackgroundScreen()
        app.instructionsScreen = InstructionsScreen()
        app.sleighScreen = SleighScreen()
        app.finalScreen = FinalScreen()
        app.setActiveMode(app.titleScreen)

        # from mazeModes
        app.maze = Maze()
        app.radiusMode = RadiusMode()
        app.grinchMode = GrinchMode()
        app.presents = 100
        app.finalPresents = 100
        app.timeSec = 0
        app.timeMin = 0

        app.timerMode = True
        app.timerDelay = 10

    def timerFired(app):
        app._activeMode.timerFired()



MyApp(width=1000, height=800)

########################################
#   Santa Maze Game (gameScreens.py)
#   Author: Sarah Chen (sarahc2)
########################################
#   Game Screens
########################################
from cmu_112_graphics import *

class TitleScreen(Mode):
    def appStarted(mode):
        mode.buttonColor = 'sea green'
        mode.buttonTextColor = 'white'

    def mousePressed(mode, event):
        if ((mode.width/2-150 <= event.x <= mode.width/2+150) 
            and (mode.height*2/3-50 <= event.y <= mode.height*2/3+50)):
            mode.app.setActiveMode(mode.app.backgroundScreen)
            mode.homeButtonColor = 'sea green'
            mode.homeButtonTextColor = 'white'
    
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
        # title
        canvas.create_text(mode.width/2, mode.height/3-50,
                            fill='firebrick4',
                            text='Ho Ho Home', 
                            font='PlayfairDisplay 120 bold')
        canvas.create_text(mode.width/2, mode.height/3+50,
                            fill='firebrick4',
                            text='the Santa Maze Game', 
                            font='PlayfairDisplay 50 bold')
        # 'Let's Begin' button
        canvas.create_rectangle(mode.width/2-150, mode.height*2/3-50,
                            mode.width/2+150, mode.height*2/3+50,
                            fill=mode.buttonColor)
        canvas.create_text(mode.width/2, mode.height*2/3,
                            fill=mode.buttonTextColor,
                            text='Let\'s Begin', 
                            font='PlayfairDisplay 40 bold')

class BackgroundScreen(Mode):
    def appStarted(mode):
        mode.titleColor = 'black'
        mode.homeButtonColor = mode.nextButtonColor = 'sea green'
        mode.homeButtonTextColor = mode.nextButtonTextColor = 'white'
        mode.backgroundText = '''It's the last few hours of Christmas Eve, and 
there are only a couple more presents left to be 
delivered. Unfortunately, Santa’s reindeer just 
contracted a novel XMAS-20 virus that can only 
affect reindeer (don’t worry, all of them are 
showing positive signs of recovery), and they 
can’t help Santa deliver the last 100 presents! 
Even though Rudolf told him the fastest way, 
Santa immediately forgot and must now figure out 
his way to town on his own. Help Santa redeem his 
bad memory by following the instructions on the 
next slide, and prove to the world that Santa 
still has what it takes to deliver presents to 
every last kid!'''

    def mousePressed(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.titleScreen)
            mode.homeButtonColor = 'sea green'
            mode.homeButtonTextColor = 'white'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.instructionsScreen)
            mode.nextButtonColor = 'sea green'
            mode.nextButtonTextColor = 'white'
    
    def mouseMoved(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.homeButtonColor = 'white'
            mode.homeButtonTextColor = 'sea green'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.nextButtonColor = 'white'
            mode.nextButtonTextColor = 'sea green'
        elif (((event.x < 50) or ((event.x > 150) 
            and (event.x < mode.width-150)) or (event.x > mode.width-50))
            or ((event.y < 50) or (event.y > 100))):
            mode.homeButtonColor = mode.nextButtonColor = 'sea green'
            mode.homeButtonTextColor = mode.nextButtonTextColor = 'white'

    def redrawAll(mode, canvas):
        # title
        canvas.create_text(mode.width/2, mode.height/10,
                            fill=mode.titleColor,
                            text='Background', 
                            font='PlayfairDisplay 64 bold')
        # 'Home' button
        canvas.create_rectangle(50, 50, 150, 100,
                            fill=mode.homeButtonColor)
        canvas.create_text(100, 75,
                            fill=mode.homeButtonTextColor,
                            text='Home', 
                            font='PlayfairDisplay 16 bold')
        # 'Next' button
        canvas.create_rectangle(mode.width-50, 50, mode.width-150, 100,
                            fill=mode.nextButtonColor)
        canvas.create_text(mode.width-100, 75,
                            fill=mode.nextButtonTextColor,
                            text='Next', 
                            font='PlayfairDisplay 16 bold')
        # background text
        canvas.create_text(mode.width/2, mode.height/2+50,
                            fill='black',
                            text=mode.backgroundText, 
                            font='PlayfairDisplay 30')

class InstructionsScreen(BackgroundScreen):
    def appStarted(mode):
        mode.titleColor = 'black'
        mode.backButtonColor = mode.nextButtonColor = 'sea green'
        mode.backButtonTextColor = mode.nextButtonTextColor = 'white'
        mode.instructionsText = '''Navigate Santa's sleigh through the maze by using the 'Up', 
'Down', 'Left', and 'Right' arrow keys and get him from the North 
Pole to the first chimney in town as fast as you can. Every extra 
minute you take, Santa will lose 10 presents from his initial 100!

Hints:
- If the Grinch finds Santa, he will be sure to steal as many 
presents as he can so long as Santa's sleigh is in his reach.
Though Santa's sleigh moves faster than the Grinch, the Grinch
can cut corners by moving diagonally.
- Press the ‘Space’ bar to “call a telephone line back to the 
knowledgable reindeer” who will reveal Santa’s ideal route 
through a series of dots.
- Press keys '1' through '7' to regenerate the maze. A higher
number implies a higher maze complexity.
- Press the 'r' key to restart the maze.

Proceed to the next page to choose Santa’s sleigh and begin. 
Hurry - you’re running out of time!'''

    def mousePressed(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.backgroundScreen)
            mode.backButtonColor = 'sea green'
            mode.backButtonTextColor = 'white'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.sleighScreen)
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
        # title
        canvas.create_text(mode.width/2, mode.height/10,
                            fill=mode.titleColor,
                            text='Instructions', 
                            font='PlayfairDisplay 64 bold')
        # 'Back' button
        canvas.create_rectangle(50, 50, 150, 100,
                            fill=mode.backButtonColor)
        canvas.create_text(100, 75,
                            fill=mode.backButtonTextColor,
                            text='Back', 
                            font='PlayfairDisplay 16 bold')
        # 'Next' button
        canvas.create_rectangle(mode.width-50, 50, mode.width-150, 100,
                            fill=mode.nextButtonColor)
        canvas.create_text(mode.width-100, 75,
                            fill=mode.nextButtonTextColor,
                            text='Next', 
                            font='PlayfairDisplay 16 bold')
        # instructions text
        canvas.create_text(mode.width/2, mode.height/2+50,
                            fill='black',
                            text=mode.instructionsText, 
                            font='PlayfairDisplay 27')

class SleighScreen(BackgroundScreen):
    def appStarted(mode):
        mode.titleColor = 'black'
        mode.backButtonColor = mode.nextButtonColor = 'sea green'
        mode.backButtonTextColor = mode.nextButtonTextColor = 'white'
        mode.mode1ButtonColor = mode.mode2ButtonColor = mode.mode3ButtonColor = 'sea green'
        mode.mode1ButtonTextColor = mode.mode2ButtonTextColor = mode.mode3ButtonTextColor = 'white'
        mode.mode1Title = '''                  Sleigh 1:
No Presents, Just Vibes'''
        mode.mode1Text = '''Santa accidentally forgot 
all his presents back at the North 
Pole. He has decided to cut his 
losses and just vibe his way to 
town (no timer). Fortunately, this 
means that Santa has nothing the 
Grinch wants, so the Grinch will 
stay home this Eve. Though the 
kids will be left empty-handed, 
sometimes Santa just needs to 
prioritize his own self care. 
Hopefully he can come up with a 
good excuse on the way though…'''
        mode.mode2Title = '''          Sleigh 2:
Will Pay To Take'''
        mode.mode2Text = '''Santa Will Pay you To Take 
this sleigh. Pros: not even the 
Grinch can be bothered by this 
sleigh, so he will not be chasing 
after Santa. Cons: Absolutely no 
visibility. Cannot see anything.
Note that Santa is smart enough
to take a flashlight with this 
sleigh. Turn up his flashlight and
make his visibility range Bigger 
by pressing the 'b' key. Make 
his visibility range Smaller by 
pressing the 's' key.'''
        mode.mode3Title = '''                      Sleigh 3:
2021 Christmas Corvette'''
        mode.mode3Text = '''Santa is now “that car guy,” 
and has finally invested in the 
shiniest! newest! cleanest! 2021 
Christmas Corvette. This sleigh of 
beauty has the highest visibility 
known to all car dudes (i.e. she, 
the car, can see the whole maze); 
However, Santa needs to be careful 
if he chooses this sleigh - not only 
because he’s a bad driver and 
doesn’t want to scrape her, but 
also because she’ll attract …the 
Grinch! (who will steal his presents)'''

    def mouseMoved(mode, event):
        # 'Back' and 'Home' button toggle
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
        # 'Play Sleigh 1' button toggle
        if ((mode.width/6-100 <= event.x <= mode.width/6+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.mode1ButtonColor = 'white'
            mode.mode1ButtonTextColor = 'sea green'
        elif ((event.x < mode.width/4-100) or (event.x > mode.width/4+100)
            or (event.y < mode.height*9/10-50) 
            or (event.y < mode.height*9/10+50)):
            mode.mode1ButtonColor = 'sea green'
            mode.mode1ButtonTextColor = 'white'
        # 'Play Sleigh 2' button toggle
        if ((mode.width/2-100 <= event.x <= mode.width/2+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.mode2ButtonColor = 'white'
            mode.mode2ButtonTextColor = 'sea green'
        elif ((event.x < mode.width/2-100) or (event.x > mode.width/2+100)
            or (event.y < mode.height*9/10-50) 
            or (event.y < mode.height*9/10+50)):
            mode.mode2ButtonColor = 'sea green'
            mode.mode2ButtonTextColor = 'white'
        # 'Play Sleigh 3' button toggle
        if ((mode.width*5/6-100 <= event.x <= mode.width*5/6+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.mode3ButtonColor = 'white'
            mode.mode3ButtonTextColor = 'sea green'
        elif ((event.x < mode.width*3/4-100) or (event.x > mode.width*3/4+100)
            or (event.y < mode.height*9/10-50) 
            or (event.y < mode.height*9/10+50)):
            mode.mode3ButtonColor = 'sea green'
            mode.mode3ButtonTextColor = 'white'

    def mousePressed(mode, event):
        # 'Back' button
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.instructionsScreen)
            mode.backButtonColor = 'sea green'
            mode.backButtonTextColor = 'white'
        # 'Home' button
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.titleScreen)
            mode.nextButtonColor = 'sea green'
            mode.nextButtonTextColor = 'white'
        # 'Play Sleigh 1' button
        elif ((mode.width/6-100 <= event.x <= mode.width/6+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.app.timeSec = 0
            mode.app.timeMin = 0
            mode.app.setActiveMode(mode.app.maze) 
            mode.mode1ButtonColor = 'sea green'
            mode.mode1ButtonTextColor = 'white'
        # 'Play Sleigh 2' button
        elif ((mode.width/2-100 <= event.x <= mode.width/2+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.app.presents = 100
            mode.app.setActiveMode(mode.app.radiusMode) 
            mode.mode2ButtonColor = 'sea green'
            mode.mode2ButtonTextColor = 'white'
        # 'Play Sleigh 3' button
        elif ((mode.width*5/6-100 <= event.x <= mode.width*5/6+100) 
            and (mode.height*9/10-50 <= event.y <= mode.height*9/10+50)):
            mode.app.presents = 100
            mode.app.setActiveMode(mode.app.grinchMode) 
            mode.mode3ButtonColor = 'sea green'
            mode.mode3ButtonTextColor = 'white'

    def redrawAll(mode, canvas):
        # title
        canvas.create_text(mode.width/2, mode.height/10,
                            fill=mode.titleColor,
                            text='Choose Your Sleigh', 
                            font='PlayfairDisplay 64 bold')
        # 'Back' button
        canvas.create_rectangle(50, 50, 150, 100,
                            fill=mode.backButtonColor)
        canvas.create_text(100, 75,
                            fill=mode.backButtonTextColor,
                            text='Back', 
                            font='PlayfairDisplay 16 bold')
        # 'Home' button
        canvas.create_rectangle(mode.width-50, 50, mode.width-150, 100,
                            fill=mode.nextButtonColor)
        canvas.create_text(mode.width-100, 75,
                            fill=mode.nextButtonTextColor,
                            text='Home', 
                            font='PlayfairDisplay 16 bold')
        # Sleigh 1
        canvas.create_rectangle(mode.width/6-100, mode.height*9/10-50, 
                            mode.width/6+100, mode.height*9/10+50,
                            fill=mode.mode1ButtonColor)
        canvas.create_text(mode.width/6, mode.height*9/10,
                            fill=mode.mode1ButtonTextColor,
                            text='Sleigh 1', 
                            font='PlayfairDisplay 35 bold')
        canvas.create_text(mode.width/6, mode.height/5,
                            fill='firebrick4',
                            text=mode.mode1Title, 
                            font='PlayfairDisplay 25 bold')
        canvas.create_text(mode.width/6, mode.height*3/5,
                            fill='black',
                            text=mode.mode1Text, 
                            font='PlayfairDisplay 15')
        # Sleigh 2
        canvas.create_rectangle(mode.width/2-100, mode.height*9/10-50, 
                            mode.width/2+100, mode.height*9/10+50,
                            fill=mode.mode2ButtonColor)
        canvas.create_text(mode.width/2, mode.height*9/10,
                            fill=mode.mode2ButtonTextColor,
                            text='Sleigh 2', 
                            font='PlayfairDisplay 35 bold')
        canvas.create_text(mode.width/2, mode.height/5,
                            fill='firebrick4',
                            text=mode.mode2Title, 
                            font='PlayfairDisplay 25 bold')
        canvas.create_text(mode.width/2, mode.height*3/5,
                            fill='black',
                            text=mode.mode2Text, 
                            font='PlayfairDisplay 15')
        # Sleigh 3
        canvas.create_rectangle(mode.width*5/6-100, mode.height*9/10-50, 
                            mode.width*5/6+100, mode.height*9/10+50,
                            fill=mode.mode3ButtonColor)
        canvas.create_text(mode.width*5/6, mode.height*9/10,
                            fill=mode.mode3ButtonTextColor,
                            text='Sleigh 3', 
                            font='PlayfairDisplay 35 bold')
        canvas.create_text(mode.width*5/6, mode.height/5,
                            fill='firebrick4',
                            text=mode.mode3Title, 
                            font='PlayfairDisplay 25 bold')
        canvas.create_text(mode.width*5/6, mode.height*3/5,
                            fill='black',
                            text=mode.mode3Text, 
                            font='PlayfairDisplay 15')

class FinalScreen(SleighScreen):
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
        elif ((event.x < mode.width/2-200) or (event.x > mode.width/2+200)
            or (event.y < mode.height*7/10-50) 
            or (event.y > mode.height*7/10+50)):
            mode.playAgainButtonColor = 'sea green'
            mode.playAgainButtonTextColor = 'white'
        if ((mode.width/2-50 <= event.x <= mode.width/2+50) 
            and (mode.height*9/10-25 <= event.y <= mode.height*9/10+25)):
            mode.homeButtonColor = 'black'
            mode.homeButtonTextColor = 'gray'
        elif ((event.x < mode.width/2-50) or (event.x > mode.width/2+50)
            or (event.y < mode.height*9/10-25) 
            or (event.y > mode.height*9/10+25)):
            mode.homeButtonColor = 'gray'
            mode.homeButtonTextColor = 'black'

    def mousePressed(mode, event):
        # 'Play Again' button
        if ((mode.width/2-200 <= event.x <= mode.width/2+200) 
            and (mode.height*7/10-50 <= event.y <= mode.height*7/10+50)):
            mode.app.presents = 0
            mode.app.setActiveMode(mode.app.sleighScreen)
            mode.playAgainButtonColor = 'sea green'
            mode.playAgainButtonTextColor = 'white'
        # 'Home' button
        elif ((mode.width/2-50 <= event.x <= mode.width/2+50) 
            and (mode.height*9/10-25 <= event.y <= mode.height*9/10+25)):
            mode.app.presents = 0
            mode.app.setActiveMode(mode.app.titleScreen)
            mode.homeButtonColor = 'gray'
            mode.homeButtonTextColor = 'black'

    def redrawAll(mode, canvas):
        # title
        canvas.create_text(mode.width/2, mode.height*3/10,
                            fill=mode.titleColor,
                            text='Congrats!', 
                            font='PlayfairDisplay 64 bold')
        canvas.create_text(mode.width/2, mode.height*4/10,
                            fill=mode.titleColor,
                            text=f'You successfully delivered {int(mode.app.finalPresents)} presents', 
                            font='PlayfairDisplay 40 bold')
        # 'Play Again' button
        canvas.create_rectangle(mode.width/2-200, mode.height*7/10-50, 
                            mode.width/2+200, mode.height*7/10+50,
                            fill=mode.playAgainButtonColor)
        canvas.create_text(mode.width/2, mode.height*7/10,
                            fill=mode.playAgainButtonTextColor,
                            text='Play Again', 
                            font='PlayfairDisplay 40 bold')
        # 'Home' button
        canvas.create_rectangle(mode.width/2-50, mode.height*9/10-25, 
                            mode.width/2+50, mode.height*9/10+25,
                            fill=mode.homeButtonColor)
        canvas.create_text(mode.width/2, mode.height*9/10,
                            fill=mode.homeButtonTextColor,
                            text='Home', 
                            font='PlayfairDisplay 20 bold')

########################################
#   Santa Maze Game (mazeModes.py)
#   Author: Sarah Chen (sarahc2)
########################################
#   Maze Modes
########################################
from mazeGenerationAndSolution import *
from cmu_112_graphics import *

class Maze(Mode):
    def appStarted(mode):
        # maze display
        mode.n = 10 # 38+ has MVC Violation
        mode.mazeDict = generateMazeDict(mode.n)
        mode.solution, mode.connDict = getMazeSolutionConnections(mode.n, mode.mazeDict, (0,0), (mode.n-1,mode.n-1))
        mode.cellWidth = mode.width / mode.n
        mode.cellHeight = mode.height / mode.n
        mode.lineWidth = mode.height / (mode.n * 10)
        mode.lineMargin = mode.lineWidth * 2 / 5
        mode.showSolution = False
        mode.visibilityR = 17
        mode.mazeFontSize = int(min(mode.cellWidth, mode.cellHeight) / 3)

        # sleigh
        mode.dotX = mode.cellWidth + mode.cellWidth / 2
        mode.dotY = mode.cellHeight / 2
        mode.dotR = min(mode.cellWidth, mode.cellHeight) / 10
        mode.dotStepSize = mode.dotR / 2
        sleighURL = 'https://www.pngarts.com/files/3/Santa-Sleigh-PNG-Background-Image.png'
        mode.sleigh = mode.loadImage(sleighURL)
        mode.sleighResized = mode.scaleImage(mode.sleigh, mode.cellWidth / 1000)

        # grinch
        mode.grinchX = mode.width - mode.cellWidth / 2
        mode.grinchY = mode.cellHeight / 2
        mode.grinchR = min(mode.cellWidth, mode.cellHeight) / 10
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
        mode.mazeDict = generateMazeDict(mode.n)
        mode.solution, mode.connDict = getMazeSolutionConnections(mode.n, mode.mazeDict, (0,0), (mode.n-1,mode.n-1))
        mode.cellWidth = mode.width / mode.n
        mode.cellHeight = mode.height / mode.n
        mode.lineWidth = mode.height / (mode.n * 10)
        mode.lineMargin = mode.lineWidth * 2 / 5
        mode.showSolution = False
        mode.visibilityR = 5
        mode.mazeFontSize = int(min(mode.cellWidth, mode.cellHeight) / 3)
        mode.app.timeMin = 0
        mode.app.timeSec = 0
        if (mode.app._activeMode == mode.app.maze):
            mode.app.presents = 0
        else:
            mode.app.presents = 100

        # sleigh
        mode.dotX = mode.cellWidth + mode.cellWidth / 2
        mode.dotY = mode.cellHeight / 2
        mode.dotR = min(mode.cellWidth, mode.cellHeight) / 3
        mode.dotStepSize = mode.dotR / 2
        mode.sleighResized = mode.scaleImage(mode.sleigh, mode.cellWidth / 1000)

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
            mode.visibilityR += 3
        elif (event.key == 's'):
            if (mode.visibilityR > 0):
                mode.visibilityR -= 3
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
            Maze.resetTimer(mode)
            mode.app.finalPresents = mode.app.presents
            Maze.restartMaze(mode)
            mode.app.setActiveMode(mode.app.finalScreen)

    def resetTimer(mode):
        mode.app.timerMode = False
        mode.app.timeSec = 0
        mode.app.timeMin = 0
    
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
        centerx0, centerx1, centery0, centery1 = Maze.getCellBounds(mode, centerX, centerY)

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

        for point in mode.connDict:
            x, y = point
            abovePoint = (x, y-1)
            belowPoint = (x, y+1)
            leftPoint = (x-1, y)
            rightPoint = (x+1, y)
            if (abovePoint not in mode.connDict[point]):
                Maze.drawAboveLine(mode, canvas, point)
            if (belowPoint not in mode.connDict[point]):
                Maze.drawBelowLine(mode, canvas, point)
            if (leftPoint not in mode.connDict[point]):
                Maze.drawLeftLine(mode, canvas, point)
            if (rightPoint not in mode.connDict[point]):
                Maze.drawRightLine(mode, canvas, point)

        # sleigh
        canvas.create_oval(mode.dotX - mode.dotR, mode.dotY - mode.dotR,
                        mode.dotX + mode.dotR, mode.dotY + mode.dotR, 
                        fill='white', outline='')
        canvas.create_image(mode.dotX, mode.dotY, 
                        image=ImageTk.PhotoImage(mode.sleighResized))

        # north pole, chimney
        canvas.create_image(mode.cellWidth / 2, mode.cellHeight / 2, 
                        image=ImageTk.PhotoImage(mode.northPoleResized))
        canvas.create_image(mode.width - mode.cellWidth / 2, 
                        mode.height - mode.cellHeight / 2,
                        image=ImageTk.PhotoImage(mode.chimneyResized))

class RadiusMode(Maze):
    def timerFired(mode):
        mode.app.timeSec += 0.03
        if (mode.app.timeSec >= 60):
            mode.app.timeMin += 1
            if (mode.app.presents >= 10):
                mode.app.presents -= 10
        mode.app.timeSec %= 60

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

        # sleigh
        canvas.create_oval(mode.dotX - mode.dotR, mode.dotY - mode.dotR,
                        mode.dotX + mode.dotR, mode.dotY + mode.dotR, 
                        fill='white', outline='')
        canvas.create_image(mode.dotX, mode.dotY, 
                        image=ImageTk.PhotoImage(mode.sleighResized))

        # time, presents label
        canvas.create_text(mode.width - 20, 20, fill='green', 
                        text=f'Time: {mode.app.timeMin}m {int(mode.app.timeSec)}s',
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
        mode.app.timeSec += 0.03
        if (mode.app.timeSec >= 60):
            mode.app.timeMin += 1
            if (mode.app.presents >= 10):
                mode.app.presents -= 10
        mode.app.timeSec %= 60
        
        GrinchMode.checkSleighGrinchIntersect(mode)
        GrinchMode.moveGrinch(mode)

    def checkSleighGrinchIntersect(mode):
        sleighX, sleighY = Maze.getCell(mode, mode.dotX, mode.dotY)
        grinchX, grinchY = Maze.getCell(mode, mode.grinchX, mode.grinchY)
        if ((sleighX, sleighY) == (grinchX, grinchY)) and (mode.app.presents > 0):
            mode.app.presents -= 0.1

    def moveGrinch(mode):
        sleighX, sleighY = Maze.getCell(mode, mode.dotX, mode.dotY)
        grinchCellX, grinchCellY = Maze.getCell(mode, mode.grinchX, mode.grinchY)
        grinchR, grinchB = Maze.getCell(mode, mode.grinchX + mode.grinchR, mode.grinchY + mode.grinchR)
        grinchL, grinchT = Maze.getCell(mode, mode.grinchX - mode.grinchR, mode.grinchY - mode.grinchR)
        grinchSol, grinchConn = getMazeSolutionConnections(mode.n, mode.mazeDict, (grinchCellX, grinchCellY), (sleighX, sleighY))
        try:
            if (len(grinchSol) >= 5) and (grinchSol[0] == grinchSol[3]):
                newCellX, newCellY = grinchSol[4]
            else:
                newCellX, newCellY = grinchSol[1]
        except:
            newCellX, newCellY = grinchSol[0]

        # find coordinates of grinchCellX, grinchCellY, newCellX, newCellY
        grinchCellXCoord = grinchCellX * mode.cellWidth + mode.cellWidth / 2
        grinchCellYCoord = grinchCellY * mode.cellHeight + mode.cellHeight / 2
        newCellXCoord = newCellX * mode.cellWidth + mode.cellWidth / 2
        newCellYCoord = newCellY * mode.cellHeight + mode.cellHeight / 2

        # move grinch to center of cell or to center of next cell
        if (grinchCellX + 1 == newCellX):
            if (grinchCellXCoord-1 < mode.grinchX <= newCellXCoord+1):
                GrinchMode.moveGrinchTowardsPoint(mode, newCellXCoord, newCellYCoord)
            else:
                GrinchMode.moveGrinchTowardsPoint(mode, grinchCellXCoord, grinchCellYCoord)
        elif (grinchCellX - 1 == newCellX):
            if (newCellXCoord-1 <= mode.grinchX < grinchCellXCoord+1):
                GrinchMode.moveGrinchTowardsPoint(mode, newCellXCoord, newCellYCoord)
            else:
                GrinchMode.moveGrinchTowardsPoint(mode, grinchCellXCoord, grinchCellYCoord)
        elif (grinchCellY + 1 == newCellY):
            if (grinchCellYCoord-1 < mode.grinchY <= newCellYCoord+1):
                GrinchMode.moveGrinchTowardsPoint(mode, newCellXCoord, newCellYCoord)
            else:
                GrinchMode.moveGrinchTowardsPoint(mode, grinchCellXCoord, grinchCellYCoord)
        elif (grinchCellY - 1 == newCellY):
            if (newCellYCoord-1 <= mode.grinchY < grinchCellYCoord+1):
                GrinchMode.moveGrinchTowardsPoint(mode, newCellXCoord, newCellYCoord)
            else:
                GrinchMode.moveGrinchTowardsPoint(mode, grinchCellXCoord, grinchCellYCoord)
        
    def moveGrinchTowardsPoint(mode, x, y):
        if (mode.grinchX > x):
            mode.grinchX -= 1
        elif (mode.grinchX < x):
            mode.grinchX += 1
        if (mode.grinchY > y):
            mode.grinchY -= 1
        elif (mode.grinchY < y):
            mode.grinchY += 1

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

        # sleigh
        canvas.create_oval(mode.dotX - mode.dotR, mode.dotY - mode.dotR,
                        mode.dotX + mode.dotR, mode.dotY + mode.dotR, 
                        fill='white', outline='')
        canvas.create_image(mode.dotX, mode.dotY, 
                        image=ImageTk.PhotoImage(mode.sleighResized))

        # grinch
        canvas.create_oval(mode.grinchX - mode.grinchR, mode.grinchY - mode.grinchR,
                        mode.grinchX + mode.grinchR, mode.grinchY + mode.grinchR,
                        fill='white', outline='')
        canvas.create_image(mode.grinchX, mode.grinchY, 
                        image=ImageTk.PhotoImage(mode.grinchResized))

        # time, presents label
        canvas.create_text(mode.width - 20, 20, fill='green', 
                        text=f'Time: {mode.app.timeMin}m {int(mode.app.timeSec)}s',
                        anchor='ne',
                        font='PlayfairDisplay 40 bold')
        canvas.create_text(mode.width - 20, 60, fill='green', 
                        text=f'Presents: {int(mode.app.presents)}',
                        anchor='ne',
                        font='PlayfairDisplay 40 bold')

        # north pole, chimney
        canvas.create_image(mode.cellWidth / 2, mode.cellHeight / 2, 
                        image=ImageTk.PhotoImage(mode.northPoleResized))
        canvas.create_image(mode.width - mode.cellWidth / 2, 
                        mode.height - mode.cellHeight / 2,
                        image=ImageTk.PhotoImage(mode.chimneyResized))

########################################
#   Santa Maze Game (mazeGenerationAndSolution.py)
#   Author: Sarah Chen (sarahc2)
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

def mazeSolver(n, mazeDict, startCell, endCell):
    flippedDict = flipMazeDict(mazeDict)
    solution = [startCell]
    lastPoint = mazeDict[startCell][0]
    mazeSolverHelper(n, mazeDict, solution, lastPoint, endCell)
    if (len(solution) == 1):
        mazeSolverHelper(n, flippedDict, solution, lastPoint, endCell)
    return flippedDict, solution

def mazeSolverInTwoParts(n, mazeDict, startCell, endCell):
    # get maze dictionary, flipped maze dictionary, and solution list from UL to BR
    flippedDict, solution = mazeSolver(n, mazeDict, (0,0), (n-1,n-1))

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

    # combine firstSol and secondSol to get finalSol
    finalSol = []
    for i in range(len(firstSol)):
        for j in range(len(secondSol)):
            if (firstSol[i] == secondSol[j]):
                firstHalf = firstSol[:i]
                secondHalf = secondSol[:j+1]
                secondHalf.reverse()
                finalSol.extend(firstHalf)
                finalSol.extend(secondHalf)
                break
        if len(finalSol) != 0:
            break

    # get rid of extras at end of finalSol
    for i in range(len(finalSol)):
        if (finalSol[i] == endCell):
            if (i == len(finalSol)-1):
                break
            finalSol = finalSol[:i+1]
            break

    return finalSol

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

def getMazeSolutionConnections(n, mazeDict, startCell, endCell):
    solution = mazeSolverInTwoParts(n, mazeDict, startCell, endCell)
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

    return solution, connDict

def flipMazeDict(mazeDict):
    flippedDict = dict()

    for key in mazeDict:
        for point in mazeDict[key]:
            flippedDict[point] = [key]

    return flippedDict
