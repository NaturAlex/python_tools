import os



def findFile(path,version,keywords):
    file_list = os.listdir(path)
    for file_name in file_list:
         file_abs_path = os.path.join(path, file_name)
         if os.path.isdir(file_abs_path):
            # print('dir:'+file_abs_path)
            findFile(file_abs_path,version,keywords)
         else:
            if file_name.endswith('-SNAPSHOT.jar'):
                if version in file_name:
                   removeFileByKeyword(path,file_name,keywords)
                elif version=='all':
                    removeFileByKeyword(path,file_name,keywords)
                elif version=='':
                    print("no version select")

def removeFileByKeyword(path,file_name,keywords):
    if keywords[0] == 'all':
        removeFile(path,file_name)
        return
    for keyword in keywords:
        if keyword in file_name:
            removeFile(path,file_name)

def removeFile(path,file_name):
    file_abs_path = os.path.join(path, file_name)
    print ('file:'+file_abs_path)
    #os.remove(file_abs_path)
    pom_file=file_abs_path.replace(".jar",".pom")
    if os.path.exists(pom_file):
        print ('file:'+pom_file)
        #os.remove(pom_file)


def main():
    path1="C:\\repository\\"
    groupid="com.ericsson.cac.iam.v2"
    artifactoryId="tmo-iam-business"
    # keyword='autotest'
    version='1.0-NSI-r24.1-SNAPSHOT'
    groupid=groupid.replace(".", "\\")
    
    file_abs_path = os.path.join(path1, groupid, artifactoryId, version)
    print(file_abs_path);
    os.system(f'explorer {file_abs_path}')

if __name__ == "__main__":
    main()
