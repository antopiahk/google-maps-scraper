import os
import shutil
import subprocess

from tqdm import tqdm
from city_queries import city_queries
import csv_utils
from distutils import dir_util

# specify the number of parallel terminal windows you want to open
PARELLEL_OPRATIONS = 6

# specify your source directory
source_dir = 'template_scraping_folder'

# cache directory to copy to each destination directory
cache_dir = 'cache'

# specify the base name for your destination directories
dest_base = 'caffeino_scraping'

# calculate the length of each part
part_len = len(city_queries) // PARELLEL_OPRATIONS

# create the ranges
ranges = [(i * part_len, (i + 1) * part_len - 1) for i in range(PARELLEL_OPRATIONS)]

processes = []

# Create the destination directories and run the processes
def begin_scraping():
    for i in range(PARELLEL_OPRATIONS):
        # create the destination directory name
        dest_dir = f"{dest_base}_{i+1}"

        # copy the template directory to the destination directory
        # copy_with_progress(source_dir, dest_dir)
        dir_util.copy_tree(source_dir, dest_dir)

        # delete everything in the destination directory except 'output' and 'cache' to keep same as template
        for item in tqdm(os.listdir(dest_dir)):
            if item not in ['output', 'cache']:
                item_path = os.path.join(dest_dir, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

        # copy the template directory to the destination directory
        dir_util.copy_tree(source_dir, dest_dir)

        # copy the cache directory into the template directory to prevent double scraping existing data
        # shutil.copytree(cache_dir, os.path.join(source_dir, cache_dir))

        # get the start and end range
        start, end = ranges[i]

        # specify the path to the Python interpreter in the venv
        python_path = os.path.join(os.path.dirname(__file__), 'venv', 'Scripts', 'python')
        
        # run the main.py script and store the process
        print("Calling Popen for folder: ", i)
        
        process = subprocess.Popen([python_path,  "main.py", str(start), str(end)], cwd=dest_dir,creationflags=subprocess.CREATE_NEW_CONSOLE)
        processes.append(process)

    # wait for all processes to complete
    for process in processes:
        process.wait()


def copy_with_progress(src, dst):
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        files = os.listdir(src)
        for file in tqdm(files, desc=f'Copying {src}'):
            src_file = os.path.join(src, file)
            dst_file = os.path.join(dst, file)
            copy_with_progress(src_file, dst_file)
    else:
        with tqdm(total=os.path.getsize(src), unit='B', unit_scale=True, desc=src) as pbar:
            with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
                for chunk in iter(lambda: fsrc.read(1024*1024), b''):  # 1MB chunks
                    fdst.write(chunk)
                    pbar.update(len(chunk))


# Collect the results from all the folders and merge them into one
def merge_folders():
    csv_utils.combine_csv_files('.', 'output/all/csv/merged-all-2.csv')


begin_scraping()
# merge_folders()