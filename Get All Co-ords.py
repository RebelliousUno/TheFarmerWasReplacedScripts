def get_all_coords():
	coords = []
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			coords.append((x, y))	
	return coords