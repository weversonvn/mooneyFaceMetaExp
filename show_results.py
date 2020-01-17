"""
=======================================================
show_results.py
=======================================================

Conjunto de funcoes para leitura e exibição dos dados obtidos.


   Copyright 2020 Weverson Nascimento

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


__author__ = "Weverson Nascimento"
__credits__ = ["Weverson Nascimento"]
__license__ = "apache-2.0"
__version__ = "0.1"
__maintainer__ = "Weverson Nascimento"
__email__ = "weverson@ufpa.br"
__status__ = "Production"

import sys, csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc

def read_file(arquivo):
    rating = np.empty(0) # to store rating responses
    answer = np.empty(0) # to store if answers are correct or not
    with open(arquivo, newline='') as f:
        reader = csv.reader(f) # read csv file
        #first = True
        try:
            for row in reader: # read row by row
                if row[4] != '': # operates only on the rows of blocks 1 and 3
                    answer = np.append(answer, row[13]) # stores answer
                    rating = np.append(rating, row[15]) # stores rating
                if row[8] != '': # operates only on the rows of blocks 2 and 4
                    answer = np.append(answer, row[17]) # stores answer
                    rating = np.append(rating, row[15]) # stores rating
        except csv.Error as e: # throw an exception if an error occurs
            sys.exit('file {}, line {}: {}'.format(arquivo, reader.line_num, e))
    rating = np.uint8(rating[2:]) # remove the first line of csv file (the same on next line)
    answer = np.uint8(answer[2:]) # and convert to int
    return rating, answer # returns both variables

def calculate_roc(rating, answer):
    total_positive = np.count_nonzero(answer) # to store the total of correct answers
    total_negative = len(answer)-total_positive # to store the total of incorrect answers
    tpr = np.empty(0) # true positive rate
    fpr = np.empty(0) # false positive rate
    for confidence in range(6):
        true_positive = 0  # to store the number of true positive answers
        false_positive = 0 # to store the number of false positive answers
        for i in range(len(rating)): # calculates the number of true and false positives
            if answer[i] == 1 and rating[i] > confidence:
                true_positive += 1
            if answer[i] == 0 and rating[i] > confidence:
                false_positive += 1
        try:
            tpr = np.append(tpr, true_positive/total_positive) # calculates true positive rate
        except ZeroDivisionError: # handle if there is no positive answer
            tpr = np.append(tpr, np.exp(-100))
        try:
            fpr = np.append(fpr, false_positive/total_negative) # calculates false positive rate
        except ZeroDivisionError: # handle if there is no negative answer
            fpr = np.append(fpr, np.exp(-100))
    roc = auc(fpr, tpr) # calculates auc-roc
    return tpr, fpr, roc

def plot_roc(tpr, fpr, roc):
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', # plots roc curve
            lw=2, label='Metacognitive sensitivity = %0.2f)' % roc) # and shows auc value
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--') # plots reference line
    plt.xlim([0.0, 1.0]) # limitates x axis
    plt.ylim([0.0, 1.05]) # limitates y axis
    plt.xlabel('p (confidence|incorrect)') # label x axis
    plt.ylabel('p (confidence|correct)') # label y axis
    plt.title('Receiver operating characteristic') # plot title
    plt.legend(loc="lower right") # position of legend
    plt.show() # shows plot

arquivo = sys.argv[1] # reads file from arguments
rating, answer = read_file(arquivo)
tpr, fpr, roc = calculate_roc(rating, answer)
plot_roc(tpr, fpr, roc)
