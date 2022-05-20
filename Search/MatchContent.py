import os


def get_files(path):
    file_path = os.listdir(path)
    file_list = []
    for name in file_path:
        if os.path.isdir(path + '/' + name):
            file_list.extend(get_files(path + '/' + name + '/'))
        elif os.path.isfile(path + '/' + name):
            if name.endswith('.txt'):
                with open(path + '/' + name, 'rt') as f:
                    if 'hello' or 'good' in f.read().lower():
                        file_list.append(path + '/' + name)
    return file_list


root = 'F:/迅雷下载'
result = get_files(root)
print(result)