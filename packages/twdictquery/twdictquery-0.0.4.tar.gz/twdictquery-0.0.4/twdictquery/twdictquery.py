__author__ = "Iyappan"
__email__ = "iyappan@trackerwave.com"
__status__ = "planning"

from sys import getsizeof

def find_query_combination(res, cmmd, comb):
    for key, value in res.items():
        if cmmd == "":
            comb.append(str(key))
            if type(value) is dict and value:
                find_query_combination(value, str(key), comb)
        else:
            comb.append(cmmd+" "+str(key))
            if type(value) is dict and value:
                find_query_combination(value, cmmd+" "+str(key), comb)
    return comb

def find_key_values(res, key, f_data):
    if type(res) is dict:
        for k, v in res.items():
            if key == k:
                f_data.append([k, v])
            find_key_values(v, key, f_data)
    elif type(res) is list:
        for r in res:
            if type(r) is dict:
                for k, v in r.items():
                    if k == key:
                        f_data.append([k, v])
                    find_key_values(v, key, f_data)
    return f_data

def find_like_values(res, key, f_data):
    if type(res) is dict:
        for k, v in res.items():
            if key in k:
                f_data.append([k, v])
            find_key_values(v, key, f_data)
    elif type(res) is list:
        for r in res:
            if type(r) is dict:
                for k, v in r.items():
                    if key in k:
                        f_data.append([k, v])
                    find_key_values(v, key, f_data)
    return f_data

def find_query(res, cmmd):
    cmmd = cmmd.split(" ")
    for i in range(len(cmmd)):
        key = cmmd[i]
        if key == "-query":
            if len(cmmd) == i+1:
                if type(res) is dict:
                    res = find_query_combination(res, "", [])
                    return {"status": True, "res": res}
            else:
                return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-count":
            res = len(res)
        elif key == "-size":
            res = str(getsizeof(res)) + " bytes"
        elif key == "-find":
            if len(cmmd) == i+2:
                res = find_key_values(res, cmmd[i+1], [])
                return {"status": True, "res": res}
            else:
                return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-like":
            if len(cmmd) == i+2:
                res = find_like_values(res, cmmd[i+1], [])
                return {"status": True, "res": res}
            else:
                return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-keys":
            if type(res) is dict:
                if len(cmmd) == i+1:
                    res = list(res.keys())
                    return {"status": True, "res": res}
            return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-help":
            res = ['-query or <key> -query', "-count or <key> -count", "-size or <key> -size", "-find <key> or <key> -find <key>", "-like or <key> -like <str>", "-keys or <key> -keys", "-help"]
        elif key in res:
            res = res[key]
        else:
            return {"status": False, "res": "invalid query '" + str(key) + "'"}
    return {"status": True, "res": res}
