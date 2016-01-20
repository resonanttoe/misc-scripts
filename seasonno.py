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
        elif seriesdir.endswith('.mp4'):
          pass
        elif seriesdir.endswith('.m4v'):
          pass
        else:
          myseason = seriesdir.split(' ')
          if len(myseason) is 1:
            pass
          else:
            seasonno = seriesdir.split(' ')[1]
            if len(seasonno) is 1:
              originalname = os.path.join(basedir + subdir + '/' + seriesdir)
              seasonno = '0' + seasonno
              print 'Renaming %s' % basedir + subdir + '/' 'Season ' + seasonno
              newname = os.path.join(basedir + subdir + '/Season ' + seasonno)
              print 'Original - ', originalname
              os.rename(originalname, newname)

if __name__ == '__main__':
  main()