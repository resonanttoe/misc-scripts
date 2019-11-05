#!/usr/bin/env python

import os
import sys

def main():
  basedir = sys.argv[1]
  for (dirpath, dirnames, filenames) in os.walk(basedir):
    for files in filenames:
      if files.startswith('.'):
        pass
      else:
        name, ext = files.split('.')
        print "Renaming to WWE - Pay-per-views - SxxExx - " + name + ' - ' \
              + dirpath.split('/')[5] + '.' + ext
        originalname = os.path.join(dirpath + '/' + files)
        newname = os.path.join(dirpath + '/' + "WWE - Pay-per-views - SxxExx - " + name + ' - ' \
              + dirpath.split('/')[5] + '.' + ext)
        os.rename(originalname, newname)

if __name__ == '__main__':
  main()