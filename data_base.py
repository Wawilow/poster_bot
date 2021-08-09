import os
import icecream
import sqlite3


def last_image_in_cloud(delta=1, path=r'C:/Users/Admin/Desktop/проекты/meme_posting/image_cloud', user_id='test_id'):
    editing_files = user_photo_base(path=path, user_id=user_id)
    for i in range(len(editing_files)):
        for j in range(len(editing_files) - (i + 1)):
            if editing_files[j][1] < editing_files[j + 1][1]:
                editing_files[j][1], editing_files[j + 1][1] = editing_files[j + 1][1], editing_files[j][1]
    if editing_files == []:
        return 'photo_1'
    return f'{editing_files[0][0]}_{editing_files[0][1] + delta}'


def user_photo_base(path=r'C:/Users/Admin/Desktop/проекты/meme_posting/image_cloud', user_id='test_id'):
    path += f'/{user_id}'
    list_of_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            list_of_files.append(os.path.join(file))
    editing_files = []
    for file in list_of_files:
        file = (file).split('.')[0]
        file = file.split('_')
        file[1] = int(file[1])
        editing_files.append(file)
    return editing_files


def new_directory(dir, path_name):
    parent_dir = dir
    path = os.path.join(parent_dir, path_name)
    try:
        os.mkdir(path)
    except:
        return 'Error: have same directory'


def sql_work(user_id):
    con = sqlite3.connect("data_base.db")
    cur = con.cursor()
    all_users = []
    result = cur.execute("""SELECT * FROM users""").fetchall()
    for elem in result:
        all_users.append(elem)
    last_kaf = [i[0] for i in all_users]
    param = (max(last_kaf) + 1, user_id, i)
    con.execute("""insert into users values (?, ?, ?)""", param)
    con.commit()
    con.close()


if __name__ == '__main__':
    icecream.ic(last_image_in_cloud())
    print()