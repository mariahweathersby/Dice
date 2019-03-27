"""
def roll_dice():
    selected = cmds.ls(sl=True) or []
    ran_roll_val = random.randint(1,6)
    usr_roll_val = cmds.intFieldGrp( 
        'numOfDice',
        query = True,
        value1 = True,
        )
	roll = can_roll(selected)
    rollOut = "You rolled a %s" % (rollVal)
"""

def roll_dice(maya):
	"""
	Input []:
	Output []:
	"""

	selected = maya.ls(sl=True) or []
	will_roll = can_roll(selected)
	print(will_roll);


def can_roll(selected_objs):
	"""
	Input [selected_objs]: Selected [obj]s in maya at runtime

	Output [run_params]:
		can_run: [Bool] based on eval, should function continue
		obj: [obj] selected maya obj/objs behaviors will execute on
		run_len: [int] number of iterations roll will need to do
	"""

	run_params = {
		can_run: False,
		obj: None,
		run_len: 0
		}

	if selected_objs == []:
		cmds.error("You must select an object")
		return run_params

	if len(selected_objs) < 0:
		run_params.can_run = True;
		run_params.obj = selected_objs;
		run_len = len(selected_objs);
		return run_params