import random

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 모음'
        ordering = ['title', ]


    def __init__(self):
        self.productNum = [] # 상품의 식별번호
        self.productName = [] # 상품의 이름
        self.productPrice = [] # 상품의 가격
        self.productID = []
        self.proType = ['coffee', 'juice', 'brunch', 'bread']
        self.productType = [] # 상품의 타입
        self.Activation = [] # True or False

    def id_issue(self):
        textList = [
                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '1','2','3','4','5','6','7','8','9','0',
                    '!','@','#','$','%','^','&','*'
                    ]
        output = []
        while True :
            for i in range(random.randint(11,16)):
                output.append(textList[random.randint(0, (len(textList)-1))])

            if output not in self.productID :
                break

        return "".join(output)




    def creProduct(self, name, price, types, acti : 'activation' ):
        # 중복 제거
        if name in self.productName :
            return
        # --------------------------------------------

        if types in self.proType:
            self.productName.append(name)
            self.productNum.append(len(self.productNum)+1)
            self.productID.append(id_issue())
            self.productPrice.append(price)
            self.proType.append(types)
            self.Activation.append(True)

        else :
            return

    def deactivate(self, name):
        if name in self.name:
            self.activation[self.productName.index(name)] = False

        else :
            return

    def activate(self, name):
        if name in self.productName :
            self.activation[self.productName.index(name)] = True
        else :
            return

    def update(self, name, price, types):
        if name in self.productName :
            a = self.productName.index(name)

            self.productName[a] = str(name)
            self.productPrice[a] = int(price)
            if types in self.proType:
                self.proType[a] = types
        else :
            return




    def str(self):
        return self.title