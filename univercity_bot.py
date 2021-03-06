from pyrogram import Client,filters
from pyromod import listen
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from selenium import webdriver
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
keyboard_hlpmali=InlineKeyboardMarkup(
    [
        [  # First row
            InlineKeyboardButton(  # Generates a callback query when pressed
                "🔲پرداخت مبلغ دلخواه",
                url="https://idpay.ir/reza-bakhsh-zaii"
            )
        ],
        [  # First row
            InlineKeyboardButton(  # Generates a callback query when pressed
                "🔙برگشت به منو اصلی",
                callback_data="backhom"
            )
        ]
    ]
)
file=open("logined.txt","a",encoding="UTF-8")
file.close()
file=open("all_user.txt","a",encoding="UTF-8")
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
def get_name_ostad(number,id):
    wb = xlrd.open_workbook(f"dars{id}.xls")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        p=sheet.row_values(i)
        if int(number) == int(p[1]):
            return p[3]
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
        code_darse=number.split("-")
        name_ostad=get_name_ostad(code_darse[0],id)
        await c.send_message(id,f"👨‍🎓 نام استاد: {name_ostad}\n🆔 کد درس: {code_darse[0]}\n💠گروه درس: {code_darse[1]}",parse_mode="markdown",reply_markup=InlineKeyboardMarkup(list_record))
#----------------------------------------------------------------------------------------------------
def plan_class(driver,id):
    try:
        url="https://puya.kashmar.ac.ir/educ/educfac/ShowStSchedule.php"
        driver.get(url) 
        time.sleep(1)
        driver.find_element_by_tag_name("table").screenshot(f"plan_class{id}.png")
        return 1
    except:
        return 0
    
def emtehanat(driver,id):
    try:
        driver.get("https://puya.kashmar.ac.ir/educ/stu_portal/ShowStExamDays.php")
        time.sleep(1) 
        driver.find_element_by_tag_name("table").screenshot(f"plan_emtehan{id}.png")
        return 1
    except:
        return 0
    
