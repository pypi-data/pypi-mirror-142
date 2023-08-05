import requests

def _pad_key(key: str):
    """pads key with / if it does not have it"""
    if key.startswith("/"):
        return key
    return "/" + key
    
def _list(url: str, target: str, method: str):
    target = _pad_key(target)
    r = requests.get("{}{}?{}".format(url, target, method))
    return r.json()["keys"]

def _url(url: str, key: str):
    key = _pad_key(key)
    return "{}{}".format(url, key)

class MKV():
    def __init__(self, url: str = "http://127.0.0.1:3000"):
        # have url without / at the end
        if url.endswith("/"):
            self.url = url[:-1]
        else:
            self.url = url

    def list(self, key_prefix: str = ""):
        return _list(self.url, key_prefix, "list")
    
    def unlinked(self, key_prefix: str = ""):
        return _list(self.url, key_prefix, "unlinked")
    
    def exists(self, key: str) -> bool:
        key = _pad_key(key)
        return key in self.list(key)
    
    def put(self, key: str, value: str) -> int:
        r = requests.put(_url(self.url, key), data=value)
        return r.status_code
    
    def get(self, key: str) -> str:
        key = _pad_key(key)
        r = requests.get(_url(self.url, key))
        return r.text
    
    def unlink(self, key: str):
        key = _pad_key(key)
        r = requests.api.request(method="UNLINK", url=_url(self.url, key))
        return r
    
    def delete(self, key: str) -> int:
        r = requests.delete(_url(self.url, key))
        return r.status_code
        

if __name__ == "__main__":
    mkv = MKV()
    # check val not in mkv
    res = mkv.list()
    print(res)
    assert "/__test" not in res
    # put val
    status = mkv.put("__test", "swag")
    print(status)
    # check if it exists
    assert mkv.exists("__test")
    # try to get
    assert mkv.get("__test") == "swag"
    # check if in list
    res = mkv.list()
    print(res)
    assert "/__test" in res
    # try to delete without unlinking
    assert mkv.delete("__test") == 403
    # unlink it
    mkv.unlink("/__test")
    # check if in unlinked
    res = mkv.unlinked()
    print(res)
    assert "/__test" in res
    # check that not in list
    res = mkv.list()
    assert "/__test" not in res
    # delete it
    print(mkv.delete("__test"))
    res = mkv.unlinked()
    # check that not in unlinked
    assert "/__test" not in res
    print(res)
    # check that not in list
    res = mkv.list()
    assert "/__test" not in res