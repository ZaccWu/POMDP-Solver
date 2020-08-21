from Environment.tagEnvironment import TagTransition
from tools.sampleUtility import chooseItemIdx
import numpy as np
transitions = TagTransition()
action = 'West'
state = 'r[0,8]n[0,7]'
robotStates = ['[0,0]', '[0,1]', '[0,2]', '[0,3]', '[0,4]', '[0,5]', '[0,6]', '[0,7]', '[0,8]', '[0,9]',
                    '[1,0]', '[1,1]', '[1,2]', '[1,3]', '[1,4]', '[1,5]', '[1,6]', '[1,7]', '[1,8]', '[1,9]',
                    '[2,5]', '[2,6]', '[2,7]', '[3,5]', '[3,6]', '[3,7]', '[4,5]', '[4,6]', '[4,7]']
opponentStates = ['[0,0]', '[0,1]', '[0,2]', '[0,3]', '[0,4]', '[0,5]', '[0,6]', '[0,7]', '[0,8]', '[0,9]',
                       '[1,0]', '[1,1]', '[1,2]', '[1,3]', '[1,4]', '[1,5]', '[1,6]', '[1,7]', '[1,8]', '[1,9]',
                       '[2,5]', '[2,6]', '[2,7]', '[3,5]', '[3,6]', '[3,7]', '[4,5]', '[4,6]', '[4,7]', '[tag]']
# tag environment
states = ['r' + i + 'n' + j for i in robotStates for j in opponentStates]

for sj in states:
    test = transitions(action, state, sj)
    if test!=0:
        print(action, state, sj, test)