async def number_do(id,c,ca,sw):
    if sw==1:
        try:
            text=""
            wb = xlrd.open_workbook(f"number_do{id}.xls")
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            for i in range(sheet.nrows):
                p=sheet.row_values(i)
                if i<sheet.nrows-1:
                    text+=f"📝کد درس: {p[0]} \n 📚نام درس: {p[1]} \n 🔶تعداد واحد: {p[2]} \n 👨‍🎓استاد: {p[3]} \n ❇نمره: {p[4]} \n 🔴وضعیت نمره: {p[5]} \n 📋شماره لیست نمره: {p[6]} \n ❇وضعیت لیست نمره: {p[7]}\n➖➖\n"
                else:
                    text+=f"🔲{p[0]}: {p[1]} \n 📜{p[2]}: {p[3]}"
            await c.send_message(id,text,reply_markup=keyboard_personal)
        except:
            # try:
            #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
            # except:
            driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
            par=get_user_pass(ca.message.chat.id).split()
            driver.maximize_window()
            login(par[0],par[1],driver)
            driver.get("https://puya.kashmar.ac.ir/educ/educfac/stuShowEducationalLogFromGradeList.php")
            time.sleep(1)
            tr=driver.find_elements_by_xpath("/html/body/center/table/tbody")
            trr=tr[0].find_elements_by_tag_name("tr")
            g=1
            htm=0
            workbook = xlsxwriter.Workbook(f"number_do{id}.xls")
            worksheet = workbook.add_worksheet()
            for i in trr:
                try:
                    if int(driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{g}]/td[1]").text)==1:
                        htm=g
                        break
                except:
                    g+=1
            f=1
            le=len(trr)
            print(le,htm)
            for i in trr:
                if htm<=le:
                    worksheet.write(f'A{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[2]").text)
                    worksheet.write(f'B{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[3]").text)
                    worksheet.write(f'C{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[4]").text)
                    worksheet.write(f'D{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[5]").text)
                    worksheet.write(f'E{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[6]").text)
                    worksheet.write(f'F{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[7]").text)
                    worksheet.write(f'G{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[8]").text)
                    worksheet.write(f'H{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[9]").text)
                    f+=1
                    htm+=2
            worksheet.write(f'A{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[1]").text)
            worksheet.write(f'B{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[2]").text)
            worksheet.write(f'C{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[3]").text)
            worksheet.write(f'D{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[4]").text)
            workbook.close()
            driver.quit()
            text=""
            wb = xlrd.open_workbook(f"number_do{id}.xls")
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            for i in range(sheet.nrows):
                p=sheet.row_values(i)
                if i<sheet.nrows-1:
                    text+=f"📝کد درس: {p[0]} \n 📚نام درس: {p[1]} \n 🔶تعداد واحد: {p[2]} \n 👨‍🎓استاد: {p[3]} \n ❇نمره: {p[4]} \n 🔴وضعیت نمره: {p[5]} \n 📋شماره لیست نمره: {p[6]} \n ❇وضعیت لیست نمره: {p[7]}\n➖➖\n"
                else:
                    text+=f"🔲{p[0]}: {p[1]} \n 📜{p[2]}: {p[3]}"
            await c.send_message(id,text,reply_markup=keyboard_personal)
    elif sw==0:
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
        par=get_user_pass(ca.message.chat.id).split()
        driver.maximize_window()
        login(par[0],par[1],driver)
        driver.get("https://puya.kashmar.ac.ir/educ/educfac/stuShowEducationalLogFromGradeList.php")
        time.sleep(1)
        tr=driver.find_elements_by_xpath("/html/body/center/table/tbody")
        trr=tr[0].find_elements_by_tag_name("tr")
        g=1
        htm=0
        workbook = xlsxwriter.Workbook(f"number_do{id}.xls")
        worksheet = workbook.add_worksheet()
        for i in trr:
            try:
                if int(driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{g}]/td[1]").text)==1:
                    htm=g
                    break
            except:
                g+=1
        f=1
        le=len(trr)
        print(le,htm)
        for i in trr:
            if htm<=le:
                worksheet.write(f'A{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[2]").text)
                worksheet.write(f'B{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[3]").text)
                worksheet.write(f'C{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[4]").text)
                worksheet.write(f'D{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[5]").text)
                worksheet.write(f'E{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[6]").text)
                worksheet.write(f'F{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[7]").text)
                worksheet.write(f'G{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[8]").text)
                worksheet.write(f'H{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{htm}]/td[9]").text)
                f+=1
                htm+=2
        worksheet.write(f'A{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[1]").text)
        worksheet.write(f'B{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[2]").text)
        worksheet.write(f'C{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[3]").text)
        worksheet.write(f'D{f}',driver.find_element_by_xpath(f"/html/body/center/table/tbody/tr[{le}]/td[4]").text)
        workbook.close()
        driver.quit()
        
def hozore(driver,id):
    try:
        url="https://puya.kashmar.ac.ir/educ/stu_portal/absReport.php"
        driver.get(url) 
        time.sleep(1) 
        driver.find_elements_by_tag_name("table")[0].screenshot(f"hozor{id}.png")
        return 1
    except:
        return 0

def vaksan(driver,id):
    try:
        url="https://puya.kashmar.ac.ir/stuoffice/stu_portal/medical/GetVaccineCard.php"
        driver.get(url) 
        time.sleep(1) 
        driver.find_element_by_id("mytable").screenshot(f"vaksan{id}.png")
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
        await c.send_message(id,"✅ثبت شد",reply_markup=keyboard_vaksan)
        return 1
    else:
        await c.send_message(id,"❌لینک اشتباه است",reply_markup=keyboard_vaksan)
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
                    worksheet.write(f'D{f}',driver.find_element_by_xpath(f"/html/body/center/table[2]/tbody/tr[{j}]/td[5]").text)
                else:
                    t+=1
                j+=1 
        workbook.close()
        return 1
    except:
        return 0
    
def login(user,pas,driver):
    try:
        driver.get("https://puya.kashmar.ac.ir/gateway/PuyaAuthenticate.php")
        driver.find_element_by_name("UserID").send_keys(user)
        driver.find_element_by_name("DummyVar").send_keys(pas)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        time.sleep(1)
        return 1
    except:
        return 0
        
def get_information(driver,user,password,ca):
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

            list_p.append(user)
            

            start=file.find("نام پدر:")
            end=file.find("\n",start)
            list_p.append(file[start+8:end])
            start=end

            list_p.append(password)
            list_p.append(ca.message.chat.id)
            change_and_save(list_p)
            return 1
        except:
            return 0
    else:
        pass

def is_raced(driver):
    try:
        url="https://puya.kashmar.ac.ir/gateway/PuyaMainFrame.php"
        driver.get(url) 
        time.sleep(1) 
        x=driver.find_elements_by_tag_name("span")
        c=x[0].text.find("راکد")
        return c
    except:
        return 0
#------------------------------====================================/////////////////////////////////////////////////////////////////////////////////////
option=webdriver.ChromeOptions()
# try:
#     option.binary_location="C:\Program Files\Google\Chrome\Application\chrome.exe"
# except:
option.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
option.add_argument("--headless")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--no-sandbox")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
api_id=13893053
api_hash="f586d92837b0f6eebcaa3e392397f47c"
bot_token="5264885028:AAGrhDzePM11mRUmbHG2rK2q6Id5dxE1XWw"
app = Client("acontet", api_id=api_id,api_hash=api_hash,bot_token=bot_token)
hozor_ids={}
update_ids={}
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
            text+=f"**📝نام و نام خانوادگی:**{p[0]}{p[1]}\n** ✏نام پدر: ** {p[3]}\n**📞شماره ملی:** {p[2]}\n**✔پسوورد:** {p[4]}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
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
        list_user=open("all_user.txt","r",encoding="UTF-8").read().split()
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
@app.on_message(filters.private & filters.user(618260788) & filters.regex("^get$"))
async def send_date(c,m):
    await m.reply_document("all_information.xls")
#--------------------------------------------------------------------------------------------------------------------------------------------------------- 
def diffDate(DateStr2, DateStr1):
   from datetime import datetime
   fmt = '%Y-%m-%d'
   d2 = datetime.strptime(DateStr2, fmt)
   d1 = datetime.strptime(DateStr1, fmt)
   return (d2-d1).days

def cheker_hozore(id):
    time=jdatetime.date.today().strftime("%H %Y-%m-%d").split(" ")
    if id in hozor_ids:
        hor=hozor_ids[id][:3]
        if (int(time[0])-int(hor)>=1) and (diffDate(time[1],hozor_ids[id][3:])>=0):
            hozor_ids[id]=f"{time[0]} {time[1]}"
            return 1
        else:
            return 0
    else:
        hozor_ids[id]=f"{time[0]} {time[1]}"
        return 1

def cheker_update(id):
    time=jdatetime.date.today().strftime("%Y-%m-%d")
    if id in update_ids:
        if (diffDate(time,update_ids[id])>0):
            update_ids[id]=time
            return 1
        else:
            return 0
    else:
        update_ids[id]=time
        return 1

@app.on_message(filters.private & filters.command("start","/"))
async def start_user(c,m):
    list_id=open("all_user.txt","r",encoding="UTF-8").read().split()
    if not(str(m.chat.id) in list_id):
        file_user=open("all_user.txt","a",encoding="UTF-8")
        file_user.write(str(m.chat.id)+" ")
        file_user.close()
    await m.reply("سلام دانشجوی گرامی🖐\n✳با این ربات راحت تر و سریع تر به پورتالت دسترسی پیدا کن.",reply_markup=keyboard_home)

@app.on_callback_query()
async def callback(c,ca):
    text=ca.data[:7]
    await c.delete_messages(ca.message.chat.id,ca.message.message_id)

    if text=="daytime":
        respons=requests.get("http://api.codebazan.ir/time-date/?json=fa")
        response=respons.json()
        ti=response["result"]["time"]
        date=response["result"]["date"]
        faawe=response["result"]["faweekname"]
        await c.send_message(ca.message.chat.id,f"🕕**ساعت**: {ti}\n📅**تاریخ**: {date}\n🗓{faawe}",reply_markup=keyboard_home)
    
    if text=="zoj_frd":
        tim=jdatetime.date.today().strftime("%Y-%m-%d")
        tadd=diffDate(tim,"1401-01-01")+1
        xer=tadd/7
        if xer%2>=1:
            await c.send_message(ca.message.chat.id,"📅این هفته **زوجه!**",reply_markup=keyboard_home)
        elif xer%2>=0:
            await c.send_message(ca.message.chat.id,"📅این هفته **فرده!**.",reply_markup=keyboard_home)
            
    if text=="pnl_usr":
        file_list=open("logined.txt","r",encoding="UTF-8").read().split()
        if str(ca.message.chat.id) in file_list:
            await c.send_message(ca.message.chat.id,"👻",reply_markup=keyboard_personal)
        else:
            username=await c.ask(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا **وارد**  شوید.\n✔برای ورود لطفا ابتدا شماره دانشجویی خود را به لاتین ارسال کنید\n🔙برای بازگشت به منو اصلی از دستور /cancel استفاده کنید.")
            await c.delete_messages(username.chat.id,username.message_id)
            await c.delete_messages(username.chat.id,username.request.message_id)
            if username.text=="/cancel":
                await c.send_message(ca.message.chat.id,"🏠",reply_markup=keyboard_home)
            else:
                password=await c.ask(username.chat.id,"🗄لطفا پسوورد خود را ارسال کنید:\n✔برای برگشت به منو اصلی دستور /cancel را ارسال کنید")
                await c.delete_messages(password.chat.id,password.message_id)
                await c.delete_messages(password.chat.id,password.request.message_id)
                if password.text=="/cancel":
                    await c.send_message(ca.message.chat.id,"🏠",reply_markup=keyboard_home)
                else:
                    sinn=1
                    khosh=await c.send_message(password.chat.id,"📥در حال دریافت اطلاعات لطفا صبور باشید")
                    # try:
                    #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                    # except:
                    driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                    driver.maximize_window()
                    if login(username.text,password.text,driver)==1:
                        time.sleep(0.5)
                        if get_information(driver,username.text,password.text,ca)==1:
                            time.sleep(0.5)
                            if is_raced(driver)==-1:
                                namer=get_name_family(password.chat.id)
                                piame=await c.send_message(ca.message.chat.id,f"📡درحال اتصال به پرتال **¦ {namer} ¦**\n",parse_mode="markdown")
                                time.sleep(0.5)
                                plan_class(driver,ca.message.chat.id)
                                await piame.edit(f"📡درحال اتصال به پرتال **¦ {namer} ¦**\n✅دریافت برنامه کلاسی\n",parse_mode="markdown")
                                time.sleep(0.5)
                                darss(driver,ca.message.chat.id)
                                await piame.edit(f"📡درحال اتصال به پرتال **¦ {namer} ¦**\n✅دریافت برنامه کلاسی\n✅دریافت لیست درس ها\n",parse_mode="markdown")
                                time.sleep(0.5)
                                emtehanat(driver,ca.message.chat.id)
                                await piame.edit(f"📡درحال اتصال به پرتال **¦ {namer} ¦**\n✅دریافت برنامه کلاسی\n✅دریافت لیست درس ها\n✅دریافت برنامه امتحانی\n",parse_mode="markdown")
                                await c.delete_messages(piame.chat.id,piame.message_id)
                                await c.send_message(password.chat.id,"✅دریافت اطلاعات کامل شد",reply_markup=keyboard_personal)
                                file_login=open("logined.txt","a",encoding="UTF-8")
                                file_login.write(str(ca.message.chat.id)+" ")
                                file_login.close()
                            else:
                                await c.send_message(password.chat.id,"❌این دانشجو وضعیت راکد دارد و دسترسی به پنل کاربری ندارد‼",reply_markup=keyboard_home)
                        else:
                            sinn=0
                    else:
                        sinn=0
                    if sinn==0:
                        await c.send_message(password.chat.id,"❌اطلاعات ورود اشتباه است به منو اصلی باز میگردید‼",reply_markup=keyboard_home)
                    driver.quit()
                    await c.delete_messages(khosh.chat.id,khosh.message_id)
        
    if text=="taghams":
        await c.send_photo(ca.message.chat.id,"taghams.jpg",reply_markup=keyboard_home)
    
    if text=="hlpmali":
        await c.send_message(ca.message.chat.id,"❇به بخش حمایت مالی خوش امدید🙏\n💎اگر مایل هستید میتوانید برای انلاین نگه داشتن ربات به مبلغ دلخواه مارا حمایت کنید",reply_markup=keyboard_hlpmali)
    
    if text=="darbare":
        await c.send_message(ca.message.chat.id,"سلام دانشجوی عزیز🖐\n🤖این ربات جهت کار شمارو برای دریافت بعضی اطلاعات از سایت تسهیل میکنه\nاگر نظری پیشنهادی یا احیانا خطایی رخ داد میتونید به بنده اعلام کنید:\n🆔@Rezabz2.",reply_markup=keyboard_home)
    
    if text=="infvaks":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            await c.send_message(ca.message.chat.id,"💉",reply_markup=keyboard_vaksan)
    
    if text=="hzrOgyb":
        if cheker_hozore(ca.message.chat.id)==1:
            try:
                par=get_user_pass(ca.message.chat.id).split()
            except:
                par=get_user_pass(ca.message.chat.id)
            if (par)==None:
                await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
            else:
                hzr=await c.send_message(ca.message.chat.id,"📥در حال دریافت...\nلطفا کمی صبر کنید")
                par=get_user_pass(ca.message.chat.id).split()
                # try:
                #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                # except:
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                driver.maximize_window()
                login(par[0],par[1],driver)
                hozore(driver,ca.message.chat.id)
                driver.quit()
                await c.send_photo(ca.message.chat.id,f"hozor{ca.message.chat.id}.png",reply_markup=keyboard_personal)
                os.remove(f"hozor{ca.message.chat.id}.png")
                await c.delete_messages(hzr.chat.id,hzr.message_id)
        elif cheker_hozore(ca.message.chat.id)==0:
            await c.send_message(ca.message.chat.id,"❌هنوز محدودیت 1 ساعته شما به پایان نرسیده است.",reply_markup=keyboard_personal)
    
    if text=="plnclas":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            plncl=await c.send_message(ca.message.chat.id,"📥در حال دریافت...\nلطفا کمی صبر کنید")
            try:
                await c.send_photo(ca.message.chat.id,f"plan_class{ca.message.chat.id}.png",reply_markup=keyboard_personal)
            except:
                par=get_user_pass(ca.message.chat.id).split()
                # try:
                #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                # except:
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                driver.maximize_window()
                login(par[0],par[1],driver)
                plan_class(driver,ca.message.chat.id)
                driver.quit()
                await c.send_photo(ca.message.chat.id,f"plan_class{ca.message.chat.id}.png",reply_markup=keyboard_personal)
            await c.delete_messages(plncl.chat.id,plncl.message_id)
    
    if text=="plncors":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            cors=await c.send_message(ca.message.chat.id,"📥در حال دریافت...\nلطفا کمی صبر کنید")
            try:
                await c.send_photo(ca.message.chat.id,f"plan_emtehan{ca.message.chat.id}.png",reply_markup=keyboard_personal)
            except:
                par=get_user_pass(ca.message.chat.id).split()
                # try:
                #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                # except:
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                driver.maximize_window()
                login(par[0],par[1],driver)
                emtehanat(driver,ca.message.chat.id)
                driver.quit()
                await c.send_photo(ca.message.chat.id,f"plan_emtehan{ca.message.chat.id}.png",reply_markup=keyboard_personal)
            await c.delete_messages(cors.chat.id,cors.message_id)
    if text=="lessons":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            lessen=await c.send_message(ca.message.chat.id,"📥در حال دریافت...\nلطفا کمی صبر کنید")
            try:
                wb = xlrd.open_workbook(f"dars{ca.message.chat.id}.xls")
            except:
                par=get_user_pass(ca.message.chat.id).split()
                # try:
                #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                # except:
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                driver.maximize_window()
                login(par[0],par[1],driver)
                darss(driver,ca.message.chat.id)
                driver.quit()
            list_key=[]
            wb = xlrd.open_workbook(f"dars{ca.message.chat.id}.xls")
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            for i in range(sheet.nrows):
                pof=sheet.row_values(i)
                list_key.append([  # First row
                        InlineKeyboardButton(  # Generates a callback query when pressed
                            f"📚{pof[0]}",
                            callback_data=f"clasrom{pof[1]}-{pof[2]}"
                        )
                    ])
            list_key.append([  # First row
                        InlineKeyboardButton(  # Generates a callback query when pressed
                            "🔙برگشت به پنل کاربری",
                            callback_data="backpnl"
                        )
                    ])
            await c.send_message(ca.message.chat.id,"📁",reply_markup=InlineKeyboardMarkup(list_key))
            await c.delete_messages(lessen.chat.id,lessen.message_id)
             
    if text=="clasrom":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            liker=await c.send_message(ca.message.chat.id,"📥در حال دریافت...\nلطفا کمی صبر کنید")
            number_less=ca.data[7:]
            code_darse=number_less.split("-")
            name_ostad=get_name_ostad(code_darse[0],ca.message.chat.id)
            # try:
            #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
            # except:
            driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
            driver.maximize_window()
            link_las=search_and_get_link(driver,ca.message.chat.id,number_less)
            await c.send_message(ca.message.chat.id,f"👨‍🎓 نام استاد: {name_ostad}\n🆔 کد درس: {code_darse[0]}\n💠گروه درس: {code_darse[1]}\n▪لینک درس: {link_las}",reply_markup=InlineKeyboardMarkup(
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
        await c.delete_messages(liker.chat.id,liker.message_id)
        driver.quit()
    if text=="numterm":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            dart=await c.send_message(ca.message.chat.id,"📥در حال دریافت...\nلطفا کمی صبر کنید")
            await number_do(ca.message.chat.id,c,ca,1)
            await c.delete_messages(dart.chat.id,dart.message_id)
        
    if text=="updinfo":
        if cheker_update(ca.message.chat.id)==1:
            try:
                par=get_user_pass(ca.message.chat.id).split()
            except:
                par=get_user_pass(ca.message.chat.id)
            if (par)==None:
                await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
            else:
                mes_job=await c.send_message(ca.message.chat.id,"♻در حال بروزرسانی اطلاعات لطفا صبور باشید")
                # try:
                #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                # except:
                neme=get_name_family(ca.message.chat.id)
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                driver.maximize_window()
                pim=await c.send_message(ca.message.chat.id,f"📡درحال اتصال به پرتال **¦ {neme} ¦**\n",parse_mode="markdown")
                login(par[0],par[1],driver)
                if plan_class(driver,ca.message.chat.id)==1:
                    await pim.delete()
                    pim=await c.send_message(ca.message.chat.id,f"📡درحال اتصال به پرتال **¦ {neme} ¦**\n✅دریافت برنامه کلاسی\n",parse_mode="markdown")
                    time.sleep(0.5)
                    darss(driver,ca.message.chat.id)
                    await pim.delete()
                    pim=await c.send_message(ca.message.chat.id,f"📡درحال اتصال به پرتال **¦ {neme} ¦**\n✅دریافت برنامه کلاسی\n✅دریافت لیست درس ها\n",parse_mode="markdown")
                    time.sleep(0.5)
                    emtehanat(driver,ca.message.chat.id)
                    await pim.delete()
                    pim=await c.send_message(ca.message.chat.id,f"📡درحال اتصال به پرتال **¦ {neme} ¦**\n✅دریافت برنامه کلاسی\n✅دریافت لیست درس ها\n✅دریافت برنامه امتحانی\n",parse_mode="markdown")
                    time.sleep(0.5)
                    await number_do(ca.message.chat.id,c,ca,0)
                    await pim.delete()
                    pim=await c.send_message(ca.message.chat.id,f"📡درحال اتصال به پرتال **¦ {neme} ¦**\n✅دریافت برنامه کلاسی\n✅دریافت لیست درس ها\n✅دریافت برنامه امتحانی\n✅دریافت نمرات ترم\n",parse_mode="markdown")
                    time.sleep(0.5)
                    vaksan(driver,ca.message.chat.id)
                    await pim.delete()
                    pim=await c.send_message(ca.message.chat.id,f"📡درحال اتصال به پرتال **¦ {neme} ¦**\n✅دریافت برنامه کلاسی\n✅دریافت لیست درس ها\n✅دریافت برنامه امتحانی\n✅دریافت نمرات ترم\n✅دریافت اطلاعات واکسناسیون\n",parse_mode="markdown")
                    time.sleep(0.5)
                    await pim.delete()
                    await c.send_message(ca.message.chat.id,"✅دریافت اطلاعات کامل شد",reply_markup=keyboard_personal)
                    await c.delete_messages(mes_job.chat.id,mes_job.message_id)
                else:
                    await c.delete_messages(pim.chat.id,pim.message_id)
                    await c.send_message(ca.message.chat.id,"❌اطلاعات ورود اشتباه است",reply_markup=keyboard_home)
                    await c.delete_messages(mes_job.chat.id,mes_job.message_id)
                driver.quit()
        elif cheker_update(ca.message.chat.id)==0:
            await c.send_message(ca.message.chat.id,"❌هنوز محدودیت یک روزه شما به پایان نرسیده است.",reply_markup=keyboard_personal)
    if text=="backhom":
        await c.send_message(ca.message.chat.id,"🏠",reply_markup=keyboard_home)
    
    if text=="vaksshw":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            vakshow=await c.send_message(ca.message.chat.id,"📥در حال دریافت...\nلطفا کمی صبر کنید")
            try:
                await c.send_photo(ca.message.chat.id,f"vaksan{ca.message.chat.id}.png",reply_markup=keyboard_vaksan)
            except:
                par=get_user_pass(ca.message.chat.id).split()
                # try:
                #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                # except:
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                driver.maximize_window()
                login(par[0],par[1],driver)
                vaksan(driver,ca.message.chat.id)
                driver.quit()
                await c.send_photo(ca.message.chat.id,f"vaksan{ca.message.chat.id}.png",reply_markup=keyboard_vaksan)
            await c.delete_messages(vakshow.chat.id,vakshow.message_id)
    
    if text=="vakssbt":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            mes_nob=await c.send_message(ca.message.chat.id,"🖐سلام به بخش ثبت کارت دیجیتال واکسناسیون💉 خوش امدید\n🔙برای برگشت به پنل کاربری از دستور /cancel استفاده کنید")
            link_vaksan=await c.ask(ca.message.chat.id,"برای ثبت کارت ئاکسن دیجیتال خود در سایت دانشگاه لطفا لینک ارسال شده از سایت سلامت را ارسال کنید.\nنمونه لینک:\nvaccinecard.salamat.gov.ir/a69f83a2127560414da948cd8603db1f0***")
            if link_vaksan.text=="/cancel":
                await c.send_message(ca.message.chat.id,"👻",reply_markup=keyboard_personal)
            else:
                ms=await c.send_message(link_vaksan.chat.id,"📤در حال بارگزاری...\nلطفا کمی صبر کنید")
                # try:
                #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
                # except:
                driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
                driver.maximize_window()
                par=get_user_pass(ca.message.chat.id).split()
                login(par[0],par[1],driver)
                await comit_vaksan(driver,link_vaksan.text,c,ca.message.chat.id)
                driver.quit()
                await c.delete_messages(ms.chat.id,ms.message_id)
            await c.delete_messages(link_vaksan.chat.id,link_vaksan.message_id)
            await c.delete_messages(link_vaksan.chat.id,link_vaksan.request.message_id)
            await c.delete_messages(mes_nob.chat.id,mes_nob.message_id)
    
    if text=="backpnl":
        await c.send_message(ca.message.chat.id,"👻",reply_markup=keyboard_personal)
    
    if text=="claszbt":
        try:
            par=get_user_pass(ca.message.chat.id).split()
        except:
            par=get_user_pass(ca.message.chat.id)
        if (par)==None:
            await c.send_message(ca.message.chat.id,"❌شما تا کنون وارد نشده اید.\n💥برای استفاده از پنل کاربری ابتدا با استفاده از دکمه پنل کاربری وارد شوید شوید.",reply_markup=keyboard_home)
        else:
            number_les=ca.data[7:]
            maseg_class=await c.send_message(ca.message.chat.id,"📥در حال دریافت لیست.\nلطفا کمی منتظر بمانید.")
            # try:
            #     driver=webdriver.Chrome(executable_path="C:\\Users\\rezabakhsh\\Desktop\\selenium\\chromedriver",chrome_options=option)
            # except:
            driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=option)
            
            driver.maximize_window()
            await get_link_recorded(driver,ca.message.chat.id,c,number_les)
            driver.quit()
            await c.delete_messages(maseg_class.chat.id,maseg_class.message_id)
    
app.run()
