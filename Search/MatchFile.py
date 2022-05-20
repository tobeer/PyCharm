import os
import time


def get_files(path):
    file_path = os.listdir(path)
    file_list = []
    for name in file_path:
        if os.path.isdir(path + '/' + name) and not name.startswith('$'):
            try:
                file_list.extend(get_files(path + '/' + name + '/'))
            except:
                continue
        elif os.path.isfile(path + '/' + name):
            if name.lower().find('log4j') != -1:
                file_list.append(path + '/' + name)
    return file_list


root = ['F:/']
result = []
start = time.time()
for i in root:
    result.extend(get_files(i))
stop = time.time()
executeTime = round(stop - start, 2)
print('Execute {0} secs'.format(executeTime))
print('=======================================')
with open('E:/PycharmProjects/PyCharm/Search/MatchedFile.txt', 'w', encoding='utf-8') as f:
    for i in result:
        f.writelines(i + '\n')
        print(i)
