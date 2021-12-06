

""" 
python basic/array_test.py
"""
def main():
    arr = ['1','2'] 
    word = '123456'
    all_exists = any(str in word for str in arr)
    print('all_exists:{}'.format(all_exists))

    arr=['Hero','r21.8']
    word='Hero-1.0-NSI-r21.8-20211201.035759-95'
    all_exists = any(str in word for str in arr)
    print('all_exists:{}'.format(all_exists))

if __name__ == '__main__':
    main()
    