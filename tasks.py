answer1 = 'c23eb'
key1 = 'rasldkfj124dadsjflkaxzcv.12adsjflkaxzcv.12adsjflkaxzcv.12a'

login2, password2 = 'Cruassilio', '2283'
key2 = 'kjhvbhnjgbyhnjbgynhhun2maTebal2sakdfjsd'

true_agent = 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
key3 = 'zxcv.,mzxv213,mxz234'

key4 = "hvatit'dvigat'svoimiTABURETKAMI"

def task1(name, password):
    if password == answer1:
        return key1

def task2(name, pincode):
    if name == login2 and pincode == password2:
        return key2

def task3(agent):
    if true_agent == agent:
        return key3

def check(key):
    if key == key1:
        return 1
    elif key == key2:
        return 2
    elif key == key3:
        return 3
    elif key == key4:
        return 4
    else:
        return 0
