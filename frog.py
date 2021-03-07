from util import Node, StackFrontier


# There is a river with 12 stones in it.
# Frog wants to move from one side of river to another. It can jump one or two stones at time
# [Ground] - (stone1) - (stone2) - (stone_n) - (stone_12) - [Ground]
# Frog  --->   Frog ----------------> Frog --->  Frog
# Frog  --------------->  Frog -----> Frog ----------------->
# 1. How many different ways frog can pass the river?
# 2. List out all the posibilities

# TODO:
# Default state is 0 which is number of steps frog has taken
# End state is when frog steps is 13 or 14
# Frog actions are always same move  over 1 or 2 stones
# Current state is number of steps frog has taken so far


initial_node = Node(state=0, parent=None, action=(1, 2))
frontier = StackFrontier()
frontier.add(initial_node)
nodes_with_finished_state = []

while True:
    if frontier.empty():
        break

    removed_node = frontier.remove()

    if removed_node.state in (13, 14):
        nodes_with_finished_state.append(removed_node)
        continue

    for action in removed_node.action:
        new_node = Node(state=removed_node.state + action, parent=removed_node, action=(1, 2))
        frontier.add(new_node)

print(len(nodes_with_finished_state))

all_paths = []
for node in nodes_with_finished_state:
    node_path = []
    while node.state != 0:
        node_path.append(node.state - node.parent.state)
        node = node.parent
    node_path.reverse()
    all_paths.append(node_path)

for el in all_paths:
    print(el)
