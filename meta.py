#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on qui 24 out 2019 17:40:17 -03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'meta'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/weverson/Documentos/codes/mooneyFaceMetaExp/meta.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "tela_inicial"
tela_inicialClock = core.Clock()
texto_tela_inicial = visual.TextStim(win=win, name='texto_tela_inicial',
    text='Bem vindo ao experimento de metacognição com faces de Mooney.\nVocê verá uma sequência de duas imagens e, após vê-las, deverá responder em qual das duas reconhece uma face humana. Apenas uma delas contém uma face.\nApós isso, você deverá informar uma estimativa da sua confiança na resposta, em uma escala de 1 a 5.\nPressione a tecla “Espaço” do seu teclado para prosseguir.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ti = keyboard.Keyboard()

# Initialize components for Routine "instrucao_resposta"
instrucao_respostaClock = core.Clock()
text_ir = visual.TextStim(win=win, name='text_ir',
    text='Pressione "1" ou "2" caso você reconheça a face humana na primeira ou segunda imagem, respectivamente.\n\nVocê terá dois segundos para responder a essa pergunta.\n\nPara indicar a confiança da sua resposta não há limite de tempo.\n\nPressione a tecla “Espaço” do seu teclado para prosseguir.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instrucao_inicio"
instrucao_inicioClock = core.Clock()
text_ii = visual.TextStim(win=win, name='text_ii',
    text='Posicione suas mãos.\n\nAo pressionar a tecla "Espaço" do seu teclado o experimento iniciará, com uma cruz de fixação sendo exibida no centro, seguida das imagens e, posteriormente, as perguntas.\n\nO experimento é composto de 4 blocos de 40 pares cada.\n\nPressione a tecla “Espaço” do seu teclado para prosseguir.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ii = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "tela_inicial"-------
# update component parameters for each repeat
key_resp_ti.keys = []
key_resp_ti.rt = []
# keep track of which components have finished
tela_inicialComponents = [texto_tela_inicial, key_resp_ti]
for thisComponent in tela_inicialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
tela_inicialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "tela_inicial"-------
while continueRoutine:
    # get current time
    t = tela_inicialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=tela_inicialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *texto_tela_inicial* updates
    if texto_tela_inicial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        texto_tela_inicial.frameNStart = frameN  # exact frame index
        texto_tela_inicial.tStart = t  # local t and not account for scr refresh
        texto_tela_inicial.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(texto_tela_inicial, 'tStartRefresh')  # time at next scr refresh
        texto_tela_inicial.setAutoDraw(True)
    
    # *key_resp_ti* updates
    waitOnFlip = False
    if key_resp_ti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_ti.frameNStart = frameN  # exact frame index
        key_resp_ti.tStart = t  # local t and not account for scr refresh
        key_resp_ti.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_ti, 'tStartRefresh')  # time at next scr refresh
        key_resp_ti.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_ti.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_ti.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_ti.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tela_inicialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "tela_inicial"-------
for thisComponent in tela_inicialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('texto_tela_inicial.started', texto_tela_inicial.tStartRefresh)
thisExp.addData('texto_tela_inicial.stopped', texto_tela_inicial.tStopRefresh)
# the Routine "tela_inicial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instrucao_resposta"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
instrucao_respostaComponents = [text_ir, key_resp]
for thisComponent in instrucao_respostaComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrucao_respostaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instrucao_resposta"-------
while continueRoutine:
    # get current time
    t = instrucao_respostaClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrucao_respostaClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_ir* updates
    if text_ir.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_ir.frameNStart = frameN  # exact frame index
        text_ir.tStart = t  # local t and not account for scr refresh
        text_ir.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_ir, 'tStartRefresh')  # time at next scr refresh
        text_ir.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrucao_respostaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrucao_resposta"-------
for thisComponent in instrucao_respostaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_ir.started', text_ir.tStartRefresh)
thisExp.addData('text_ir.stopped', text_ir.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instrucao_resposta" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instrucao_inicio"-------
# update component parameters for each repeat
key_resp_ii.keys = []
key_resp_ii.rt = []
# keep track of which components have finished
instrucao_inicioComponents = [text_ii, key_resp_ii]
for thisComponent in instrucao_inicioComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrucao_inicioClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instrucao_inicio"-------
while continueRoutine:
    # get current time
    t = instrucao_inicioClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrucao_inicioClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_ii* updates
    if text_ii.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_ii.frameNStart = frameN  # exact frame index
        text_ii.tStart = t  # local t and not account for scr refresh
        text_ii.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_ii, 'tStartRefresh')  # time at next scr refresh
        text_ii.setAutoDraw(True)
    
    # *key_resp_ii* updates
    waitOnFlip = False
    if key_resp_ii.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_ii.frameNStart = frameN  # exact frame index
        key_resp_ii.tStart = t  # local t and not account for scr refresh
        key_resp_ii.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_ii, 'tStartRefresh')  # time at next scr refresh
        key_resp_ii.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_ii.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_ii.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_ii.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_ii.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_ii.keys = theseKeys.name  # just the last key pressed
            key_resp_ii.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrucao_inicioComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrucao_inicio"-------
for thisComponent in instrucao_inicioComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_ii.started', text_ii.tStartRefresh)
thisExp.addData('text_ii.stopped', text_ii.tStopRefresh)
# check responses
if key_resp_ii.keys in ['', [], None]:  # No response was made
    key_resp_ii.keys = None
thisExp.addData('key_resp_ii.keys',key_resp_ii.keys)
if key_resp_ii.keys != None:  # we had a response
    thisExp.addData('key_resp_ii.rt', key_resp_ii.rt)
thisExp.addData('key_resp_ii.started', key_resp_ii.tStartRefresh)
thisExp.addData('key_resp_ii.stopped', key_resp_ii.tStopRefresh)
thisExp.nextEntry()
# the Routine "instrucao_inicio" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
