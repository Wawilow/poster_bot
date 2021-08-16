import time
import datetime
import last_post

def time_now():
    now = datetime.datetime.now()
    return [*str(now).split(' ')[0].split('-'), *(str(now).split(' ')[1].split('.')[0]).split(':')]


def unixtime_convert(date): # превращает обычную дата тайм дату в юникс дату
    try:
        unixtime = time.mktime(date.timetuple())
        return unixtime
    except:
        return 'error unitime convert'


def for_vk_post_convert(): #превращает нынешнюю дату в дату+1 день в формате unixtime
    return unixtime_convert(one_day_plus_time(datetime.datetime.now()))


def next_post_time(VK, groupId):
    return [*str(last_post.last_postponed_post(VK, groupId)).split(' ')[0].split('-'),
     *str(last_post.last_postponed_post(VK, groupId)).split(' ')[1].split(':')]


if __name__ == '__main__':
    pass