import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Fungsi untuk menggambar zona HOME
def gambar_home_zone(ax):
    home_area = patches.Rectangle((45, 2.5), 10, 10, linewidth=2, edgecolor='black', facecolor='white')
    ax.add_patch(home_area)
    ax.text(50, 5, 'HOME', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Fungsi untuk menggambar camp zone (atas)
def gambar_camp_zone(ax):
    camp_zone_boxes = {'cyan': (50, 92), 'green': (85, 92), 'yellow': (15, 92)}
    for warna, (x, y) in camp_zone_boxes.items():
        kotak = patches.Rectangle((x-5, y-5), 10, 10, linewidth=2, edgecolor='black', facecolor=warna)
        ax.add_patch(kotak)

# Fungsi untuk menggambar garis merah horizontal terbelah
def gambar_garis_merah(ax):
    garis_merah_kiri = patches.Rectangle((10, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    garis_merah_kanan = patches.Rectangle((60, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(garis_merah_kiri)
    ax.add_patch(garis_merah_kanan)
    ax.text(50, 72.5, 'Celah', horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')

# Fungsi untuk menggambar disaster zone (segitiga)
def gambar_disaster_zone(ax):
    x_center, y_center = 50, 55
    disaster_zones = [
        (x_center - 4, y_center + 3, 'yellow'),
        (x_center - 19, y_center - 12, 'green'),
        (x_center + 11, y_center - 12, 'cyan')
    ]
    for x, y, color in disaster_zones:
        ax.add_patch(patches.Rectangle((x, y), 8, 8, linewidth=2, edgecolor='black', facecolor=color))

# Fungsi untuk menggambar kotak logistik (samping kiri dan kanan)
def gambar_kotak_logistik(ax):
    logistik_kiri = [('red', 47), ('cyan', 37), ('yellow', 27), ('green', 17)]
    logistik_kanan = [('yellow', 47), ('green', 37), ('red', 27), ('cyan', 17)]
    
    for color, y in logistik_kiri:
        ax.add_patch(patches.Rectangle((0, y), 7, 7, linewidth=2, edgecolor='black', facecolor=color))
    for color, y in logistik_kanan:
        ax.add_patch(patches.Rectangle((93, y), 7, 7, linewidth=2, edgecolor='black', facecolor=color))

# Fungsi untuk menggambar konektor/jalur
def gambar_konektor(ax):
    konektor = [
        ((50, 10), (50, 15)),  # Vertikal dari HOME ke titik cabang
        ((50, 15), (20, 15)),   # Horizontal dari titik cabang ke kiri
        ((20, 15), (20, 30)),    # Vertikal dari titik cabang ke atas
        ((20, 30), (50, 30)),  # Horizontal dari titik atas ke kanan
        ((50, 15), (80, 15)),  # Horizontal dari titik cabang ke kanan
        ((80, 15), (80, 30)),  # Vertikal dari titik cabang ke atas
        ((80, 30), (50, 30)),  # Horizontal dari titik atas ke kiri
        ((35, 30), (35, 47.5)),  # Vertikal ke kotak hijau
        ((65, 30), (65, 47.5)),  # Vertikal ke kotak cyan
        ((50, 30), (50, 62)),  # Vertikal ke kotak kuning tengah
        ((50, 72), (50, 77)),  # Vertikal ke kotak kuning atas
        ((50, 77), (15, 77)),  # Horizontal ke kotak kuning kiri atas
        ((15, 77), (15, 90)),  # Vertikal ke kotak kuning
        ((50, 77), (50, 90)),  # Vertikal ke kotak cyan atas
        ((50, 77), (85, 77)),  # Horizontal ke kotak hijau kanan atas
        ((85, 77), (85, 90)),  # Vertikal ke kotak hijau atas
        ((50, 53), (40, 62.5)),  # Diagonal dari titik kuning tengah ke kiri
        ((50, 53), (60, 62.5)),  # Diagonal dari titik kuning tengah ke kanan
        ((40, 62.5), (50, 72)),  # Diagonal kembali ke titik atas
        ((60, 62.5), (50, 72)),  # Diagonal kembali ke titik atas
        ((4, 20), (20, 20)),     # Horizontal dari kotak hijau kiri
        ((20, 30), (4, 30)),     # Horizontal dari kotak kuning kiri
        ((20, 30), (20, 40)),    # Vertikal dari kotak cyan kiri
        ((20, 40), (4, 40)),     # Horizontal dari kotak cyan kiri
        ((80, 20), (96, 20)),    # Horizontal dari kotak cyan kanan
        ((80, 30), (80, 40)),    # Vertikal dari kotak hijau kanan
        ((80, 40), (96, 40)),    # Horizontal dari kotak hijau kanan
        ((80, 40), (80, 50)),    # Vertikal dari kotak kuning kanan
        ((80, 50), (96, 50))     # Horizontal dari kotak kuning kanan
    ]
    for (x_start, y_start), (x_end, y_end) in konektor:
        ax.plot([x_start, x_end], [y_start, y_end], color='black', linestyle='-', linewidth=1)

# Fungsi utama untuk menggambar lapangan
def gambar_lapangan(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    gambar_home_zone(ax)
    gambar_camp_zone(ax)
    gambar_garis_merah(ax)
    gambar_disaster_zone(ax)
    gambar_kotak_logistik(ax)
    gambar_konektor(ax)

# Koordinat objek di disaster zone
disaster_objects = [
    (50, 62),   # Kotak di Disaster Zone Yellow
    (35, 47.5), # Kotak di Disaster Zone Green
    (65, 47.5)  # Kotak di Disaster Zone Cyan
]

# Koordinat objek di logistic zone
logistic_objects = [
    (4, 40),   # Kotak kiri atas - Logistic Zone Cyan
    (4, 30),   # Kotak kiri tengah - Logistic Zone Yellow
    (4, 20),   # Kotak kiri bawah - Logistic Zone Green
    (96, 50),  # Kotak kanan atas - Logistic Zone Yellow
    (96, 40),  # Kotak kanan tengah - Logistic Zone Green
    (96, 20)   # Kotak kanan bawah - Logistic Zone Cyan
]

# Fungsi untuk menggambar objek di zona tertentu
def draw_objects(ax, objects, radius=1, color='black'):
    # Menggambar objek sebagai lingkaran di axis yang diberikan
    for x, y in objects:
        ax.add_patch(patches.Circle((x, y), radius, color=color))

# Fungsi utama untuk menggambar objek di disaster dan logistic zones
def gambar_objek(ax):
    # Menggambar objek di disaster zone dan logistic zones
    draw_objects(ax, disaster_objects)  # Gambar objek di disaster zone
    draw_objects(ax, logistic_objects)   # Gambar objek di logistic zone

# Fungsi untuk memperbarui posisi robot, objek, dan timer
def update(frame):
    global elapsed_time, robot_arrived_home, stop_timer_countdown, stop_timer_flag
    global saved_objects  # Objek yang sedang diselamatkan

    # Update posisi robot
    if frame < len(jalur):
        x_start, y_start = jalur[frame]
        robot.center = (x_start, y_start)

        # Update posisi objek yang mengikuti robot (jika ada objek yang diselamatkan)
        if saved_objects:
            for i, (color, obj) in enumerate(saved_objects):
                obj.center = (x_start - 3 * (i + 1), y_start)  # Objek mengikuti robot dengan jarak

        # Cek jika robot tiba di zona pengambilan objek
        for color, coords in pengambilan_objek.items():
            if coords == (x_start, y_start):  # Jika koordinat robot sesuai dengan zona pengambilan objek
                if color not in [obj[0] for obj in saved_objects]:  # Cek apakah objek belum diselamatkan
                    obj_color = warna_objek[color]  # Mendapatkan warna objek dari dictionary warna_objek
                    
                    # Tentukan zona pengambilan objek (disaster atau logistic)
                    zone_type = 'disaster zone' if color in ['cyan', 'green', 'yellow'] else 'logistic zone'
                    
                    saved_objects.append((color, plt.Circle((x_start, y_start), 1, color=obj_color)))
                    ax.add_patch(saved_objects[-1][1])  # Tambahkan objek lingkaran ke plot
                    print(f"Objek berwarna {obj_color} pada {zone_type} diselamatkan")

        # Deteksi jika robot tiba di Camp Zone untuk meletakkan objek
        for i in range(len(saved_objects) - 1, -1, -1):
            color, obj = saved_objects[i]
            
            # Ambil bagian awal dari warna hingga _ (misal cyan_left menjadi cyan)
            base_color = color.split('_')[0]
            
            # Mendapatkan koordinat camp zone berdasarkan warna dasar
            camp_zone_coords = camp_zones_arrival.get(base_color, None)
            
            if camp_zone_coords is not None:
                x_camp, y_camp = camp_zone_coords  # Koordinat camp zone
                
                # Memeriksa apakah posisi robot berada dalam zona camp
                if x_camp - 5 <= x_start <= x_camp + 5 and y_camp - 5 <= y_start <= y_camp + 5:
                    obj.remove()  # Menghapus objek dari plot
                    print(f"Objek berwarna {base_color} diletakkan di Camp Zone dan menghilang.")
                    saved_objects.pop(i)  # Menghapus objek dari daftar

    # Cek jika robot tiba di HOME
    if frame == len(jalur) - 1 and not robot_arrived_home:
        robot_arrived_home = True
        print(f"Robot tiba di HOME pada {elapsed_time} detik. Menunggu 5 detik sebelum menghentikan timer...")
        stop_timer_countdown = 5  # Setel countdown untuk 5 detik

    # Update visual timer
    if robot_arrived_home:
        if stop_timer_countdown is not None and stop_timer_countdown > 0:
            elapsed_time += 1
            stop_timer_countdown -= 1
        elif stop_timer_countdown == 0:
            print(f"Timer berhenti pada {elapsed_time} detik")
            ani.event_source.stop()  # Hentikan animasi setelah countdown selesai
            stop_timer_countdown = None
            plt.pause(5)  # Menunggu selama 5 detik
            on_animation_end()  # Memanggil fungsi untuk menutup visualisasi
    else:
        elapsed_time += 1

    # Perbarui timer visual
    timer_text.set_text(f'Timer: {elapsed_time} s')

    # Kembalikan semua elemen yang diupdate untuk animasi
    return [robot] + [obj for _, obj in saved_objects] + [timer_text]

def on_animation_end():
    plt.close()  # Menutup jendela visualisasi

# Kordinat objek dari Disaster Zone dan Logistic Zone
pengambilan_objek = {
    'cyan': (65, 47.5),     # Disaster Zone Cyan
    'green': (35, 47.5),    # Disaster Zone Green
    'yellow': (50, 62),     # Disaster Zone Yellow
    'cyan_left': (4, 40),   # Logistic Zone Kiri Cyan
    'yellow_left': (4, 30), # Logistic Zone Kiri Yellow
    'green_left': (4, 20),  # Logistic Zone Kiri Green
    'cyan_right': (96, 20), # Logistic Zone Kanan Cyan
    'green_right': (96, 40),# Logistic Zone Kanan Green
    'yellow_right': (96, 50),# Logistic Zone Kanan Yellow
}

# Warna objek tetap sama, hanya zona yang berubah
warna_objek = {
    'cyan_left': 'cyan',
    'yellow_left': 'yellow',
    'green_left': 'green',
    'cyan_right': 'cyan',
    'yellow_right': 'yellow',
    'green_right': 'green',
    'cyan': 'cyan',
    'green': 'green',
    'yellow': 'yellow'
}

# kordinat objek diletakkan di Camp Zone
camp_zones_arrival = {
    'yellow': (15, 90),  # Koordinat center dari kotak kuning
    'green': (85, 90),   # Koordinat center dari kotak hijau
    'cyan': (50, 90)     # Koordinat center dari kotak cyan
}

# Fungsi untuk memvalidasi warna
def validate_colors():
    invalid_colors = [color for color in pengambilan_objek.keys() if color not in warna_objek]
    if invalid_colors:
        raise ValueError(f"Invalid colors found in pengambilan_objek: {', '.join(invalid_colors)}")
    print("Semua warna di pengambilan_objek valid.")

# Panggil fungsi validasi sebelum memulai simulasi
validate_colors()

# Jalur robot (dibuat lebih modular)
jalur = [
    # mulai dari home ke disaster zone terdekat cyan
    (50, 10), (50, 15), (80, 15), (80, 30), (65, 30), (65, 47.5),
    # lanjut dari disaster zone cyan ke disaster zone green
    (65, 30), (35, 30), (35, 47.5),
    # lanjut dari disaster zone green ke disaster zone yellow
    (35, 30), (50, 30), (50, 62),
    # lanjut dari disaster zone yellow ke camp zone yellow
    (50, 53), (40, 62.5), (50, 72), (50, 77), (15, 77), (15, 90),
    # lanjut dari camp zone yellow ke camp zone green
    (15, 77), (85, 77), (85, 90),
    # lanjut dari camp zone green ke camp zone cyan
    (85, 77), (50, 77), (50, 90),
    # the key of pola jalur 6.3.3
    # lanjut dari camp zone cyan ke disaster zone sebelah kiri
    (50, 72), (40, 62.5), (50, 53), (50, 30),
    # lanjut dari disaster zone ke logistic zone cyan
    (20, 30), (20, 40), (4, 40),
    # lanjut dari logistic zone cyan ke logistic zone green
    (20, 40), (20, 20), (4, 20),
    # lanjut dari logistic zone green ke logistic zone yellow
    (20, 20), (20, 30), (4, 30),
    # lanjut dari logistic zone yellow ke disaster zone
    (50, 30), (50, 53), (40, 62.5), (50, 72),
    # lanjut dari disaster zone ke camp zone yellow
    (50, 77), (15, 77), (15, 90),
    # lanjut dari camp zone yellow ke camp zone green
    (15, 77), (85, 77), (85, 90),
    # lanjut dari camp zone green ke camp zone cyan
    (85, 77), (50, 77), (50, 90),
    # lanjut dari camp zone cyan ke disaster zone sebelah kanan
    (50, 72), (60, 62.5), (50, 53), (50, 30),
    # lanjut dari disaster zone ke logistic zone cyan
    (80, 30), (80, 20), (96, 20),
    # lanjut dari logistic zone cyan ke logistic zone yellow
    (80, 20), (80, 50), (96, 50),
    # lanjut dari logistic zone yellow ke logistic zone green
    (80, 50), (80, 40), (96, 40),
    # the key of pola jalur 4.3.3.3
    # lanjut dari logistic zone green ke disaster zone
    (80, 40), (80, 30), (50, 30), (50, 53), (60, 62.5), (50, 72),
    # lanjut dari disaster zone ke camp zone green
    (50, 77), (85, 77), (85, 90),
    # lanjut dari camp zone green ke camp zone yellow
    (85, 77), (15, 77), (15, 90),
    # lanjut dari camp zone yellow ke camp zone cyan
    (15, 77), (50, 77), (50, 90),
    # the key of pola jalur 6.3.3.3
    # lanjut dari camp zone cyan ke disaster zone
    (50, 72), (40, 62.5), (50, 53), (50, 30),
    # lanjut dari disaster zone ke home
    (20, 30), (20, 15), (50, 15), (50, 10),
]

# Setup untuk simulasi
fig, ax = plt.subplots(figsize=(8, 8))
gambar_lapangan(ax)
gambar_objek(ax)

# Menggambar robot sebagai lingkaran
robot = plt.Circle(jalur[0], 1.5, color='blue')
ax.add_patch(robot)

# Menambahkan judul dan timer
ax.set_title("Simulasi Lapangan 1", fontsize=14, fontweight='bold')
timer_text = ax.text(70, 95, 'Timer: 0 s', horizontalalignment='center', fontsize=12)

# Inisialisasi variabel timer
elapsed_time = 0  # Timer untuk menghitung waktu
robot_arrived_home = False  # Flag untuk menandai apakah robot sudah kembali ke HOME
stop_timer_countdown = None  # Untuk menghitung countdown 5 detik setelah robot tiba di HOME
stop_timer_flag = False  # Flag untuk memastikan timer visual terus berjalan
saved_objects = []  # Daftar objek yang diselamatkan oleh robot

# Animasi pergerakan robot
ani = FuncAnimation(fig, update, frames=len(jalur) + 5, interval=1000, blit=True, repeat=False)

# Tampilkan plot
plt.show()