import argparse
import parse_url

'''
  main function for WebCrawler

  1.Takes two mandatory arguments 'url' and 'depth'
  2.'url' is the initial url to start crawling with. If not supplied defaults to http://www.recruiterbox.com
  3.'depth' is the number of iterations to go through each new link recursivly found from initial url.
     If not supplied defaults to 2
  4.Call parse_url which parses initial url
  
'''

def main():
    list1 = []
    Parser = argparse.ArgumentParser(description = "WebCrawler")
    Parser.add_argument('-url',help = 'Initial url', nargs = '?', default = "https://www.python.org", type = str)
    Parser.add_argument('-depth',help = 'Depth for crawl', nargs = '?', default = 2, type = int)
    args = Parser.parse_args()
    argsdict = vars(args)
    url = argsdict['url']
    depth = argsdict['depth']
    if url == None or depth == None:
        print "Arguments empty. Please enter valid url and depth"
        exit(0)
    print "Url considered - ",url
    print "Going for",depth,"number of depths"
    parse_url.parse_url(url,list1,depth)

if __name__ == '__main__':
    main()