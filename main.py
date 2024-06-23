base = 10000
orders = [
		(Items.Power, base),
		(Items.Hay, base),
		(Items.Wood, base),
		(Items.Carrot, base),
		(Items.Pumpkin, base),
		(Items.Gold, base),	
		(Items.Cactus, base),	
		(Items.Bones, base)				
			]
clear()
while base>0:
	while(plant_all(base, base, base, base, base, base, base, base)):
		buy_water_tank(5000)
		traverse_grid()
		c = get_all_costs()
		base = unlock_things()

			
	
	