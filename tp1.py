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
        app.titleScreenMode = TitleScreenMode()
        app.avatarMode = AvatarMode()
        app.storyMode = StoryMode()
        app.setActiveMode(app.titleScreenMode)

class TitleScreenMode(Mode):
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
            mode.app.setActiveMode(mode.app.storyMode)
    
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

class StoryMode(Mode):
    def appStarted(mode):
        mode.titleColor = 'black'
        mode.backButtonColor = mode.storyButtonColor = 'sea green'
        mode.backButtonTextColor = mode.storyButtonTextColor = 'white'

    def mousePressed(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.titleScreenMode)
            mode.backButtonColor = 'sea green'
            mode.backButtonTextColor = 'white'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.avatarMode)
            mode.nextButtonColor = 'sea green'
            mode.nextButtonTextColor = 'white'

    def mouseMoved(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.backButtonColor = 'white'
            mode.backButtonTextColor = 'sea green'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.storyButtonColor = 'white'
            mode.storyButtonTextColor = 'sea green'
        elif (((event.x < 50) or ((event.x > 150) 
            and (event.x < mode.width-150)) or (event.x > mode.width-50))
            and ((event.y < 50) or (event.y > 100))):
            mode.backButtonColor = mode.storyButtonColor = 'sea green'
            mode.backButtonTextColor = mode.storyButtonTextColor = 'white'
    
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
                            fill=mode.storyButtonColor)
        canvas.create_text(mode.width-100, 75,
                            fill=mode.storyButtonTextColor,
                            text='Next', 
                            font='PlayfairDisplay 16 bold')

class AvatarMode(StoryMode):
    # def appStarted(mode):
    #     mode.titleColor = 'black'
    #     mode.backButtonColor = mode.storyButtonColor = 'sea green'
    #     mode.backButtonTextColor = mode.storyButtonTextColor = 'white'

    def mousePressed(mode, event):
        if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.storyMode)
            mode.backButtonColor = 'sea green'
            mode.backButtonTextColor = 'white'
        elif ((mode.width-150 <= event.x <= mode.width-50) 
            and (50 <= event.y <= 100)):
            mode.app.setActiveMode(mode.app.titleScreenMode)
            mode.storyButtonColor = 'sea green'
            mode.storyButtonTextColor = 'white'
    
    # def mouseMoved(mode, event):
    #     if ((50 <= event.x <= 150) and (50 <= event.y <= 100)):
    #         mode.backButtonColor = 'white'
    #         mode.backButtonTextColor = 'sea green'
    #     elif ((mode.width-150 <= event.x <= mode.width-50) 
    #         and (50 <= event.y <= 100)):
    #         mode.storyButtonColor = 'white'
    #         mode.storyButtonTextColor = 'sea green'
    #     elif (((event.x < 50) or ((event.x > 150) 
    #         and (event.x < mode.width-150)) or (event.x > mode.width-50))
    #         and ((event.y < 50) or (event.y > 100))):
    #         mode.backButtonColor = mode.storyButtonColor = 'sea green'
    #         mode.backButtonTextColor = mode.storyButtonTextColor = 'white'

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
        ### 'Next' button
        canvas.create_rectangle(mode.width-50, 50, mode.width-150, 100,
                            fill=mode.storyButtonColor)
        canvas.create_text(mode.width-100, 75,
                            fill=mode.storyButtonTextColor,
                            text='Next', 
                            font='PlayfairDisplay 16 bold')

MyApp(width=1000, height=800)
