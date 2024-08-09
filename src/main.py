import shutil
import os
from logger import logger

def copy_all_contents(src_dir,dest_dir):
    logger.error("hello")
    if not os.path.exists(dest_dir):
        raise Exception(f"Directory {dest_dir} does not exist")
    input(f'Press any key to delete {dest_dir} directory and all contents...')
    
    #Delete dest_dir before copying
    # shutil.rmtree(dest_dir)

    contents = list(map(lambda x: f"{src_dir}/{x}",os.listdir(src_dir)))




copy_all_contents("","../static/test")
