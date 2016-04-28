''' ADAPTED EXAMPLE '''

# graph is in adjacent list representation
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    visited = set()
    # push the first path into the queue
    queue.append([start])    
    while queue:
        print "y-------------------------"
        # get the first path from the queue
        path = queue.pop(0)
        print path, "\n\n\n"
        # print path, "\n\n"
        # get the last node from the path
        node = path[-1]
        # print node, "\n"
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue        
        elif node not in visited:        
            for adjacent in graph.get(node, []):
                print "x"
                new_path = list(path)
                print adjacent
                print new_path
                new_path.append(adjacent)
                print new_path, "\n\n"
                queue.append(new_path)
            visited.add(node)

print bfs(graph, '1', '11')