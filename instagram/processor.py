from direct.models import DirectMessage
import datetime
from django.db.models import Q
import time
def one_minute_before_now(nowtime:datetime.datetime) -> datetime.datetime:
    hour = 0
    minute = 0
    if nowtime.minute == 0:
        hour = nowtime.hour - 1
        minute = 59
    else:
        hour = nowtime.hour
        minute = nowtime.minute - 1
    result = datetime.datetime(nowtime.year,nowtime.month,nowtime.day,hour,minute,nowtime.second)
    return result

def check_new_messages(user) -> tuple:
    while True:
        now = datetime.datetime.now()
        before_now_one_minute = one_minute_before_now(now)
        new_message = DirectMessage.objects.filter(
            send_date__gte = before_now_one_minute,send_date__lte = now,reciver = user,
            send_state = True,seen_state = False
        ).first()
        if new_message:
            return True,new_message
        time.sleep(1)

