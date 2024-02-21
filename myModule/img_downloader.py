import os, re, requests

def image_downloader(url):
  response = requests.get(url)
  text = response.text

  p = r'<img.*?src="(.*?)"[^\>]+>'
  img_addrs = re.findall(p, text)

  for i in img_addrs:
      os.system("wget {}".format(i))

  return "DONE"