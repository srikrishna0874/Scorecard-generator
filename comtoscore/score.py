import math as m
import os
import tkinter as tk
import re
import pandas as pd
import numpy as np
import string
from datetime import datetime
import time

txt = open("commentary.txt", "r").read()
docs = []
for i in txt.split('\n'):
    docs.append(i)

ball = re.findall(r'\n([0-9].[0-6]|[1-2][0-9].[1-6])\n', txt)
sent = []
ball_no = []

for i in range(len(docs)):
    if docs[i] in ball:
        sentence = docs[i]+","+docs[i+1]
        sent.append(sentence)
sent.reverse()
line = []
for i in range(len(sent)):
    line.append(sent[i].split(','))
batsmen = []
bowlers = []
for i in range(len(line)):
    players = line[i][1].split('to')
    batsmen.append(players[1])
    bowlers.append(players[0])
batsmen = list(dict.fromkeys(batsmen))
bowlers = list(dict.fromkeys(bowlers))

myBat = pd.DataFrame(0, batsmen, ['status', 'R', 'B', '4s', '6s', 'SR'])
myBat['status'] = "not out"
myBowl = pd.DataFrame(0, bowlers, ['O', 'M', 'R', 'W', 'NB', 'WD', 'ECO', 'B'])
extra = 0
wide = 0
score = 0
wickets = 0
noBall = 0
b = 0
lg = 0
fall = []


