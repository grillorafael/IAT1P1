__author__ = 'rafael'

#ref http://www.mkyong.com/regular-expressions/how-to-extract-html-links-with-regular-expression/
#useful link http://aima.cs.berkeley.edu/python/readme.html

from utils import *
from linknode import *
from linkproblem import *
from search import *
import time

def main():
    fromUrl = "http://portfolio.local/site/portfolio"
    goalUrl = "http://www.yiiframework.com/"

    #Important Nodes
    initialNode = LinkNode(fromUrl)

    #Problem Definition
    problem = LinkProblem(initialNode, goalUrl)
    #print deepSearch(problem)
    start_time = time.time()

    solution = deepSearch(problem)
    print solution
    print (time.time() - start_time) / 60, "minutes"
    print solution.path()

main()