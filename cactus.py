def plant_cactus():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			fast_goto_2(x,y)
			if (get_entity_type() != Entities.Cactus):
				harvest()
			if (get_ground_type() != Grounds.Soil):
				till()
			
			buy(Items.Cactus_Seed)
			plant(Entities.Cactus)			
def sort_cactus():
	swap_count = 0
	size = get_world_size()
	while True:
		for x in range(size):
			for y in range(size):
				fast_goto_2(x,y)
				current_cactus = measure()
				north_cactus = measure(North)
				east_cactus = measure(East)
				if (y != size-1) and (current_cactus > north_cactus): 
					swap(North)		
					swap_count += 1	
				elif (x != size-1) and (current_cactus > east_cactus):
					swap(East)
					swap_count += 1
		if (swap_count == 0):
			#sorted
			return
		else:
			#not sorted
			swap_count = 0

def cactus_farmer():
	plant_cactus()
	sort_cactus()
	harvest()
	
cactus_farmer()