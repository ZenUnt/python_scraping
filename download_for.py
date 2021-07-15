import requests
import os, time

save_dir = './image'
base_url = 'https://uta.pw/shodou/img/{0}/{1}.png'

def download_all():
  if not os.path.exists(save_dir):
    os.mkdir(save_dir)
  for id in range(1, 11):
    download_file(id)
    time.sleep(1)

def download_file(id):
  url = base_url.format(id%31, id)
  save_file = save_dir + '/' + str(id) + '.png'
  res = requests.get(url)
  if not res.ok:
    print("失敗", res.status_code)
    return
  with open(save_file, 'wb') as fp:
    fp.write(res.content)
  print("save: ", save_file)

if __name__ == '__main__':
  download_all()
