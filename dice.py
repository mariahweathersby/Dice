import sys
sys.path.append(r'C:\Users\maria\OneDrive\Desktop\Maya-TA-Tools\dice\dice')

import random
import maya.cmds as cmds
import helpers.helpers as helper

from classes.Dice_class import Dice_class as Dice


def UI():
    if cmds.window('diceRoll', exists = True):
        cmds.deleteUI('diceRoll')

    cmds.window('diceRoll')
    cmds.columnLayout()

    cmds.intFieldGrp(
        'numOfDice',
        label = 'Number of Dice',
        command = ('create_dice()'),
        value1 = 0
        )

    cmds.button(
        label = "Roll Dice",
        command = 'roll_dice()'
        )
    cmds.showWindow('diceRoll')

UI();

helper.roll_dice(cmds)

