from pyrogram import Client,filters
from pyromod import listen
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
import time,xlsxwriter,xlrd,os,requests,jdatetime
#--------------------------------------------------------------------------------------------------------------------------------------------------------
admin=618260788
keyboard_kansel=ReplyKeyboardMarkup(
                [
                    ["لغو عملیات"]
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
keyboard_admin=ReplyKeyboardMarkup(
                [
                    ["👁‍🗨👤نمایش کاربران"],
                    ["✔ارسال همگانی"]
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
keyboard_home=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📅تاریخ امروز",
                        callback_data="daytime"
                    ),  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "⁉زوج یا فرد",
                        callback_data="zoj_frd"
                    ),
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "👤پنل کاربری",
                        callback_data="pnl_usr"
                    )
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🗓تقویم آموزشی",
                        callback_data="taghams"
                    ),
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "💳حمایت مالی💵",
                        callback_data="hlpmali"
                    ),
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🤖درباره ربات🖋",
                        callback_data="darbare"
                    )
                ]
            ]
            )
keyboard_personal=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "💉اطلاعات واکسناسیون",
                        callback_data="infvaks"
                    ),  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📑لیست حضور و غیاب",
                        callback_data="hzrOgyb"
                    ),
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🗒برنامه کلاسی",
                        callback_data="plnclas"
                    ),  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📜برنامه امتحانی",
                        callback_data="plncors"
                    ),
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📚درس ها",
                        callback_data="lessons"
                    ),  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📈نمرات ترم",
                        callback_data="numterm"
                    ),
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🔄بروزرسانی  اطلاعات",
                        callback_data="updinfo"
                    )
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🔙برگشت به منو اصلی",
                        callback_data="backhom"
                    )
                ]
            ]
            )
keyboard_vaksan=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "👁‍🗨لیست واکسن های ثبت شده",
                        callback_data="vaksshw"
                    )
                    ],[# First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "✔ثبت واکسن",
                        callback_data="vakssbt"
                    )
                ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🔙برگشت به پنل کاربری",
                        callback_data="backpnl"
                    )
                ]
            ]
            )
file=open("logined.txt","a",encoding="UTF-8")
file.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    wb = xlrd.open_workbook("all_information.xls")
except:
    workbook = xlsxwriter.Workbook("all_information.xls")
    worksheet = workbook.add_worksheet()
    worksheet.write('A1',0)
    worksheet.write('B1',0)
    worksheet.write('C1',0)
    worksheet.write('D1',0)
    worksheet.write('E1',0)
    worksheet.write('F1',0)
    workbook.close()
#----------------------------------------------------------------------------------------------------
def change_and_save(list_par):
    workbook = xlsxwriter.Workbook('3_day.xls')
    worksheet = workbook.add_worksheet()
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    ser=sheet.nrows+1
    for i in range(ser):
        if ser==i+1:
            p=list_par
        else:
            p=sheet.row_values(i)
        c=i+1
        worksheet.write(f'A{c}',p[0])
        worksheet.write(f'B{c}',p[1])
        worksheet.write(f'C{c}',p[2])
        worksheet.write(f'D{c}',p[3])
        worksheet.write(f'E{c}',p[4])
        worksheet.write(f'F{c}',p[5])
    workbook.close()
    os.remove("all_information.xls")
    os.rename("3_day.xls","all_information.xls")
def exist_number(number):
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        p=sheet.row_values(i)
        if int(number) == int(p[2]):
            return i
    return -1
def get_user_pass(number):
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        p=sheet.row_values(i)
        if int(number) == int(p[5]):
            return f"{p[2]} {p[4]}"
        
def get_name_family(number):
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        p=sheet.row_values(i)
        if int(number) == int(p[2]) or int(number) == int(p[5]):
            return p[0]+p[1]
def get_code(path,number):
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        p=sheet.row_values(i)
        if str(number) in p:
            return p[2]
    return -1
