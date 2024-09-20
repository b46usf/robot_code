import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import time

# Fungsi untuk menggambar lapangan
def gambar_lapangan(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Area HOME
    area_home = patches.Rectangle((45, 2.5), 10, 10, linewidth=2, edgecolor='black', facecolor='white')
    ax.add_patch(area_home)
    ax.text(50, 5, 'HOME', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

    # Tiga Kotak berwarna di atas (mewakili camp zone)
    kotak_atas = {'cyan': (50, 92), 'green': (85, 92), 'yellow': (15, 92)}
    for warna, (x, y) in kotak_atas.items():
        kotak = patches.Rectangle((x-5, y-5), 10, 10, linewidth=2, edgecolor='black', facecolor=warna)
        ax.add_patch(kotak)

    # Garis merah horizontal yang terbelah
    garis_merah_kiri = patches.Rectangle((10, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(garis_merah_kiri)
    garis_merah_kanan = patches.Rectangle((60, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(garis_merah_kanan)
    ax.text(50, 72.5, 'Celah', horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')

    # Tiga kotak membentuk segitiga sama sisi di bagian tengah adalah DISASTER ZONE
    x_center = 50
    y_center = 55
    ax.add_patch(patches.Rectangle((x_center - 4, y_center + 3), 8, 8, linewidth=2, edgecolor='black', facecolor='yellow')) 
    ax.add_patch(patches.Rectangle((x_center - 19, y_center - 12), 8, 8, linewidth=2, edgecolor='black', facecolor='green'))
    ax.add_patch(patches.Rectangle((x_center + 11, y_center - 12), 8, 8, linewidth=2, edgecolor='black', facecolor='cyan'))

    # Kotak merah dan kuning berada di samping kanan dan kiri secara vertikal
    ax.add_patch(patches.Rectangle((0, 47), 7, 7, linewidth=2, edgecolor='black', facecolor='red'))
    ax.add_patch(patches.Rectangle((0, 37), 7, 7, linewidth=2, edgecolor='black', facecolor='cyan'))
    ax.add_patch(patches.Rectangle((0, 27), 7, 7, linewidth=2, edgecolor='black', facecolor='yellow'))
    ax.add_patch(patches.Rectangle((0, 17), 7, 7, linewidth=2, edgecolor='black', facecolor='green'))

    ax.add_patch(patches.Rectangle((93, 47), 7, 7, linewidth=2, edgecolor='black', facecolor='yellow'))
    ax.add_patch(patches.Rectangle((93, 37), 7, 7, linewidth=2, edgecolor='black', facecolor='green'))
    ax.add_patch(patches.Rectangle((93, 27), 7, 7, linewidth=2, edgecolor='black', facecolor='red'))
    ax.add_patch(patches.Rectangle((93, 17), 7, 7, linewidth=2, edgecolor='black', facecolor='cyan'))

    # Konektor (jalur) baru
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

# Fungsi untuk memperbarui posisi robot dan timer
def update(frame):
    # Update posisi robot
    x_start, y_start = jalur[frame]
    robot.center = (x_start, y_start)
    
    # Update timer berdasarkan waktu berlalu
    elapsed_time = time.time() - start_time
    timer_text.set_text(f'Timer: {elapsed_time:.1f} s')
    
    return robot, timer_text

# Jalur robot berdasarkan prioritas penyelamatan korban sesuai warna
jalur = [
    # mulai dari home ke disaster zone terdekat green
    (50, 10), (50, 15), (20, 15), (20, 30), (35, 30), (35, 47.5),
    # lanjut dari disaster zone green ke disaster zone cyan
    (35, 30), (65, 30), (65, 47.5),
    # lanjut dari disaster zone cyan ke disaster zone yellow
    (65, 30), (50, 30), (50, 62),
    # lanjut dari disaster zone yellow ke camp zone yellow
    (50, 53), (40, 62.5), (50, 72), (50, 77), (15, 77), (15, 90),
    # lanjut dari camp zone yellow ke camp zone green
    (15, 77), (85, 77), (85, 90),
    # lanjut dari camp zone green ke jalur camp zone cyan
    (85, 77), (50, 77), (50, 90),
    # the key of pola jalur 6.3.3
]

# Setup untuk simulasi
fig, ax = plt.subplots(figsize=(8, 8))
gambar_lapangan(ax)

# Menggambar robot sebagai lingkaran
robot = plt.Circle(jalur[0], 1.5, color='blue')
ax.add_patch(robot)

# Menambahkan judul dan timer
ax.set_title("Simulasi Lapangan 1", fontsize=14, fontweight='bold')
timer_text = ax.text(70, 95, 'Timer: 0 s', horizontalalignment='center', fontsize=12)

# Mulai waktu
start_time = time.time()

# Animasi pergerakan robot
ani = FuncAnimation(fig, update, frames=len(jalur), interval=1000, blit=True, repeat=False)

plt.show()
