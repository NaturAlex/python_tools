''' 
    python data_type.py
'''

def main():
    num = 5
    print(type(num))
    num_str = str(num)
    string = "6"
    bool_true = True
    bool_str = "0"
    print(num_str)
    print(int(string))
    print(str(bool_true))
    # 只有空转bool为False, 其他都为true, python bool的True和False都要首字母大写
    print(bool(''))
    print(bool(None))
    print(bool('False')) #返回true

if __name__ == '__main__':
    main()
    