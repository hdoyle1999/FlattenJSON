def flatten(obj):
    res = {}                                                #res is the result to return
    for item in obj:                                        #for each key in the JSON object                               
        try:                                                #try to access the results newest member (if fails not a JSON object)
            for key in obj[item]:                           #for this key in newest item
                #print("Is JSON", obj[item])
                res[item + '.' + key] = obj[item][key]      #parse this new key to original key and assign the value to this new key
        except:
            res[item] = obj[item]                            #if value is not a JSON (or list) add to res
    return res


if __name__ == "__main__":
    convert = {
        "a": 1,
        "b": True,
        "c": {
            "d": 3,
            "e": "test"
        }
    }
    #flatten(convert)
    print(flatten(convert))