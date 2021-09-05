import time
import datetime

def time_now():
    now = datetime.datetime.now()
    return [*str(now).split(' ')[0].split('-'), *(str(now).split(' ')[1].split('.')[0]).split(':')]


def data_time_to_list(time):
    pass


def unix_time_convert(date):  # превращает обычную дата тайм дату в юникс дату
    if type(date) != type(datetime.date(2011, 11, 4)) and type(date) != type(datetime.datetime(2011, 2, 15, 4, 45, 13)):
        return f'date type error'
    try:
        unix_time = time.mktime(date.timetuple())
        return unix_time
    except:
        return 'error unix time convert'


def data_time_list_convert(date):
    if type(date) != type(datetime.date(2011, 11, 4)) and type(date) != type(datetime.datetime(2011, 2, 15, 4, 45, 13)):
        return f'date type error'
    try:
        if type(date) == type(datetime.datetime(2011, 2, 15, 4, 45, 13)):
            date = [*str(date).split(' ')[0].split('-'), *(str(date).split(' ')[1].split('.')[0]).split(':')]
        if type(date) == type(datetime.date(2011, 11, 4)):
            date = [*(str(date).split('-')), '0', '0', '0']
    except:
        return 'convert date error'
    try:
        date = [int(i) for i in date]
    except:
        return 'convert date error, int error'
    return date



if __name__ == '__main__':
    pass