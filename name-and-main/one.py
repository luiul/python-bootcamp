def func(): 
    print("func() in one.py")

print("Top level in one.py")

if __name__ == '__main__': 
    print('one.py is being rund directly')
    print(__name__)
else: 
    print('one.py has been imported')
    print(__name__)