import os
import argparse
'''
python ./remove_local_dependency.py
'''
delete = False
DEBUG = True
<<<<<<< HEAD
REPO_PATH="C:\\repository\\com\\ericsson\\"
# REPO_PATH = "C:\\repository\\com\\ericsson\\nsi\\iam\\v2\\Hero"
wait_delete_file = set()


def findFile(path, keywords):
=======
# REPO_PATH="C:\\repository\\com\\ericsson\\"
REPO_PATH="C:\\repository\\com\\ericsson\\nsi\\iam\\v2\\Hero"
wait_delete_file = set()


def findFile(path,keywords):
>>>>>>> 46667e3 (init)
    file_list = os.listdir(path)  
    for file_name in file_list:
        file_abs_path = os.path.join(path, file_name)
        if os.path.isdir(file_abs_path):
            # print('dir:'+file_abs_path)
<<<<<<< HEAD
            findFile(file_abs_path, keywords)
=======
            findFile(file_abs_path,keywords)
>>>>>>> 46667e3 (init)
        else:
            if all(str in file_name for str in keywords):
                wait_delete_file.add(path)
    

def deletefiles(wait_delete_file_set):
    print("There are {} dir path ready to delete".format(len(wait_delete_file_set)))
    for filedir in wait_delete_file_set:
        print("delete dir:"+filedir)
        wait_delete_files = os.listdir(filedir)
        for f in wait_delete_files:
            print("delete files: "+f)
        if not DEBUG:
            os.remove(f)
            
<<<<<<< HEAD
def main(depend, version, debug, keyword_array):
=======
def main(depend,version,debug,keyword_array):
>>>>>>> 46667e3 (init)
    # keyword='autotest'
    # version='all'
    # keywords=['token-validation']
    if not keyword_array or not len(keyword_array): 
        keywords = []
        keywords.append(depend)
        keywords.append(version)
    else:
        keywords = keyword_array
<<<<<<< HEAD
    DEBUG = debug
    findFile(REPO_PATH, keywords)
=======
    DEBUG=debug
    findFile(REPO_PATH,keywords)
>>>>>>> 46667e3 (init)
    deletefiles(wait_delete_file)

"""
python tools\clean_local_maven_repo.py --dependency Hero --version r21.8 --debug true
python tools\clean_local_maven_repo.py --help
python tools\clean_local_maven_repo.py --keyword Hero --keyword r21.8 --debug true

"""
parser = argparse.ArgumentParser(usage="delete local repo dependencies", description='delete local repo dependencies')
parser.add_argument('--dependency',dest='depend', metavar='Hero', type=str, help='dependency name')
parser.add_argument('--version',dest='version', metavar='21.4', type=str, help='dependency name')
parser.add_argument('--debug',dest='debug', metavar='True', type=bool, help='if true, only print not delete files',required=True, default=False, choices=[True,False])
parser.add_argument('--keyword',dest='keywords', metavar='--keyword hero --keyword 21.4', type=str, help='delete by keyword',action='append')
try:
    args = parser.parse_args()
except Exception as e:
    print(e)

<<<<<<< HEAD
depend = args.depend
version = args.version
debug  = args.debug
keyword_array = args.keywords
if __name__ == "__main__":
    try:
        main(depend, version, debug, keyword_array)
=======
depend=args.depend
version=args.version
debug=args.debug
keyword_array=args.keywords
if __name__ == "__main__":
    try:
        main(depend,version,debug,keyword_array)
>>>>>>> 46667e3 (init)
    except Exception as e:
        print(e)
    



