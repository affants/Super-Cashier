import pandas as pd
from tabulate import tabulate



class Transaction:
    '''Class yang menjalankan program penghitungan seperti mesin kasir.

    Methods:
    --------
    __init__:
        Menginisiasi program dan menjalan variabel dictionary kosong (dict) dan variabel tagihan (int).
    menu:
        Menampilkan pilihan menu dan input user untuk memilih menu (int)
    checkout:
        Menampilkan keseluruhan barang belanja pelanggan dan print dengan method tabulate.
    add_item:
        Menambahkan barang belanja baru. nama_barang (str), jumlah_barang (int), harga_barang (int)
    update_nama_barang:
        Mengganti nama barang yang sudah ada.
    update_jumlah_barang:
        Mengganti jumlah barang yang sudah ada.
    update_harga_barang:
        Mengganti harga barang yang sudah ada.
    hapus_barang:
        Menghapus barang yang sudah ada.
    reset_transaction:
        Menghapus keseluruhan barang. 
    
    '''
    def __init__(self):
        '''
        Fungsi ini adalah fungsi awal yang akan dijalankan (Initialization) dan akan menginisiasi dictionary
        dari barang yang dibeli oleh pelanggan dan membuat variabel tagihan total. 
        '''
        self.order = {}
        self.tagihan = 0

        self.menu()

    def menu(self):
        '''
        Fungsi ini untuk mengeluarkan angka dan menu yang akan dipilih oleh pelanggan. Pada menu ini pelanggan
        dapat memilih fitur untuk menambah barang, mengubah nama barang , mengubah jumlah barang, menghapus barang,
        menghapus keseluruhan barang, dan melihat total tagihan.

        Attributes:
        pil_menu (int) : input angka 1 - 7.

        '''
        print("=====Selamat Datang=====")
        print("Silahkan memilih menu kasir")
        print("1. Beli Barang")
        print("2. Mengubah nama barang")
        print("3. Mengubah jumlah barang")
        print("4. Mengubah harga barang")
        print("5. Menghapus barang")
        print("6. Menghapus semua belanjaan")
        print("7. Checkout")
        print('\n')
        print('Pilih nomer sesuai menu')
        print('\n')
        while True:
            try:
                pil_menu = int(input('Nomer berapa?  '))
                if pil_menu < 1 or pil_menu > 7:
                    print("Masukkan angka yang ada di menu")
                    break
                else:
                    break
            except:
                print("masukkan angka")
            

        if pil_menu == 1:
            self.add_item()
        
        if pil_menu == 2:
            self.update_nama_barang()
        
        if pil_menu == 3:
            self.update_jumlah_barang()

        if pil_menu == 4:
            self.update_harga_barang()

        if pil_menu == 5:
            self.hapus_barang()

        if pil_menu == 6:
            self.reset_transaction()

        if pil_menu == 7:
            self.total_price()

        
        
    def Checkout(self):
        '''Fungsi ini akan menampilkan barang apa saja yang sudah dipilih oleh pelanggan.

        tampilan akan berbentuk seperti tabel dan berisi nama barang, jumlah barang, harga barang, dan 
        harga total barang. 
        '''
        print("==============Rincian Belanja Anda!===============")
        tabel = pd.DataFrame.from_dict(self.order, orient="index", columns=['Jumlah',
                                                                            'harga per item',
                                                                            'Total Harga'])
        print(tabulate(tabel, showindex=True, headers=['Jumlah', 'Harga Per Item', 'Total Harga']))
        print('\n')
        print('\n')
        print("----------------Terima Kasih--------------------")

    def add_item(self):
        '''Fungsi ini untuk menambah barang yang ingin dibeli
        
        Parameters: 
            self

        Attributes:
        nama_barang (str): nama barang yang akan dibeli
        jumlah_barang (int): jumlah barang yang akan dibeli
        harga_barang (init): harga barang satuan yang akan dibeli.

        Menghasilkan:
        dictionary dengan key: nama_barang dan value: jumlah_barang, harga_barang, total_harga

        total_harga = jumlah_barang*harga_barang
         
        '''
        nama_barang = input("Barang yang ingin dibeli : ").lower()

        while True:
            try:
                jumlah_barang = int(input("Berapa banyak yang ingin dibeli? "))
                if jumlah_barang <= 0 :
                    raise Exception()
                harga_barang = int(input("Berapa harga item tersebut? "))
                if harga_barang <= 0 :
                    raise Exception()
                print('\n')
                break
            except:
                print("Jumlah barang dan Harga harus berupa angka atau tidak boleh 0\nKembali isikan nama barang")
                self.add_item()
                break

        total_harga = jumlah_barang * harga_barang
        self.order[nama_barang] = [jumlah_barang, harga_barang, total_harga]

        self.Checkout()
        print('\n')
        self.menu()



    def update_nama_barang(self):
        '''Fungsi untuk mengganti nama barang

        Attribute:
        ----------
        nama_barang (str)
        nama_new (str)

        '''
        if len(self.order) == 0:
            print('Anda belum membeli barang')
            self.__init__()
        
        while True:
            nama_barang = input('Masukkan nama barang yang ingin diganti namanya?   ').lower()
            if nama_barang in self.order:
                break
            else:
                print(f'Barang {nama_barang} belum anda beli')
                pass
            
        while True:
            try:
                nama_new = input('Masukkan nama barang yang baru:  ')
                break
            except:
                pass

        self.order[nama_new] = self.order[nama_barang]
        del self.order[nama_barang]
        
        self.Checkout()
        print('\n')
        self.menu()

    def update_jumlah_barang(self):
        '''Fungsi untuk mengganti jumlah barang

        Attribute:
        ----------
        nama_barang (str)
        jumlah_new (int)
        '''
        if len(self.order) == 0:
            print('Anda belum membeli barang')
            self.__init__()
        
        while True:
            nama_barang = input('Masukkan nama barang yang ingin diganti jumlahnya?   ').lower()
            if nama_barang in self.order:
                break
            else:
                print(f'Barang {nama_barang} belum anda beli')
                pass
            
        while True:
            try:
                jumlah_new = int(input('Masukkan jumlah barang:  '))
                break
            except:
                print('jumlah barang adalah angka')
                pass

        self.order[nama_barang][0] = jumlah_new
        total_harga_new = self.order[nama_barang][0] * self.order[nama_barang][1]
        self.order[nama_barang][2] = total_harga_new

        self.Checkout()
        print('\n')
        self.menu()
        
    def update_harga_barang(self):
        '''Fungsi untuk mengganti harga barang

        Attribute:
        ----------
        nama_barang (str)
        harga_new (int)

        '''
        if len(self.order) == 0:
            print('Anda belum membeli barang')
            self.__init__()
            
        while True:
            nama_barang = input('Masukkan nama barang yang ingin diganti harganya:   ').lower()
            if nama_barang in self.order:
                break
            else:
                print(f'Barang {nama_barang} belum anda beli')
                pass
        while True:
            try :
                harga_new = int(input("Masukkan harga barang :   "))
                break
            except :
                print("harga harus angka")

        self.order[nama_barang][1] = harga_new
        total_harga_new = self.order[nama_barang][0] * self.order[nama_barang][1]
        self.order[nama_barang][2] = total_harga_new

        self.Checkout()
        print('\n')
        self.menu()

    def hapus_barang(self):
        '''Fungsi untuk menghapus barang.

        Attribute:
        ----------
        nama_barang (str)

        '''
        if len(self.order) == 0:
            print('Anda belum membeli barang')
            self.__init__()

        while True:
            nama_barang = input('Masukkan nama barang yang ingin dihapus:   ').lower()
            if nama_barang in self.order:
                del self.order[nama_barang]
                print(f'Barang {nama_barang} telah berhasil dihapus')
                break
            else:
                print(f'Barang {nama_barang} belum anda beli')
                pass

        self.Checkout()
        print('\n')
        self.menu()

    def reset_transaction(self):
        '''Fungsi untuk menghapus keseluruhan barang
        
       Attribute:
       ---------
       pil_menu (str) : input string "y" atau "n"

        '''
        if len(self.order) == 0:
            print('Anda belum membeli barang')
            self.__init__()

        while True:
            pil_hapus = input("Apakah anda yakin ingin menghapus seluruh barang ? y/n").lower()
            if pil_hapus == "y":
                self.order.clear()
                print("Seluruh barang sudah terhapus, silahkan belanja kembali ")
                break
            else:
                print("Terima kasih")
                pass

        self.Checkout()
        print('\n')
        self.menu()  

    def total_price(self):
        '''Fungsi untuk menampilkan total tagihan belanja.

        kondisi:
        --------
        total_tagihan lebih dari 200.000 dapat diskon 5%
        total_tagihan lebih dari 300.000 dapat diskon 8%
        total_tagihan lebih dari 500.000 dapat diskon 10%

        '''
        if len(self.order) == 0:
            print('Anda belum membeli barang')
            self.__init__()

        for item in self.order:
            self.tagihan += self.order[item][2] 

        print(f'total tagihan anda sebesar {self.tagihan}')
        
        if self.tagihan > 500000:
            potongan = 0.1
            print("Wohoo selamat anda mendapatkan diskon 10%")
        
        elif self.tagihan > 300000:
            potongan = 0.08
            print("Wohoo selamat anda mendapatkan diskon 8%")
       
        elif self.tagihan > 200000:
            potongan = 0.05
            print("Wohoo selamat anda mendapatkan diskon 5%")
        
        else:
            potongan = 0
            print("\n")  

        total_tagihan = self.tagihan - (self.tagihan*potongan)
        print(f'Tagihan anda menjadi Rp {total_tagihan}')

        return total_tagihan
    
tran_123 = Transaction()