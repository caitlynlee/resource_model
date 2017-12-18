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
    mywin = visual.Window([1000,750], color=(0,0,0), colorSpace='rgb255', monitor="testMonitor")

    ### Instruction screen
    showInstructions(mywin, condition, 1)

    ### Run 1
    doTask(mywin, 1, condition)
    wait(mywin, 3)

    ## Instruction screen
    showInstructions(mywin, condition, 2)

    ### Run 2
    doTask(mywin, 2, condition)
    wait(mywin, 3)

    ## Instruction screen
    showInstructions(mywin, condition, 3)


    ### Run 3
    doTask(mywin, 3, condition)
    wait(mywin, 3)

    finish_text = "End"
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
    wait(mywin, 3)

    if condition == 1:
        if runNum < 3:
            trialText = str(runNum) + "/8"
        else:
            trialText = "3/3"

    if condition == 2:
        trialText = "1/1"

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
        go.draw()
        trial.draw()
        mywin.flip()
        core.wait(8)

        if event.getKeys():
            continuing = False

        stop.draw()
        trial.draw()
        mywin.flip()
        core.wait(5)

def wait(mywin, t):
    waitText = "+"
    wait = visual.TextStim(mywin, text=waitText, color=(255,255,255),
                                           colorSpace='rgb255', pos=(0,0),
                                           height=0.1)

    wait.draw()
    mywin.flip()
    core.wait(t)

def showInstructions(mywin, condition, interval):
    i1_8 = "FIRST SET OF INSTRUCTIONS FOR 8TRIAL CONDITION"
    i2_8 = "SECOND SET OF INSTRUCTIONS FOR 8TRIAL CONDITION"
    i3_8 = "THIRD SET OF INSTRUCTIONS FOR 8TRIAL CONDTION"

    i1_1 = "FIRST SET OF INSTRUCTIONS FOR 1TRIAL CONDITION"
    i2_1 = "SECOND SET OF INSTRUCTIONS FOR 1TRIAL CONDITION"
    i3_1 = "THIRD SET OF INSTRUCTIONS FOR 1TRIAL CONDTION"

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

    instruction_text.draw()
    mywin.flip()
    core.wait(15)