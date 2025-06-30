import glob, shutil, sys,os
print("hello world")
load_case_dir  = os.getcwd()
common_files_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(common_files_dir)
print(f"copying all relevant files from {common_files_dir} to  {load_case_dir}")
