#!/usr/bin/env python
"""Shebang - when script executes, tells computer what program and in which directory to use."""

import os
import sys
import subprocess

def findmkv(basedir): 
	"""Returns a list of files that end in .mkv."""
	baselisting = os.listdir(basedir)
	mkvfiles = []
	for files in baselisting:
		if files.endswith('.mkv'):
			mkvfiles.append(files)
	return mkvfiles

def convertvideo(mkv):
	"""take one file to convert at a time, not all files since process will restart upon interruption"""
	handbrakecommand = "/Applications/HandbrakeCLI --all-audio -m -O -e 'x264' -i mkv -o  '${1%avi}'.mp4 --all-subtitles --subtitle-default=none --preset='Super HQ 1080p30 Surround'"
	subprocess.run(handbrakecommand)


def main():
	basedir = sys.argv[1]
	mkvlist = findmkv(basedir)
	for mkv in mkvlist:
		convertvideo(mkv)

	"""Go over base listing and get all the individual files.
	Baselisting is an iterable, for loop is iterating over it (baselisting) to produce files
	Function: what you want it to do (output), and what it needs to do it (input) """


if __name__ == '__main__':
	main() 

"""double underscore = private - shouldn't be accessible to any other script."""