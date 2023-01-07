import os 
# import pathlib

def Todo_app():
    topshiriqlar = [] 
    topshiriq = input("Topshiriqni kiriting: ")
    topshiriqlar.append(topshiriq)
    os.system('cls')
    while True:
        topshiriq_qoshish = input("Topshiriq qo'shish: ")
        os.system('cls')
        topshiriqlar.append(topshiriq_qoshish)
        bajarilgan_topshiriqlar= int(input("Nachanchi toshiriq bajarildi : "))
        os.system('cls')
        bajarilganlari= topshiriqlar[bajarilgan_topshiriqlar -1 ]
        def bajarilgan(text):
            result = ''
            for x in text:
                result = result + x +'\u0336'
            m = topshiriqlar.index(bajarilganlari)
            topshiriqlar.remove(bajarilganlari)
            topshiriqlar.insert(m,result)
            for num, txt in enumerate(topshiriqlar):
                roixt = f" {num + 1} {txt}"
                print(roixt)
        print(bajarilgan(bajarilganlari))
        ask = input('''
    Yana urinib koring 😊
    urinib korish uchun : 'cont' ni bosing
    chiqish uchun 😒: 'exit' ni bosin
        ''')
        if ask == "cont":
            continue
        else:
            print("Charchameng kep turing janob 👨‍💻")
            break

Todo_app()