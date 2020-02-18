# mooneyFaceMetaExp

## Descrição
Este projeto contém um experimento de avaliação de metacognição utilizando um teste baseado em faces de Mooney.

O experimento consiste de 5 blocos de 40 _trials_ cada, onde cada _trial_ é composto pela exibição de um par de imagens, uma contendo uma face e outra não, uma por vez, seguida da pergunta em tela de qual das duas imagens continha a face, e posteriormente uma pergunta do nível de confiança na resposta, variando em uma escala de 1 até 5. Cada imagem é exibida por 200 ms, com um intervalo de 300 ms entre elas, e o participante tem 2000 ms para responder a pergunta de qual das imagens contém a face. Não há limite de tempo para responder o nível de confiança. A ordem das imagens é definida aleatoriamente no início de cada experimento. O bloco 2 é igual ao bloco 4, bem como o bloco 3 é igual ao bloco 5. O bloco 1 é para o participante se habituar ao experimento, e seus dados são desprezados.

Os resultados de cada experimento são exibidos através do gráfico da curva AUC-ROC, onde a área abaixo da curva ROC representa a sensibilidade metacognitiva do participante do experimento.

## Requisitos:
* [PsychoPy v3.2.3](https://www.psychopy.org/) 
* [Numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [Scikit-learn](https://scikit-learn.org/)

## Uso:
##### Existem duas maneiras de executar o experimento:
* Abra o arquivo **meta.psyexp** dentro do Psychopy e rode o experimento
* Execute `python meta.py` no terminal dentro do diretório raiz do projeto 

##### Para a exibição dos resultados:
* Execute `python show_results.py` dentro do diretório raiz do projeto


## Licença:

   Copyright 2019 Weverson Nascimento

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
