#I.S.: Membuat menu utama untuk Aset Perusahaan Clothes 
#F.S.: Menampilkan hasil menu dari Aset Berwujud & Tak Berwujud
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
    print("===========================================")
    print("  << ASET BERWUJUD ( TANGIBLE ASSETS ) >>")
    print("===========================================")
    print("1. Gudang Barang Dagangan ( Stok Pakaian )")
    print("2. Bahan Baku")
    print("3. Vendor Produksi")
    print("4. Vendor Packaging")
    print("0. KELUAR")
    print("===========================================")
    PilihanTangible = int(input('Pilihan Anda?  '))
    #validasi
    while (PilihanTangible < 0) or (PilihanTangible > 4):
        print('Nomor Aset Berwujud tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("===========================================")
        print("  << ASET BERWUJUD ( TANGIBLE ASSETS ) >>")
        print("===========================================")
        print("1. Gudang Barang Dagangan ( Stok Pakaian )")
        print("2. Bahan Baku")
        print("3. Vendor Produksi")
        print("4. Vendor Packaging")
        print("0. KELUAR")
        print("===========================================")
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
    while (PilihanMenuStok < 0) or (PilihanMenuStok > 3):
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

#subrutin memasukkan elemen array Nama Barang (NB), Banyak Stok (BS) sekaligus penambahan
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
    print('       << PENGHAPUSAN DATA STOK >>')
    print('===========================================')
    if BanyakDataStok == 0:
        print('Tidak ada data stok yang tersedia!')
        os.system('pause')
        return BanyakDataStok
    
    while True: 
        TampilDataStok(NB, BS, BanyakDataStok)
        NamaHapus = input('Masukkan Nama Barang yang akan dihapus (atau ketik "BATAL" untuk kembali): ').upper()
        
        if NamaHapus == "BATAL":
            return BanyakDataStok  
        
        indexHapus = -1  
        i = 0
        
        while i < BanyakDataStok:  
            if NB[i] == NamaHapus:
                indexHapus = i  
            i += 1  
        
        if indexHapus == -1:
            print(f'Barang "{NamaHapus}" tidak ditemukan! Coba lagi.')
            os.system('pause')
            os.system('cls')
        else:
            i = indexHapus
            while i < BanyakDataStok - 1:
                NB[i] = NB[i + 1]  
                BS[i] = BS[i + 1]
                i += 1
            
            NB[BanyakDataStok - 1] = ""  
            BS[BanyakDataStok - 1] = 0
            
            BanyakDataStok -= 1
            print(f'Barang "{NamaHapus}" berhasil dihapus!')
            os.system('pause')
            os.system('cls')
            return BanyakDataStok  

#subrutin menu pilihan bahan baku
def MenuBahanBaku (PilihanMenuBahan):
    print ('===========================================')
    print ('             << BAHAN BAKU >>')
    print ('===========================================')
    print ('1. Pengisian Data Bahan Baku ')
    print ('2. Penampilan Data Bahan Baku ')
    print ('3. Penghapusan Data Bahan Baku ')
    print ('0. Kembali ')
    PilihanMenuBahan = int(input('Pilihan Anda? '))
    #validasi
    while (PilihanMenuBahan < 0) or (PilihanMenuBahan > 3):
        print('Nomor Pilihan Anda Tidak Valid. Input Ulang!')
        os.system('pause')
        os.system('cls')
        print ('===========================================')
        print ('            << BAHAN BAKU >>')
        print ('===========================================')
        print ('1. Pengisian Data Bahan Baku ')
        print ('2. Penampilan Data Bahan Baku ')
        print ('3. Penghapusan Data Bahan Baku ')
        print ('0. Kembali ')
        PilihanMenuBahan = int(input('Pilihan Anda? '))
    
    return PilihanMenuBahan

#subrutin isi data bahan baku sekaligus penambahan
def IsiDataBahan(Bahan, HB, BanyakBeli, BanyakDataBahan):
    i = BanyakDataBahan
    os.system('cls')
    print()
    print(f'Data Bahan Baku Ke-{i+1}')
    print('-------------------------')
    
    Bahan[i] = str(input('Nama Bahan Baku        : ')).upper()
    
    while (Bahan[i] != 'STOP'):
        HB[i] = int(input('Harga per-Meter (Rp)   : '))
        BanyakBeli[i] = int(input('Jumlah Dibeli (Meter)  : '))
        
        i += 1
        print()
        print(f'Data Bahan Baku Ke-{i+1}')
        print('-------------------------')
        Bahan[i] = str(input('Nama Bahan Baku        : ')).upper()
    
    BanyakDataBahan = i
    return BanyakDataBahan


#subrutin menghitung total biaya untuk bahan baku
def MenghitungTotalBiayaBahan(HB, BanyakBeli, BanyakDataBahan):
    TotalHargaSeluruhBahan = 0
    for i in range(BanyakDataBahan):
        TotalHargaSeluruhBahan += HB[i] * BanyakBeli[i]
    return TotalHargaSeluruhBahan

# Subrutin menampilkan data bahan baku
def TampilDataBahan(Bahan, HB, BanyakBeli, BanyakDataBahan):
    os.system('cls')  
    print()
    print('                        DAFTAR TOTAL BIAYA UNTUK BAHAN BAKU')
    print('----------------------------------------------------------------------------------------------')
    print('| No |     Bahan Baku      | Harga per-Meter (Rp) | Banyak Dibeli (Meter) |    Total (Rp)    |')
    print('----------------------------------------------------------------------------------------------')

    for i in range(BanyakDataBahan):
        TotalHargaPerBahan = HB[i] * BanyakBeli[i]
        print("| {:<2} | {:<19} | Rp. {:>16,.2f} | {:>21} | Rp. {:>12,.2f} |".format(
            i + 1, Bahan[i], HB[i], BanyakBeli[i], TotalHargaPerBahan))

    print('----------------------------------------------------------------------------------------------')
    TotalHargaSeluruhBahan = MenghitungTotalBiayaBahan(HB, BanyakBeli, BanyakDataBahan)
    print(f"Total biaya dikeluarkan untuk bahan baku: Rp. {TotalHargaSeluruhBahan:,.2f}.")

#subrutin menghapus data bahan baku
def HapusDataBahan(Bahan, HB, BanyakDataBahan):
    os.system('cls')
    print('===========================================')
    print('    << PENGHAPUSAN DATA BAHAN BAKU >>')
    print('===========================================')
    if BanyakDataBahan == 0:
        print('Tidak ada data bahan baku yang tersedia!')
        os.system('pause')
        return BanyakDataBahan
    
    while True: 
        TampilDataBahan(Bahan, HB, BanyakBeli, BanyakDataBahan)
        BahanHapus = input('Masukkan Nama Bahan yang akan dihapus (atau ketik "BATAL" untuk kembali): ').upper()
        
        if BahanHapus == "BATAL":
            return BanyakDataBahan  
        
        indexHapus = -1  
        i = 0
        
        while i < BanyakDataBahan:  
            if Bahan[i] == BahanHapus:
                indexHapus = i  
            i += 1  
        
        if indexHapus == -1:
            print(f'Bahan "{BahanHapus}" tidak ditemukan! Coba lagi.')
            os.system('pause')
            os.system('cls')
        else:
            i = indexHapus
            while i < BanyakDataBahan - 1:
                Bahan[i] = Bahan[i + 1]  
                HB[i] = HB[i + 1]
                i += 1
            
            Bahan[BanyakDataBahan - 1] = ""  
            HB[BanyakDataBahan - 1] = 0
            
            BanyakDataBahan -= 1
            print(f'Bahan "{BahanHapus}" berhasil dihapus!')
            os.system('pause')
            os.system('cls')
            return BanyakDataBahan 

#subrutin menu pilihan produksi
def MenuVendorProduksi (PilihanMenuProduksi):
    print ('===========================================')
    print ('           << VENDOR PRODUKSI >>')
    print ('===========================================')
    print ('1. Pengisian Data Vendor Produksi ')
    print ('2. Penampilan Data Vendor Produksi ')
    print ('3. Penghapusan Data Vendor Produksi ')
    print ('4. Cari Data Vendor Produksi ')
    print ('0. Kembali ')
    PilihanMenuProduksi = int(input('Pilihan Anda? '))
    #validasi
    while (PilihanMenuProduksi < 0) or (PilihanMenuProduksi > 4):
        print('Nomor Pilihan Anda Tidak Valid. Input Ulang!')
        os.system('pause')
        os.system('cls')
        print ('===========================================')
        print ('            << VENDOR PRODUKSI >>')
        print ('===========================================')
        print ('1. Pengisian Data Vendor Produksi ')
        print ('2. Penampilan Data Vendor Produksi ')
        print ('3. Penghapusan Data Vendor Produksi ')
        print ('4. Cari Data Vendor Produksi ')
        print ('0. Kembali ')
        PilihanMenuProduksi = int(input('Pilihan Anda? '))
    
    return PilihanMenuProduksi

#subrutin mengisi data produksi sekaligus penambahan
def IsiDataProduksi(BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi):
    i = BanyakDataProduksi
    os.system('cls')
    print()
    print(f'Data Barang Produksi ke-{i+1}')
    print('------------------------------')
    
    BarangProduksi[i] = str(input('Nama Barang Produksi : ')).upper()
    
    while (BarangProduksi[i] != 'STOP'):
        HargaProduksi[i] = int(input('Harga Satuan (Rp)    : '))
        BanyakProduksi[i] = int(input('Total Produksi       : '))
        
        i += 1
        print()
        print(f'Data Barang Produksi ke-{i+1}')
        print('------------------------------')
        BarangProduksi[i] = str(input('Nama Barang Produksi : ')).upper()
    
    BanyakDataProduksi = i
    return BanyakDataProduksi   

#subrutin menghitung total harga produksi
def MenghitungTotalHargaProduksi(HargaProduksi, BanyakProduksi, BanyakDataProduksi):
    TotalHargaSeluruhProduksi = 0
    for i in range(BanyakDataProduksi):
        TotalHargaSeluruhProduksi += HargaProduksi[i] * BanyakProduksi[i]
    return TotalHargaSeluruhProduksi

#subrutin Bubble Sort untuk mengurutkan data produksi berdasarkan total harga secara descending
def BubbleSortProduksiDescending(BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi):
    for i in range(BanyakDataProduksi - 1):
        for j in range(BanyakDataProduksi - 1 - i):
            # Menghitung total harga produksi untuk perbandingan
            total_j = HargaProduksi[j] * BanyakProduksi[j]
            total_j1 = HargaProduksi[j + 1] * BanyakProduksi[j + 1]

            if total_j < total_j1:  # Tukar jika total harga lebih kecil
                # Tukar total harga
                BarangProduksi[j], BarangProduksi[j + 1] = BarangProduksi[j + 1], BarangProduksi[j]
                HargaProduksi[j], HargaProduksi[j + 1] = HargaProduksi[j + 1], HargaProduksi[j]
                BanyakProduksi[j], BanyakProduksi[j + 1] = BanyakProduksi[j + 1], BanyakProduksi[j]

#subrutin tampil data produksi
def TampilDataProduksi (BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi):
    os.system('cls')  
    BubbleSortProduksiDescending(BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi)
    print()
    print('                               DAFTAR TOTAL BIAYA PRODUKSI')
    print('-----------------------------------------------------------------------------------------------')
    print('| No |  Barang Produksi  | Harga per-Produksi (Rp) | Banyak Produksi |       Total (Rp)       |')
    print('-----------------------------------------------------------------------------------------------')
    for i in range(BanyakDataProduksi):
        TotalHargaPerProduk = HargaProduksi[i] * BanyakProduksi[i]
        print("| {:<2} | {:<17} | Rp. {:>19,.2f} | {:>15} | Rp. {:>18,.2f} |".format(
            i + 1, BarangProduksi[i], HargaProduksi[i], BanyakProduksi[i], TotalHargaPerProduk))

    print('-----------------------------------------------------------------------------------------------')
    TotalHargaSeluruhProduksi = MenghitungTotalHargaProduksi(HargaProduksi, BanyakProduksi, BanyakDataProduksi)
    print(f"Total biaya dikeluarkan untuk produksi: Rp. {TotalHargaSeluruhProduksi:,.2f}.")

#subrutin menghapus data produksi
def HapusDataProduksi(BarangProduksi, HargaProduksi, BanyakDataProduksi):
    os.system('cls')
    print('===========================================')
    print('  << PENGHAPUSAN DATA VENDOR PRODUKSI >>')
    print('===========================================')
    if BanyakDataProduksi == 0:
        print('Tidak ada data vendor produksi yang tersedia!')
        os.system('pause')
        return BanyakDataProduksi
    
    while True: 
        TampilDataProduksi (BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi)
        ProduksiHapus = input('Masukkan Nama Produk yang akan dihapus (atau ketik "BATAL" untuk kembali): ').upper()
        
        if ProduksiHapus == "BATAL":
            return BanyakDataProduksi  
        
        indexHapus = -1  
        i = 0
        
        while i < BanyakDataProduksi:  
            if BarangProduksi[i] == ProduksiHapus:
                indexHapus = i  
            i += 1  
        
        if indexHapus == -1:
            print(f'Produk "{ProduksiHapus}" tidak ditemukan! Coba lagi.')
            os.system('pause')
            os.system('cls')
        else:
            i = indexHapus
            while i < BanyakDataProduksi - 1:
                BarangProduksi[i] = BarangProduksi[i + 1]  
                HargaProduksi[i] = HargaProduksi[i + 1]
                i += 1
            
            BarangProduksi[BanyakDataProduksi - 1] = ""  
            HargaProduksi[BanyakDataProduksi - 1] = 0
            
            BanyakDataProduksi -= 1
            print(f'Produk "{ProduksiHapus}" berhasil dihapus!')
            os.system('pause')
            os.system('cls')
            return BanyakDataProduksi  

#subrutin mencari Nama Produk dengan Binary Search pada data yang terurut DESCENDING
def CariProdukDesc(BarangProduksi, HargaProduksi,BanyakProduksi, BanyakDataProduksi):
    # Memasukkan Produk yang dicari
    os.system('cls')
    print('===========================')
    print('<< PENCARIAN NAMA PRODUK >>')
    print('===========================')
    ProdukCari = str(input("Produk yang dicari: ")).upper()
    # Proses pencarian
    Ia = 0
    Ib = BanyakDataProduksi - 1
    Ketemu = False
    while (not Ketemu) and (Ia <= Ib):
        # Menghitung posisi tengah (K)
        k = (Ia + Ib) // 2
        if (BarangProduksi[k] == ProdukCari):
            Ketemu = True
        else:
            if (BarangProduksi[k] > ProdukCari): 
                # Pencarian dilanjutkan ke kanan
                Ia = k + 1
            else:
                # Pencarian dilanjutkan ke kiri
                Ib = k - 1

    os.system('cls')
    print('<<HASIL PENCARIAN>>')
    print('-------------------')
    if(Ketemu):
        print(f'Produk yang dicari: {ProdukCari}')
        print(f'Harga Produksi    : {HargaProduksi[k]}')
        print(f'Banyak Produksi   : {BanyakProduksi[k]}')
        os.system('pause')
        os.system('cls')
    else:
        print(f'Produk {ProdukCari} tidak ditemukan!')    
        os.system('pause')
        os.system('cls') 

#subrutin menu pilihan packaging
def MenuVendorPackaging (PilihanMenuPackaging):
    print ('===========================================')
    print ('           << VENDOR PACKAGING >>')
    print ('===========================================')
    print ('1. Pengisian Data Vendor Packaging ')
    print ('2. Penampilan Data Vendor Packaging ')
    print ('3. Penghapusan Data Vendor Packaging ')
    print ('4. Cari Data Vendor Packaging ')
    print ('0. Kembali ')
    PilihanMenuPackaging = int(input('Pilihan Anda? '))
    #validasi
    while (PilihanMenuPackaging < 0) or (PilihanMenuPackaging > 4):
        print('Nomor Pilihan Anda Tidak Valid. Input Ulang!')
        os.system('pause')
        os.system('cls')
        print ('===========================================')
        print ('            << VENDOR PACKAGING >>')
        print ('===========================================')
        print ('1. Pengisian Data Vendor Packaging ')
        print ('2. Penampilan Data Vendor Packaging ')
        print ('3. Penghapusan Data Vendor Packaging ')
        print ('4. Cari Data Vendor Packaging ')
        print ('0. Kembali ')
        PilihanMenuPackaging = int(input('Pilihan Anda? '))
    
    return PilihanMenuPackaging

#subrutin mengisi data produksi sekaligus penambahan
def IsiDataPackaging(JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging):
    i = BanyakDataPackaging
    os.system('cls')
    print()
    print(f'Data Jenis Packaging ke-{i+1}')
    print('------------------------------')
    
    JenisPackaging[i] = str(input('Jenis Packaging   : ')).upper()
    
    while (JenisPackaging[i] != 'STOP'):
        HargaSatuan[i] = int(input('Harga Satuan (Rp) : '))
        BBP[i] = int(input('Banyak Pembelian  : '))
        
        i += 1
        print()
        print(f'Data Jenis Packaging ke-{i+1}')
        print('------------------------------')
        JenisPackaging[i] = str(input('Jenis Packaging   : ')).upper()
    
    BanyakDataPackaging = i
    return BanyakDataPackaging   

#subrutin menghitung total harga Packaging
def MenghitungTotalHargaPackaging(HargaSatuan, BPP, BanyakDataPackaging):
    TotalHargaSeluruhPackaging = 0
    for i in range(BanyakDataPackaging):
        TotalHargaSeluruhPackaging += HargaSatuan[i] * BPP[i]
    return TotalHargaSeluruhPackaging

# Subrutin Bubble Sort untuk mengurutkan data packaging berdasarkan total harga secara ascending
def BubbleSortPackagingAscending(JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging):
    for i in range(BanyakDataPackaging - 1):
        for j in range(BanyakDataPackaging - 1 - i):
            # Menghitung total harga packaging untuk perbandingan
            total_j = HargaSatuan[j] * BBP[j]
            total_j1 = HargaSatuan[j + 1] * BBP[j + 1]

            if total_j > total_j1:  # Tukar jika total harga lebih besar (ascending)
                # Tukar total harga
                JenisPackaging[j], JenisPackaging[j + 1] = JenisPackaging[j + 1], JenisPackaging[j]
                HargaSatuan[j], HargaSatuan[j + 1] = HargaSatuan[j + 1], HargaSatuan[j]
                BBP[j], BBP[j + 1] = BBP[j + 1], BBP[j]


#subrutin tampil data Packaging
def TampilDataPackaging (JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging):
    os.system('cls')  
    BubbleSortPackagingAscending(JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging)
    print()
    print('                               DAFTAR TOTAL BIAYA PACKAGING')
    print('-------------------------------------------------------------------------------------------------')
    print('| No |  Jenis Packaging  | Harga per-Packaging (Rp) | Banyak Packaging |       Total (Rp)       |')
    print('-------------------------------------------------------------------------------------------------')
    for i in range(BanyakDataPackaging):
        TotalHargaPerPackaging = HargaSatuan[i] * BBP[i]
        print("| {:<2} | {:<17} | Rp. {:>19,.2f}  | {:>16} | Rp. {:>18,.2f} |".format(
            i + 1, JenisPackaging[i], HargaSatuan[i], BBP[i], TotalHargaPerPackaging))

    print('-------------------------------------------------------------------------------------------------')
    TotalHargaSeluruhPackaging = MenghitungTotalHargaPackaging(HargaSatuan, BBP, BanyakDataPackaging)
    print(f"Total biaya dikeluarkan untuk Packaging: Rp. {TotalHargaSeluruhPackaging:,.2f}.")

#subrutin menghapus data packaging
def HapusDataPackaging(JenisPackaging, HargaSatuan, BanyakDataPackaging):
    os.system('cls')
    print('===========================================')
    print('  << PENGHAPUSAN DATA VENDOR PACKAGING >>')
    print('===========================================')
    if BanyakDataPackaging == 0:
        print('Tidak ada data vendor packaging yang tersedia!')
        os.system('pause')
        return BanyakDataPackaging
    
    while True: 
        TampilDataPackaging (JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging)
        PackagingHapus = input('Masukkan jenis packaging yang akan dihapus (atau ketik "BATAL" untuk kembali): ').upper()
        
        if PackagingHapus == "BATAL":
            return BanyakDataPackaging  
        
        indexHapus = -1  
        i = 0
        
        while i < BanyakDataPackaging:  
            if JenisPackaging[i] == PackagingHapus:
                indexHapus = i  
            i += 1  
        
        if indexHapus == -1:
            print(f'Packaging "{PackagingHapus}" tidak ditemukan! Coba lagi.')
            os.system('pause')
            os.system('cls')
        else:
            i = indexHapus
            while i < BanyakDataPackaging - 1:
                JenisPackaging[i] = JenisPackaging[i + 1]  
                HargaSatuan[i] = HargaSatuan[i + 1]
                i += 1
            
            JenisPackaging[BanyakDataPackaging - 1] = ""  
            HargaSatuan[BanyakDataPackaging - 1] = 0
            
            BanyakDataPackaging -= 1
            print(f'Packaging "{PackagingHapus}" berhasil dihapus!')
            os.system('pause')
            os.system('cls')
            return BanyakDataPackaging  

#subrutin mencari Jenis Packaging dengan Binary Search pada data yang terurut ASCENDING
def CariPackAsc(JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging):
    # Memasukkan jenus packaging yang dicari
    os.system('cls')
    print('===============================')
    print('<< PENCARIAN JENIS PACKAGING >>')
    print('===============================')
    PackagingCari = str(input("Packaging yang dicari: ")).upper()
    # Proses pencarian
    Ia = 0
    Ib = BanyakDataPackaging - 1
    Ketemu = False
    while (not Ketemu) and (Ia <= Ib):
        # Menghitung posisi tengah (K)
        k = (Ia + Ib) // 2
        if (JenisPackaging[k] == PackagingCari):
            Ketemu = True
        else:
            if (JenisPackaging[k] > PackagingCari): 
                # Pencarian dilanjutkan ke kanan
                Ia = k + 1
            else:
                # Pencarian dilanjutkan ke kiri
                Ib = k - 1

    os.system('cls')
    print('<<HASIL PENCARIAN>>')
    print('-------------------')
    if(Ketemu):
        print(f'Packaging yang dicari: {PackagingCari}')
        print(f'Harga Satuan         : {HargaSatuan[k]}')
        print(f'Banyak Pack Dibeli   : { BBP[k]}')
        os.system('pause')
        os.system('cls')
    else:
        print(f'Packaging {PackagingCari} tidak ditemukan!')    
        os.system('pause')
        os.system('cls')    

#subrutin menu Intangible assets
def IntangibleAssets(PilihanIntangible):
    print("===========================================")
    print('<< ASET TAK BERWUJUD ( INTANGIBLE ASSETS ) >>')
    print("===========================================")
    print("1. Brand & Nama Usaha")
    print("2. Website & Sosial Media (Marketing)")
    print("3. Database Karyawan")
    print("4. Kelola Aset Tak Berwujud")
    print("0. KELUAR")
    PilihanIntangible = int(input('Pilihan Anda? '))
    while (PilihanIntangible < 0) or (PilihanIntangible > 4):
        print('Nomor Aset Tak Berwujud tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("===========================================")
        print('<< ASET TAK BERWUJUD ( INTANGIBLE ASSETS ) >>')
        print("===========================================")
        print("1. Brand & Nama Usaha")
        print("2. Website & Sosial Media (Marketing)")
        print("3. Database Karyawan")
        print("4. Kelola Aset Tak Berwujud")
        print("0. KELUAR")
        PilihanIntangible = int(input('Pilihan Anda? '))

    return PilihanIntangible

#subrutin submenu untuk mengelola aset tak berwujud
def SubmenuIntangibleAssets():
    print("===========================================")
    print('<< KELOLA ASET TAK BERWUJUD >>')
    print("===========================================")
    print("1. Penciptaan dan Penambahan Aset Tak Berwujud")
    print("2. Penghapusan Aset Tak Berwujud")
    print("3. Urutkan dan Cari Aset Tak Berwujud")
    print("4. Hancurkan Semua Aset Tak Berwujud")
    print("0. KEMBALI")
    PilihanSubIntangible = int(input('Pilihan Anda? '))
    while (PilihanSubIntangible < 0) or (PilihanSubIntangible > 4):
        print('Nomor pilihan tidak ada, Ulangi!')
        os.system('pause')
        os.system('cls')
        print("===========================================")
        print('<< KELOLA ASET TAK BERWUJUD >>')
        print("===========================================")
        print("1. Penciptaan dan Penambahan Aset Tak Berwujud")
        print("2. Penghapusan Aset Tak Berwujud")
        print("3. Urutkan dan Cari Aset Tak Berwujud")
        print("4. Hancurkan Semua Aset Tak Berwujud")
        print("0. KEMBALI")
        PilihanSubIntangible = int(input('Pilihan Anda? '))

    return PilihanSubIntangible

# Subrutin menu
def MenuBrand(intangible_assets):
    while True:
        os.system('cls')
        print("===========================================")
        print("<< BRAND & NAMA USAHA >>")
        print("===========================================")
        print("1. Tambah Brand/Nama Usaha")
        print("2. Lihat Semua Brand/Nama Usaha")
        print("3. Hapus Brand/Nama Usaha")
        print("4. Urutkan Brand/Nama Usaha (Ascending)")
        print("5. Cari Brand/Nama Usaha")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilihan Anda? ").strip()
        
        if pilihan == "0":
            break
        elif pilihan == "1":
            TambahIntangibleAsset(intangible_assets)
        elif pilihan == "2":
            TraversalIntangibleAssets(intangible_assets)
        elif pilihan == "3":
            HapusIntangibleAsset(intangible_assets)
        elif pilihan == "4":
            UrutkanIntangibleAssets(intangible_assets)
        elif pilihan == "5":
            CariIntangibleAsset(intangible_assets)
        else:
            print("Pilihan tidak valid, coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

#subrutin traversal aset tak berwujud
def TraversalIntangibleAssets(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< DAFTAR ASET TAK BERWUJUD >>')
    print("===========================================")
    for i, asset in enumerate(IntangibleAssetsList):
        print(f"{i+1}. {asset}")
    os.system('pause')

# Subrutin untuk menambahkan brand
def TambahBrand(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< TAMBAH BRAND >>')
    print("===========================================")
    brand_name = input("Masukkan nama brand: ").strip()
    year_established = input("Masukkan tahun didirikan: ").strip()
    description = input("Masukkan deskripsi brand: ").strip()
    IntangibleAssetsList.append(f"Brand: {brand_name}, Tahun Didirikan: {year_established}, Deskripsi: {description}")
    print(f'Brand "{brand_name}" berhasil ditambahkan!')
    os.system('pause')

# Subrutin untuk menambahkan website
def TambahWebsite(MarketingAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< TAMBAH WEBSITE >>')
    print("===========================================")
    website_name = input("Masukkan nama website: ").strip()
    url = input("Masukkan URL website: ").strip()
    description = input("Masukkan deskripsi website: ").strip()
    MarketingAssetsList.append(f"Website: {website_name}, URL: {url}, Deskripsi: {description}")
    print(f'Website "{website_name}" berhasil ditambahkan!')
    os.system('pause')

# Subrutin untuk menambahkan social media
def TambahSocialMedia(MarketingAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< TAMBAH SOCIAL MEDIA >>')
    print("===========================================")
    platform_name = input("Masukkan nama platform social media: ").strip()
    account_name = input("Masukkan nama akun: ").strip()
    followers = input("Masukkan jumlah pengikut: ").strip()
    description = input("Masukkan deskripsi akun: ").strip()
    MarketingAssetsList.append(f"Social Media: {platform_name}, Akun: {account_name}, Pengikut: {followers}, Deskripsi: {description}")
    print(f'Akun social media "{account_name}" berhasil ditambahkan!')
    os.system('pause')

# Subrutin utama untuk menambahkan aset pemasaran
def TambahMarketingAsset(MarketingAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< TAMBAH ASET PEMASARAN >>')
    print("===========================================")
    asset_type = int(input("Pilih jenis aset (1: Website, 2: Social Media): "))
    if asset_type == 1:
        TambahWebsite(MarketingAssetsList)
    elif asset_type == 2:
        TambahSocialMedia(MarketingAssetsList)
    else:
        print("Jenis aset tidak valid!")
        os.system('pause')    

# Subrutin untuk menambahkan karyawan
def TambahKaryawan(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< TAMBAH KARYAWAN >>')
    print("===========================================")
    employee_name = input("Masukkan nama karyawan: ").strip()
    employee_id = input("Masukkan NIP karyawan: ").strip()
    position = input("Masukkan jabatan karyawan: ").strip()
    salary = 0
    if position.lower() == "intern":
        salary = 3500000
    elif position.lower() == "staff":
        salary = 7000000
    elif position.lower() == "manager":
        salary = 15000000
    else:
        print("Jabatan tidak valid! Gaji akan diatur ke 0.")
    
    IntangibleAssetsList.append(f"Karyawan: {employee_name}, NIP: {employee_id}, Jabatan: {position}, Gaji: {salary}")
    print(f'Karyawan "{employee_name}" berhasil ditambahkan!')
    os.system('pause')    

#subrutin penghapusan aset tak berwujud
def HapusIntangibleAsset(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< HAPUS ASET TAK BERWUJUD >>')
    print("===========================================")
    TraversalIntangibleAssets(IntangibleAssetsList)
    index = int(input("Masukkan nomor aset yang akan dihapus: ")) - 1
    if 0 <= index < len(IntangibleAssetsList):
        asset = IntangibleAssetsList.pop(index)
        print(f'Aset "{asset}" berhasil dihapus!')
    else:
        print("Nomor aset tidak valid!")
    os.system('pause')

#subrutin pengurutan aset tak berwujud (ascending) menggunakan max-min sort
def UrutkanIntangibleAssets(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< URUTKAN ASET TAK BERWUJUD (ASCENDING) >>')
    print("===========================================")
    for i in range(len(IntangibleAssetsList) - 1):
        min_index = i
        for j in range(i + 1, len(IntangibleAssetsList)):
            if IntangibleAssetsList[j] < IntangibleAssetsList[min_index]:
                min_index = j
        IntangibleAssetsList[i], IntangibleAssetsList[min_index] = IntangibleAssetsList[min_index], IntangibleAssetsList[i]
    print("Aset tak berwujud berhasil diurutkan!")
    os.system('pause')

# Subrutin utama untuk menambahkan aset tak berwujud
def TambahIntangibleAsset(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< TAMBAH ASET TAK BERWUJUD >>')
    print("===========================================")
    asset_type = int(input("Pilih jenis aset (1: Brand, 2: Karyawan): "))
    if asset_type == 1:
        TambahBrand(IntangibleAssetsList)
    elif asset_type == 2:
        TambahKaryawan(IntangibleAssetsList)
    else:
        print("Jenis aset tidak valid!")
        os.system('pause')

#subrutin pencarian aset tak berwujud menggunakan sequential search
def CariIntangibleAsset(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< CARI ASET TAK BERWUJUD >>')
    print("===========================================")
    asset_cari = input("Masukkan nama aset yang dicari: ").strip()
    found = False
    for i, asset in enumerate(IntangibleAssetsList):
        if asset_cari.lower() in asset.lower():
            print(f'Aset "{asset_cari}" ditemukan pada posisi {i+1}: {asset}')
            found = True
            break
    if not found:
        print(f'Aset "{asset_cari}" tidak ditemukan.')
    os.system('pause')

#subrutin penghancuran semua aset tak berwujud
def HancurkanIntangibleAssets(IntangibleAssetsList):
    os.system('cls')
    print("===========================================")
    print('<< HANCURKAN SEMUA ASET TAK BERWUJUD >>')
    print("===========================================")
    IntangibleAssetsList.clear()
    print("Semua aset tak berwujud berhasil dihancurkan!")
    os.system('pause')

#badan program utama
os.system('cls')                   
#penciptaan array Nama Barang (NB) dan BanyakStok (BS)
NB = ['/'] * MAKSDATA
BS = [0] * MAKSDATA
#penciptaan array Bahan, Harga Bahan (HB), Banyak Beli
Bahan = ['/'] * MAKSDATA
HB = [0] * MAKSDATA
BanyakBeli = [0] * MAKSDATA
#penciptaan array Barang Produksi, Harga Produksi, Banyak Produksi
BarangProduksi = ['/'] * MAKSDATA
HargaProduksi = [0] * MAKSDATA
BanyakProduksi = [0] * MAKSDATA
#penciptaan array Jenis Packaging, Harga Satuan, Banyak Beli Pack (BBP)
JenisPackaging = ['/'] * MAKSDATA
HargaSatuan = [0] * MAKSDATA
BBP = [0] * MAKSDATA
#penciptaan list untuk Intangible Assets
IntangibleAssetsList = []
#inisialisasi
BanyakDataStok = 0
BanyakDataBahan = 0
BanyakDataProduksi = 0
BanyakDataPackaging = 0
#inisialisasi pilihan
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
                    case 1: #stok pakaian
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
                                    BanyakDataStok = HapusDataStok(NB, BS, BanyakDataStok)
                            
                            os.system('cls')
                            PilihanMenuStok = MenuStokPakaian (PilihanMenuStok) 
                    case 2: #bahan baku      
                        PilihanMenuBahan = 0 
                        PilihanMenuBahan = MenuBahanBaku (PilihanMenuBahan)  
                        while (PilihanMenuBahan != 0):                                                      
                            match(PilihanMenuBahan):  
                                case 1:
                                    BanyakDataBahan = IsiDataBahan(Bahan, HB, BanyakBeli, BanyakDataBahan)
                                    os.system('cls')
                                case 2:
                                    TampilDataBahan(Bahan, HB, BanyakBeli, BanyakDataBahan)
                                    os.system('pause')
                                    os.system('cls')
                                case 3:
                                    BanyakDataBahan = HapusDataBahan(Bahan, HB, BanyakDataBahan)
                            
                            os.system('cls')
                            PilihanMenuBahan = MenuBahanBaku (PilihanMenuBahan)  
                    case 3: #vendor produksi
                        PilihanMenuProduksi = 0 
                        PilihanMenuProduksi = MenuVendorProduksi (PilihanMenuProduksi)  
                        while (PilihanMenuProduksi != 0):                                                      
                            match(PilihanMenuProduksi):  
                                case 1:
                                    BanyakDataProduksi = IsiDataProduksi(BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi)
                                    os.system('cls')
                                case 2:
                                    TampilDataProduksi (BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi)
                                    os.system('pause')
                                    os.system('cls')
                                case 3:
                                    BanyakDataProduksi = HapusDataProduksi(BarangProduksi, HargaProduksi, BanyakDataProduksi)                            
                                case 4:
                                    BubbleSortProduksiDescending(BarangProduksi, HargaProduksi, BanyakProduksi, BanyakDataProduksi)
                                    CariProdukDesc(BarangProduksi, HargaProduksi,BanyakProduksi, BanyakDataProduksi)

                            os.system('cls')
                            PilihanMenuProduksi = MenuVendorProduksi (PilihanMenuProduksi)
                    case 4: #vendor packaging
                        PilihanMenuPackaging = 0 
                        PilihanMenuPackaging = MenuVendorPackaging (PilihanMenuPackaging)  
                        while (PilihanMenuPackaging != 0):                                                      
                            match(PilihanMenuPackaging):  
                                case 1:
                                    BanyakDataPackaging = IsiDataPackaging(JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging)
                                    os.system('cls')
                                case 2:
                                    TampilDataPackaging (JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging)
                                    os.system('pause')
                                    os.system('cls')
                                case 3:
                                    BanyakDataPackaging = HapusDataPackaging(JenisPackaging, HargaSatuan, BanyakDataPackaging)                            
                                case 4:
                                    BubbleSortPackagingAscending(JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging)
                                    CariPackAsc(JenisPackaging, HargaSatuan, BBP, BanyakDataPackaging)
                            
                            os.system('cls')
                            PilihanMenuPackaging = MenuVendorPackaging (PilihanMenuPackaging)                        
                    
                os.system('cls')
                PilihanTangible = TangibleAssets(PilihanTangible)

        


        case 2 :
            PilihanIntangible = 0
            PilihanIntangible = IntangibleAssets(PilihanIntangible)
            while (PilihanIntangible != 0):
                os.system('cls')
                match (PilihanIntangible):
                    case 1:
                        print("Brand & Nama Usaha")
                        TambahBrand(IntangibleAssetsList)
                        os.system('pause')
                    case 2:
                        print("Website & Sosial Media (Marketing)")
                        TambahSocialMedia(IntangibleAssetsList)
                        TambahMarketingAsset(IntangibleAssetsList)
                        os.system('pause')
                    case 3:
                        print("Database Karyawan")
                        TambahKaryawan(IntangibleAssetsList)
                        os.system('pause')
                    case 4:
                        TambahIntangibleAsset(IntangibleAssetsList)
                        UrutkanIntangibleAssets(IntangibleAssetsList)
                        CariIntangibleAsset(IntangibleAssetsList)
                        HapusIntangibleAsset(IntangibleAssetsList)
                        HancurkanIntangibleAssets(IntangibleAssetsList)
                os.system('cls')
                PilihanIntangible = IntangibleAssets(PilihanIntangible)
            
    os.system('cls')
    Pilihan = MenuUtama(Pilihan)
