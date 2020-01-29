from room import Room
from player import Player
from world import World
from util import Stack, Queue, Graph, MapGraph, RoomObject
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] # paths traversed

reverse_path = [] # paths traversed in reverse
opposite_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

room_paths = {}

room_paths[player.current_room.id] = player.current_room.get_exits()

while len(room_paths) < len(room_graph)-1:
    if player.current_room.id not in room_paths:
        room_paths[player.current_room.id] = player.current_room.get_exits()
        last_room_visited = reverse_path[-1]
        room_paths[player.current_room.id].remove(last_room_visited)
    while len(room_paths[player.current_room.id]) == 0:
        reverse = reverse_path.pop()
        traversal_path.append(reverse)
        player.travel(reverse)
    movement_direction = room_paths[player.current_room.id].pop(0)
    traversal_path.append(movement_direction)
    reverse_path.append(opposite_direction[movement_direction])
    player.travel(movement_direction)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)



# print(player.current_room)
for move in traversal_path:
    player.travel(move)

    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")




# ######
# UNCOMMENT TO WALK AROUND
# ######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
