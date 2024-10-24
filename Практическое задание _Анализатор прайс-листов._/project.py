import os
import csv
import pandas as pd

'''
'output_all.html' - файл со  всеми наименованиями  товара 
                    в файлах корневой директории
'output_sel.html' - файл с отобранными  наименованиями  товара
'''

class PriceMachine():
    
    def __init__(self):
        self.data = []

    def load_prices(self):
        s1 = []
        lst = ['№', 'наименование', 'цена', 'вес', 'файл', 'цена за кг']
        s1.append(lst)
#        print(s1[0])
        file_path = []
        files = os.listdir(".")
        for i in range(len(files)):
            if 'price' in files[i]:
                file_path.append(files[i])
        for name in file_path:
            s = []
            print('file: - ', name)
            with open(name, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    s.append(row)
            for i in range(len(s[0])):
                if (s[0][i] == 'продукт' or s[0][i] == 'товар'
                        or s[0][i] == 'название' or s[0][i] == 'наименование'):
                    i1 = i
            for i in range(len(s[0])):
                if (s[0][i] == 'цена' or s[0][i] == 'розница'):
                    i2 = i
            for i in range(len(s[0])):
                if s[0][i] == 'фасовка' or s[0][i] == 'масса' or s[0][i] == 'вес':
                    i3 = i
            for i in range(1, len(s)):
                lst = [i, s[i][i1], s[i][i2], s[i][i3], name,
                       round((int(s[i][i2]) / int(s[i][i3])), 2)]
                s1.append(lst)
        return s1

    @staticmethod
    def find_text():
        print('Введите товар для поиска')
        text = str(input())
        return text

    def _search_product_price_weight(self, data):
        self.s1 = data
        lst = [['№', 'наименование', 'цена', 'вес', 'файл', 'цена за кг']]
        s2 = []
        a = self.find_text()
        for i in range(len(s1)):
            b = s1[i][1]
            if a.lower() in b.lower():
                s2.append(s1[i])
        s2.sort(key=lambda x: x[5])
        print()
        for i in range(len(s2)):
            s2[i][0] = i + 1
            lst.append(s2[i])
        for x in lst:
            print(x)
        return lst

    @staticmethod
    def export_to_html(lst, file_name):
        html = pd.DataFrame(lst).to_html(header=None, index=False, border=0)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html)
        print(" === File ", file_name,  "    CREATED !!! ===")


# ================================================
    
pm = PriceMachine()

s1 = pm.load_prices()
pm.export_to_html(s1, file_name='output_all.html')

a = "GO!"
while a != "exit":
    result = pm._search_product_price_weight(s1)
    print('Продолжить ?  - "enter"; Выйти из программы? - "exit"')
    a = (str(input())).lower()

pm.export_to_html(result, file_name='output_sel.html')

print('the end  -  Good Bye!')

print("================================")
