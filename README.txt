WEBCRAWLER

* main function is to be executed by calling the 'main.py' file in the 'src' folder

* Running  python main.py -h  provides help on how to execute.

* Two arguments should be passed to main function through command line arguments.

* First argument is 'url' which is the initial input url.

* Second argument is 'depth' which specifies the recursion depth of crawl.

* If arguments are not specified, default values are assigned automatically. 'url' takes 'https://www.python.org' as default value. 'depth' takes '2'.

* Examples:

    1. python main.py -url https://www.python.org -depth 3
    2. python main.py -url https://www.python.org
    3. python main.py -depth 3
    4. python main.py 

* While crawling webpages, a timeout variable is used, which skips the indexing of current webpage if it could not be reached within 10 seconds.

* With different types of exception handling, at the end, the number of links crawled for a particular combination of a url and a depth may vary for different runs. This is due to the varying internet traffic upon the webpages being crawled.

* The final output of the list of links is written into 'output.txt' file

* OPEN ISSUE:

	The input url supplied should be a VALID one! The program will execute even if the format of input url is not proper.





