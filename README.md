# Penjelasan Code

## Import
```python
import time
import os
from datetime import datetime, timedelta
```
- time : Untuk fungsi atur waktunya. <br>
- os : Untuk mengecek dan menghapus file (os.path.exists, os.remove). <br>
- datetime dan timedelta : Untuk mencatat waktu saat ini dan menghitung selisih waktu

## Simpan File Riwayat
```python
RIWAYAT_FILE = "riwayat.txt"
```

##  Fungsi alarm_suara
```python
def alarm_suara():
    try:
        import winsound
        for _ in range(3):
            winsound.Beep(10001, 500)
            time.sleep(0.5)
    except ImportError:
        print("\n(Bunyi alarm tidak tersedia di sistem ini.)")
```
#### Bagian Fungsi alarm_suara
```python
for _ in range(3):
    winsound.Beep(10001, 500)
    time.sleep(0.5)
```
- winsound.Beep(10001, 500) : Mengeluarkan bunyi dengan frekuensi 10001 Hz selama 500 milidetik (0.5 detik). <br>
- for _ in range(3) : Mengulanginya sebanyak 3 kali.

## Fungsi simpan_riwayat(note)
```python
def simpan_riwayat(note):
    sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RIWAYAT_FILE, "a") as f:
        f.write(f"{sekarang} - {note}\n")

```
#### Bagian Fungsi simpan_riwayat(note)
```python
sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```
- Mengambil waktu saat ini menggunakan datetime.now() dan disimpan dengan format tahun - bulan - tanggal Jam:Menit:Detik dengan .strftime("%Y-%m-%d %H:%M:%S") lalu dimasukkan ke variabel *Sekarang*
  
#### Bagian Fungsi simpan_riwayat(note)
```python
with open(RIWAYAT_FILE, "a") as f:
```
- Membuka file riwayat.txt (nama disimpan di variabel RIWAYAT_FILE) <br>
- Mode "a" artinya append: menambahkan data di akhir file tanpa menghapus isinya. <br>
- as f memberi nama f sebagai alias file handler agar bisa digunakan dalam blok ini.

#### Bagian Fungsi simpan_riwayat(note)
```python
f.write(f"{sekarang} - {note}\n")
```
- Format isi file

## Fungsi tampilkan_riwayat()
```python
def tampilkan_riwayat():
    if not os.path.exists(RIWAYAT_FILE):
        print("Belum ada riwayat.")
        return

    sekarang = datetime.now()
    batas = sekarang - timedelta(days=1)
    print("\nRiwayat:")
    with open(RIWAYAT_FILE, "r") as f:
        for baris in f:
            waktu_str, note = baris.strip().split(" - ", 1)
            waktu = datetime.strptime(waktu_str, "%Y-%m-%d %H:%M:%S")
            if waktu > batas:
                print(f" - {waktu_str}: {note}")

```

#### Bagian Fungsi tampilkan_riwayat()
```python
if not os.path.exists(RIWAYAT_FILE):
        print("Belum ada riwayat.")
        return
```
- Cek apakah file-nya ada. Jika tidak maka akan muncul pesan

#### Bagian Fungsi tampilkan_riwayat()
```python
for baris in f:
            waktu_str, note = baris.strip().split(" - ", 1)
            waktu = datetime.strptime(waktu_str, "%Y-%m-%d %H:%M:%S")
            if waktu > batas:
                print(f" - {waktu_str}: {note}")
```
- Membaca file per baris dan menampilkan riwayat dalam 24 jam terakhir

## Fungsi hapus_riwayat()
```python
def hapus_riwayat():
    if os.path.exists(RIWAYAT_FILE):
        konfirmasi = input("Ingin menghapus seluruh riwayat? (y/n): ")
        if konfirmasi.lower() == "y":
            os.remove(RIWAYAT_FILE)
            print("Riwayat berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Tidak ada riwayat untuk dihapus.")
```
- Kasih pilihan untuk menghapus seluruh isi riwayat setelah konfirmasi.

## Fungsi hitung_mundur_interaktif()
```python
def hitung_mundur_interaktif(detik, mode, judul="", catatan=""):
    if mode == "Belajar":
        print(f"\nSemangat yaa belajar {judul} !!!\n")
        if catatan:
            print(f"Catatan: {catatan}\n")

    while detik > 0:
        menit, sisa_detik = divmod(detik, 60)
        print(f"{mode}: {menit:02d}:{sisa_detik:02d}", end="\r")
        detik -= 1
        time.sleep(1)
    
    print(f"\n{mode} selesai!")
    alarm_suara()
    return True
```

