class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return f'{self.vertices}'

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')
            

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.vertices[vertex]:
                    stack.push(next_vertex)
                    

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enstack a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #    Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                # Copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
        #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                # Copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex,  target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None



class RoomObject:
    def __init__(self, name):
        self.name = name
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):
        return f'{self.name}'


class MapGraph:
    def __init__(self):
        self.last_id = 0
        self.rooms = {}
        self.connections = {}
      
    def __repr__(self):
      return f'{self.rooms}'

    def add_connection(self, room_id, next_room_id):
        """
        Creates a bi-directional connection
        """
        if room_id == next_room_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        # elif next_room_id in self.connections[room_id] or room_id in self.connections[next_room_id]:
        #     print("WARNING: connection already exists")
        #     return False
        else:
            self.connections[room_id] = next_room_id 
            self.connections[next_room_id] = room_id
            return True

    def add_room(self, name):
        """
        Create a new room with a sequential integer ID
        """
        self.rooms[self.last_id] = RoomObject(name)
        self.connections[self.last_id] = {}
        self.last_id += 1  # automatically increment the ID to assign the new room

    def populate_graph(self, num_rooms, avg_connections):
        """
        Takes a number of rooms and an average number of connections
        as arguments

        Creates that number of rooms and a randomly distributed connections
        between those rooms.

        The number of rooms must be greater than the average number of connections.
        """
        # Reset graph
        self.last_id = 0
        self.rooms = {}
        self.connections = {}
        # !!!! IMPLEMENT ME

        # Add rooms
        for i in range(num_rooms):
            self.add_room(f'room {i}')
        # Create connections
        target_connections = (num_rooms * avg_connections)
        total_connections = 0
        collisions = 0
        while total_connections < target_connections:
            # create a random connection
            room_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_connection(room_id, friend_id):
                total_connections += 2
            else:
                collisions += 1

        print(f"COLLISIONS: {collisions}")
        print(f'TOTAL connections: {total_connections}')
    def get_all_paths(self, room_id):
        """
        Takes a room's room_id as an argument

        Returns a dictionary containing every room in that room's
        extended network with the shortest connection path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # create a queue
        q = Queue()
        # enqueue the starting point in a list to start a path
        q.enqueue([room_id])
        # while queue not empty
        while q.size() > 0:

            #dequeue path and assign to variable
            path = q.dequeue()
            # find last vertex in path
            curr_friend = path[-1]
            # if vertex not in visited:
            if curr_friend not in visited:
                # DO THE THING 
                visited[curr_friend] = path
                # add to visited
                # make new paths(copy) and enqueue for each vertex
                for friend_id in self.connections[curr_friend]:
                    new_path = list(path)
                    new_path.append(friend_id)
                    q.enqueue(new_path)
                    



        print(f'room: {self.rooms[room_id]}')
        print(f'Friends: {self.connections[room_id]}')
        return visited
