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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# START HERE
Map = MapGraph()
for room in world.rooms:
    Map.add_room(world.rooms[room])
    if world.rooms[room].n_to is not None:
        next_room = world.rooms[room].get_room_in_direction('n')
        if Map.add_connection(world.rooms[room], next_room):
            Map.add_connection(world.rooms[room], next_room)
        # print('room')
        # print(world.rooms[room])
        # print('connection')
        # print(world.rooms[room].n_to)
        # print(next_room)
    elif world.rooms[room].s_to is not None:
        next_room = world.rooms[room].get_room_in_direction('s')
        if Map.add_connection(world.rooms[room], next_room):
            Map.add_connection(world.rooms[room], next_room)

        # print('room')
        # print(world.rooms[room])
        # print('connection')
        # print(world.rooms[room].s_to)
        # print(next_room)
    elif world.rooms[room].e_to is not None:
        next_room = world.rooms[room].get_room_in_direction('e')
        if Map.add_connection(world.rooms[room], next_room):
            Map.add_connection(world.rooms[room], next_room)

        # print('room')
        # print(world.rooms[room])
        # print('connection')
        # print(world.rooms[room].e_to)
        # print(next_room)
    elif world.rooms[room].w_to is not None:
        next_room = world.rooms[room].get_room_in_direction('w')
        if Map.add_connection(world.rooms[room], next_room):
            Map.add_connection(world.rooms[room], next_room)

        # print('room')
        # print(world.rooms[room])
        # print('connection')
        # print(world.rooms[room].w_to)
        # print(next_room)



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


# print(world)
# for k in world.rooms:
#     print(f'{world.rooms[k]}')
print(Map.connections)
print('-------------------Visited Rooms----------------------')
print(visited_rooms)
print('---------------MAP------------------')
# print(Map)

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
