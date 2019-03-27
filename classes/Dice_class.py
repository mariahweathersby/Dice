class Dice_class:
    """description of class"""

    def __init__(self, diceObj):
        self.obj = diceObj
        self.dice_coords = {
                1: [0, 0, 0],
                2: [270, 0, 0],
                3: [0, 0, 270],
                4: [0, 0, 90],
                5: [90, 0, 0],
                6: [180, 0, 0]
            }

        print ("Init Dice Object: %s" % (self.obj) )

    def rollDice(self, selected_val):
        rotate_args = self.dice_coords[selected_val][:]
        rotate_args.append(self.obj)
        print(rotate_args)

        cmds.rotate(*rotate_args)
