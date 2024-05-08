class sahmatyarislari():
    def __init__(self,yarismaci_adi,yarismaci_derecesi):
        self.yarismaci_adi=yarismaci_adi
        self.yarismaci_derecesi=yarismaci_derecesi
   
    def yaris_vaxtlari(self):
        print("hefte ici gunorta saat 1de")
    def gunluk_yaris_sayi(self):
        return 15
  


class avropayarislari(sahmatyarislari):
    pass
  
      

class dunyacempionati(sahmatyarislari):
    pass

def yariszamani(a):
    a.yaris_vaxtlari()


print(dir(avropayarislari))


sahmatci=avropayarislari("emin",2)
print(sahmatci.yarismaci_adi)
yariszamani(sahmatci)
sahmatci2=dunyacempionati("emin",2)
yariszamani(sahmatci2)

print(sahmatci.gunluk_yaris_sayi())

sahmatci2.yaris_vaxtlari()
print(sahmatci2.yarismaci_adi)






    
