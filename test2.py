import sys


''' 
python test2.py
'''

if __name__ == '__main__':
    print("main name")
    branch = "22.9.0-SNAPSHOT"
    index = branch.find(".")
    print(index)
    branch = "NSI-r"+branch[(index - 2):(index + 2)]
    print(branch)
    #print(len(sys.argv))
    #print(sys.argv[0])
    #print(sys.argv[1])
    #main('hello')




