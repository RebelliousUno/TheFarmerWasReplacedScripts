def traverse_grid():
	if (get_pos_y() == get_world_size()-1):
		move(East)
	move(North)