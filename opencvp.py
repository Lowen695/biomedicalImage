# import os
# from contextlib import contextmanager
#
# @contextmanager
# def change_dir(destination):
#     try:
#         cwd = os.getcwd()
#         os.chdir(destination)
#         yield
#     finally:
#         os.chdir(cwd)
#
# with change_dir('sample_path'):
#     print(os.listdir())
import os

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASS')

print(user)
print(password)


