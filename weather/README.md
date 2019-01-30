# โปรแกรม weather

โปรแกรมแปลง Format XML เป็น json เขียนด้วยภาษา Python 3

โดยใช้ module ที่ชื่อว่า xmltodict เข้ามาช่วยในการทำงานของโปรแกรม

สามารถโหลด module โดยใช้คำสั่งใน CMD ตามด้านล่าง

```sh
$ pip install xmltodict
```

สามารถรันใน CMD ได้โดยเข้าไปที่ Directory ของโปรแกรม weather
แล้วใช้คำสั่งด้านล่าง เพื่อรันโปรแกรม weather

```sh
$ py -3 weather.py
```

โดยโปรแกรมจะมีโค้ดที่เรียกไฟล์ .xml เพื่ออ่านข้อมูล

แล้วส่ง output ออกมาเป็นไฟล์ .json


***โดยส่วนของการใช้ module xmltodict ได้นำโค้ดตัวอย่างจากเว็บไซต์ด้านล่าง มาปรับใช้ในการทำโปรแกรมนี้ด้วย***

 - http://carrefax.com/new-blog/2018/3/12/convert-xml-to-json
