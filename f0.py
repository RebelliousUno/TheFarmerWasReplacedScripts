def load_jurassic_park():
	size = get_world_size()
	for x in range(size):
		for y in range(size):
			buy_one(Items.Egg)
			fast_goto_2(x, y)
			use_item(Items.Egg)
	
def harvest_park():
	size = get_world_size()
	for x in range(size):
		for y in range(size):
			fast_goto_2(x,y)
			c = measure()
			n = measure(North)
			e = measure(East)
			s = measure(South)
			w = measure(West)
			count = 0
			if (c==n):
				count += 1
			if (c==e):
				count += 1
			if (c==s):
				count += 1
			if (c==w):
				count += 1
			if (count>=3):
				harvest()
				
def jurassic_park():		
	load_jurassic_park()		
	harvest_park()