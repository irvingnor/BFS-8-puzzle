import Queue
import time
import sys

possible_movements = [[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8],[5,7,9],[6,8]]
direction = [['R','D'],['L','R','D'],['L','D'],['U','R','D'],['U','L','R','D'],['U','L','D'],['U','R'],['U','L','R'],['U','L']]
empty_symbol = "0"
goal_state = "012345678"
file_name = "entrada.txt"

def generateNeighbors(state):
	list_result = []
	empty_position = state[0].find(empty_symbol)
	i = 0
	level = state[2]+1
	for position in possible_movements[empty_position]:
		tmp_result = state[0]
		tmp_result = tmp_result[0:empty_position] + tmp_result[position-1] + tmp_result[empty_position+1:9]
		tmp_result = tmp_result[0:position-1] + empty_symbol + tmp_result[position:9]
		movement = direction[empty_position][i]
		i = i+1
		list_result.append([tmp_result,state[1]+movement,level])
	return list_result

def bfs( initialState , goalTest ):
	frontier = Queue.Queue()
	frontier.put(initialState)
	copy_frontier = set()
	copy_frontier.add(initialState[0])
	explored = set([])
	nodes_expanded = 0

	while not frontier.empty():
		state = frontier.get()
		copy_frontier.remove(state[0])
		explored.add(state[0])
		nodes_expanded = nodes_expanded + 1

		if state[0] == goal_state:
			return [state,nodes_expanded]

		neighbors = generateNeighbors(state)
		for neighbor in neighbors:
			if not( neighbor[0] in copy_frontier ) and not(neighbor[0] in explored) :
				frontier.put(neighbor)
				copy_frontier.add(neighbor[0])

	return False
# https://www.cs.princeton.edu/courses/archive/fall12/cos226/assignments/8puzzle.html
# https://puzzling.stackexchange.com/questions/52110/8-puzzle-unsolvable-proof
# https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
# input_test =  "724506831"   "125340678"  "813402765"  "013425786"  ///Unsovable//"123456870"  -  "210345678"  - "702853641" - "103245678" -"812043765"
file = open("entrada.txt", "r")
input_test = file.readline()
input_test = input_test[0:len(input_test)-1]
test_v = [input_test,"",0]

start = time.time()
result = bfs(test_v,goal_state)
end = time.time()

elapsed_time = end - start

if type(result) is list:
	number_nodes = result[1]
	result = result[0]
	print "Path to goal:\t\t" + str(result[1])
	print "Cost to the path:\t" + str(result[2])
	print "Nodes expanded/visited:\t" + str(number_nodes) 
	print "Running time:\t\t" + str(elapsed_time) + " seconds"
	print "Used memory:\t\t" + str(sys.getsizeof(result)*number_nodes) + " bytes"
else:
	print str(result)