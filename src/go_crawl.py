import urllib2
import re

'''
    Method to crawl new links recursively from list of links obtained in initial url for 'depth' steps

    1. Parse list of links obtained from initial url
    2. Append the resulting links to a list
    3. Take the 'depth' number of links from new list and crawl again
    4. This method calls itself for 'depth' number of times to crawl and reach a webpage which is 
        'depth' number of distance from initial url 

'''

def crawl(list1,depth,final,prefinal):
    list2 = []
    prefinal = []
    dummy = []
    for item in list1[:depth]:
        try:
                f1 = urllib2.urlopen(item, timeout = 10).read()
                temp = re.findall(r'(href=\S+)', f1)
                for item1 in temp:
                    k = item1[6:]           # To trim 'href="' tag 
                    k = k.split('"')[0]
                    if k.startswith("http" or "https") and len(list2) < depth:
                        if k.endswith("/"):
                            k = k[:-1]      # To trim '/' at the end of urls to avoid duplicates
                            list2.append(k)
                            dummy.append(k)
                        else:
                            list2.append(k)
                            dummy.append(k)
                    list2 = []
                dummy = list(set(dummy))
                prefinal.append(dummy)
                dummy = []

        except ValueError as ex:
            pass

        except urllib2.URLError as ex:
            pass

        except Exception as ex:
            pass

    final.append(prefinal)
    print "In depth - ",len(final)
    if len(final) < depth:
        prefinal = [ item for sublist in prefinal for item in sublist] # Flatten list
        prefinal = list(set(prefinal))
        crawl(prefinal,depth,final,prefinal) # Call 'crawl' method recursively for 'depth' times

    return final
