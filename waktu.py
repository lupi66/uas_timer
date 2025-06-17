import tkinter as tk
from tkinter import messagebox, simpledialog

class PengingatBelajar:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Belajar")
        self.root.geometry("300x200")
        
        self.label = tk.Label(root, text="", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.mulai_sesi()

    def mulai_sesi(self):
        belajar = simpledialog.askinteger("Input", "Berapa menit waktu belajar?", minvalue=1)
        istirahat = simpledialog.askinteger("Input", "Berapa menit waktu istirahat?", minvalue=1)

        if belajar is None or istirahat is None:
            messagebox.showinfo("Batal", "Program dibatalkan.")
            self.root.destroy()
            return
        
        self.mulai_timer(belajar * 60, "Belajar")

        self.root.after(belajar * 60 * 1000, lambda: self.selesai_belajar(istirahat))

    def mulai_timer(self, durasi, mode):
        def update():
            nonlocal durasi
            menit, detik = divmod(durasi, 60)
            self.label.config(text=f"{mode}: {menit:02d}:{detik:02d}")
            if durasi > 0:
                durasi -= 1
                self.root.after(1000, update)
        
        update()

    def selesai_belajar(self, durasi_istirahat):
        messagebox.showinfo("Selesai Belajar", "Waktu belajar selesai! Saatnya istirahat.")
        self.mulai_timer(durasi_istirahat * 60, "Istirahat")

        self.root.after(durasi_istirahat * 60 * 1000, self.setelah_istirahat)

    def setelah_istirahat(self):
        lanjut = messagebox.askyesno("Lanjut Belajar?", "Waktu istirahat selesai.\nMau lanjut belajar?")
        if lanjut:
            self.mulai_sesi()
        else:
            messagebox.showinfo("Selesai", "Program selesai. Semangat terus ya!")
            self.root.destroy()

# Jalankan program
if __name__ == "__main__":
    root = tk.Tk()
    app = PengingatBelajar(root)
    root.mainloop()
