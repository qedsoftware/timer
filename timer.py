#!/usr/bin/env python

# timer.py
# 2013-07-10 
# William Wu 

# import packages
import sys, os, subprocess, getopt, time

# usage
def usage():
	print('Times how long it takes to run something, in seconds.')
	print('Usage:\n\t%s [cli-command]' % sys.argv[0])
	
# check that an argument has been provided
if len(sys.argv) < 2:
	usage()
	sys.exit()

# main method
def main(argv):

	try:
		opts, args = getopt.gnu_getopt(argv, "h", ["help"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
	command = "".join(args)

	t1 = time.time()
	os.system(command)
	t2 = time.time()
	print "Time elapsed: %lf" % (t2 - t1)

# invoke main
if __name__ == "__main__":
	main(sys.argv[1:])
