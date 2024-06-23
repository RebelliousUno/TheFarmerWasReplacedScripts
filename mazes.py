

def create_maze(): 

	if (get_ground_type() != Grounds.Turf):
		till()	
	plant(Entities.Bush)	
	while not can_harvest():
		water_ground()
		buy(Items.Fertilizer)
		use_item(Items.Fertilizer)
	
	while (get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure):
		buy(Items.Fertilizer)
		use_item(Items.Fertilizer)

def is_on_edge(x, y):
	size = get_world_size()
	return x == 0 or x == size-1 or y==0 or y==size-1

def left_hand_rule():		
	dir = [North, East, South, West]
	while get_entity_type() == Entities.Hedge:
		facing = dir[0]
		left = dir[len(dir)-1]
		right = dir[1]
		back = dir[2]
		if (move(left)):
			dir.remove(left)
			dir.insert(0, left)
		elif (move(facing)):
			pass
		elif (move(right)):
			dir.remove(facing)
			dir.append(facing)
		else:
			move(back)
			dir.remove(facing)
			dir.remove(right)
			dir.append(facing)
			dir.append(right)
	harvest()
	return False

def maze_runner():
	count = 0
	harvest()
	create_maze()
	while left_hand_rule():
		count += 1
		if (count>300): 
			return		
	
maze_runner()