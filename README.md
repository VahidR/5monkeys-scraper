5monkeys-scraper
================

a 5monkeys.se website scraper

Description
-----------
This small tool scratches the http://www.5monkeys.se/ and builds a tree representation of the HTML elements on the page and then writes an 2-char indented hierarchical ASCII representation of the tree representation to stdout. 

The script would output something along the lines of:
```bash
$ ./fetch_5m.py
*** Fetching and parsing http://www.5monkeys.se/
[html]
  [head]
    [title]
    [/title]
    [meta /]
    [meta /]
    [meta /]
    [link /]
    [link /]
  [/head]
...
```

Attention
---------
I have written this tool on "Aug 7 2013". The site layout was not changed on "Sep 4 2013" too. Any change after this date, should be checked...
