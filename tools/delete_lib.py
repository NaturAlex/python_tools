#! /usr/bin/env python
import os
import argparse
'''
python ./tools/delete_lib.py --help
python tools/delete_lib.py --dependency Hero --version r21.8 --debug
python tools/delete_lib.py --keyword Hero --keyword r21.8 --debug
python tools/delete_lib.py --keyword Hero --keyword r23.7 --debug
'''
DEBUG = False
REPO_PATH = "C:\\repository\\com\\ericsson\\"
# REPO_PATH = "C:\\repository\\com\\ericsson\\nsi\\iam\\v2\\Hero"
wait_delete_file = set()


def findFile(path, keywords):
    file_list = os.listdir(path)  
    for file_name in file_list:
        file_abs_path = os.path.join(path, file_name)
        if os.path.isdir(file_abs_path):
            # print('dir:'+file_abs_path)
            findFile(file_abs_path,keywords)
        else:
            if all(str in file_name for str in keywords):
                wait_delete_file.add(path)
    

def deletefiles(wait_delete_file_set):
    print("There are {} dir path ready to delete".format(len(wait_delete_file_set)))
    for filedir in wait_delete_file_set:
        print("delete dir:" + filedir)
        wait_delete_files = os.listdir(filedir)
        for f in wait_delete_files:
            f = filedir+'/'+f
            print("ready to delete files: "+f)
            if not DEBUG:
                os.remove(f)
                print("delete success: "+f)


def main(depend, version,debug, keyword_array):
    # keyword='autotest'
    # version='all'
    # keywords=['token-validation']
    if not keyword_array or not len(keyword_array): 
        keywords = []
        keywords.append(depend)
        keywords.append(version)
    else:
        keywords = keyword_array
    findFile(REPO_PATH,keywords)
    deletefiles(wait_delete_file)


parser = argparse.ArgumentParser(usage='''delete local repo dependencies
    Eg: python delete_lib.py --dependency Hero --version r21.8 --debug  
        python delete_lib.py --dependency Hero --version r21.8
        python delete_lib.py --keyword Hero --keyword r21.8 --debug
        python delete_lib.py --keyword Hero --keyword r21.8''',
        description='''will loop repopath and find jar files by keywords or (dependency and version) e''')
parser.add_argument('--dependency', dest='depend', metavar='ex: Hero', type=str, help='dependency name')
parser.add_argument('--version', dest='version', metavar='ex: 21.4', type=str, help='dependency version')
# parser.add_argument('--debug', dest='debugStr', help='if true, only print not delete files')
parser.add_argument('--debug', dest='debugStr', action='store_true', help='if true, only print not delete files')
parser.add_argument('--keyword', dest='keywords', metavar='ex: --keyword hero --keyword 21.4', type=str, help='delete by keyword, higher priority than dependency', action='append')
try:
    args = parser.parse_args()
except Exception as e:
    print(e)

depend = args.depend
version = args.version
keyword_array = args.keywords
debug = args.debugStr
DEBUG = debug
print("DEBUG:" + str(DEBUG))
if __name__ == "__main__":
    try:
        main(depend, version, debug, keyword_array)
    except Exception as e:
        print(e)
    



