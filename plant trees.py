def check_empty_neighbours():
	x = get_pos_x()
	y = get_pos_y()
	size = get_world_size()-1
	return (x+y) % 2 != size%2
	

def plant_trees():
	if (get_ground_type() != Grounds.Soil):
		till()
	if can_harvest():
		harvest()
	if check_empty_neighbours():
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
plant_trees()
