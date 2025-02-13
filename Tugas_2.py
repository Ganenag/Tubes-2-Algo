import os

MAKSDATA = 10

#subrutin menu utama
def MenuUtama(Pilihan):
    print('=======================================')
    print('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>')
    print('=======================================')
    print('1. Aset Berwujud ( Tangible Assets )')
    print('2. Aset Tak Berwujud ( Intangible Asstes )')
    print('0. KELUAR')
    Pilihan = int(input('Pilihan Anda?  '))
    #validasi
    while (Pilihan < 0) or (Pilihan > 2):
        print('Nomor Aset Perusahaan tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print('=======================================')
        print('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>')
        print('=======================================')
        print('1. Aset Berwujud ( Tangible Assets )')
        print('2. Aset Tak Berwujud ( Intangible Asstes )')
        print('0. KELUAR')
        Pilihan = int(input('Pilihan Anda?  '))

    return Pilihan

#subrutin menu Tangible assets
def TangibleAssets(PilihanTangible):
    print("=====================================")
    print("<< ASET BERWUJUD ( TANGIBLE ASSETS ) >>")
    print("=====================================")
    print("1. Gudang Barang Dagangan ( Stok Pakaian )")
    print("2. Bahan Baku")
    print("3. Vendor Produksi")
    print("4. Vendor Packaging")
    print("0. KELUAR")
    print("---------------------------------")
    PilihanTangible = int(input('Pilihan Anda?  '))
    #validasi
    while (PilihanTangible < 0) or (PilihanTangible > 4):
        print('Nomor Aset Berwujud tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("=====================================")
        print("<< ASET BERWUJUD ( TANGIBLE ASSETS ) >>")
        print("=====================================")
        print("1. Gudang Barang Dagangan ( Stok Pakaian )")
        print("2. Bahan Baku")
        print("3. Vendor Produksi")
        print("4. Vendor Packaging")
        print("0. KELUAR")
        print("---------------------------------")
        PilihanTangible = int(input('Pilihan Anda?  '))
        
    return PilihanTangible

#subrutin menu pilihan stok pakaian
def MenuStokPakaian (PilihanMenuStok):
    print ('===========================================')
    print ('<<GUDANG BARANG DAGANGAN ( STOK PAKAIAN )>>')
    print ('===========================================')
    print ('1. Pengisian Data Stok ')
    print ('2. Penampilan Data Stok ')
    print ('3. Penghapusan Data Stok ')
    print ('0. Kembali ')
    PilihanMenuStok = int(input('Pilihan Anda? '))
    #validasi
    while (PilihanMenuStok < 0) or (PilihanMenuStok > 4):
        print('Nomor Pilihan Anda Tidak Valid. Input Ulang!')
        os.system('pause')
        os.system('cls')
        print ('===========================================')
        print ('<<GUDANG BARANG DAGANGAN ( STOK PAKAIAN )>>')
        print ('===========================================')
        print ('1. Pengisian Data Stok ')
        print ('2. Penampilan Data Stok ')
        print ('3. Penghapusan Data Stok ')
        print ('0. Kembali ')
        PilihanMenuStok = int(input('Pilihan Anda? '))
    
    return PilihanMenuStok

#subrutin memasukkan elemen array Nama Barang (NB), Banyak Stok (BS)
def IsiDataStok(NB, BS, BanyakDataStok):
    i = BanyakDataStok
    os.system('cls')
    print()
    print(f'Data Stok Ke-{i+1}')
    print(f'------------------')
    #memasukkan elemen Nama Barang pertama
    NB[i] = str(input('Nama Barang : ')).upper()
    while (NB[i] != 'STOP'):
        #memasukkan banyak siswa
        BS[i] = int(input('Banyak Stok : '))
        #memasukkan elemen Nama Barang berikutnya
        i = i + 1
        print()
        print(f'Data Stok Ke-{i+1}')
        print(f'------------------')
        NB[i] = str(input('Nama Barang : ')).upper()
    
    BanyakDataStok = i
    return BanyakDataStok

#subrutin menghitung total banyak stok
def MenghitungTotalStok (BS, BanyakDataStok):
    TotalStok = 0
    for i in range (BanyakDataStok):
        TotalStok += BS[i] 

    return TotalStok

#subrutin menampilkan data stok barang di gudang
def TampilDataStok (NB, BS, BanyakDataStok):
    os.system('cls')
    print()
    print('  DAFTAR STOK BARANG DI GUDANG')
    print('-------------------------------------')
    print('| No |     Nama Barang     |  Stok  |')
    print('-------------------------------------')
    for i in range(BanyakDataStok):
        print(f'| {i+1:>2} | {NB[i]:19} | {BS[i]:6} |')

    print('-------------------------------------')
    TotalStok = MenghitungTotalStok (BS, BanyakDataStok)
    print(f'Total stok dalam gudang tersedia {TotalStok} barang.')

#subrutin menghapus data stok
def HapusDataStok(NB, BS, BanyakDataStok):
    os.system('cls')
    print('===========================================')
    print('<< PENGHAPUSAN DATA STOK >>')
    print('===========================================')
    if BanyakDataStok == 0:
        print('Tidak ada data stok yang tersedia!')
        os.system('pause')
        return BanyakDataStok
    
    TampilDataStok(NB, BS, BanyakDataStok)
    NamaHapus = input('Masukkan Nama Barang yang akan dihapus: ').upper()
    
    indexHapus = -1
    for i in range(BanyakDataStok):
        if NB[i] == NamaHapus:
            indexHapus = i
    
    if indexHapus == -1:
        print(f'Barang "{NamaHapus}" tidak ditemukan!')
        os.system('pause')
        os.system('cls')
        TampilDataStok(NB, BS, BanyakDataStok)
        NamaHapus = input('Masukkan Nama Barang yang akan dihapus: ').upper()
    else:
        for i in range(indexHapus, BanyakDataStok - 1):
            NB[i] = NB[i + 1]
            BS[i] = BS[i + 1]
        NB[BanyakDataStok - 1] = '/'
        BS[BanyakDataStok - 1] = 0
        BanyakDataStok -= 1
        print(f'Barang "{NamaHapus}" berhasil dihapus!')
    
    return BanyakDataStok



#subrutin menu Intangible assets
def IntangibleAssets(PilihanIntangible):
    print("===========================================")
    print('<< ASET TAK BERWUJUD ( INTANGIBLE ASSETS ) >>')
    print("===========================================")
    print("1. Brand & Nama Usaha")
    print("2. Website & Sosial Media (Marketing)")
    print("3. Database Karyawan")
    print("0. KELUAR")
    PilihanIntangible = int(input('Pilihan Anda? '))
    while (PilihanIntangible < 0) or (PilihanIntangible > 3):
        print('Nomor Aset Tak Berwujud tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("===========================================")
        print('<< ASET TAK BERWUJUD ( INTANGIBLE ASSETS ) >>')
        print("===========================================")
        print("1. Brand & Nama Usaha")
        print("2. Website & Sosial Media (Marketing)")
        print("3. Database Karyawan")
        print("0. KELUAR")
        PilihanIntangible = int(input('Pilihan Anda? '))

    return PilihanIntangible


#badan program utama
os.system('cls')
BanyakDataStok = 0
Pilihan = 0
Pilihan = MenuUtama(Pilihan)
while (Pilihan != 0):
    os.system('cls')
    #proses menu
    match (Pilihan):
        case 1 :
            PilihanTangible = 0
            PilihanTangible = TangibleAssets(PilihanTangible)
            while (PilihanTangible != 0):
                os.system('cls')
                match (PilihanTangible):
                    case 1:
                        #penciptaan array Nama Barang (NB), Banyak Stok (BS)                        
                        NB = ['/'] * MAKSDATA
                        BS = [0] * MAKSDATA
                        PilihanMenuStok = 0 
                        PilihanMenuStok = MenuStokPakaian (PilihanMenuStok)  
                        while (PilihanMenuStok != 0):                                                      
                            match(PilihanMenuStok):    
                                case 1:
                                    #pengisian data stok
                                    BanyakDataStok = IsiDataStok(NB, BS, BanyakDataStok)
                                    os.system('cls')
                                case 2:
                                    TampilDataStok (NB, BS, BanyakDataStok)
                                    os.system('pause')
                                    os.system('cls')
                                case 3:
                                    HapusDataStok(NB, BS, BanyakDataStok)
                                    os.system('pause')
                                    os.system('cls')
                                
                                    
                                
                            os.system('cls')
                            PilihanMenuStok = MenuStokPakaian (PilihanMenuStok)  

                os.system('cls')
                PilihanTangible = TangibleAssets(PilihanTangible)

        


        case 2 :
            PilihanIntangible = 0
            PilihanIntangible = IntangibleAssets(PilihanIntangible)
            
    os.system('cls')
    Pilihan = MenuUtama(Pilihan)
