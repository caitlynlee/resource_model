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
    instructions = ("These are the directions la la la")
    instruction_text = visual.TextStim(mywin,text=instructions,
                                       color=(255,255,255), colorSpace='rgb255',
                                       pos=(0,100), height=20, units = 'pix',
                                       wrapWidth = 500)

    ready = False
    while not ready:
        instruction_text.draw()

        mywin.flip()
        if event.getKeys():
            ready = True


    ### Run 1
    doTask(mywin, 1, condition)
    wait(mywin, 3)

    ## Instruction screen
    instructions2 = ("These are the 2nd set of directions la la la more directions more more more directions more more more let's see if this wrap thing works la la la more more more ")
    instruction_text2 = visual.TextStim(mywin,text=instructions2,
                                       color=(255,255,255), colorSpace='rgb255',
                                       pos=(0,100), height=20, units = 'pix',
                                       wrapWidth = 500)

    ready = False
    while not ready:
        instruction_text2.draw()

        mywin.flip()
        if event.getKeys():
            ready = True

    ### Run 2
    doTask(mywin, 2, condition)
    wait(mywin, 3)

    ## Instruction screen
    instructions3 = ("These are the 3rd set of directions la la la more directions more more more directions more more more let's see if this wrap thing works la la la more more more ")
    instruction_text3 = visual.TextStim(mywin,text=instructions3,
                                       color=(255,255,255), colorSpace='rgb255',
                                       pos=(0,100), height=20, units = 'pix',
                                       wrapWidth = 500)

    ready = False
    while not ready:
        instruction_text3.draw()

        mywin.flip()
        if event.getKeys():
            ready = True


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


run(2)
