import time
import os
from datetime import datetime, timedelta

RIWAYAT_FILE = "riwayat.txt"

def alarm_suara():
    try:
        import winsound
        for _ in range(3):
            winsound.Beep(10001, 500)
            time.sleep(0.5)
    except ImportError:
        print("\n(Bunyi alarm tidak tersedia di sistem ini.)")

def simpan_riwayat(note):
    sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RIWAYAT_FILE, "a") as f:
        f.write(f"{sekarang} - {note}\n")

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
