program AsetPerusahaan;

uses
  crt;

type
  TBarang = record
    kode: Integer;
    nama: string[50];
    stok: Integer;
  end;

var
  Pilihan, PilihanTangiable, PilihanIntangiable, MenuStokPakaian: Integer;
  Barang: array[1..100] of TBarang;


Procedure MenuUtama(var Pilihan: Integer);
begin
  clrscr;
  writeln('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>');
  writeln('---------------------------------------');
  writeln('1. Aset Berwujud (Tangible Assets)');
  writeln('2. Aset Tak Berwujud (Intangible Assets)');
  writeln('0. KELUAR');
  write('Pilihan Anda? ');
  readln(Pilihan);

  // Validasi input
  while (Pilihan < 0) or (Pilihan > 2) do
  begin
    writeln('Nomor Aset Perusahaan tidak ada, Ulangi!');
    readln;  
    clrscr;
    writeln('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>');
    writeln('---------------------------------------');
    writeln('1. Aset Berwujud (Tangible Assets)');
    writeln('2. Aset Tak Berwujud (Intangible Assets)');
    writeln('0. KELUAR');
    write('Pilihan Anda? ');
    readln(Pilihan);
  end;
end;

Procedure TangiableAssets(var PilihanTangiable: Integer);
begin
  clrscr;
  writeln('=====================================');
  writeln('<< ASET BERWUJUD (TANGIBLE ASSETS) >>');
  writeln('=====================================');
  writeln('1. Gudang Barang Dagangan (Stok Pakaian)');
  writeln('2. Bahan Baku');
  writeln('3. Vendor Produksi');
  writeln('4. Vendor Packaging');
  writeln('0. KELUAR');
  writeln('---------------------------------');
  write('Pilihan Anda? ');
  readln(PilihanTangiable);

  // Validasi input
  while (PilihanTangiable < 0) or (PilihanTangiable > 4) do
  begin
    writeln('Nomor Aset Berwujud tidak ada, Ulangi!');
    readln;  
    clrscr;
    writeln('=====================================');
    writeln('<< ASET BERWUJUD (TANGIBLE ASSETS) >>');
    writeln('=====================================');
    writeln('1. Gudang Barang Dagangan (Stok Pakaian)');
    writeln('2. Bahan Baku');
    writeln('3. Vendor Produksi');
    writeln('4. Vendor Packaging');
    writeln('0. KELUAR');
    writeln('---------------------------------');
    write('Pilihan Anda? ');
    readln(PilihanTangiable);
  end;
end;
procedure MenuStokPakaian(var MenuStokPakaian:Integer);
  writeln('==========================================');
  writeln('<< Gudang Barang Dagangan (Stok Pakaian)>>');
  writeln('==========================================');
  writeln('1. Gudang Barang Dagangan (Stok Pakaian)');
  writeln('2. Bahan Baku');
  writeln('3. Vendor Produksi');
  writeln('4. Vendor Packaging');
  writeln('0. KELUAR');
  write('Pilihan Anda?');
  read
  
  


Procedure TambahBarang(var JumlahBarang : Integer);
begin
  clrscr;  // Membersihkan layar
  // Memeriksa apakah jumlah barang masih kurang dari 100
  if JumlahBarang < 100 then
  begin
    Inc(JumlahBarang);  // Menambah jumlah barang
    with Barang[JumlahBarang] do
    begin
      // Memasukkan data barang baru
      write('Masukkan Kode Barang: ');
      readln(kode);
      write('Masukkan Nama Barang: ');
      readln(nama);
      write('Masukkan Stok Barang: ');
      readln(stok);
    end;
    writeln('Barang berhasil ditambahkan!');  // Menampilkan pesan sukses
  end
  else
    writeln('Gudang sudah penuh, tidak bisa menambah barang baru.');  // Menampilkan pesan jika gudang penuh
  readln;  // Menunggu input dari pengguna sebelum melanjutkan
end;

