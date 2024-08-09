import shutil
import os
from logger import logger

def delete_contents_of_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                logger.info(f"Removing file {file_path}")
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                logger.info(f"Removing directory {file_path}")
                shutil.rmtree(file_path)
        except Exception as e:
            logger.error(f'Failed to delete {file_path}. Reason: {e}')

def copy_all_contents(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        raise Exception(f"Directory {dest_dir} does not exist")
    
    # Uncomment this line if you want to delete contents of dest_dir before copying
    delete_contents_of_directory(dest_dir)
    
    for filename in os.listdir(src_dir):
        file_path_src = os.path.join(src_dir, filename)
        file_path_dest = os.path.join(dest_dir, filename)
        
        if os.path.isdir(file_path_src):
            if not os.path.exists(file_path_dest):
                os.makedirs(file_path_dest)
            logger.info(f"Copying directory {file_path_src}...")
            copy_all_contents(file_path_src, file_path_dest)
        else:
            logger.info(f"Copying file {file_path_src} to {file_path_dest}")
            shutil.copy2(file_path_src, file_path_dest)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
logger.info(f"script_dir: {script_dir}")

src_dir = "../static"
dest_dir = "../public"

# Convert relative paths to absolute paths based on the script's directory
src_dir_abs = os.path.abspath(os.path.join(script_dir, src_dir))
dest_dir_abs = os.path.abspath(os.path.join(script_dir, dest_dir))

logger.info(f'src_dir: {src_dir_abs}')
logger.info(f'dest_dir: {dest_dir_abs}')

# Uncomment this line if you want to delete contents of dest_dir before copying
delete_contents_of_directory(dest_dir_abs)

# Recursively copy all contents from src_dir to dest_dir
copy_all_contents(src_dir_abs, dest_dir_abs)