def search_and_get_link(driver,id,number):
    driver.get("http://vu.kashmar.ac.ir/vu1400-2/meeting.list.php?fid=4145431")
    driver.find_element_by_tag_name("input").send_keys(number)
    time.sleep(1)
    web=driver.find_element_by_class_name("btn-info")
    return web.get_attribute("href")

async def get_link_recorded(driver,id,c,number):
    list_record=[]
    driver.get("http://vu.kashmar.ac.ir/vu1400-2/meeting.list.php?fid=4145431")
    driver.find_element_by_tag_name("input").send_keys(number)
    time.sleep(1)
    web=driver.find_elements_by_tag_name("button")
    for i in web:
        if i.get_attribute("data-target")=="#ModalRecords":
            i.click()
    time.sleep(1)
    ol=driver.find_elements_by_xpath("/html/body/div/div[4]/div/div/div[2]/ol/li")
    if len(ol)==0:
        await c.send_message(id,"❌هنوز کلاس ضبط شده ای ثبت نشده است")
    else:
        xx=ol[0].text.find("-")
        yy=ol[0].text.find("-",xx+1)
        name=ol[0].text[xx+1:yy]
        for j in ol:
            find=j.text.find(" تاریخ")
            title=j.text[:find]
            link=j.text.replace(title,"")
            set=j.find_element_by_tag_name("a")
            linked=set.get_attribute("href")
            list_record.append([
                        InlineKeyboardButton(  # Opens a web URL
                            f"📍{title}",
                            url=f"{linked}"
                        )
                    ])
        list_record.append(
                    [  # First row
                        InlineKeyboardButton(  # Generates a callback query when pressed
                            "🔙برگشت به پنل کاربری",
                            callback_data="backpnl"
                        )
                    ]
                )
        await c.send_message(id,f"👨‍🎓 نام استاد: {name}",parse_mode="markdown",reply_markup=InlineKeyboardMarkup(list_record))
#----------------------------------------------------------------------------------------------------
def plan_class(driver,id):
    try:
        url="https://puya.kashmar.ac.ir/educ/educfac/ShowStSchedule.php"
        driver.get(url) 
        time.sleep(1) 
        driver.save_screenshot(f"plan_class{id}.png")
        img=Image.open(f"plan_class{id}.png")
        width, height = img.size
        left = 0
        top = 40
        right = width
        bottom = height-85
        im1 = img.crop((left, top, right, bottom))
        im1.save(f"plan_class{id}.png")
        return 1
    except:
        return 0
    
def emtehanat(driver,id):
    try:
        driver.get("https://puya.kashmar.ac.ir/educ/stu_portal/ShowStExamDays.php")
        time.sleep(1) 
        driver.save_screenshot(f"plan_emtehan{id}.png")
        img=Image.open(f"plan_emtehan{id}.png")
        width, height = img.size
        left = 0
        top = 40
        right = width
        bottom = height-85
        im1 = img.crop((left, top, right, bottom))
        im1.save(f"plan_emtehan{id}.png")
        return 1
    except:
        return 0
    
def number_do(driver,id):
    try:
        driver.get("https://puya.kashmar.ac.ir/educ/educfac/stuShowEducationalLogFromGradeList.php")
        time.sleep(1) 
        driver.save_screenshot(f"number{id}.png")
        img=Image.open(f"number{id}.png")
        width, height = img.size
        left = 0
        top = 0
        right = width-15
        bottom = height
        im1 = img.crop((left, top, right, bottom))
        im1.save(f"number{id}.png")
        return 1
    except:
        return 0
    
def hozore(driver,id):
    try:
        url="https://puya.kashmar.ac.ir/educ/stu_portal/absReport.php"
        driver.get(url) 
        time.sleep(1) 
        driver.save_screenshot(f"hozor{id}.png")
        img=Image.open(f"hozor{id}.png")
        width, height = img.size
        left = 155
        top = 20
        right = 900
        bottom = 300
        im1 = img.crop((left, top, right, bottom))
        im1.save(f"hozor{id}.png")
        return 1
    except:
        return 0

