import gitdump as gd
import os
import argparse
import sys


def parser(help=False):
  
  parser = argparse.ArgumentParser(description='Dump all repos of a github account at once.')

  
  parser.add_argument('-u', '--username', dest='username',
                      help='sername of the github account')

  parser.add_argument('-l', '--location', dest='location',
                      help='location to save dumped repos')

  def help_msg():
    parser.print_help(sys.stderr)
    sys.exit(1)

  if help:
    help_msg()
  elif len(sys.argv)==1:
    help_msg()

  return parser.parse_args()


def main():
  print(gd.logo())
  args = parser()
  if args.username and args.location:
    username = args.username
    location = args.location
    
    rl = gd.github_data(username)
    datetime_str = gd.datetime_init()
    dir = f'{location}{username}_[{datetime_str}]'
   
    gd.dump(dir, rl)
    
  else:
    print("[gitdump]> Github Username or Output File Location parameters missing !\n")
    parser(True)
  
