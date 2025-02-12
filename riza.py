#I.S.: Membuat menu utama untuk Aset Perusahaan Clothes 
#F.S.: Menampilkan hasil menu dari Aset Berwujud & Tak Berwujud
import os

MAKSDATA = 10
#subrutin menu utama
def MenuUtama(Pilihan):
    print('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>')
    print('---------------------------------------')
    print('1. Aset Berwujud ( Tangiable Assets )')
    print('2. Aset Tak Berwujud ( Intangiable Asstes )')
    print('0. KELUAR')
    Pilihan = int(input('Pilihan Anda?  '))
    #validasi
    while (Pilihan < 0) or (Pilihan > 2):
        print('Nomor Aset Perusahaan tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>')
        print('---------------------------------------')
        print('1. Aset Berwujud ( Tangiable Assets )')
        print('2. Aset Tak Berwujud ( Intangiable Asstes )')
        print('0. KELUAR')
        Pilihan = int(input('Pilihan Anda?  '))
    return Pilihan
#subrutin menu tangiable assets
def TangiableAssets(PilihanTangiable):
    print("=====================================")
    print("<< ASET BERWUJUD ( TANGIABLE ASSETS ) >>")
    print("=====================================")
    print("1. Gudang Barang Dagangan ( Stok Pakaian )")
    print("2. Bahan Baku")
    print("3. Vendor Produksi")
    print("4. Vendor Packaging")
    print("0. KELUAR")
    print("---------------------------------")
    PilihanTangiable = int(input('Pilihan Anda?  '))
    #validasi
    while (PilihanTangiable < 0) or (PilihanTangiable > 4):
        print('Nomor Aset Berwujud tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("=====================================")
        print("<< ASET BERWUJUD ( TANGIABLE ASSETS ) >>")
        print("=====================================")
        print("1. Gudang Barang Dagangan ( Stok Pakaian )")
        print("2. Bahan Baku")
        print("3. Vendor Produksi")
        print("4. Vendor Packaging")
        print("0. KELUAR")
        print("---------------------------------")
        PilihanTangiable = int(input('Pilihan Anda?  '))
        
    return PilihanTangiable
#subrutin menu pilihan stok pakaian
def MenuStokPakaian (PilihanMenuStok):
    print ('===========================================')
    print ('<<GUDANG BARANG DAGANGAN ( STOK PAKAIAN )>>')
    print ('===========================================')
    print ('1. Pengisian Data Stok ')
    print ('2. Penambahan Data Stok ')
    print ('3. Penghapusan Data Stok ')
    print ('0. Kembali ')
    PilihanMenuStok = int(input('Pilihan Anda? '))
    #validasi
    while (PilihanMenuStok < 0) or (PilihanMenuStok > 3):
        print('Nomor Pilihan Anda Tidak Valid. Input Ulang!')
        os.system('pause')
        os.system('cls')
        print ('===========================================')
        print ('<<GUDANG BARANG DAGANGAN ( STOK PAKAIAN )>>')
        print ('===========================================')
        print ('1. Pengisian Data Stok ')
        print ('2. Penambahan Data Stok ')
        print ('3. Penghapusan Data Stok ')
        print ('0. Kembali ')
        PilihanMenuStok = int(input('Pilihan Anda? '))
    return PilihanMenuStok
#subrutin memasukkan elemen array No, Nama Barang (NB), Banyak Stok (BS)
def IsiDataStok(No, NB, BS):
    i = 0
    print()
    print(f'Data Stok Barang Ke-{i+1}')
    print(f'-------------------------')
    #memasukkan elemen No pertama
    No[i] = str(input('Nomor Stok : ')).upper()
    while (No[i] != 'STOP'):
        #memasukkan nama barang dan banyaknya stok
        NB[i] = str(input('Nama Barang        : ')).upper()
        BS[i]   = int(input('Banyak Stok           : '))
        #memasukkan elemen No berikutnya
        i = i + 1
        print()
        print(f'Data Stok Barang Ke-{i+1}')
        print(f'-------------------------')
        #memasukkan elemen No berikutnya
        No[i] = str(input('Nomor Stok : ')).upper()
    N = i
    return N

#Subrutin Menu Intagiable Assets 
def IntangiableAssetsMenu():
    print("===========================================")
    print("<< ASET TAK BERWUJUD ( INTANGIBLE ASSETS ) >>")
    print("===========================================")
    print("1. Brand & Nama Usaha")
    print("2. Website & Sosial Media")
    print("3. Database Karyawan")
    print("4. Tambah Gaji Karyawan")
    print("0. KELUAR")
    PilihanIntangiable = int(input('Pilihan Anda? '))
    
    # Validasi input
    while (PilihanIntangiable < 0) or (PilihanIntangiable > 4):
        print('Nomor Aset Tak Berwujud tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("===========================================")
        print("<< ASET TAK BERWUJUD ( INTANGIBLE ASSETS ) >>")
        print("===========================================")
        print("1. Brand & Nama Usaha")
        print("2. Website & Sosial Media")
        print("3. Database Karyawan")
        print("4. Tambah Gaji Karyawan")
        print("0. KELUAR")
        PilihanIntangiable = int(input('Pilihan Anda? '))
    
    return PilihanIntangiable

#subrtuin Nama Brand Usaha 
def BrandNamaUsaha():
    print("========================")
    print("<< BRAND & NAMA USAHA >>")
    print("========================")
    NamaBR = str(input("Masukan Nama Brand: "))
    TahunBR = int(input("Masukkan Tahun Brand: "))
    InfoBR = str(input("Masukkan Keterangan Brand: "))
    print(f"Brand '{NamaBR}' ini berdiri pada Tahun '{TahunBR}' dengan keterangan '{InfoBR}' telah disimpan.")
    os.system('pause')

#subrutin Website dan Sosial Media Perusahaan 
def WebsiteSosialMedia():
    print("============================")
    print("<< WEBSITE & SOSIAL MEDIA >>")
    print("============================")
    website = str(input("Masukkan URL Website: "))
    socialMedia = str(input("Masukkan Akun Sosial Media: "))
    print(f"Website '{website}' dan Sosial Media '{socialMedia}' telah disimpan.")
    os.system('pause')

#Subrutin pada database Karyawan
def DatabaseKaryawan():
    print("=======================")
    print("<< DATABASE KARYAWAN >>")
    print("=======================")
    namaKaryawan = str(input("Masukkan Nama Karyawan: "))
    jabatKaryawan = str(input("Masukkan Posisi Karyawan: "))
    nipKaryawan = int(input("Masukkan NIP Karyawan:    "))
    print(f"Karyawan '{namaKaryawan}' dengan posisi '{jabatKaryawan}' telah disimpan.")
    os.system('pause')

#subrutin pada info tambahan gaji karyawan 
def TambahGajiKaryawan():
    print("===========================================")
    print("<< MENAMBAH GAJI KARYAWAN >>")
    print("===========================================")
    nipKaryawan = str(input("Masukkan NIP Karyawan: "))
    jabatKaryawan = str(input("Masukkan Jabatan Karyawan (Manager/Staff/Intern): ")).upper()
    
    # Menentukan gaji berdasarkan jabatan
    if jabatKaryawan == "Manager":
        Gaji = 15000000  # Gaji untuk Manager
    elif jabatKaryawan == "Staff":
        Gaji = 6000000   # Gaji untuk Staff
    elif jabatKaryawan == "Intern":
        Gaji = 2500000   # Gaji untuk Intern
    else:
        print("Jabatan tidak valid. Silakan masukkan jabatan yang benar!")
        os.system('pause')
        return  # Keluar dari fungsi jika jabatan tidak valid
    
    print(f"Gaji untuk Karyawan ID '{nipKaryawan}' dengan jabatan '{jabatKaryawan}' telah diatur menjadi '{salary}'.")
    os.system('pause')

#badan program utama
os.system('cls')
Pilihan = 0
Pilihan = MenuUtama(Pilihan)
while (Pilihan != 0):
    os.system('cls')
    #proses menu
    match (Pilihan):
        case 1 :
            PilihanTangiable = 0
            PilihanTangiable = TangiableAssets(PilihanTangiable)
            while (PilihanTangiable != 0):
                os.system('cls')
                match (PilihanTangiable):
                    case 1:
                        #penciptaan array No, Nama Barang (NB), Banyak Stok (BS)
                        No = ['/'] * MAKSDATA
                        NB = ['/'] * MAKSDATA
                        BS = [0] * MAKSDATA
                        PilihanMenuStok = 0 
                        MenuStokPakaian (PilihanMenuStok)    
                        while (PilihanMenuStok != 0):
                            os.system('cls')
                            match (PilihanMenuStok):
                                case 1:
                                    N = IsiDataStok(No, NB, BS)                   
                                    
        case 2:
            while True:
                os.system('cls')
                PilihanIntangiable = IntangiableAssetsMenu()
                if PilihanIntangiable == 0:
                    break  # Keluar dari loop jika pengguna memilih 0
                match (PilihanIntangiable):
                    case 1:
                        BrandNamaUsaha()
                    case 2:
                        WebsiteSosialMedia()
                    case 3:
                        DatabaseKaryawan()
                    case 4:
                        TambahGajiKaryawan()
                        
    os.system('cls')
    Pilihan = MenuUtama(Pilihan)
    print('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>')
    print('---------------------------------------')
    print('1. Aset Berwujud ( Tangiable Assets )')
    print('2. Aset Tak Berwujud ( Intangiable Asstes )')
    print('0. KELUAR')
    Pilihan = int(input('Pilihan Anda?  '))
    #validasi
    while (Pilihan < 0) or (Pilihan > 2):
        print('Nomor Aset Perusahaan tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>')
        print('---------------------------------------')
        print('1. Aset Berwujud ( Tangiable Assets )')
        print('2. Aset Tak Berwujud ( Intangiable Asstes )')
        print('0. KELUAR')
        Pilihan = int(input('Pilihan Anda?  '))