def vaksan(driver,id):
    try:
        url="https://puya.kashmar.ac.ir/stuoffice/stu_portal/medical/GetVaccineCard.php"
        driver.get(url) 
        time.sleep(1) 
        driver.save_screenshot(f"vaksan{id}.png")
        img=Image.open(f"vaksan{id}.png")
        width, height = img.size
        left =250
        top = 350
        right = width
        bottom = height
        im1 = img.crop((left, top, right, bottom))
        im1.save(f"vaksan{id}.png")
        return 1
    except:
        return 0
    
async def comit_vaksan(driver,link,c,id):
    if link[:10]=="vaccinecar":
        link="https://"+link
    if link[:35]=="https://vaccinecard.salamat.gov.ir/":
        driver.get("https://puya.kashmar.ac.ir/stuoffice/stu_portal/medical/GetVaccineCard.php")
        driver.find_element_by_id("VaccineLink").send_keys(link)
        driver.find_element_by_name("send").click()
        await c.send_message(id,"ثبت شد",reply_markup=keyboard_vaksan)
        return 1
    else:
        await c.send_message(id,"لینک اشتباه است",reply_markup=keyboard_vaksan)
        return 0
        
def darss(driver,id):
    try:
        driver.get("https://puya.kashmar.ac.ir/educ/educfac/IssueAck.php")
        time.sleep(1) 
        web=driver.find_elements_by_xpath("/html/body/center/table[2]/tbody/tr")
        j=2
        t=1
        x=len(web)
        workbook = xlsxwriter.Workbook(f"dars{id}.xls")
        worksheet = workbook.add_worksheet()
        for i in web:
            if (j<x):
                text=driver.find_element_by_xpath(f"/html/body/center/table[2]/tbody/tr[{j}]/td[6]").text
                if text=="انتخاب":
                    f=j-t
                    worksheet.write(f'A{f}',driver.find_element_by_xpath(f"/html/body/center/table[2]/tbody/tr[{j}]/td[4]").text)
                    worksheet.write(f'B{f}',driver.find_element_by_xpath(f"/html/body/center/table[2]/tbody/tr[{j}]/td[2]").text)
                    worksheet.write(f'C{f}',driver.find_element_by_xpath(f"/html/body/center/table[2]/tbody/tr[{j}]/td[3]").text)
                else:
                    t+=1
                j+=1 
        workbook.close()
        return 1
    except:
        return 0
    
def login(user,pas,driver):
    driver.get("https://puya.kashmar.ac.ir/gateway/PuyaAuthenticate.php")
    driver.find_element_by_name("UserID").send_keys(user)
    driver.find_element_by_name("DummyVar").send_keys(pas)
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    time.sleep(1)
    
def get_information(driver,user,ca):
    num=exist_number(user)
    if num==-1:
        try:
            list_p=[]
            driver.get("https://puya.kashmar.ac.ir/educ/registration/EditFullDataOfPerson.php")
            file=driver.find_element_by_id("form1").text
            start=file.find("نام :")
            end=file.find("\n",start)
            list_p.append(file[start+5:end])
            start=end

            start=file.find("نام خانوادگی:")
            end=file.find("\n",start)
            list_p.append(file[start+13:end])
            start=end

            start=file.find("شماره دانشجویی:")
            end=file.find("\n",start)
            list_p.append(file[start+15:end])
            start=end

            start=file.find("نام پدر:")
            end=file.find("\n",start)
            list_p.append(file[start+8:end])
            start=end

            start=file.find("شماره ملی:")
            end=file.find("\n",start)
            list_p.append(file[start+10:end])
            start=end
            list_p.append(ca.message.chat.id)
            change_and_save(list_p)
        except:
            pass
    else:
        names=get_name_family(user)
        return names

#------------------------------====================================/////////////////////////////////////////////////////////////////////////////////////

