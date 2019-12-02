import urllib.request
from tqdm import tqdm

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

filepath = 'list.txt'
print(tqdm)
with open(filepath) as fp:
   line = fp.readline()
  #  print(line)
   current = line.split(' ', 1)
   url = current[0]
   name = current[1]
   cnt = 1
   while line:
    print("Downloading {}: {}".format(name.strip(), url.strip()))
    # urllib.request.urlretrieve(url, name + '.ts')
    download_url(url, name + '.ts')
    line = fp.readline()
    if not line:
      break
    current = line.split(' ', 1)
    url = current[0]
    name = current[1]
    cnt += 1
