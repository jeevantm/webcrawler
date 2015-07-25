from compiler.ast import flatten

'''
    Method to write all the links obtained from crawling

    1. Take input as a list from 'go_crawl' method
    2. Flatten the list and remove duplicates if found
    3. Write all the links crawled to a file 'final.txt'

'''

def write(list1):
    last = []
    last = flatten(list1)
    last = list(set(last))
    print len(last),"links crawled"
    txt1 = open('output.txt','w')
    for i in range(len(last)):
        txt1.write(str(i+1)+": "+str(last[i])+'\n')
