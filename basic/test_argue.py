import argparse
# from typing_extensions import Required

''' 
python basic/test_argue.py -h
python basic/test_argue.py 123 --key my_int_key --num 1 --num 2 --drink tea
python basic/test_argue.py 123 --key my_int_key --num 1 --num 2 --drink tea --notdebug
python basic/test_argue.py 123 --key my_int_key --num 1 --num 2 --drink tea --debug
'''

def main(args):
    mykey = args.mykey
        
      

parser = argparse.ArgumentParser(usage="test argue", description='test argue how to use')
# metavar ,示例值
parser.add_argument('first_param', metavar='1', type=int, nargs='?',
                    help='an integer for the accumulator')
parser.add_argument('--key',type=str, dest='mykey',  default="k",
                    help='string, only print')
# array param
parser.add_argument('--num',type=int, dest='num_array', help='int num array', action='append', required=True)
# choic param
parser.add_argument('--drink', type=str, dest='drink', help='tea or coffee', choices=['tea','coffee'])
# bool param
parser.add_argument('--debug',  dest='debug', help='is debug', action='store_true', default=True)
parser.add_argument('--notdebug',  dest='debug', help='not deubg',action='store_false', default=False)

args = parser.parse_args()
print('args:{}'.format(args)) #Namespace(first_param=123, mykey='my_int_key')
print('args.mykey:{}'.format(args.mykey))
print('args.num_array:{}'.format(args.num_array))
if args.debug:
    print('args.debug:{}'.format(args.debug))
if __name__ == '__main__':
    main(args)
    