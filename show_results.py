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

def read_file(arquivo):
    rating = np.empty(0) # to store rating responses
    answer = np.empty(0) # to store if answers are correct or not
    with open(arquivo, newline='') as f:
        reader = csv.reader(f) # read csv file
        try:
            for row in reader: # read row by row
                if row[4] != '': # operates only on the rows of blocks 1 and 3
                    answer = np.append(answer, row[13]) # stores answer
                    rating = np.append(rating, row[14]) # stores rating
                if row[8] != '': # operates only on the rows of blocks 2 and 4
                    answer = np.append(answer, row[17]) # stores answer
                    rating = np.append(rating, row[14]) # stores rating
        except csv.Error as e: # throw an exception if an error occurs
            sys.exit('file {}, line {}: {}'.format(arquivo, reader.line_num, e))
    rating = rating[2:] # remove the first line of csv file (the same on next line)
    answer = answer[2:]
    return rating, answer # returns both variables

arquivo = sys.argv[1]
rating, answer = read_file(arquivo)