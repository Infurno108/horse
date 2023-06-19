import urllib.request

def get_img(url, local_file_name):
    with urllib.request.urlopen(url) as resource:
        with open(local_file_name, 'wb') as f:
            f.write(resource.read())

get_img('https://cdn.camplonghorn.com/dailyphotos/2023/Indian%20Springs/1st%20Term%202023/Day%2014%20-%20Saturday,%20June%2017/AR_1st_14_0014_vday.jpg','iacocca_2.jpg')