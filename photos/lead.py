import urllib.request

def get_img(url, local_file_name):
    with urllib.request.urlopen(url) as resource:
        with open(local_file_name, 'wb') as f:
            f.write(resource.read())

get_img('https://cdn.camplonghorn.com/dailyphotos/2022/Indian%20Springs/2nd%20Term%202022/Day%2021%20-%20Saturday,%20July%209/LH_2nd_21_0004_wrangler.JPG','photos/ranger.jpg')