<!-- omit in toc -->
# Python 3 Bootcamp

<!-- omit in toc -->
## Description

Course [slides](https://drive.google.com/drive/folders/1CKqOQzst1cGURXGiRVivi2Xsc0n-X8CR?usp=sharing). Course [Python 3 notebooks](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp). Older [Python 2 notebooks](https://github.com/jmportilla/Complete-Python-Bootcamp) for reference.

<!-- omit in toc -->
## Table of Contents

- [1. Overview](#1-overview)
- [2. Introduction](#2-introduction)
- [3. Data Types](#3-data-types)
  - [3.1. Numbers](#31-numbers)
  - [3.2. Variable Assigments](#32-variable-assigments)
  - [3.3. Strings](#33-strings)
    - [3.3.1. Indexing](#331-indexing)
    - [3.3.2. Slicing](#332-slicing)
    - [3.3.3. Immutability](#333-immutability)

# 1. Overview

<details>
<summary>Overview of the course.</summary>
- Introduction
  - Python 2 vs Python 3
  - How to approach course
- Python setup
  - Installation
  - Environment selection
  - Jupyter notebook
  - Learning resources
  - Github
- Object and data structure basics
  - Numbers
  - Strings
  - Lists
  - Dictionaries
  - Tuples
  - Files
  - Sets
  - Booleans
- Comparison operators
  - Basic operators
  - Chained comparison operators
- Python Statements
  - If, elif, and else
  - For loops
  - While loops
  - range()
  - List comprehension
- Methods and Functions
  - Methods
  - Functions
  - Lambda expressions
  - Nested statements
  - Scope
- OOP
  - Objects
  - Classes
  - Methods
  - Inheritance
  - Special methods
- Errors and exception handling
  - Errors
  - Exceptions
  - Try
  - Except
  - Finally
- Modules and Packages
  - Creating modules
  - Installing modules
  - Exploring the Python ecosystem
- Built-in Functions
  - map
  - reduce
  - filter
  - zip
  - enumerate
  - all and anz
  - complex
- Decorators in Python
- Python Generators
  - Iteration vs generation
  - Creating generators
- Advanced Bonus Content
  - Advanced Python modules
  - Advanced Python object and data structures
  - Level up your knowledge
<details>

# 2. Introduction

<detail>
<summary>Why Choose Python?</summary>

- Designed for clear, logical code that is easy to read and learn.
- Lots of existing libraries and frameworks written in Python allowing users to apply Python to a wide variety of tasks.
- Focuses on optimizing developer time, rather than a computer's processing time.
- Great documentation online.
</detail>

-
<detail>
<summary>What can you do with Python?</summary>
- This course first focuses on "base" Python, which consists of the core components of the language and writing scripts and small programs.
- Later we begin to learn about outside libraries and frameworks that greatly expand Python's capabilities.
- Automate simple tasks
  - Searching for files and editing them
  - Scraping information from a website
  - Reading and editing excel files
  - Work with PDFs
  - Automate emails and text messages
  - Fill out forms
- Data Science and Machine Learning
  - Analyze large data files
  - Create visualizations
  - Perform machine learning tasks
  - Create and run predictive algorithms
- Create websites
  - Use web frameworks such as Django and Flask to handle the backend of a website and user data
  - Create interactive dashboards for users
</detail>

No Install Options

- [Jupyter Try](https://jupyter.org/try)
- [Replit](https://replit.com/)
- [Kaggle](https://www.kaggle.com/code)
- [Google Collab](https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index#recent=true)

There are several ways to run Python code. First let's discuss the various options for development environments.
<detail>
<summary>There are 3 main types of environments.</summary>

- Text Editors (VS Code)
  - General editors for any text file
  - Work with variety of file types
  - Can be customized with plugins and add-ons
  - Keep in mind, most are not designed with only Python in mind.
- Full IDEs (PyCharm, Spyder)
  - Development Environments designed specifically for Python.
  - Larger programs.
  - Only community editions are free.
  - Designed specifically for Python, lots of extra functionality.
- Notebook Environments (Jupyter Notebook)
  - Great for learning.
  - See input and output next to each other.
  - Support in-line markdown notes, visualizations, videos, and more.
  - Special file formats that are not .py
</detail>

# 3. Data Types

| Name           | Type  | Description                                                       |
| -------------- | ----- | ----------------------------------------------------------------- |
| Integers       | int   | Whole numbers, such as: 3 300 200                                 |
| Floating point | float | Numbers with decimal point: 2.3 4.6 100.0                         |
| Strings        | str   | Ordered sequence of characters: "hello" 'Sammy' "2000" "93 Cl™    |
| Lists          | list  | Ordered sequence of objects: [10, "hello",200.3]                  |
| Dictionaries   | dict  | Unordered Key:Value pairs: ("mykey" :"value" ,"name" : "Frankie") |
| Tuples         | tup   | Ordered immutable sequence of objects: (10,"hello",200.3)         |
| Sets           | set   | Unordered collection of unique objects: ("a","b")                 |
| Booleans       | bool  | Logical value indicating True or False                            |

## 3.1. Numbers

There are two main number types we will work with:

- Integers which are whole numbers.
- Floating Point numbers which are numbers with a decimal.

Notes:

- [Issues and limitations of floating point arithmetic](https://docs.python.org/2/tutorial/floatingpoint.html).
- [Caret operator](https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-in-python-do)

## 3.2. Variable Assigments

Rules for variable names

- Names can not start with a number.
- There can be no spaces in the name, use `_` instead.
- Can't use any of these symbols `:",<>?\()!@#$%^&*~-+`
- It's considered best practice (PEP8) that names are lowercase.
- Avoid using words that have special meaning in Python like "list" and "str"

Python uses Dynamic Typing. This means you can reassign variables to different data types. This makes Python very flexible in assigning data types, this is different than other languages that are "Statically-Typed"

- Pros of Dynamic Typing:
  - Very easy to work with
  - Faster development time
- Cons of Dynamic Typing:
  - May result in bugs for unexpected data types!
  - You need to be aware of `type()`

## 3.3. Strings

Strings are sequences of characters, using the syntax of either single quotes or double quotes.Because strings are **ordered sequences** it means we can using **indexing** and **slicing** to grab sub-sections of the string.

### 3.3.1. Indexing

Indexing notation uses `[ ]` notation after the string (or variable assigned the string). Indexing allows you to grab a single character from the string. These actions use `[]` square brackets and a number index to indicate positions of what you wish to grab.

| Character:     | h   | e   | l   | l   | o   |
| -------------- | --- | --- | --- | --- | --- |
| Index:         | 0   | 1   | 2   | 3   | 4   |
| Reverse Index: | -5  | -4  | -3  | -2  | -1  |

### 3.3.2. Slicing

Slicing allows you to grab a subsection of multiple characters, a "slice" of the string. This has the following syntax:

```python
[start:stop:step]
```

- `start` is a numerical index for the slice start.
- `stop` is the index you will go up to (but not include).
- `step` is the size of the "jump" you take.

### 3.3.3. Immutability

Continue here!
