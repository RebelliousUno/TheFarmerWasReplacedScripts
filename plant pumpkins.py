def plant_pumpkin():			
	buy(Items.Pumpkin_Seed)
	if (get_ground_type() != Grounds.Soil):
		harvest()
		till()
	while (get_entity_type() != Entities.Pumpkin):
		buy(Items.Fertilizer)
		harvest()
		plant(Entities.Pumpkin)
		water_ground()
		use_item(Items.Fertilizer)
		water_ground()

#Old Method
def plant_pumpkins():
	emptySpots = False
	while True:
		plant_pumpkin()
		traverse_grid()
		if (get_entity_type() != Entities.Pumpkin):
			emptySpots = True
		if ((get_pos_x() == 0) and (get_pos_y() == 0)):
			if (not emptySpots):
				harvest()
				return
			emptySpots = False

def plant_pumpkins_2():
	coords = get_all_coords()			
	while len(coords) > 0:
		x, y = coords.pop(0)
		fast_goto(x, y)
		if (get_entity_type() != Entities.Pumpkin):
			plant_pumpkin()
			coords.append((x,y))
	while not can_harvest():
		if (get_entity_type() != Entities.Pumpkin):
			plant_pumpkins_2()
			break
		do_a_flip()
		
	harvest()
								
plant_pumpkins_2()