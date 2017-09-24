import urllib.request
import os, errno
import json
import re

# Open Json File
with open('url.json') as url_file:
  data = json.load(url_file)

# A function for checking if the directory exist
def check_path_exist(path):
  try:
    os.makedirs(path)
  except OSError as exception:
    if exception.errno != errno.EEXIST:
      raise  

for url in data["url"]:
  url_local_name = url.replace('https://s3-us-west-1.amazonaws.com/yeah-assets/', '')
  url_local_path = './img/' + url_local_name

  # Generate the directory name 
  create_local_dir = './img/' + re.sub('([^/]+)$', '', url_local_name)
  # Check if directory exists
  check_path_exist(create_local_dir)
  # Download images to the local path
  urllib.request.urlretrieve(url, url_local_path)