#------------------------------------------------------------
api_id=13893053
api_hash="f586d92837b0f6eebcaa3e392397f47c"
bot_token="5264885028:AAGrhDzePM11mRUmbHG2rK2q6Id5dxE1XWw"
app = Client("acontet", api_id=api_id,api_hash=api_hash,bot_token=bot_token)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
@app.on_message(filters.user(admin) & filters.command("start","/"))
async def start_admin(c,m):
    await m.reply("به پنل مدیر خوش امدی",reply_markup=keyboard_admin)
@app.on_message(filters.user(admin) & filters.regex("^👁‍🗨👤نمایش کاربران$"))
async def show_user(c,m):
    await m.reply("♻در حال انجام عملیات لطفا صبر کنید✅")
    wb = xlrd.open_workbook("all_information.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    text=""
    x=0
    for i in range(0,sheet.nrows):
        p=sheet.row_values(i)
        if int(p[5])!=0:
            text+=f"**📝نام و نام خانوادگی:**{p[0]}{p[1]}\n** ✏نام پدر: ** {p[3]}\n**📞شماره ملی:** {p[2]}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            x+=1
        elif sheet.nrows==1:
            text+="🔴لیست خالی است"
        if x==20:
            await m.reply(text)
            text=""
            x=0
    if x<20:
        await m.reply(text)
    if x!=0:
        await m.reply("✅عملیات با موفقیت انجام شد")

@app.on_message(filters.user(admin) & filters.regex("^✔ارسال همگانی$"))
async def send_to_all(c,m):
    try:
        list_user=open("all_users.txt","r",encoding="UTF-8").read().split()
        await m.reply("🤖به بخش ارسال پیام همگانی خوش امدید",reply_markup=keyboard_kansel)
        message=await c.ask(admin,"✉پیام مورد نظر را ارسال کنید:")
        if message.text=="لغو عملیات":
            await m.reply("✅به منو قبل بر میگردید",reply_markup=keyboard_admin)
        else:
            leng=len(list_user)
            id=message.message_id
            for i in list_user:
                await c.forward_messages(int(i),admin,id)
            await m.reply(f"✅عملیات انجام شد\n✔این پیام به {leng} کاربر ارسال شد.",reply_markup=keyboard_admin)
    except:
        await m.reply("❌شخصی برای ارسال وجود ندارد",reply_markup=keyboard_admin)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
def diffDate(DateStr2, DateStr1):
   from datetime import datetime
   fmt = '%Y-%m-%d'
   d2 = datetime.strptime(DateStr2, fmt)
   d1 = datetime.strptime(DateStr1, fmt)
   return (d2-d1).days

@app.on_message(filters.private & filters.command("start","/"))
async def start_user(c,m):
    try:
        file=open("all_user.txt","r",encoding="UTF-8")
    except:
        file=open("all_user.txt","a",encoding="UTF-8")
        file.close()
    list_id=open("all_user.txt","r",encoding="UTF-8").read().split()
    if not(str(m.chat.id) in list_id):
        file_user=open("all_user.txt","a",encoding="UTF-8")
        file_user.write(str(m.chat.id)+" ")
        file_user.close()
    await m.reply("سلام دانشجوی گرامی ",reply_markup=keyboard_home)

@app.on_callback_query()
async def callback(c,ca):
    text=ca.data[:7]
    await c.delete_messages(ca.message.chat.id,ca.message.message_id)

    if text=="daytime":
        respons=requests.get("http://api.codebazan.ir/time-date/?json=fa")
        response=respons.json()
        time=response["result"]["time"]
        date=response["result"]["date"]
        faawe=response["result"]["faweekname"]
        await c.send_message(ca.message.chat.id,f"**ساعت**: {time}\n**تاریخ**: {date}\n{faawe}",reply_markup=keyboard_home)
    
    if text=="zoj_frd":
        tim=jdatetime.date.today().strftime("%Y-%m-%d")
        tadd=diffDate(tim,"1401-01-01")
        xer=tadd//7
        if xer%2!=0:
            await c.send_message(ca.message.chat.id,"این هفته فرده.",reply_markup=keyboard_home)
        else:
            await c.send_message(ca.message.chat.id,"این هفته زوجه.",reply_markup=keyboard_home)
            
    if text=="pnl_usr":
        file_list=open("logined.txt","r",encoding="UTF-8").read().split()
        if str(ca.message.chat.id) in file_list:
            await c.send_message(ca.message.chat.id,"👻",reply_markup=keyboard_personal)
        else:
            username=await c.ask(ca.message.chat.id,"شما تا کنون وارد نشده اید.\nبرای استفاده از پنل کاربری ابتدا وارد  شوید.\nبرای ورود لطفا ابتدا شماره دانشجویی خود را ارسال کنید\nبرای بازگشت به منو اصلی از دستور /cancel استفاده کنید.")
            if username.text=="/cancel":
                await c.send_message(ca.message.chat.id,"🏠",reply_markup=keyboard_home)
            else:
                password=await c.ask(username.chat.id,"لطفا پسوورد خود را ارسال کنید:\nبرای برگشت به منو اصلی دستور /cancel را ارسال کنید")
                if password.text=="/cancel":
                    await c.send_message(ca.message.chat.id,"🏠",reply_markup=keyboard_home)
                else:
                    await c.send_message(password.chat.id,"در حال گرفتن اطلاعات اطفا صبور باشید")
                # try:
                    option=webdriver.ChromeOptions()
                    option.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
                    option.add_argument("--headless")
                    option.add_argument("--disable-dev-shm-usage")
                    option.add_argument("--no-sandbox")
                    driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                    login(username.text,password.text,driver)
                    get_information(driver,username.text,ca)
                    hozore(driver,password.chat.id)
                    plan_class(driver,password.chat.id)
                    vaksan(driver,password.chat.id)
                    darss(driver,password.chat.id)
                    emtehanat(driver,password.chat.id)
                    number_do(driver,password.chat.id)
                    await c.send_message(password.chat.id,"دریافت اطلاعات کامل شد",reply_markup=keyboard_personal)
                    driver.quit()
                    file_login=open("logined.txt","a",encoding="UTF-8")
                    file_login.write(str(ca.message.chat.id)+" ")
                    file_login.close()
                    
                # except:
                    await c.send_message(password.chat.id,"پسوورد اشتباه است به منو اصلی باز میگردید",reply_markup=keyboard_home)
        
    if text=="taghams":
        await c.send_photo(ca.message.chat.id,"taghams.jpg",reply_markup=keyboard_home)
    
    if text=="hlpmali":
        await c.send_message(ca.message.chat.id,"این بخش در حال توسعه میباشد.",reply_markup=keyboard_home)
    
    if text=="darbare":
        await c.send_message(ca.message.chat.id,"فعلا هیچ اطلاعاتی ندارد.",reply_markup=keyboard_home)
    
    if text=="infvaks":
        await c.send_message(ca.message.chat.id,"💉",reply_markup=keyboard_vaksan)
    
    if text=="hzrOgyb":
        await c.send_photo(ca.message.chat.id,f"hozor{ca.message.chat.id}.png",reply_markup=keyboard_personal)
    
    if text=="plnclas":
        await c.send_photo(ca.message.chat.id,f"plan_class{ca.message.chat.id}.png",reply_markup=keyboard_personal)
    
    if text=="plncors":
        await c.send_photo(ca.message.chat.id,f"plan_emtehan{ca.message.chat.id}.png",reply_markup=keyboard_personal)
    
    if text=="lessons":
        list_key=[]
        wb = xlrd.open_workbook(f"dars{ca.message.chat.id}.xls")
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for i in range(sheet.nrows):
            p=sheet.row_values(i)
            list_key.append([  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        f"📚{p[0]}",
                        callback_data=f"clasrom{p[1]}-{p[2]}"
                    )
                ])
        list_key.append([  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🔙برگشت به پنل کاربری",
                        callback_data="backpnl"
                    )
                ])
        await c.send_message(ca.message.chat.id,"📚",reply_markup=InlineKeyboardMarkup(list_key))
    
    if text=="clasrom":
        number_less=ca.data[7:]
        option=webdriver.ChromeOptions()
        option.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
        option.add_argument("--headless")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--no-sandbox")
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
        link_las=search_and_get_link(driver,ca.message.chat.id,number_less)
        await c.send_message(ca.message.chat.id,f"▪لینک درس: {link_las}",reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📝لیست کلاس های ضبط شده",
                        callback_data=f"claszbt{number_less}"
                    )
                    ],[  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🔙برگشت به پنل کاربری",
                        callback_data="backpnl"
                    )
                ]
            ]
            ))
        driver.quit()
    if text=="numterm":
        await c.send_photo(ca.message.chat.id,f"number{ca.message.chat.id}.png",reply_markup=keyboard_personal)
    
    if text=="updinfo":
        par=get_user_pass(ca.message.chat.id).split()
        if len(par)==0:
            await c.send_message(ca.message.chat.id,"شما تا کنون وارد نشده اید.\nبرای استفاده از پنل کاربری ابتدا وارد شوید.",reply_markup=keyboard_personal)
        else:
            await c.send_message(ca.message.chat.id,"در حال گرفتن اطلاعات اطفا صبور باشید")
            try:
                option=webdriver.ChromeOptions()
                option.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
                option.add_argument("--headless")
                option.add_argument("--disable-dev-shm-usage")
                option.add_argument("--no-sandbox")
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                login(par[0],par[1],driver)
                get_information(driver,par[0],ca)
                hozore(driver,ca.message.chat.id)
                plan_class(driver,ca.message.chat.id)
                vaksan(driver,ca.message.chat.id)
                darss(driver,ca.message.chat.id)
                emtehanat(driver,ca.message.chat.id)
                number_do(driver,ca.message.chat.id)
                driver.quit()
                await c.send_message(ca.message.chat.id,"دریافت اطلاعات کامل شد",reply_markup=keyboard_personal)
            except:
                await c.send_message(ca.message.chat.id,"پسوورد اشتباه است به منو اصلی باز میگردید",reply_markup=keyboard_home)
    
    if text=="backhom":
        await c.send_message(ca.message.chat.id,"🏠",reply_markup=keyboard_home)
    
    if text=="vaksshw":
        await c.send_photo(ca.message.chat.id,f"vaksan{ca.message.chat.id}.png",reply_markup=keyboard_vaksan)
    
    if text=="vakssbt":
        await c.send_message(ca.message.chat.id,"سلام خوش امدید\nبرای برگشت به پنل کاربری از دستور /cancel استفاده کنید")
        link_vaksan=await c.ask(ca.message.chat.id,"برای ثبت کارت ئاکسن دیجیتال خود در سایت دانشگاه لطفا لینک ارسال شده از سایت سلامت را ارسال کنید.\nنمونه لینک:\nvaccinecard.salamat.gov.ir/a69f83a2127560414da948cd8603db1f0***")
        if link_vaksan.text=="/cancel":
            us=get_name_family(ca.message.chat.id)
            await c.send_message(ca.message.chat.id,f"📍 سلام {us} عزیز به پنل کاربری خوش امدید.",reply_markup=keyboard_personal)
        else:
            option=webdriver.ChromeOptions()
            option.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
            option.add_argument("--headless")
            option.add_argument("--disable-dev-shm-usage")
            option.add_argument("--no-sandbox")
            driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
            par=get_user_pass(ca.message.chat.id).split()
            login(par[0],par[1],driver)
            await comit_vaksan(driver,link_vaksan.text,c,ca.message.chat.id)
            driver.quit()
    
    if text=="backpnl":
        us=get_name_family(ca.message.chat.id)
        await c.send_message(ca.message.chat.id,f"📍 سلام {us} عزیز به پنل کاربری خوش امدید.",reply_markup=keyboard_personal)
    
    if text=="claszbt":
        number_les=ca.data[7:]
        option=webdriver.ChromeOptions()
        option.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
        option.add_argument("--headless")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--no-sandbox")
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
        await get_link_recorded(driver,ca.message.chat.id,c,number_les)
        driver.quit()
    

app.run()
