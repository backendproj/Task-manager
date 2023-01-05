import os
def todo_app():
    while True:
        list = []
        list_new = []
        ask = input("Topshiriqni kiriting: ")
        list.append(ask)
        os.system("cls")
        if len(list) >= 1 :
                ask2 = input("Topshiriq qo'shish: ")
                os.system("cls")
                list.append(ask2)
                end = int(input("Nechanchi topshiriq bajarildi: "))
                os.system("cls")
                for  joy, soz in enumerate(list):
                    x = f"{joy+1}.{soz}"
                    list_new.append(x)
                for i in list_new:
                    if list_new.index(i) == end - 1:
                        def strike(text):
                            i = 0
                            new_text = ''
                            while i < len(text):
                                new_text = new_text + (text[i] + u'\u0336')
                                i = i + 1
                            return(new_text)
                        print(strike(list_new[end - 1]))
                    else:
                        print(i)  
        exit = input("Exit exit or not: ")
        if exit == "not":
            continue
        else:
            os.system("cls")
            print("Oldik unda 🥂")
            break
todo_app()       

# Ustoz agar bunday bolmasa boshqacha qilib qoygan bo'lsam togirlab bering keyin ozimga pull request qvoring yana ;

