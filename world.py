import random

def raqamni_taxmin_qilish():
    tasodifiy_son = random.randint(1, 100)
    taxminlar = 0
    print("1 dan 100 gacha son o'yladim. Uni topishga harakat qiling!")

    while True:
        foydalanuvchi_soni = input("Raqamni kiriting: ")
        
        if foydalanuvchi_soni.isdigit():
            foydalanuvchi_soni = int(foydalanuvchi_soni)
            taxminlar += 1
            
            if foydalanuvchi_soni < tasodifiy_son:
                print("Kattaroq son kiriting.")
            elif foydalanuvchi_soni > tasodifiy_son:
                print("Kichikroq son kiriting.")
            else:
                print(f"Tabriklaymiz! {taxminlar} ta urinishda to'g'ri topdingiz.")
                break
        else:
            print("Iltimos, raqam kiriting.")

raqamni_taxmin_qilish()
