import shutil
import os
from logger import logger
from markdown_blocks import markdown_to_html_node
from markdown_to_textnode import extract_title

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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Open the file in read mode
    with open(from_path, 'r') as md_file:
        md_contents = md_file.read()
    with open(template_path, 'r') as template_file:
        template_contents = template_file.read()
    
    html_str = markdown_to_html_node(md_contents).to_html()
    title = extract_title(md_contents)
    
    html_contents = template_contents.replace("{{ Title }}",title).replace("{{ Content }}",html_str)

    with open(dest_path,'w') as html_file:
        html_file.write(html_contents)

def generate_pages_recursive(from_path, template_path, dest_path):
    for filename in os.listdir(from_path):
        file_path_src = os.path.join(from_path, filename)
        file_path_dest = os.path.join(dest_path, filename).replace('.md','.html')
        
        if os.path.isdir(file_path_src):
            if not os.path.exists(file_path_dest):
                os.makedirs(file_path_dest)
            logger.info(f"Copying directory {file_path_src}...")
            generate_pages_recursive(file_path_src, template_path, file_path_dest)
        else:
            logger.info(f"Generating page from {file_path_src} to {file_path_dest} using {template_path}")
            # Open the file in read mode
            with open(file_path_src, 'r') as md_file:
                md_contents = md_file.read()
            with open(template_path, 'r') as template_file:
                template_contents = template_file.read()
            
            html_str = markdown_to_html_node(md_contents).to_html()
            title = extract_title(md_contents)
            
            html_contents = template_contents.replace("{{ Title }}",title).replace("{{ Content }}",html_str)

            with open(file_path_dest,'w') as html_file:
                html_file.write(html_contents)

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

from_path = "../content"
template_path = "../template.html"
dest_path = "../public"

from_path_abs = os.path.abspath(os.path.join(script_dir, from_path))
template_path_abs = os.path.abspath(os.path.join(script_dir, template_path))
dest_path_abs = os.path.abspath(os.path.join(script_dir, dest_path))

# generate_page(from_path_abs, template_path_abs, dest_path_abs)
generate_pages_recursive(from_path_abs, template_path_abs, dest_path_abs)
