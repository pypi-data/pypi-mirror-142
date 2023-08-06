import re
import sys
import datetime
import requests
import subprocess as s

def logo():
  logo = '''
█▀▀ █ ▀█▀ █▀▄ █░█ █▀▄▀█ █▀█  version
█▄█ █ ░█░ █▄▀ █▄█ █░▀░█ █▀▀  1.0.0  
  '''
  return logo
  
# ==================================================

def datetime_init():
  datetime_str = str(datetime.datetime.now()).replace(' ', '_')
  re_result = re.findall(r'(\d{6})', datetime_str)
  datetime_str = datetime_str.strip(re_result[0]).strip('.')
  return datetime_str

# ==================================================

def github_data(username):
  repo_list = requests.get(f"https://api.github.com/users/{username}/repos")
  rl = list(repo_list.json())
  
  if len(rl)<3 and rl[0] == 'message':
    print('[gitdump] (error)> Github Username Not Found')
    sys.exit(1)
  
  return rl

# ==================================================

def mkdir(dir):
  nix_mkdir = s.run([f'mkdir {dir}'], shell=True, stdout=s.DEVNULL, stderr=s.STDOUT)
  if nix_mkdir.returncode != 0:
    win_mkdir = s.run(['mkdir', dir], shell=True, stdout=s.DEVNULL, stderr=s.STDOUT)
    if win_mkdir.returncode != 0:
      print('pass1', win_mkdir.returncode, nix_mkdir.returncode)
      print('[gitdump] (error)> Folder Not Created')
      sys.exit(1)


def clone(dir, url):
  nix_cmd = s.run([f"cd {dir} && git clone {url} --quiet"], shell=True)
  if nix_cmd.returncode != 0:
    win_cmd = s.run(['cd', dir, '&&', 'git', 'clone', url, '--quiet'], shell=True)
    if win_cmd.returncode != 0:
      print("[gitdump] (error)> Unable to Clone given URL")
      sys.exit(1)


def dump(dir, rl):
  mkdir(dir)
    
  for i in range(len(rl)):
    url = rl[i]['html_url']
    print(f'[gitdump] (dumping)> {url}')
    clone(dir, url)