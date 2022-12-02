#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import library yang dibutuhkan


import pandas as pd
from tabulate import tabulate

class Transaction:
    
    def __init__(self):
        
        """
        Fungsi untuk menginisiasi dictionary
        self.item adalah sarana untuk menyimpan dictionary
        self.table adalah sarana untuk menyimpan table dalam bentuk dataframe
        
        """
        self.item = {}
        self.table = pd.DataFrame()
    
    def add_item(self, name, amount, price):
        
        """
        fungsi menambahkan item

        parameters
        name(str)       : nama barang yang akan ditambahkan
        amount(int)     : jumlah barang yang akan ditambah
        price(int)      : harga barang yang akan ditambah

        """
        self.item.update({name: [amount, price]})
        print(f'item yang dibeli adalah {self.item}')
        
    def name_update(self, name, new_name):
        
        """
        fungsi memperbarui nama item

        parameters
        name(str)         : nama barang 
        new_name(int)     : nama barang yang baru

        """
        temp = self.item[name]
        self.item.pop(name)
        self.item.update({new_name: temp})
        print('Nama barang diperbarui')
        
    def amount_update(self, name, new_amount):
        
        """
        fungsi memperbarui nama item

        parameters
        name(str)           : nama barang 
        new_amount(int)     : jumlah barang yang baru

        """
        self.item[name][0] = new_amount
        print('Jumlah barang diperbarui')
    
    def price_update(self, name, price_update):
        
        """
        fungsi memperbarui nama item

        parameters
        name(str)             : nama barang 
        price_update(int)     : harga barang yang baru

        """
        self.item[name][1] = price_update
        print('Harga barang diperbarui')
        
    def delete_item(self, name):
        
        """
        fungsi memperbarui menghapus item

        parameters
        name(str)             : nama barang yang akan dihapus

        """
        self.item.pop(name)
        print('barang dihapus')
        
    def reset_transaction(self):
        
        """fungsi menghapus seluruh data secara sekaligus"""
        
        self.item.clear()
        print('Data berhasil direset')
        
    def check_order(self):
        
        """
        fungsi memeriksa pesanan belanjaan
        hasil dari fungsi ini menampilkan seluruh daftar belanjaan, termasuk total harga setiap item
        
        """
        data = self.item
        
        try:
            
            if data != {}:
                print('Pemesanan sudah benar')

                for i in data.keys():
                    val = data[i][0]*data[i][1]
                    data[i].append(val)
                    self.table = pd.DataFrame.from_dict(data, orient='index')
                    self.table.columns = ['Jumlah barang', 'Harga barang', 'Total']


                #print(self.table)
                print(tabulate(self.table, self.table.columns, tablefmt="github"))

            else: 
                print('Terjadi kesalahan')
                
                
        except: 
            print("Terjadi Error")
            
            
            
    def total_price(self):
        
        """
        fungsi menampilkan jumlah total belanja 
        hasil dari fungsi ini menampilkan seluruh daftar belanjaan berserta yang sudah diporong diskon jika memenyuhi persyaratan
        
        """

        table = self.table
        try:
            
            if table.empty:
                print('Data kosong')

            else:
                total = int(sum(table['Total']))

                if total >= 200_000 and total <= 300_000:
                    grand_total = total-(total*0.05)
                    print(f'Total belanja anda adalah {grand_total}')
                elif total > 300_000 and total <= 500_000:
                    grand_total = total-(total*0.08)
                    print(f'Total belanja anda adalah {grand_total}')
                elif total > 500_000:
                    grand_total = total-(total*0.1)
                    print(f'Total belanja anda adalah {grand_total}')
                else:
                    print(f'Total belanja anda adalah {total}')
                    
        except:
            print('Terjadi Error')


belanja = Transaction()

# test case 1
belanja.add_item('Aayam Goreng', 2, 20000),
belanja.add_item('Pasta Gigi', 3, 15000),
belanja.add_item('Mainan Mobil', 1, 200000)
belanja.add_item('Mi Instan', 5, 3000)

# test case 2
#belanja.delete_item('Pasta Gigi')

# test case 3
#belanja.reset_transaction()

# test case 4
belanja.check_order()
belanja.total_price()

        


# In[ ]:




