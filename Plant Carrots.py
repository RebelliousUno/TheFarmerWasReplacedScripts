def plant_carrots():
	water_ground()
	buy(Items.Carrot_Seed)
	if (get_ground_type() != Grounds.Soil):
		harvest()
		till()
	if (can_harvest() or get_entity_type() != Entities.Carrots):
		harvest()		
		plant(Entities.Carrots)
	else:
		do_a_flip()