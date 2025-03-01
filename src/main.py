from textnode import *
from htmlnode import HTMLNode, ParentNode, LeafNode
from document_processor import *
import os
import shutil
import sys


def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line.split(" ",1)[1]
	raise Exception("No Header Found in markdown file")


def generate_page(from_path, template_path, dest_path, basepath):
	print(f'Generating page from {from_path} to {dest_path} using template {template_path}')

	if not os.path.exists(from_path):
		raise FileNotFoundError("From path does not exist")
	
	with open(from_path,'r',) as file:
		markdown = file.read()
	

	print(f"markdown copied from {from_path}")

	title = extract_title(markdown)

	nodes = markdown_to_htmlnode(markdown)

	#print(nodes)

	HTML = nodes.to_html()

	with open(template_path,'r') as file:
		template = file.read()
	

	print("Template read")

	title_filled_template = template.replace("{{ Title }}", title)
	filled_template = title_filled_template.replace("{{ Content }}", HTML)
	base_filled_template = filled_template.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

	if not os.path.exists(os.path.dirname(dest_path)):
		#print("THE PATH YOU SEEK: " + os.path.dirname(dest_path))
		os.makedirs(os.path.dirname(dest_path))

	with open(dest_path,'w') as file:
		file.write(base_filled_template)

	print(f"Content successfuly written to {dest_path}")
	


def copy_from_src_to_dest_dir(src, dest):
	try:
		
		if not os.path.exists(src):
			raise FileExistsError("Source Dir does not exist")
		if not os.path.exists(dest):
			os.makedirs(dest)
		
		if os.path.isfile(dest):
			raise NotADirectoryError("Dest is not a directory")
		if os.path.isfile(src):
			raise NotADirectoryError("Source is not a directory")
	except FileExistsError as e:
		print(e)
		return None
	
	dest_contents = os.listdir(dest)
	shutil.rmtree(dest)
	os.mkdir(dest)

	#shutil.copy(src,dest)

	print(repr(os.listdir(src)))

	recursive_copy(src,dest)

def recursive_copy(src_file, dest, template="./template.html"):
	if os.path.isfile(src_file):
		print("copied: " + src_file)
		shutil.copy(src_file,dest)

	src_contents = os.listdir(src_file)

	
	for file in src_contents:
		file_path = os.path.join(src_file,file)
		
		if os.path.isfile(file_path):
			print("Copying File: " + file_path + " - to destination: " + dest)
			file_name, extension = os.path.splitext(file)
			if extension != ".md":
				shutil.copy(file_path,dest)
				print("Copy successful")
			else:
				dest_path = os.path.join(dest, f"{file_name}.html")
				generate_page(file_path,template, dest_path)
		else:
			dest_path = os.path.join(dest,file)
			print("Creating new dest folder: " + dest_path)
			os.mkdir(dest_path)
			recursive_copy(file_path,dest_path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
	src_contents = os.listdir(dir_path_content)

	
	for file in src_contents:
		file_path = os.path.join(dir_path_content,file)
		
		if os.path.isfile(file_path):
			print("Copying File: " + file_path + " - to destination: " + dest_dir_path)
			file_name, extension = os.path.splitext(file)
			if extension != ".md":
				shutil.copy(file_path,dest_dir_path)
				print("Copy successful")
			else:
				dest_path = os.path.join(dest_dir_path, f"{file_name}.html")
				generate_page(file_path,template_path, dest_path, basepath)
		else:
			dest_path = os.path.join(dest_dir_path,file)
			print("Creating new dest folder: " + dest_path)
			os.mkdir(dest_path)
			generate_pages_recursive(file_path,template_path, dest_path,basepath)


def initialize_site(basepath):
	dest = "docs"
	src = "static"

	copy_from_src_to_dest_dir(src, dest)

	generate_pages_recursive("content","template.html",dest, basepath)

	

def main():
	#dummy = TextNode("We out here", TextType.BOLD, "sunny.com")
	#node = HTMLNode("p", 'this is value', ['object1', 'object2'], {"href": "https://www.google.com", "target": "_blank"})
	#print(repr(node))
	#print("*this* will not go *well*".split("*"))

	""" dest = "./public"
	src = "./static"

	copy_from_src_to_dest_dir(src, dest)

	contents = os.listdir("./content")

	generate_page("./content/index.md", "./template.html","./public/index.html") """
	basepath = '/'
	if len(sys.argv) > 1:
		if sys.argv[1]:
			basepath = sys.argv[1]
		else:
			basepath = '/'
	print(basepath)
	initialize_site(basepath)

main()