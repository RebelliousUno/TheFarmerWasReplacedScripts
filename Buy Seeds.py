def buy(seed):
	size = get_world_size()
	if (num_items(seed) < size):
		trade(seed,(size**2))
		
def buy_one(seed):
	size = get_world_size()
	if (num_items(seed) < size):
		while(trade(seed)):
			pass