from __future__ import division

#import some libraries from PsychoPy
from psychopy import visual, core, event, data, sound
import os
import itertools
import random
import json

def run(condition):
    ###
    ### Do all the setting up
    ###

    #create a window
    mywin = visual.Window([1000,750], color=(0,0,0), colorSpace='rgb255')

    ### Instruction screen
    showInstructions(mywin, condition, 1, 0)

    ### Run 1
    doTask(mywin, 1, condition)
    if condition == 1:
        prop = 1/8
    else:
        prop = 1
    wait(mywin, 3, prop)

    ## Instruction screen
    if condition == 2:
        prop = 0
    showInstructions(mywin, condition, 2, prop)

    ### Run 2
    doTask(mywin, 2, condition)
    if condition ==1:
        prop = 2/8
    else:
        prop = 1
    wait(mywin, 3, prop)

    ## Instruction screen
    if condition == 2:
        prop = 0
    showInstructions(mywin, condition, 3, prop)

    ### Run 3
    doTask(mywin, 3, condition)
    wait(mywin, 3, 1)

    finish_text = "END"
    finish = visual.TextStim(mywin, text=finish_text, color=(255,255,255),
                                           colorSpace='rgb255', pos=(0,0),
                                           height=0.075)
    finish.draw()
    mywin.flip()
    core.wait(5)


    #cleanup
    mywin.close()
    core.quit()


def doTask(mywin, runNum, condition):
    if condition == 1:
        if runNum < 3:
            trialText = str(runNum) + "/8"
            prop = (runNum - 1)/8
        else:
            prop = 7/8
            trialText = "3/3"

    if condition == 2:
        prop = 0
        trialText = "1/1"

    wait(mywin, 3, prop)

    go_text = "GO"
    go = visual.TextStim(mywin, text=go_text, color=(255,255,255),
                                           colorSpace='rgb255', pos=(0,0),
                                           height=0.075)

    stop_text = "STOP"
    stop = visual.TextStim(mywin, text=stop_text, color=(255,255,255),
                                           colorSpace='rgb255', pos=(0,0),
                                           height=0.075)

    trial = visual.TextStim(mywin, text=trialText, color=(255,255,255),
                                           colorSpace='rgb255', pos=(0.8,0.8),
                                           height=0.075)


    continuing = True

    while continuing:
        if (random.random()) > 0.6:
            print("incrementing")
            if condition == 1:
                prop += (1/8)*(1/20)
            if condition == 2:
                prop += 1/20
            print("prop = " + str(prop))

        fillBar(mywin, prop)
        go.draw()
        trial.draw()
        mywin.flip()
        core.wait(5)

        if event.getKeys():
            continuing = False

        fillBar(mywin, prop)
        stop.draw()
        trial.draw()
        mywin.flip()
        core.wait(3)


def wait(mywin, t, prop):
    waitText = "+"
    wait = visual.TextStim(mywin, text=waitText, color=(255,255,255),
                                           colorSpace='rgb255', pos=(0,0),
                                           height=0.1)

    wait.draw()
    fillBar(mywin, prop)
    mywin.flip()
    core.wait(t)

def showInstructions(mywin, condition, interval, prop):
    i1_8 = "Thank you for agreeing to participate today. You will be asked to complete a series of tasks. The instructions on the screen will guide you through the process. Please pay close attention and try as hard as you can. \n\nThe first task is a grip strength task. Each time the screen says go, please grip the force meter as hard as you can and hold it for a few seconds (until the screen says STOP).\n\n There will be a bar at the bottom of the screen to indicate your progress through the study."
    i2_8 = "Reminder: each time the screen says go, please grip the force meter as hard as you can and hold it for a few seconds (until the screen says STOP)."
    i3_8 = "Reminder: each time the screen says go, please grip the force meter as hard as you can and hold it for a few seconds (until the screen says STOP)."

    i1_1 = "Thank you for agreeing to participate today. You will be asked to complete a series of tasks. The instructions on the screen will guide you through the process. Please pay close attention and try as hard as you can. \n\nThe first task is a grip strength task. Each time the screen says go, please grip the force meter as hard as you can and hold it for a few seconds (until the screen says STOP).\n\n There will be a bar at the bottom of the screen to indicate your progress through the study."
    i2_1 = "The next task is also a grip strength task. \n\nReminder: each time the screen says go, please grip the force meter as hard as you can and hold it for a few seconds (until the screen says STOP)."
    i3_1 = "The next task is also a grip strength task. \n\nReminder: each time the screen says go, please grip the force meter as hard as you can and hold it for a few seconds (until the screen says STOP)."

    if condition == 1:
        if interval == 1: instructions = i1_8
        if interval == 2: instructions = i2_8
        if interval == 3: instructions = i3_8

    if condition == 2:
        if interval == 1: instructions = i1_1
        if interval == 2: instructions = i2_1
        if interval == 3: instructions = i3_1

    instruction_text = visual.TextStim(mywin,text=instructions,
                                       color=(255,255,255), colorSpace='rgb255',
                                       pos=(0,100), height=20, units = 'pix',
                                       wrapWidth = 500)

    emptyBar = visual.Rect(mywin, width=500, height=20, units='pix',
                                  lineColor=(255,255,255), lineColorSpace='rgb255',
                                  pos=(0,-220), fillColor = (0,0,0),
                                  fillColorSpace = 'rgb255')

    instruction_text.draw()

    fillBar(mywin, prop)

    mywin.flip()
    core.wait(15)


def fillBar(mywin, prop):
    emptyBar = visual.Rect(mywin, width=500, height=20, units='pix',
                                  lineColor=(255,255,255), lineColorSpace='rgb255',
                                  pos=(0,-220), fillColor = (0,0,0),
                                  fillColorSpace = 'rgb255')

    fill =  visual.Rect(mywin, width=500*prop, height=20, units='pix',
                                  lineColor=(255,255,255), lineColorSpace='rgb255',
                                  pos=(-250+(prop*500)/2,-220), fillColor = (255,255,255),
                                  fillColorSpace = 'rgb255')

    emptyBar.draw()
    fill.draw()
