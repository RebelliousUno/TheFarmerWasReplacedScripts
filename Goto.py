def reset_drone():
	harvest_all()
	fast_goto(0,0)

def fast_goto_2(target_x, target_y):
    size = get_world_size()
    
    current_x = get_pos_x()
    current_y = get_pos_y()
    
    # Calculate the shortest distance in the toroidal grid
    move_x = (target_x - current_x) % size
    move_y = (target_y - current_y) % size
    
    if move_x > size / 2:
        move_x -= size
    if move_y > size / 2:
        move_y -= size
    
    # Move in the X direction
    if move_x != 0:
        if move_x > 0:
            move(East)
        else:
            move(West)
    
    # Move in the Y direction
    if move_y != 0:
        if move_y > 0:
            move(North)
        else:
            move(South)
    
    # Recur only if there is still distance to cover
    if move_x != 0 or move_y != 0:
        fast_goto(target_x, target_y)

def fast_goto(target_x, target_y):
	size = get_world_size()
	
	move_x = get_pos_x()-target_x
	move_y = get_pos_y()-target_y		
	
	if (move_y < 0):
		if (abs(move_y) <= size/2):
			move(North)
		else:
			move(South)
	elif (move_y > 0):
		if (abs(move_y) <= size/2):
			move(South)
		else:
			move(North)
	elif (move_x < 0):
		if (abs(move_x) <= size/2):			 
			move(East)
		else: 
			move(West)
	elif (move_x > 0):
		if (abs(move_x) <= size/2):
			move(West)
		else:
			move(East)
	if ((move_x != 0) or (move_y != 0)):
		fast_goto(target_x, target_y)


def goto(target_x, target_y):	
	move_x = get_pos_x()-target_x
	move_y = get_pos_y()-target_y
	if (move_y < 0):
		move(North)
	elif (move_y > 0):
		move(South)
	elif (move_x < 0): 
		move(East)
	elif (move_x > 0):
		move(West)
	if ((move_x != 0) or (move_y != 0)):
		goto(target_x, target_y)

fast_goto(0,1)