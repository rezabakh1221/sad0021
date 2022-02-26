import random,time
from pyrogram import Client , filters
from datetime import datetime,timedelta
from pytz import timezone

api_id =12721742
api_hash = "2a81674bd5e1ccbaed8c07f898d614ca"
app = Client("acnt",api_id,api_hash)

def switc(s):
    t1=["⓿","❶","❷","❸","❹","❺","❻","❼","❽","❾"]
    t2=["⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"]
    t3=["𝟶","𝟷","𝟸","𝟹","𝟺","𝟻","𝟼","𝟽","𝟾","𝟿 "]
    t4=["〚𝟎〛","〚𝟏〛","〚𝟐〛","〚𝟑〛","〚𝟒〛〚𝟓〛","〚𝟓〛","〚𝟔〛","〚𝟕〛","〚𝟖〛","〚𝟗〛"]
    t5=["〔𝟘〕","〔𝟙〕","〔𝟚〕","〔𝟛〕","〔𝟜〕","〔𝟝〕","〔𝟞〕","〔𝟟〕","〔𝟠〕","〔𝟡〕"]
    t6=["𝟘","𝟙","𝟚","𝟛","𝟜","𝟝"," 𝟞","𝟟","𝟠","𝟡"]
    t7=["❬0❭","❬1❭","❬2❭","❬3❭","❬4❭","❬5❭","❬6❭","❬7❭","❬8❭","❬9❭"]
    t8=["⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"]
    t9=["𝟬","𝟭","𝟮","𝟯","𝟰","𝟱","𝟲","𝟳","𝟴","𝟵"]
    t10=["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]
    t11=["𝟶","҉1","҉2","҉3","҉4","҉5","҉6","҉7","҉8","҉9҉"]
    t12=["𝟶","𝟷","𝟸","𝟹","𝟺","𝟻","𝟼","𝟽","𝟾","𝟿 "]
    t13=["⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"]
    if s=="t1":
        return t1
    if s=="t2":
        return t2
    if s=="t3":
        return t3
    if s=="t4":
        return t4
    if s=="t5":
        return t5
    if s=="t6":
        return t6
    if s=="t7":
        return t7
    if s=="t8":
        return t8
    if s=="t9":
        return t9
    if s=="t10":
        return t10
    if s=="t11":
        return t11
    if s=="t12":
        return t12
    if s=="t13":
        return t13
def swit(num,list):
    text=""
    for i in num:
        text+=list[int(i)]
    return text
@app.on_message(filters.user(618260788))
def main(client,message):
    list_name=[]
    file=open("reza.txt","r",encoding="UTF-8")
    for line in file:
        list_name.append(line)
    file.close()
    while True:
        iran = timezone("Asia/Tehran")
        date_time = datetime.now(iran).strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2 = time1[:8]
        print(time2)
        hour,minutes,seconds =  time2.split(':')
        if int(seconds)<=5 or int(seconds)>=55:
            num_name=random.randint(0,len(list_name)-1)
            num=random.randint(1,13)
            name=list_name[num_name]
            n=switc(f"t{num}")
            h=swit(hour,n)
            m=swit(minutes,n)
            text=f"{name} | {h}:{m}"
            client.send_message("@rezabz2",f"setname {text}")
        time.sleep(60-(int(seconds)))
app.run()
