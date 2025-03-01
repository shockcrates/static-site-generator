from textnode import *
from htmlnode import HTMLNode, ParentNode, LeafNode
import os
import shutil





def copy_from_src_to_dest_dir(src, dest):
	try:
		if not os.path.exists(dest):
			raise FileExistsError("Destination Dir does not exist")
		if not os.path.exists(src):
			raise FileExistsError("Source Dir does not exist")
		
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

def recursive_copy(src_file, dest):
	if os.path.isfile(src_file):
		print("copied: " + src_file)
		shutil.copy(src_file,dest)

	src_contents = os.listdir(src_file)

	
	for file in src_contents:
		file_path = os.path.join(src_file,file)
		if os.path.isfile(file_path):
			print("Copying File: " + file_path + " - to destination: " + dest)
			shutil.copy(file_path,dest)
			print("Copy successful")
		else:
			dest_path = os.path.join(dest,file)
			print("Creating new dest folder: " + dest_path)
			os.mkdir(dest_path)
			recursive_copy(file_path,dest_path)

def main():
	#dummy = TextNode("We out here", TextType.BOLD, "sunny.com")
	#node = HTMLNode("p", 'this is value', ['object1', 'object2'], {"href": "https://www.google.com", "target": "_blank"})
	#print(repr(node))
	#print("*this* will not go *well*".split("*"))

	dest = "./public"
	src = "./static"

	copy_from_src_to_dest_dir(src, dest)

main()