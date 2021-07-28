<!-- omit in toc -->
# 🐍 Python3 Bootcamp

<!-- omit in toc -->
## Description

Learn how to use Python for real-world tasks, such as working with PDF files, sending emails, reading Excel files, Scraping websites for informations, working with image files, and much more. Course [slides](https://drive.google.com/drive/folders/1CKqOQzst1cGURXGiRVivi2Xsc0n-X8CR?usp=sharing). Course [Python 3 notebooks](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp). Older [Python 2 notebooks](https://github.com/jmportilla/Complete-Python-Bootcamp) for reference.

<!-- omit in toc -->
## Table of Contents

- [1. Overview and Introduction](#1-overview-and-introduction)
- [2. Data Types](#2-data-types)
  - [2.1. Numbers](#21-numbers)
  - [2.2. Variable Assigments](#22-variable-assigments)
  - [2.3. Strings](#23-strings)
    - [2.3.1. Indexing](#231-indexing)
    - [2.3.2. Slicing](#232-slicing)
    - [2.3.3. Immutability](#233-immutability)
  - [2.4. Lists](#24-lists)
  - [2.5. Dictionaries](#25-dictionaries)
  - [2.6. Tuples](#26-tuples)
  - [2.7. Sets](#27-sets)
  - [2.8. Booleans](#28-booleans)
  - [2.9. I/O with Basic Files](#29-io-with-basic-files)
  - [2.10. Useful Links](#210-useful-links)
- [Python Statements](#python-statements)
  - [If, Elif, Else Statements](#if-elif-else-statements)
  - [For Loops (and Tuple Unpacking)](#for-loops-and-tuple-unpacking)
  - [WHile Loop](#while-loop)

# 1. Overview and Introduction

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
</details>

<details>
<summary>Why Choose Python?</summary>
- Designed for clear, logical code that is easy to read and learn.
- Lots of existing libraries and frameworks written in Python allowing users to apply Python to a wide variety of tasks.
- Focuses on optimizing developer time, rather than a computer's processing time.
- Great documentation online.
</details>

<details>
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
</details>

No Install Options

- [Jupyter Try](https://jupyter.org/try)
- [Replit](https://replit.com/)
- [Kaggle](https://www.kaggle.com/code)
- [Google Collab](https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index#recent=true)

There are several ways to run Python code. First let's discuss the various options for development environments.
<details>
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
</details>

# 2. Data Types

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

## 2.1. Numbers

There are two main number types we will work with:

- Integers which are whole numbers.
- Floating Point numbers which are numbers with a decimal.

Notes:

- [Issues and limitations of floating point arithmetic](https://docs.python.org/2/tutorial/floatingpoint.html).
- [Caret operator](https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-in-python-do)

## 2.2. Variable Assigments

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

## 2.3. Strings

Strings are sequences of characters, using the syntax of either single quotes or double quotes.Because strings are **ordered sequences** it means we can using **indexing** and **slicing** to grab sub-sections of the string.

### 2.3.1. Indexing

Indexing notation uses `[ ]` notation after the string (or variable assigned the string). Indexing allows you to grab a single character from the string. These actions use `[]` square brackets and a number index to indicate positions of what you wish to grab.

| Character:     | h   | e   | l   | l   | o   |
| -------------- | --- | --- | --- | --- | --- |
| Index:         | 0   | 1   | 2   | 3   | 4   |
| Reverse Index: | -5  | -4  | -3  | -2  | -1  |

### 2.3.2. Slicing

Slicing allows you to grab a subsection of multiple characters, a "slice" of the string. This has the following syntax:

```python
[start:stop:step]
```

- `start` is a numerical index for the slice start.
- `stop` is the index you will go up to (but not include).
- `step` is the size of the "jump" you take.

### 2.3.3. Immutability

String are immutable, i.e. Strings are not mutable! (meaning you can't use indexing to change individual elements of a string). String object does not support item assignment. Once a the characters in the strings are defined, you can not change them. If we want to reassign one of the characters, we have to do it with concatenation. Useful methods for strings:

```python
str.upper()
str.lower()
str.spilt()
```

[Pyformat](https://pyformat.info/).

## 2.4. Lists

Lists are ordered sequences that can hold a variety of object types. They use `[]` brackets and commas to separate objects in the list. Lists support indexing and slicing. Lists car be nested and also have a variety of useful methods that can be called off of them. Lists are mutable.

## 2.5. Dictionaries

Dictionaries are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead. This key-value pair allows users to quickly grab objects without needing to know an index location.

- Dictionaries: Objects retrieved by key name. Unordered and can not be sorted.
- Lists: Objects retrieved by location. Ordered Sequence can be indexed or sliced.

## 2.6. Tuples

Tuples are very similar to lists. However they have one key difference immutability. Once an element is inside a tuple, it can not be reassigned. Tuples use parenthesis: `(1,2,3)`.

## 2.7. Sets

Sets are unordered collections of unique elements. Meaning there can only be one representative of the same object.

## 2.8. Booleans

Booleans are operators that allow you to convey `True` or `False` statements. These are very important later on when we deal with **control flow** and **logic**.

## 2.9. I/O with Basic Files

Reading, Writing, Appending Modes:
- `mode='r'` is read only
- `mode='w'` is write only (will overwrite files or create new!)
- `mode='a'` is append only (will add on to files)
- `mode='r+'` is reading and writing
- `mode= 'w+'` is writing and reading (Overwrites existing files or creates new file!)

## 2.10. Useful Links

- [Best Practice](http://codingbat.com/python)
- [More Mathematical (and Harder) Practice](https://projecteuler.net/archives)
- [List of Practice Problems](http://www.codeabbey.com/index/task_list)
- [A SubReddit Devoted to Daily Practice Problems](https://www.reddit.com/r/dailyprogrammer)
- [A very tricky website with very few hints and touch problems (Not for beginners but still interesting)](http://www.pythonchallenge.com/)

# Python Statements

Let's begin to learn about **control flow** We often only want certain code to execute when a particular condition has been met (condition -> action).

## If, Elif, Else Statements

To control this flow of logic we use some keywords:

- `if`
- `elif`
- `else`

Control Flow syntax makes use of colons and indentation (whitespace). This indentation system is crucial to Python and is what sets it apart from other programming languages.

## For Loops (and Tuple Unpacking)

Many objects in Python are "iterable", i.e. we can iterate over every element in the object, e.g. every element in a list or every character in a string. We can use `for` loops to execute a block of code for every iteration.

The term iterable means you can "iterate" over the object, e.g. you can iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary. Basic syntax:

```python
my_iterable = [1,2,3]
for item_name in my_iterable:
  do_something(item_name)
```

See notebook to read about tuple unpacking.

## WHile Loop

While loops will continue to execute a block of code while some condition remains `True`. For example, while my pool is not full, keep filling my pool with water. Basic syntax:

```python
while bool_cond:
  # do something
```

