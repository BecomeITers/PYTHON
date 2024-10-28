dict = {};
def Add(key, value):
    if key in dict:
        print("Da co ma so trong danh sach")
    else:
        dict[key] = value;

def Delete(key):
    if key not in dict:
        print("Ko thay ma so de xoa")
    else:
        del dict[key]

def Change(key, value):
    if key not in dict:
        print("Ko thay ma so de sua")
    else:
        dict[key] = value

def Print():
    if not dict:
        print("Danh sach trong")
    else:
        for key, value in dict.items():
            print(f"Key: {key}, Value: {value}")