def get_all_costs():
	costs = {
		Unlocks.Speed: 0,
		Unlocks.Grass: 0,
		Unlocks.Carrots: 0,
		Unlocks.Trees: 0,
		Unlocks.Pumpkins: 0,
		Unlocks.Mazes: 0,
		Unlocks.Sunflowers: 0,
		Unlocks.Expand: 0,
		Unlocks.Cactus: 0
	}
	for c in costs:
		cost = get_cost(c)
		costs[c] = cost
	return costs

def unlock_things():
	costs = get_all_costs()
#	quick_print(costs)
	min_cost = 0
	for c in costs:
		cost = costs[c]
		if cost == None: 
			continue
		for key in cost:			
			if (num_items(key) >= cost[key]):
				unlock(c)
			if (min_cost != 0):
				min_cost = min(min_cost, cost[key])
			else:
				min_cost = cost[key]
	return min_cost
	
unlock_things()