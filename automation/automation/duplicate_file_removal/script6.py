from sys import *
import os
import hashlib
import os.path
from os import path

def CalculateChecksum(path, blocksize=1024):
	fd = open(path,'rb')
	hobj = hashlib.md5()

	buffer = fd.read(blocksize)
	while len(buffer)>0:
		hobj.update(buffer)
		buffer = fd.read(blocksize)

	fd.close()
	return hobj.hexdigest()	

def DirectoryTraversal(path):
	print("Contents of the directory are")
	duplicate = {}
	for Folder, Subfolder, Filename in os.walk(path):
		print("Directory name is:" +Folder)
		for sub in Subfolder:
			print("Subfolder of " +Folder+ " is " + sub)
		for file in Filename:
			print("File name is:"+file)
			actualpath = os.path.join(Folder,file)
			hash = CalculateChecksum(actualpath)
			#print(hash)

			if hash in duplicate:
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash]=[actualpath]	
	return duplicate

def DisplayDuplicate(duplicate):
	output = list(filter(lambda x: len(x)>1,duplicate.values()))

	if(len(output)>0):
		print("There are duplicate files")
	else:
		print("There are no duplicate files")
		return
	i = 0	
	icnt = 0
	for result in output:
		icnt = 0
		#print(result)
		for path in result:
			icnt+=1
			if icnt>=2:
				i+=1
				os.remove(path)
	print("Number of files deleted are:",i)				
def main():
	print("Marvellous infosystems")
	print("Directory traversel script")

	if(len(argv)!=2):
		print("Error:Invalide number of arguments")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("It is a directory cleaner script")
		exit()
	
	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage :Provide the absolute path of directory")
		exit()
	    
	arr={}
	if path.exists(argv[1])==True:
		print("############ Path exist ###########")
		print(argv[1])
		if os.path.isabs(argv[1])==True:
			print("############ Path is absolute ###########")
			arr = DirectoryTraversal(argv[1])
		else:
			print("Path is not absolute")	
		
	DisplayDuplicate(arr)
if __name__ == '__main__':
	main()	


#check path is existing or not.
#check path is absolute or not
#if not make it absolute
#total number of files scanned,duplicate, and deleted print as statistics
#ask user before deleting file