for i in range(len(line)):
    ball_no = line[i][0]
    players = line[i][1].split('to')
    bat_name = players[1]
    bal_name = players[0]
    #print(bal_name,end=" ")

    line[i][2] = line[i][2].lower()
    line[i][3] = line[i][3].lower()
    #line[i][4]=line[i][4].lower()
    #print(line[i][2],end=" ")
    #print(len(line[i][2]))
    if line[i][2] == ' wide':
        #print("Hi")
        wide += 1
        score += 1
        myBowl.loc[bal_name, 'R'] = myBowl.loc[bal_name, 'R']+1
        myBowl.loc[bal_name, 'WD'] = myBowl.loc[bal_name, 'WD']+1

    elif line[i][2] == ' no ball':
        noBall += 1

        if line[i][3] == ' 1 run':
            score += 1
            myBat.loc[bat_name, 'R'] += 1
        elif line[i][3] == ' 2 runs':
            score += 2
            myBat.loc[bat_name, 'R'] += 2
        elif line[i][3] == ' 3 runs':
            score += 2
            myBat.loc[bat_name, 'R'] += 3
        elif line[i][3] == ' six' or line[i][3] == ' 6 runs' or line[i][3] == ' 6':
            score += 6
            myBat.loc[bat_name, 'R'] += 6
        elif line[i][3] == ' four' or line[i][3] == ' 4' or line[i][3] == ' 4 runs':
            score += 4
            myBat.loc[bat_name, 'R'] += 4
        elif line[i][3] == ' leg byes' or line[i][3] == ' leg bye' or line[i][3] == ' lb':
            line[i][4] = line[i][4].lower()
            if line[i][4] == ' four' or line[i][4] == ' 4 runs' or line[i][4] == ' 4':
                myBowl.loc[bal_name, 'R'] += 4
                score += 4
                lg += 4

            if line[i][4] == ' six' or line[i][4] == ' 6 runs' or line[i][4] == ' 6':
                myBowl.loc[bal_name, 'R'] += 6
                score += 6
                lg += 6

            if line[i][4] == ' 1 run' or line[i][4] == ' 1':
                myBowl.loc[bal_name, 'R'] += 1
                score += 1
                lg += 1

            if line[i][4] == ' 2 runs' or line[i][4] == ' 2':
                myBowl.loc[bal_name, 'R'] += 2
                score += 2
                lg += 2

            if line[i][4] == ' 3 runs' or line[i][4] == ' 3':
                myBowl.loc[bal_name, 'R'] += 3
                score += 3
                lg += 3

            if line[i][4] == ' 5 runs' or line[i][4] == ' 5':
                myBowl.loc[bal_name, 'R'] += 5
                score += 5
                lg += 5

        elif line[i][3] == ' byes' or line[i][3] == ' bye' or line[i][3] == ' b':
            line[i][4] = line[i][4].lower()
            if line[i][4] == ' four' or line[i][4] == ' 4 runs' or line[i][4] == ' 4':
                myBowl.loc[bal_name, 'R'] += 4
                score += 4
                lg += 4

            if line[i][4] == ' six' or line[i][4] == ' 6 runs' or line[i][4] == ' 6':
                myBowl.loc[bal_name, 'R'] += 6
                score += 6
                lg += 6

            if line[i][4] == ' 1 run' or line[i][4] == ' 1':
                myBowl.loc[bal_name, 'R'] += 1
                score += 1
                lg += 1

            if line[i][4] == ' 2 runs' or line[i][4] == ' 2':
                myBowl.loc[bal_name, 'R'] += 2
                score += 2
                lg += 2

            if line[i][4] == ' 3 runs' or line[i][4] == ' 3':
                myBowl.loc[bal_name, 'R'] += 3
                score += 3
                lg += 3

            if line[i][4] == ' 5 runs' or line[i][4] == ' 5':
                myBowl.loc[bal_name, 'R'] += 5
                score += 5
                lg += 5

    elif line[i][2] == ' four' or line[i][2] == ' 4' or line[i][2] == ' 4 runs':
        score += 4

        myBat.loc[bat_name, 'R'] += 4
        myBat.loc[bat_name, 'B'] += 1
        myBat.loc[bat_name, '4s'] += 1

        myBowl.loc[bal_name, 'B'] += 1
        myBowl.loc[bal_name, 'R'] += 4

    elif line[i][2] == ' six' or line[i][2] == ' 6' or line[i][2] == ' 6 runs':
        score += 6

        myBat.loc[bat_name, 'R'] += 6
        myBat.loc[bat_name, 'B'] += 1
        myBat.loc[bat_name, '6s'] += 1

        myBowl.loc[bal_name, 'B'] += 1
        myBowl.loc[bal_name, 'R'] += 6

    elif line[i][2] == ' 1 run' or line[i][2] == ' 1':
        score += 1

        myBat.loc[bat_name, 'R'] += 1
        myBat.loc[bat_name, 'B'] += 1

        myBowl.loc[bal_name, 'R'] += 1
        myBowl.loc[bal_name, 'B'] += 1
    elif line[i][2] == ' 2 runs' or line[i][2] == ' 2':
        score += 2
        myBat.loc[bat_name, 'R'] += 2
        myBat.loc[bat_name, 'B'] += 1

        myBowl.loc[bal_name, 'R'] += 2
        myBowl.loc[bal_name, 'B'] += 1

    elif line[i][2] == ' 3 runs' or line[i][2] == ' 3':
        score += 3
        myBat.loc[bat_name, 'R'] += 3
        myBat.loc[bat_name, 'B'] += 1

        myBowl.loc[bal_name, 'R'] += 3
        myBowl.loc[bal_name, 'B'] += 1

    elif line[i][2] == ' no run':
        myBat.loc[bat_name, 'B'] += 1

        myBowl.loc[bal_name, 'B'] += 1

    elif line[i][2] == ' leg byes' or line[i][2] == ' leg bye' or line[i][2] == ' lb':
        myBat.loc[bat_name, 'B'] += 1
        myBowl.loc[bal_name, 'B'] += 1
        score += 1

        if line[i][3] == ' four' or line[i][3] == ' 4 runs' or line[i][3] == ' 4':
            myBowl.loc[bal_name, 'R'] += 4
            score += 4
            lg += 4

        if line[i][3] == ' six' or line[i][3] == ' 6 runs' or line[i][3] == ' 6':
            myBowl.loc[bal_name, 'R'] += 6
            score += 6
            lg += 6

        if line[i][3] == ' 1 run' or line[i][3] == ' 1':
            myBowl.loc[bal_name, 'R'] += 1
            score += 1
            lg += 1

        if line[i][3] == ' 2 runs' or line[i][3] == ' 2':
            myBowl.loc[bal_name, 'R'] += 2
            score += 2
            lg += 2

        if line[i][3] == ' 3 runs' or line[i][3] == ' 3':
            myBowl.loc[bal_name, 'R'] += 3
            score += 3
            lg += 3

        if line[i][3] == ' 5 runs' or line[i][3] == ' 5':
            myBowl.loc[bal_name, 'R'] += 5
            score += 5
            lg += 5

    elif line[i][2] == ' byes' or line[i][2] == ' bye':
        myBat.loc[bat_name, 'B'] += 1
        myBowl.loc[bal_name, 'B'] += 1
        score += 1

        if line[i][3] == ' four' or line[i][3] == ' 4 runs' or line[i][3] == ' 4':
            myBowl.loc[bal_name, 'R'] += 4
            score += 4
            b += 4

        if line[i][3] == ' six' or line[i][3] == ' 6 runs' or line[i][3] == ' 6':
            myBowl.loc[bal_name, 'R'] += 6
            score += 6
            b += 6

        if line[i][3] == ' 1 run' or line[i][3] == ' 1':
            myBowl.loc[bal_name, 'R'] += 1
            score += 1
            b += 1

        if line[i][3] == ' 2 runs' or line[i][3] == ' 2':
            myBowl.loc[bal_name, 'R'] += 2
            score += 2
            b += 2

        if line[i][3] == ' 3 runs' or line[i][3] == ' 3':
            myBowl.loc[bal_name, 'R'] += 3
            score += 3
            b += 3

        if line[i][3] == ' 5 runs' or line[i][3] == ' 5':
            myBowl.loc[bal_name, 'R'] += 5
            score += 5
            b += 5

    else:
        myBat.loc[bat_name, 'B'] += 1
        myBowl.loc[bal_name, 'B'] += 1

        add = str(score)+'-'+str(wickets)+'('+bat_name+','+ball_no+')'
        fall.append(add)
        content = line[i][2].split('!')
        #print(content[0])
        con = content[0].split()
        #print(con)
        if content[0] == ' out bowled':
            myBat.loc[bat_name, 'status'] = 'b '+bal_name
            myBowl.loc[bal_name, 'W'] += 1
            wickets += 1

        elif con[len(con)-2] == 'run' and con[len(con)-1] == 'out':
            myBat.loc[bat_name, 'status'] = 'run out'
            wickets += 1

        else:
            content2 = content[0].split('by')
            myBat.loc[bat_name, 'status'] = 'c '+content2[1]+' b '+bal_name
            myBowl.loc[bal_name, 'W'] += 1
            wickets += 1

    myBat.loc[bat_name, 'SR'] = (
        (myBat.loc[bat_name, 'R']/myBat.loc[bat_name, 'B'])*100)
    myBowl.loc[bal_name, 'O'] = myBowl.loc[bal_name, 'B']/6
    myBowl.loc[bal_name, 'ECO'] = myBowl.loc[bal_name, 'R'] / \
        myBowl.loc[bal_name, 'O']

myBowl['O'] = myBowl['O'].apply(lambda x: float(
    round(x, 2)) if m.ceil(x)-x > 0.5 else float(m.ceil(x)))
myBowl['ECO'] = myBowl['ECO'].apply(lambda x: round(x, 2))
myBat['SR'] = myBat['SR'].apply(lambda x: round(x, 2))

print(myBat)
print()
print("Extra                              "+str(wide+noBall+lg+b) +
      "("+str(wide)+"w "+str(noBall)+"nb "+str(lg)+"lb "+str(b)+" b)")

print("Score                              " +
      str(score)+"("+str(wickets)+"w "+"20 Ov)")
print()
print(myBowl)
