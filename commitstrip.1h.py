#!/usr/local/bin/python3

# <xbar.title>CommitStrip random</xbar.title>
# <xbar.version>0.0.1</xbar.version>
# <xbar.author>浩</xbar.author>
# <xbar.author.github>blackstorm<</xbar.author.github>
# <xbar.desc>Random CommitStrip comics</xbar.desc>
# <xbar.image>https://i.imgur.com/CllAUAl.png</xbar.image>
# <xbar.abouturl>https://github.com/blackstorm/xbar-plugins</xbar.abouturl>
# <xbar.dependencies>Python,Requests</xbar.dependencies>

import base64
import random
import re
from random import randrange

import requests


def get(url, is_json = True):
    r = requests.get(url)
    if r.status_code == 200:
        if is_json:
            return r.json()
        else:
            return r.content

def random():
  res = get("https://www.commitstrip.com/en/wp-json/wp/v2/posts?per_page=100")
  randed = res[randrange(100)]
  return get("https://www.commitstrip.com/en/wp-json/wp/v2/posts/{}".format(randed["id"]))

def get_image_to_base64(image_url):
    r = requests.get(image_url)
    if r.status_code == 200:
        return base64.b64encode(r.content).decode("utf-8")
    else:
        return None

print('CommitStrip')
print('---')

comics = random()
print(comics["title"]["rendered"] + "| href=" + comics["link"])
print('---')

image_url = re.search("http[^ \"]+", comics["content"]["rendered"])[0]
image = get_image_to_base64(image_url)
if image:
  print("| href=" + comics["link"] + "| image=" + get_image_to_base64(image_url))
else:
  print("Load image error!")
print('---')