# Simulasi Robot Berbasis Graf

Proyek ini mensimulasikan pergerakan robot pada lapangan yang dibangun menggunakan **Matplotlib**. Robot akan bergerak mengikuti jalur yang ditentukan menggunakan algoritma **Breadth-First Search (BFS)** untuk mencapai area target.

## Fitur
- Gambar lapangan lengkap dengan area penting (HOME, kotak berwarna, garis merah, dan kotak lainnya).
- Implementasi algoritma **BFS** untuk menemukan jalur terpendek.
- Simulasi pergerakan robot sesuai dengan rute yang telah dihitung.

## Prasyarat
Anda perlu menginstal beberapa paket Python agar simulasi dapat berjalan dengan baik. Gunakan perintah berikut untuk menginstal semua dependensi:

```bash
pip install -r requirements.txt
```

### Dependensi
- `matplotlib`: Untuk menggambar lapangan dan robot.
- `numpy`: Untuk manipulasi data yang diperlukan (misalnya array).
- `collections`: Modul bawaan Python untuk mendukung struktur data seperti deque.

## Cara Menjalankan Simulasi

1. Clone repositori ini ke komputer Anda:
   ```bash
   git clone https://github.com/username/simulasi-robot-graf.git
   ```

2. Masuk ke direktori proyek:
   ```bash
   cd simulasi-robot-graf
   ```

3. Instal semua dependensi:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan simulasi:
   ```bash
   python main.py
   ```

## Penjelasan Kode

### 1. Fungsi `gambar_lapangan()`
Fungsi ini bertanggung jawab menggambar lapangan untuk simulasi, yang terdiri dari:
- **Area HOME**: Tempat robot memulai dan mengakhiri perjalanan.
- **Kotak berwarna**: Representasi target yang harus dicapai oleh robot.
- **Garis merah**: Sebuah garis yang terputus di tengah lapangan.
- **Konektor**: Garis hitam yang menghubungkan titik-titik penting.

### 2. Fungsi `gambar_robot()`
Fungsi ini menggambar dan memperbarui posisi robot pada lapangan berdasarkan koordinat yang diberikan.

### 3. Fungsi `bfs()`
Fungsi ini menggunakan algoritma **Breadth-First Search (BFS)** untuk menemukan jalur terpendek dari satu titik ke titik lainnya pada graf yang telah didefinisikan.

### 4. Fungsi `gerak_robot()`
Fungsi ini bertanggung jawab untuk memindahkan robot sesuai dengan rute yang diberikan dalam simulasi.

### 5. Fungsi `simulasi()`
Fungsi utama untuk memulai simulasi. Fungsi ini menggambar lapangan, menentukan graf untuk pergerakan robot, dan menjalankan simulasi pergerakan robot di sepanjang rute yang telah ditentukan.

## Struktur Graf
Graf ini terdiri dari node dan edge yang mewakili jalur yang bisa dilalui oleh robot. Setiap node adalah koordinat tertentu pada lapangan, dan edge menghubungkan node-node yang bisa dilalui oleh robot.

Contoh graf:
```python
graph = {
    (50, 10): [(50, 20)],
    (50, 20): [(50, 10), (5, 20), (95, 20), (15, 20), (85, 20)],
    # dan seterusnya...
}
```

## Visualisasi Lapangan

Lapangan terdiri dari beberapa elemen utama:
- **HOME**: Titik awal robot (di koordinat (50, 10)).
- **Kotak Berwarna**: Titik tujuan yang harus dicapai robot.
- **Garis Merah Terputus**: Ditempatkan di tengah lapangan sebagai tantangan untuk dilalui.
- **Konektor Hitam**: Menghubungkan area-area penting pada lapangan.

## Pengembangan Lanjutan
Anda dapat mengembangkan proyek ini lebih lanjut dengan ide-ide berikut:
- Menambahkan rintangan yang harus dihindari oleh robot.
- Menggunakan algoritma pencarian jalur lain seperti **A* (A-star)**.
- Mengubah lapangan untuk menambah tingkat kesulitan.

## Kontribusi
Kami menerima kontribusi dalam bentuk _pull request_ atau _issue_. Jika Anda menemukan bug atau ingin menambahkan fitur baru, jangan ragu untuk membuat _issue_ atau _fork_ proyek ini.


