__author__ = 'rafael'


from utils import *


def deepSearch(problem, maxIteration = 400, maxDepth = 2):
    currentNode = problem.initial

    if problem.goalTest(currentNode.state):
        return currentNode
    frontier = [currentNode]
    explored = []

    iteration = 0
    while iteration < maxIteration:
        if len(frontier) == 0:
            return -1
        currentNode = frontier.pop()
        explored.append(currentNode.state)

        actions = problem.getActions(currentNode)

        if currentNode.depth <= maxDepth:
            for action in actions:
                if action != "" and action[0] != '/' and action.find('css') == -1 and action.find('@') == -1 and action.find('http') != -1:
                    child = problem.childNode(currentNode, action)
                    print child
                    if child not in frontier and child.state not in explored:
                        if problem.goalTest(child.state):
                            return child
                        if child.depth < maxDepth:
                            frontier.append(child)
        iteration+=1

    print iteration
    return