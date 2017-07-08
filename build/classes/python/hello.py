import sys

def main(arg1, arg2, arg3):
    aFunction(arg1, arg2, arg3)

def aFunction(arg1, arg2, arg3):
    print "calling python function with paramters:"
    print arg1
    print arg2
    print arg3
    
aFunction(sys.argv[0], sys.argv[1], sys.argv[2])