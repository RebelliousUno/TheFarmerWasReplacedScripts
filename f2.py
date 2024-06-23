def harvest_all():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			fast_goto_2(x, y)
			harvest()