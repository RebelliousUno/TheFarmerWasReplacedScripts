def harvest_sunflowers(sunflowers):
	while len(sunflowers)>0:
		power, (x, y) = sunflowers.pop(len(sunflowers)-1)
		fast_goto(x,y)
		harvest()		
		
def plant_sunflower(power, x, y): 
	if (get_ground_type() != Grounds.Soil):
		till()
	if (get_entity_type() != Entities.Sunflower):
		harvest()
		plant(Entities.Sunflower)
		water_ground()
		tree_add(power,(measure(), (x, y)))

#Orchestration Function
def plant_sunflowers():
	buy(Items.Sunflower_Seed)	
	power = plant_sunflower_grid()
	harvest_sunflowers(power)
	
def plant_sunflower_grid():
	power = []
	fast_goto(0,0)
	size = get_world_size()
	for x in range(size):
		for y in range(size):
			fast_goto(x,y)
			plant_sunflower(power, x, y)
	return power

plant_sunflowers()