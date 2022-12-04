Requirement:

Andi meminta saya membuat self-service cashier di supermarket miliknya, berikut requirements-nya:

1. Membuat objek dari sebuah class: trnsct = Transaction()

2. User ingin membuat instance baru dengan menambahkan nama item, jumlah item, dan harga item

3. User ingin memperbarui item dengan memasukkan nama item dan jumlah item atau harga item tanpa menghapus item tersebut

4. User ingin menghapus item dari daftar dengan memasukkan nama item. User ingin menghapus semua item dari daftar secara sekaligus 

5. User ingin memeriksa daftar item yang akan dibeli, jika pesanan sudah sesuai maka akan mengeluarkan output "Pemesanan sudah benar" beserta daftar item, dan akan mengeluarkan peringatan, "Terdapat kesalahan input" jika pesanan tidak sesuai

6. User ingin menghitung total belanja yang sudah dibeli, ketentuannya adalah sebagai berikut:
a. Jika total belanja di atas 200.000 maka akan mendapat diskon sebesar 5%
b. Jika total belanja di atas 300.000 maka akan mendapat diskon sebesar 8%
c. Jika total belanja di atas 800.000 maka akan mendapat diskon sebesar 10%

Alur Program dan penjelasan code

script ini digunakan untuk otomasi pemesan item di sebuah supermarket

1. calon customer measukkan item apa yang akan dibeli, berapa banyak yang akan dibeli, dan berapa harganya. Fungsi dari tindakan tersebut adalah add_item

2. jika user ingin memperbarui item maka ia harus menggunakan fungsi name_update memasukkan nama item dan jumlah item atau harga item tanpa menghapus item tersebut

3. jika user ingin menghapus item dari daftar dengan memasukkan nama item melalui fungsi delete_item, dan menggunakan fungsi reset transaction untuk menghapus seluruh item dalam daftar secara sekaligus 

4. jika user ingin memeriksa daftar item yang akan dibeli dengan fungsi check_order, pesanan sudah sesuai maka akan mengeluarkan output "Pemesanan sudah benar" beserta daftar item, dan akan mengeluarkan peringatan, "Terdapat kesalahan input" jika pesanan tidak sesuai

5. jika user ingin menghitung total belanja yang sudah dibeli, maka ia harus menggunakan fungsi total_price

Test Case

```python

```

Conclusion:

Pada project ini saya membuat:
Transaction Class, dengan beberapa fungsi seperti
1. Add_item untuk menambahkan instaance baru seperti nama barang, jumlah barang, dan harga barang
2. Update untuk memperbarui instance tanpa menghapusnya, seperti memperbarui nama, jumlah, dan harga barang
3. delete_item untuk menghapus item tertentu dan reset_transaction untuk menghapus seluruh item secara bersamaan
4. check_order untuk memeriksa item apa saja yang sudah dibeli dan juga total harga yang bersalah dari perkalian antara jumlah barang dikali dengan harga per barang
5. price_total untuk menghitung berapa uang yang harus dibayarkan setelah diskon, dan jika memenuhi persyaratan

Untuk future work, bisa ditingkatkan untuk kemungkinan yang terjadi diluar aturan yang diberikan seperti membuat ID yang unique agar tidak menjadi masalah jika terjadi dupiikasi data


