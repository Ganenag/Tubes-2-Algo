import os

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
        print('<< ASET PERUSAHAAN CLOTHES SCREAMOUS >>')
        print('---------------------------------------')
        print('1. Aset Berwujud ( Tangiable Assets )')
        print('2. Aset Tak Berwujud ( Not Tangiable Asstes )')
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
        
    return PilihanTangiable

#subrutin menu intangiable assets
def IntangiableAssets(PilihanIntangiable):
    print("===========================================")
    print('<< ASET TAK BERWUJUD ( INTANGIABLE ASSETS ) >>')
    print("===========================================")
    print("1. Brand & Nama Usaha")
    print("2. Website & Sosial Media (Marketing)")
    print("3. Database Karyawan")
    print("0. KELUAR")
    PilihanIntangiable = int(input('Pilihan Anda? '))
    while (PilihanIntangiable < 0) or (PilihanIntangiable > 3):
        print('Nomor Aset Tak Berwujud tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("===========================================")
        print('<< ASET TAK BERWUJUD ( INTANGIABLE ASSETS ) >>')
        print("===========================================")
        print("1. Brand & Nama Usaha")
        print("2. Website & Sosial Media (Marketing)")
        print("3. Database Karyawan")
        print("0. KELUAR")

    return PilihanIntangiable


#badan program utama
os.system('cls')
Pilihan = 0
Pilihan = MenuUtama(Pilihan)
while (Pilihan != 0):
    os.system('cls')
    match (Pilihan):
        case 1 :
            PilihanTangiable = 0
            PilihanTangiable = TangiableAssets(PilihanTangiable)
        case 2 :
            PilihanIntangiable = 0
            PilihanIntangiable = IntangiableAssets(PilihanIntangiable)
            
    os.system('cls')
    print('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>')
    print('---------------------------------------')
    print('1. Aset Berwujud ( Tangiable Assets )')
    print('2. Aset Tak Berwujud ( Intangiable Asstes )')
    print('0. KELUAR')
    Pilihan = int(input('Pilihan Anda?  '))
