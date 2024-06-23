def plant_grass():
	if (get_ground_type() != Grounds.Turf):
		harvest()
		till()
	if can_harvest():
		harvest()