Andi meminta saya membuat self-service cashier di supermarket miliknya, berikut requirements-nya:

1. Membuat objek dari sebuah class: trnsct = Transaction()

class Transaction:

2. User ingin membuat instance baru dengan menambahkan nama item, jumlah item, dan harga item

def add_item(self, name, amount, price):

3. User ingin memperbarui item dengan memasukkan nama item dan jumlah item atau harga item tanpa menghapus item tersebut

def name_update(self, name, new_name):
def amount_update(self, name, new_amount):
def price_update(self, name, price_update):

4. User ingin menghapus item dari daftar dengan memasukkan nama item
User ingin menghapus semua item dari daftar secara sekaligus 

def delete_item(self, name):
def reset_transaction(self):

5. User ingin memeriksa daftar item yang akan dibeli, jika pesanan sudah sesuai maka akan mengeluarkan output "Pemesanan sudah benar" beserta daftar item, dan akan mengeluarkan peringatan, "Terdapat kesalahan input" jika pesanan tidak sesuai

def check_order(self):

6. User ingin menghitung total belanja yang sudah dibeli, ketentuannya adalah sebagai berikut:
a. Jika total belanja di atas 200.000 maka akan mendapat diskon sebesar 5%
b. Jika total belanja di atas 300.000 maka akan mendapat diskon sebesar 8%
c. Jika total belanja di atas 800.000 maka akan mendapat diskon sebesar 10%

def total_price(self):


```python

```
