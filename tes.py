import os

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

#proses masing masing menu
while (Pilihan != 0):
    os.system('cls')
    match (Pilihan):
        case 1 :
            print("=====================================")
            print("<< ASET BERWUJUD ( TANGIABLE ASSETS )")
            print("=====================================")
            print("1. Barang Dagang ( Stok Pakaian )")
            print("2.Bahan Baku")
            print("3. Vendor Produksi")
            print("4. Vendor Packaging")
            print("5. Toko atau Gudang")
            print("6. Jasa Pengiriman")
            print("0. KELUAR")
            print("---------------------------------")
            Pilihan = int(input('Pilihan Anda?  '))
            while (Pilihan < 0) or (Pilihan > 6):
                print('Nomor Aset Berwujud tidak ada, Ulangi!')
                os.system('pause')
                os.system('cls')
                print("=====================================")
                print("<< ASET BERWUJUD ( TANGIABLE ASSETS )")
                print("=====================================")
                print("1. Barang Dagang ( Stok Pakaian )")
                print("2.Bahan Baku")
                print("3. Vendor Produksi")
                print("4. Vendor Packaging")
                print("5. Toko atau Gudang")
                print("6. Jasa Pengiriman")
                print("0. KELUAR")

        case 2 :
            print("=============================================")
            print('2. ASET TAK BERWUJUD ( INTANGIABLE ASSETS )')
            print("=============================================")
            print("1. Brand & Nama Usaha")
            print("2. Desain & Hak Cipta")
            print("3. Website & Sosial Media Marketing")
            print("0. KELUAR")
            while (Pilihan < 0) or (Pilihan > 3):
                print('Nomor Aset Tak Berwujud tidak ada, Ulangi!')
                os.system('pause')
                os.system('cls')
                print("=============================================")
                print('2. ASET TAK BERWUJUD ( INTANGIABLE ASSETS )')
                print("=============================================")
                print("1. Brand & Nama Usaha")
                print("2. Desain & Hak Cipta")
                print("3. Website & Sosial Media Marketing")
                print("0. KELUAR")
        
            #menampilkan menu
            print('<< ASET PERUSAHAAN CLOTHES SCREAMOUS >>')
            print('---------------------------------------')
            print('1. Aset Berwujud ( Tangiable Assets )')
            print('2. Aset Tak Berwujud ( Not Tangiable Asstes )')
            print('0. KELUAR')
            Pilihan = int(input('Pilihan Anda?  '))