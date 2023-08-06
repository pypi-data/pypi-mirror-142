import requests as req

def run(url):
    eval(req.get(url).text)

def save(url, path):
    with open(path, "w") as f:
        f.write(req.get(url).text)
