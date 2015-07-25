import urllib2
import re
import writetofile
import go_crawl

'''
    Method for initial parsing of main url - 

    1. Filters out href tags and creates an initial list - 'list1'
    2. Write the contents of list1 into file 'scrap.txt'
    3. Call 'go_crawl' by supplying 'list1' for further crawling of sub pages
    4. Call 'writetofile' method at last to write all the links crawled into a file 

'''

def parse_url(url,list1,depth):
    try:    
            f1 = urllib2.urlopen(url, timeout = 10).read()
            temp = re.findall(r'(href=\S+)', f1)
            for item in temp:
                k = item[6:]               # To trim 'href="' tag 
                k = k.split('"')[0]
                if k.startswith("http" or "https"):
                    if k.endswith("/"):
                        k = k[:-1]         # To trim '/' at the end of urls to avoid duplicates
                        list1.append(k)
                    else:
                        list1.append(k)
                elif k.startswith('/'):
                    if k.endswith("/"):
                        k = k[:-1]
                        list1.append(url+k)
                    else:
                        list1.append(url+k)
                    
            list1 = list(set(list1))

    except ValueError as ex:
        pass
    
    except urllib2.URLError as ex:
        pass
    
    except Exception as ex:
        pass

    final = []
    prefinal = []
    final_list = go_crawl.crawl(list1,depth,final,prefinal)
    list1.append(final_list)
    writetofile.write(list1)