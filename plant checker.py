#OLD PLanting
def plant_all(hay, wood, carrot, pumpkin, power, gold, cactus, bone):
	
	if (num_items(Items.Hay) <= hay):
		plant_grass()
	elif (num_items(Items.Wood) <= wood):
		plant_trees()
	elif (num_items(Items.Carrot) <= carrot):
		plant_carrots()
	elif (num_items(Items.Power) <= power):
		plant_sunflowers()
	elif (num_items(Items.Pumpkin) <= pumpkin):
		plant_pumpkins_2()
	elif (num_items(Items.Gold) <= gold):
		maze_runner()
	elif (num_items(Items.Cactus) <= cactus):
		cactus_farmer()
	elif (num_items(Items.Bones) <= bone):
		jurassic_park()
	else:
		return False
	return True

def plant_all_2(plant_order):
	if (len(plant_order)>0 and num_items(plant_order[0][0]) < plant_order[0][1]):
		plant_selector(plant_order[0][0])
	else:
		tmp = plant_order.pop(0)
		plant_order.append(tmp)

def plant_selector(plant):
	if (plant == Items.Carrot):
		plant_carrots()
	elif (plant == Items.Power):
		plant_sunflowers()
	elif (plant == Items.Hay):
		plant_grass()
	elif (plant == Items.Wood):
		plant_trees()
	elif (plant == Items.Pumpkin):
		plant_pumpkins_2()
	elif (plant == Items.Gold):
		maze_runner()
	elif (plant == Items.Cactus):
		cactus_farmer()
	elif (plant == Items.Bones):
		jurassic_park()
	