5monkeys-scraper
================

a 5monkeys.se website scraper

Story
-----
Sometimes ago, I got an interview test from www.5monkeys.se. Within the test, they asked me to write a python script that scrapes their website based on some requirements that they asked for. 
I implemented the the code as sent it at the same "day", but NEVER got any feedback, neither positive, nor negative!!

Here is the task description and my solution... Feel free to copy and get the core idea behind it... It's GPLv2, so have fun :)


Description
-----------
Write a Python script that fetches http://www.5monkeys.se/ and builds a tree representation of the HTML elements on the page and then writes an 2-char indented hierarchical ASCII representation of the tree representation to stdout? You are free to use whatever open-source Python libraries you feel are appropriate for the task at hand :-)

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
