import yaml
import os

''' 
python testuse/test5.py
'''

# def yaml_as_dict(my_file):
#   try:
#     my_dict = {}
#     with open(my_file, 'r') as fp:
#             docs = yaml.safe_load_all(fp)
#             for doc in docs:
#                 for key, value in doc.items():
#                     my_dict[key] = value
#     return my_dict
#   except Exception as e:
#     print("occur error:", e)
#     if os.path.exists(my_file):
#       with open(my_file, 'r') as f:
#         fc = f.read()
#         print("file content:")
#         print(fc)
#     raise e
def yaml_as_dict(my_file):
    my_dict = {}
    with open(my_file, 'r') as fp:
        try:
          fc = fp.read()
          docs = yaml.safe_load_all(fc)
          for doc in docs:
              for key, value in doc.items():
                  my_dict[key] = value
        except Exception as e:
            print("occur error:", e)
            print("file content:")
            print(fc)
            raise e
    return my_dict

if __name__ == '__main__':
  myfile='iam_config/eric-idm-ca-idv.config.yml'
  my_dict = yaml_as_dict(myfile)
  print(my_dict)



