#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on ter 29 out 2019 11:30:46 -03
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
    winType='pyglet', allowGUI=True, allowStencil=False,
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
f = np.arange(40)
d = np.arange(40)
ff = np.arange(40)
dd = np.arange(40)
np.random.shuffle(f)
np.random.shuffle(d)
np.random.shuffle(ff)
np.random.shuffle(dd)
primeiro = np.empty(40)
segundo = np.empty(40)
terceiro = np.empty(40)
quarto = np.empty(40)
e = np.random.randint(2, size=40)
ee = np.random.randint(2, size=40)
caminho = "./mooneyfaces/"
file = ""
i = 0

# Initialize components for Routine "fixate"
fixateClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "case_1"
case_1Clock = core.Clock()
image_1 = visual.ImageStim(
    win=win,
    name='image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "inter_time"
inter_timeClock = core.Clock()
text_it = visual.TextStim(win=win, name='text_it',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "case_2"
case_2Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "resposta"
respostaClock = core.Clock()
text_resposta = visual.TextStim(win=win, name='text_resposta',
    text='Qual a imagem com a face humana, 1 ou 2?',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "confianca"
confiancaClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Responda qual o grau de confiança na sua resposta, sendo 1 menos confiante e 5 mais confiante.\n\nSelecione sua resposta clicando na barra abaixo ou pressionando o número correspondente no teclado, e, em seguida, pressione a tecla "Enter".',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.6], low=1, high=5, labels=[''], scale='')

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

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=40, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixate"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixateComponents = [text]
    for thisComponent in fixateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "fixate"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixate"-------
    for thisComponent in fixateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "case_1"-------
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    case_1Components = [image_1]
    for thisComponent in case_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    case_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "case_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = case_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=case_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if e[i] == 0:
            file = caminho + 'f' + str(f[i]) + '.jpg'
        else:
            file = caminho + 'd' +str(d[i]) + '.jpg'
        
        # *image_1* updates
        if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_1.frameNStart = frameN  # exact frame index
            image_1.tStart = t  # local t and not account for scr refresh
            image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
            image_1.setAutoDraw(True)
        if image_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_1.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                image_1.tStop = t  # not accounting for scr refresh
                image_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_1, 'tStopRefresh')  # time at next scr refresh
                image_1.setAutoDraw(False)
        if image_1.status == STARTED:  # only update if drawing
            image_1.setImage(file, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in case_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "case_1"-------
    for thisComponent in case_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_1.started', image_1.tStartRefresh)
    trials.addData('image_1.stopped', image_1.tStopRefresh)
    
    # ------Prepare to start Routine "inter_time"-------
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    # keep track of which components have finished
    inter_timeComponents = [text_it]
    for thisComponent in inter_timeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    inter_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "inter_time"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = inter_timeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=inter_timeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_it* updates
        if text_it.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_it.frameNStart = frameN  # exact frame index
            text_it.tStart = t  # local t and not account for scr refresh
            text_it.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_it, 'tStartRefresh')  # time at next scr refresh
            text_it.setAutoDraw(True)
        if text_it.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_it.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text_it.tStop = t  # not accounting for scr refresh
                text_it.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_it, 'tStopRefresh')  # time at next scr refresh
                text_it.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inter_timeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "inter_time"-------
    for thisComponent in inter_timeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_it.started', text_it.tStartRefresh)
    trials.addData('text_it.stopped', text_it.tStopRefresh)
    
    # ------Prepare to start Routine "case_2"-------
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    case_2Components = [image_2]
    for thisComponent in case_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    case_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "case_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = case_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=case_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if e[i] == 1:
            file = caminho + 'f' + str(f[i]) + '.jpg'
        else:
            file = caminho + 'd' + str(d[i]) + '.jpg'
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        if image_2.status == STARTED:  # only update if drawing
            image_2.setImage(file, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in case_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "case_2"-------
    for thisComponent in case_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    i = i + 1
    trials.addData('image_2.started', image_2.tStartRefresh)
    trials.addData('image_2.stopped', image_2.tStopRefresh)
    
    # ------Prepare to start Routine "resposta"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    respostaComponents = [text_resposta, key_resp_2]
    for thisComponent in respostaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    respostaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "resposta"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = respostaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=respostaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_resposta* updates
        if text_resposta.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_resposta.frameNStart = frameN  # exact frame index
            text_resposta.tStart = t  # local t and not account for scr refresh
            text_resposta.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_resposta, 'tStartRefresh')  # time at next scr refresh
            text_resposta.setAutoDraw(True)
        if text_resposta.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_resposta.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_resposta.tStop = t  # not accounting for scr refresh
                text_resposta.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_resposta, 'tStopRefresh')  # time at next scr refresh
                text_resposta.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respostaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resposta"-------
    for thisComponent in respostaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_resposta.started', text_resposta.tStartRefresh)
    trials.addData('text_resposta.stopped', text_resposta.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    
    # ------Prepare to start Routine "confianca"-------
    # update component parameters for each repeat
    rating.reset()
    # keep track of which components have finished
    confiancaComponents = [text_2, rating]
    for thisComponent in confiancaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    confiancaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "confianca"-------
    while continueRoutine:
        # get current time
        t = confiancaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=confiancaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confiancaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "confianca"-------
    for thisComponent in confiancaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    trials.addData('rating.started', rating.tStart)
    trials.addData('rating.stopped', rating.tStop)
    # the Routine "confianca" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 40 repeats of 'trials'


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
