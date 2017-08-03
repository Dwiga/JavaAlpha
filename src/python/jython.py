import sys

"""def main(arg1, arg2, arg3):
    if len(arg1) > 0 and len(arg2) > 0 and len(arg3) > 0:
        aFunc(arg1, arg2, arg3)"""
        
def aFunc(arg1, arg2, arg3):
    # @type arg1 
    a = int(arg1) * int(arg2) * int(arg3)
    print(a)
    
aFunc(sys.argv[0], sys.argv[1], sys.argv[2])