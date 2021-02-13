# Expert System
This is a expert system which process a given set of information with a given set of rules

## Description
This program analyzes different types of tourists, and based on given data it acts like an expert to provide
the ability of their identification. It provides also a user interface, where all questions are multiple choice,
the concept of such method: it ask a series of questions based on different category where user gives all the facts
he knows, based on which the most suitable answer is found. At this point currently is a trade off: it can return more
than one response, it happens when a series of facts satisfies more than one tourist.

## Installation
You can just clone it and run it if you have python installed on your machine, after navigating to the project folder.
```
https://github.com/FilipAdrian/expert-system-AI.git
python main.py
```
## Base Principle
* Checks the ration of each category and starts with characteristic that has the highest occurrence.
* It does not check a category twice 
* Removes redundant answers