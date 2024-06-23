def buy_water_tank(num):
	while (num_items(Items.Wood) >= 5 and (num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)) < num):
		trade(Items.Empty_Tank)
		
def water_ground():
	if (get_water()	< 0.5 and num_items(Items.Water_Tank) > 0):
		use_item(Items.Water_Tank)