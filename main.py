__author__ = 'rafael'

#ref http://www.mkyong.com/regular-expressions/how-to-extract-html-links-with-regular-expression/
#useful link http://aima.cs.berkeley.edu/python/readme.html

from linknode import *
from linkproblem import *
from search import *
import time, sys

def main():
    #fromUrl = "http://portfolio.local/site/portfolio"
    #goalUrl = "http://www.yiiframework.com/"

    if len(sys.argv) == 3:
        fromUrl = sys.argv[1]
        goalUrl = sys.argv[2]
    else:
        print "Not enough arguments"
        return

    #Important Nodes
    initialNode = LinkNode(fromUrl)

    #Problem Definition
    problem = LinkProblem(initialNode, goalUrl)

    start_time = time.time()
    solution = deepSearch(problem, 400, 2)

    if solution != -1:
        print solution
        print solution.path()
    else:
        print "Goal not found"

    print (time.time() - start_time) / 60, "minutes"

main()