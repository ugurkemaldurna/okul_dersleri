# absolute path vs relative path
# tam yol veya bağıl yol 
# .. üst klasör gösterir 
# . nokta dosyanın kendisi

# f = open("C:\\Users\\Asus\\Desktop\\code\\test.txt")

# print ( f.read())

# f.close()

# import random as rnd

# print(rnd.randrange(0,100))
# print(rnd.random())

# def final_hesapla(vize):
#     if vize < 50:
#         final_icin_gerekli_not = (50 . 0,4 * vize ) / 0.6
#         print("Final için almanız gereken not:" , math.ceil(final_icin_gerekli_not))
#     else:
#         print("Final için almanız gereken not: 50")
# def selam_soyle():
#     print("Merhaba")

# import benimfonksiyonlar
# benimfonksiyonlar.selam_soyle()

# from benimfonksiyonlar import selam_soyle

# def selam_soyle():
#     print("beşinci.py içinden ..")

# benimfonksiyonlar.selam_soyle()

# from benimfonksiyonlar import *

# final_hesapla(26)


# import mymodule.oto
# print(mymodule.oto.version)
# mymodule.oto.ecu_ver()

# import math
# print(math.pow(2,10))
# print(math.sqrt(25))
# print(math.pi)
# print(math.log(21))
# log 3 tabanında 5 nedir?
# print(math.log(3,5))
# if __name__ == "__main__":
#     print("python yorumlayıcısının çağırdığı dosya içerisindesiniz.")

import math 
a = 3 
b = math.pi
c = "001"
d = 5.2
e = 1_000_000
# print("Hata yaz")
# print(a , " " , "pi=" , b ," " , c," " , d," ",sep="")
# print(   "d:{1} pi={0}".format(b,d)   )
print("{0:0>7}\t{0:#>7}\t{0:x>7}".format(a))
print("{0}\t{0}\t{0}".format(e))