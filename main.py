from flet import *
import sqlite3

conn = sqlite3.connect("dato.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name Text,
mail Text,
phone Text,
address Text,
mathematics INTEGER,
Arabic INTEGER,
Kurdish INTEGER,
English INTEGER,
sciences INTEGER,
Social_studies INTEGER,
Religion INTEGER, 
Art INTEGER,
Sport INTEGER

)
""")
conn.commit()


def main(page: Page):
    page.title = 'school'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 800
    page.bgcolor = "51cdf9"
    page.themo_mod = ThemeMode.SYSTEM
    # ...............................
    table_name = 'student'
    query = f'SELECT COUNT(*) FROM{table_name}'
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]

    def add(e):
        cursor.execute(
            " INSERT INTO student(name,mail,phone,address,mathematics,Arabic,Kurdish,English,sciences,Social_studies, Religion,Art,Sport) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (tname.value, tmaile.value, tphone.value, taddress.value, mathmatics.value, Arabic.value, Kurdish.value,
             sciences.value, Social_studies.value, English.value, Religion.value, Arts.value, Sport.value))
        conn.commit()

    def show(r):
        page.clean()
        c = conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        print(users)
        if not users == "":
            keys = ["id", "name", "mail", "phone", "address", "mathematics", "Arabic", "Kurdish", "English", "sciences",
                    "Social_studies", "Religion", "Art", "Sport"]
            result = [dict(zip(keys, values)) for values in users]
            for x in result:

                m=x["mathematics"]
                a = x["Arabic"]
                k = x["Kurdish"]
                e = x["English"]
                s = x["sciences"]
                ss = x["Social_studies"]
                r = x["Religion"]
                aa = x["Art"]
                sp = x["mathematics"]
                res=(m+a+k+e+s+ss+r+aa+sp)/9
                if res < 50:
                    a=Text('😢 کەفتی',color="red")
                if res >50:
                    a = Text('😍 سەرکەفتی',color= "green")
                page.add(
                    Card(
                        color='amber',
                        content=Container(
                            content=Column([
                                ListTile(
                                    leading=Icon(icons.PERSON),
                                    title=Text('Name :   ' + x['name'], color='white'),
                                    subtitle=Text('Email :'+x['mail'],color='red'),


                                ),
                                Row([
                                    Text('مۆبایل :'+x['phone']),
                                    Text('ناڤ و نیشان:' + x['address'])
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text("بیرکاری"+str(x["mathematics"]),color='blue'),Text("عەرەبی"+str(x["Arabic"]),color='blue'),Text("کوردی"+str(x["Kurdish"]),color='blue')
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text("ئینگلیزی" + str(x["English"]), color='blue'),
                                    Text("زانست" + str(x["sciences"]), color='blue'),
                                    Text("کۆمەڵایەتی" + str(x["Social_studies"]), color='blue')
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text("ئایین" + str(x["Religion"]), color='blue'),
                                    Text("هۆنەری" + str(x["Art"]), color='blue'),
                                    Text("وەرزش" + str(x["Sport"]), color='blue')
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    a
                                ],alignment=MainAxisAlignment.CENTER)

                            ])
                        )
                    )
                )
                page.update()

    # ............................................
    tname = TextField(label='ناڤێ قوتابی', icon=icons.PERSON, rtl=True, height=38)
    tmaile = TextField(label='ئیمێڵ', icon=icons.MAIL, rtl=True, height=38)
    tphone = TextField(label='ژمارا مۆبایلێ', icon=icons.PHONE, rtl=True, height=38)
    taddress = TextField(label='ناڤ ونیشان', icon=icons.LOCATION_CITY, rtl=True, height=38)
    # .............................................
    marktext = Text("Marks student - نمرێن قوتابی", text_align='center', weight='bold')
    mathmatics = TextField(label='بیرکاری', width=110, rtl=True, height=38)
    Arabic = TextField(label='عەرەبی', width=110, rtl=True, height=38)
    Kurdish = TextField(label='کوردی', width=110, rtl=True, height=38)
    sciences = TextField(label='زانست', width=110, rtl=True, height=38)
    Social_studies = TextField(label='کۆمەڵایەتی', width=110, rtl=True, height=38)
    English = TextField(label='ئینگلیزی', width=110, rtl=True, height=38)
    Religion = TextField(label='ئایین', width=110, rtl=True, height=38)
    Arts = TextField(label='هۆنەری', width=110, rtl=True, height=38)
    Sport = TextField(label='وەرزش', width=110, rtl=True, height=38)

    # ................................................
    addbuttn = ElevatedButton("زێدەکرنا قوتابی", width=170, style=ButtonStyle(bgcolor='white', padding=30),
                              on_click=add)
    showbuttn = ElevatedButton("خستنە روویا هەموو قوتابیان", width=170, style=ButtonStyle(bgcolor='white', padding=20),
                               on_click=show)
    # .....................................................

    page.add(Row([Image(src="sh1.gif", width=280)], alignment=MainAxisAlignment.CENTER),
        Row([Text("ئەپلیکێشنا مامۆستا و قوتابیان", size=20, font_family="Times new roman", color='black')],
            alignment=MainAxisAlignment.CENTER),
        Row([
            Text("ژمارا قوتابیێن تۆمارکری :", size=20, font_family="Times new roman", color='black'),
            Text(row_count, size=20, font_family="Times new roman", color='blue')], alignment=MainAxisAlignment.CENTER,
            rtl=True),
        tname,
        tmaile,
        tphone,
        taddress,
        Row([marktext], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([Arabic, Kurdish, English], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([sciences, Social_studies, mathmatics], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([Religion, Arts, Sport], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([addbuttn, showbuttn], alignment=MainAxisAlignment.CENTER, rtl=True)

    )

    page.update()


app(main)
