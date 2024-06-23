def plant_bush():
	if (get_ground_type() != Grounds.Turf):			
		till()
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)