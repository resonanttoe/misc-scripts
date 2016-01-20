#!/usr/bin/env python

import os
import sys

def main():
  basedir = sys.argv[1]
  for subdir in os.listdir(basedir):
    if os.path.isdir(os.path.join(basedir + subdir)):
      for seriesdir in os.listdir(basedir + subdir):
        if seriesdir.startswith('.'):
          pass
        if seriesdir.startswith('Series'):
          seasonno = seriesdir.split(' ')[1]
          print 'Renaming %s' % basedir + subdir + '/' 'Season ' + seasonno
          originalname = os.path.join(basedir + subdir + '/' + seriesdir)
          newname = os.path.join(basedir + subdir + '/Season ' + seasonno)
          os.rename(originalname, newname)


if __name__ == '__main__':
  main()