#### Bagian Fungsi hitung_mundur_interaktif()
```python
if mode == "Belajar":
        print(f"\nSemangat yaa belajar {judul} !!!\n")
        if catatan:
            print(f"Catatan: {catatan}\n")
```
- Menampilkan judul dan catatan yang di input oleh User.

#### Bagian Fungsi hitung_mundur_interaktif()
```python
while detik > 0:
        menit, sisa_detik = divmod(detik, 60)
        print(f"{mode}: {menit:02d}:{sisa_detik:02d}", end="\r")
        detik -= 1
        time.sleep(1)
```
- Menampilkan countdown timer

#### Bagian Fungsi hitung_mundur_interaktif()
```python
print(f"\n{mode} selesai!")
    alarm_suara()
    return True
```
- Setelah waktu habis, bunyi alarm akan diputar.

## Fungsi mulai_sesi()
```python
def mulai_sesi():
    judul = input("Mau belajar apa hari ini: ")
    catatan = input("Catatan kecil (boleh dikosongkan): ")
    try:
        belajar = int(input("Belajar berapa menit: "))
        istirahat = int(input("Istirahat berapa menit: "))
    except ValueError:
        print("Masukkan angka yang valid.")
        return

    simpan_riwayat(f"Mulai belajar: {judul} | Catatan: {catatan}")
    print("\nSesi belajar dimulai...")
    selesai = hitung_mundur_interaktif(belajar * 60, "Belajar", judul, catatan)
    if not selesai:
        return
    
    print("Waktu belajar selesai! Saatnya istirahat...")
    selesai = hitung_mundur_interaktif(istirahat * 60, "Sisa Waktu Istirahat")
    if not selesai:
        return

    simpan_riwayat(f"Selesai belajar: {judul} | Catatan: {catatan}")
    lanjut = input("Mau lanjut belajar lagi? (y/n): ")
    if lanjut.lower() == "y":
        mulai_sesi()
    else:
        print("Sesi diselesaikan.")
```

#### Bagian Fungsi mulai_sesi()
```python
judul = input("Mau belajar apa hari ini: ")
    catatan = input("Catatan kecil (boleh dikosongkan): ")
    try:
        belajar = int(input("Belajar berapa menit: "))
        istirahat = int(input("Istirahat berapa menit: "))
    except ValueError:
        print("Masukkan angka yang valid.")
        return

    simpan_riwayat(f"Mulai belajar: {judul} | Catatan: {catatan}")
    print("\nSesi belajar dimulai...")
    selesai = hitung_mundur_interaktif(belajar * 60, "Belajar", judul, catatan)
    if not selesai:
        return
    
    print("Waktu belajar selesai! Saatnya istirahat...")
    selesai = hitung_mundur_interaktif(istirahat * 60, "Sisa Waktu Istirahat")
    if not selesai:
        return

    simpan_riwayat(f"Selesai belajar: {judul} | Catatan: {catatan}")
```
- Fungsi utama untuk memulai satu sesi belajar lalu sesi istirahat. <br>
- Mencatat riwayat awal dan akhir.

#### Bagian Fungsi mulai_sesi()
```python
 lanjut = input("Mau lanjut belajar lagi? (y/n): ")
    if lanjut.lower() == "y":
        mulai_sesi()
    else:
        print("Sesi diselesaikan.")
```
- Setelah selesai istirahat, bisa pilih lanjut belajar atau diselesaikan

## Blok Main (Program Utama)
```python
if __name__ == "__main__":
        while True:
            print("\n=== ATUR WAKTU BELAJAR ===")
            print("1. Mulai sesi belajar sekarang")
            print("2. Tampilkan riwayat belajar")
            print("3. Hapus riwayat belajar")
            print("4. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                mulai_sesi()
            elif pilihan == "2":
                tampilkan_riwayat()
            elif pilihan == "3":
                hapus_riwayat()
            elif pilihan == "4":
                print("Program dihentikan.")
                break
            else:
                print("Pilihan tidak valid.")
```
- Menu utama interaktif. <br>
- Memanggil fungsi sesuai input User. <br>
- Berulang sampai User memilih keluar. <br>