Procedure HapusBarang(var JumlahBarang : Integer);
var
  kodeHapus, i, j: Integer;
  ditemukan: Boolean;
begin
  clrscr;
  ditemukan := False; 
  write('Masukkan Kode Barang yang ingin dihapus: ');
  readln(kodeHapus);
  for i := 1 to JumlahBarang do
  begin
    if Barang[i].kode = kodeHapus then
    begin
      ditemukan := True;
      for j := i to JumlahBarang - 1 do
        Barang[j] := Barang[j + 1];
      Dec(JumlahBarang);
      writeln('Barang berhasil dihapus!');
      break;
    end;
  end;
  if not ditemukan then
    writeln('Barang dengan kode tersebut tidak ditemukan.');
  readln;
end;

Procedure TampilBarang;
var
  i: Integer;
begin
  clrscr;
  writeln('Data Barang:');
  for i := 1 to JumlahBarang do
  begin
    writeln('Kode: ', Barang[i].kode, ', Nama: ', Barang[i].nama, ', Stok: ', Barang[i].stok);
  end;
  readln;
end;

Procedure IntangiableAssets(var PilihanIntangiable: Integer);
begin
  clrscr;
  writeln('===========================================');
  writeln('<< ASET TAK BERWUJUD (INTANGIBLE ASSETS) >>');
  writeln('===========================================');
  writeln('1. Brand & Nama Usaha');
  writeln('2. Website & Sosial Media (Marketing)');
  writeln('3. Database Karyawan');
  writeln('0. KELUAR');
  write('Pilihan Anda? ');
  readln(PilihanIntangiable);

  // Validasi input
  while (PilihanIntangiable < 0) or (PilihanIntangiable > 3) do
  begin
    writeln('Nomor Aset Tak Berwujud tidak ada, Ulangi!');
    readln;  
    clrscr;
    writeln('===========================================');
    writeln('<< ASET TAK BERWUJUD (INTANGIBLE ASSETS) >>');
    writeln('===========================================');
    writeln('1. Brand & Nama Usaha');
    writeln('2. Website & Sosial Media (Marketing)');
    writeln('3. Database Karyawan');
    writeln('0. KELUAR');
    write('Pilihan Anda? ');
    readln(PilihanIntangiable);
  end;
end;
begin
  

begin
  clrscr;
  Pilihan := 0; 
  MenuUtama(Pilihan);

  while Pilihan <> 0 do
  begin
    case Pilihan of
      1: begin
           PilihanTangiable := 0;
           PilihanTangiable := TangiableAssets('PilihanTangiable');
           while PilihanTangiable <> 0 do
           clrscr;
           case Pilihan of
           1: begin  
                //penciptaan array no, Namabarang(NB), Banyak stok(BS)
                
         end;
      2: begin
           PilihanIntangiable := 0;  // Inisialisasi pilihan untuk Aset Tak Berwujud
           IntangiableAssets(PilihanIntangiable);
         end;
    end;

    // Kembali ke menu utama setelah memilih opsi
    clrscr;
    writeln('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>');
    writeln('---------------------------------------');
    writeln('1. Aset Berwujud (Tangible Assets)');
    writeln('2. Aset Tak Berwujud (Intangible Assets)');
    writeln('0. KELUAR');
    write('Pilihan Anda? ');
    readln(Pilihan);

  // Validasi input
  while (Pilihan < 0) or (Pilihan > 2) do
      begin
        writeln('Nomor Aset Perusahaan tidak ada, Ulangi!');
        readln;  
        clrscr;
        writeln('<< ASET PERUSAHAAN CLOTHES DREIELFOG >>');
        writeln('---------------------------------------');
        writeln('1. Aset Berwujud (Tangible Assets)');
        writeln('2. Aset Tak Berwujud (Intangible Assets)');
        writeln('0. KELUAR');
        write('Pilihan Anda? ');
        readln(Pilihan);
      end;
    MenuUtama(Pilihan);
  end;
  
  writeln('Terima kasih telah menggunakan program ini!');
  readln;  
end.
