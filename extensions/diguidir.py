#/usr/bin/python
#--coding--:utf-8
import os
enter_dir = raw_input("Please input your dir:")
level = 1
space = ' '
def list_file(enter_dir,level):
	if os.path.isdir(enter_dir):
		list_path = os.listdir(enter_dir)
		for file in list_path:
			if level > 1:
				print ("|" + space*4)*(level-1)+"|__"+file
			else:
				print "|----",file
			if os.path.isdir(enter_dir+'/'+file):
				tree_level = level + 1
				list_file(enter_dir+'/'+file,tree_level)
	else:
		print "You enter dictory path is fialed, please retry...."
list_file(enter_dir,level)
