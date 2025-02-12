program AsetPerusahaan;

uses
  crt;

var
  Pilihan, PilihanTangiable, PilihanIntangiable: Integer;

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
  clrscr;
  Pilihan := 0; 
  MenuUtama(Pilihan);

  while Pilihan <> 0 do
  begin
    case Pilihan of
      1: begin
           PilihanTangiable := 0;  // Inisialisasi pilihan untuk Aset Berwujud
           TangiableAssets(PilihanTangiable);
         end;
      2: begin
           PilihanIntangiable := 0;  // Inisialisasi pilihan untuk Aset Tak Berwujud
           IntangiableAssets(PilihanIntangiable);
         end;
    end;

    // Kembali ke menu utama setelah memilih opsi
    clrscr;
    MenuUtama(Pilihan);
  end;
  
  writeln('Terima kasih telah menggunakan program ini!');
  readln;  
end.
