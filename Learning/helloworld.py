''' 
    python helloworld.py
    python helloworld.py 123 456
'''
import sys

script_name = sys.argv[0]

args = sys.argv[1:]

if __name__ == '__main__':
    print('hello world')
    print(args)