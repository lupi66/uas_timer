# Penjelasan Code

## Import
```python
import tkinter as tk
from tkinter import messagebox, simpledialog
```
tkinter untuk tampilan GUI (Graphical User Interface). <br>
messagebox dan simpledialog: dialog pop-up untuk input dan notifikasi.

## Tampilan Timer Belajar
```python
class PengingatBelajar:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Belajar")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.mulai_sesi()
```
__init__ : fungsi awal 

## Input User
```python
def mulai_sesi(self):
      belajar = simpledialog.askinteger("Input", "Berapa menit waktu belajar?", minvalue=1)
      istirahat = simpledialog.askinteger("Input", "Berapa menit waktu istirahat?", minvalue=1)
```
askinteger : hanya menerima angka bulat

## Jika User Memilih Cancel, Program dihentikan
```python
if belajar is None or istirahat is None:
            messagebox.showinfo("Batal", "Program dibatalkan.")
            self.root.destroy()
            return
```

## Ubah Timer dari Menit ke Detik
```python
self.mulai_timer(belajar * 60, "Belajar")
```


