from implementation import *
start, goal = (1, 4), (7, 8)
came_from, cost_so_far = a_star_search(diagram4, start, goal)
print came_from, cost_so_far
draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)
print()