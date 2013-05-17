__author__ = 'rafael'

#ref http://www.mkyong.com/regular-expressions/how-to-extract-html-links-with-regular-expression/
#useful link http://aima.cs.berkeley.edu/python/readme.html

from utils import *
import linknode, linkproblem, re, urllib2

regexUrl = "\\s*(?i)href\\s*=\\s*(\"([^\"]*\")|'[^']*'|([^'\">\\s]+))"

def main():
    fromUrl = "http://portfolio.local"
    urlToSearch = "https://github.com/grillorafael/jquery-ajax-page-change"


    #Important Nodes
    initialNode = linknode.LinkNode(fromUrl)
    goalNode = linknode.LinkNode(urlToSearch)

    #Problem Definition
    problem = linkproblem.LinkProblem(initialNode, goalNode)


    print initialNode
    print goalNode

    print initialNode.depth
    print goalNode.depth

    #print initialNode.expand(problem)
    #print goalNode.expand(problem)

    print initialNode.path()
    print goalNode.path()

    '''
        urls = getUrlLinks(fromUrl)
        print len(urls)
        for url in urls:
            print url[0]
    '''

def getUrlLinks(url):
    response = urllib2.urlopen(url)
    source = response.read()
    urls = re.findall(regexUrl, source)
    return urls

main()