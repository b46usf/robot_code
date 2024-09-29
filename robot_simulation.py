import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Fungsi untuk menggambar zona HOME
def draw_home_zone(ax):
    home_area = patches.Rectangle((45, 2.5), 10, 10, linewidth=2, edgecolor='black', facecolor='white')
    ax.add_patch(home_area)
    ax.text(50, 5, 'HOME', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Fungsi untuk menggambar camp zone
def draw_camp_zones(ax):
    camp_zones = {'cyan': (50, 95), 'green': (15, 95), 'yellow': (85, 95)}
    for color, (x, y) in camp_zones.items():
        box = patches.Rectangle((x - 5, y - 5), 10, 10, linewidth=2, edgecolor='black', facecolor=color)
        ax.add_patch(box)

# Fungsi untuk menggambar dinding garis merah horizontal
def draw_red_gaps(ax):
    left_gap = patches.Rectangle((10, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    right_gap = patches.Rectangle((60, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(left_gap)
    ax.add_patch(right_gap)
    ax.text(50, 72.5, 'Celah', horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')

# Fungsi untuk menggambar disaster zone
def draw_disaster_zones(ax):
    disaster_zones = [
        (46.5, 50, 'yellow'),# Yellow zone
        (34, 42, 'green'),   # Green zone
        (59, 42, 'cyan')     # Cyan zone
    ]
    for x, y, color in disaster_zones:
        ax.add_patch(patches.Rectangle((x, y), 7, 7, linewidth=2, edgecolor='black', facecolor=color))

# Fungsi untuk menggambar kotak logistik
def draw_logistic_boxes(ax):
    left_boxes = [('red', 29), ('cyan', 20), ('yellow', 47), ('green', 38)]
    right_boxes = [('yellow', 29), ('green', 20), ('red', 47), ('cyan', 38)]
    
    for color, y in left_boxes:
        ax.add_patch(patches.Rectangle((0, y), 6, 6, linewidth=2, edgecolor='black', facecolor=color))
    for color, y in right_boxes:
        ax.add_patch(patches.Rectangle((94, y), 6, 6, linewidth=2, edgecolor='black', facecolor=color))

# Fungsi untuk menggambar konektor/jalur
def draw_connectors(ax):
    connectors = [
        ((50, 10), (50, 23)),  # Vertikal dari HOME ke titik cabang
        ((50, 23), (94, 23)),  # HORIZONTAL BELOK KANAN
        ((80, 23), (80, 41)),  # VERTIKAL BELOK KIRI
        ((94, 32), (20, 32)),  # HORIZONTAL BELOK KIRI
        ((50, 32), (50, 50)),  # HORIZONTAL NAIK KEATAS
        ((50, 45), (60, 52.5)),  # DIAGONAL NAIK KEATAS
        # ((50, 45), (40, 52.5)),  # DIAGONAL NAIK KEATAS
        # ((40, 52.5), (50, 63)),  # DIAGONAL NAIK KEATAS
        ((60, 52.5), (50, 63)),  # DIAGONAL NAIK KEATAS
        ((50, 63), (50, 90)),  # VERTIKAL NAIK KEATAS
        ((50, 86), (85, 86)),  # HORIZONTAL KE KANAN
        ((85, 86), (85, 90)),  # VERTIKAL KE ATAS
        ((50, 79), (85, 79)),  # HORIZONTAL KE KANAN
        ((85, 79), (85, 86)),  # VERTIKAL KE KIRI
        ((37.5, 32), (37.5, 42)),  # VERTIKAL KE ATAS
        ((62.5, 32), (62.5, 42)),  # VERTIKAL KE ATAS
        ((15, 86), (85, 86)),  # HORIZONTAL KE KIRI
        ((15, 79), (85, 79)),  # HORIZONTAL KE KIRI
        ((15, 79), (15, 90)),  # VERTIKAL KE BAWAH
        ((80, 41), (94, 41)),  # VERTIKAL KE ATAS
        ((20, 50), (20, 23)),  # BELOK KANAN KIRI
        ((20, 23), (6, 23)),  # BELOK KANAN
        ((20, 41), (6, 41)),  # HORIZONTAL KE KIRI
        ((20, 50), (6, 50)),  # HORIZONTAL KE KIRI
        # ((80, 30), (80, 40)),    # Vertikal dari kotak hijau kanan
        # ((80, 40), (96, 40)),    # Horizontal dari kotak hijau kanan
        
    ]
    for (x_start, y_start), (x_end, y_end) in connectors:
        ax.plot([x_start, x_end], [y_start, y_end], color='black', linestyle='-', linewidth=1)

# Fungsi utama untuk menggambar lapangan
def draw_field(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    draw_home_zone(ax)
    draw_camp_zones(ax)
    draw_red_gaps(ax)
    draw_disaster_zones(ax)
    draw_logistic_boxes(ax)
    draw_connectors(ax)

# Koordinat objek di disaster zone
disaster_objects = [
    (50, 53),   # Kotak di Disaster Zone Yellow
    (37.5, 45), # Kotak di Disaster Zone Green
    (62.5, 45)  # Kotak di Disaster Zone Cyan
]

# Koordinat objek di logistic zone
logistic_objects = [
    (3, 23),   # Kotak kiri atas - Logistic Zone Cyan
    (3, 50),   # Kotak kiri tengah - Logistic Zone Yellow
    (3, 41),   # Kotak kiri bawah - Logistic Zone Green
    (97, 32),  # Kotak kanan atas - Logistic Zone Yellow
    (97, 23),  # Kotak kanan tengah - Logistic Zone Green
    (97, 41)   # Kotak kanan bawah - Logistic Zone Cyan
]

# Fungsi untuk menggambar objek di zona tertentu
def draw_point_pickup(ax, objects, radius=1, color='black'):
    for x, y in objects:
        ax.add_patch(patches.Circle((x, y), radius, color=color))

# Fungsi utama untuk menggambar objek di disaster dan logistic zones
def draw_objects(ax):
    # Menggambar objek di disaster zone dan logistic zones
    draw_point_pickup(ax, disaster_objects)  # Gambar objek di disaster zone
    draw_point_pickup(ax, logistic_objects)   # Gambar objek di logistic zone

# Fungsi untuk memperbarui posisi robot dan objek
def update(frame):
    global elapsed_time, saved_objects

    # Update posisi robot
    if frame < len(robot_path):
        x_start, y_start = robot_path[frame]
        robot.center = (x_start, y_start)

        # Update posisi objek yang mengikuti robot
        if saved_objects:
            for i, (color, obj) in enumerate(saved_objects):
                obj.center = (x_start - 3 * (i + 1), y_start)

        # Cek jika robot tiba di zona pengambilan objek
        check_pickup_objects(x_start, y_start)

        # Cek jika robot tiba di Camp Zone untuk meletakkan objek
        check_drop_objects(x_start, y_start)

    # Cek jika robot tiba di HOME
    check_arrival_home(frame)

    # Update timer visual
    timer_text.set_text(f'Timer: {elapsed_time} s')
    
    return [robot] + [obj for _, obj in saved_objects] + [timer_text]

def check_pickup_objects(x_start, y_start):
    for color, coords in pickup_coordinates.items():
        if coords == (x_start, y_start):
            if color not in [obj[0] for obj in saved_objects]:
                obj_color = object_colors[color]
                zone_type = 'disaster zone' if color in ['cyan', 'green', 'yellow'] else 'logistic zone'
                saved_objects.append((color, plt.Circle((x_start, y_start), 1, color=obj_color)))
                ax.add_patch(saved_objects[-1][1])
                print(f"Objek berwarna {obj_color} pada {zone_type} diselamatkan")

def check_drop_objects(x_start, y_start):
    for i in range(len(saved_objects) - 1, -1, -1):
        color, obj = saved_objects[i]
        base_color = color.split('_')[0]
        camp_zone_coords = camp_zones_arrival.get(base_color, None)

        if camp_zone_coords is not None:
            x_camp, y_camp = camp_zone_coords
            if x_camp - 5 <= x_start <= x_camp + 5 and y_camp - 5 <= y_start <= y_camp + 5:
                obj.remove()
                print(f"Objek berwarna {base_color} diletakkan di Camp Zone dan menghilang.")
                saved_objects.pop(i)

def check_arrival_home(frame):
    global robot_arrived_home, elapsed_time, stop_timer_countdown
    
    # Cek jika robot tiba di HOME
    if frame == len(robot_path) - 1 and not robot_arrived_home:
        robot_arrived_home = True
        print(f"Robot tiba di HOME pada {elapsed_time} detik. Menunggu 5 detik sebelum menghentikan timer...")
        stop_timer_countdown = 5

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
            # plt.close()  # Menutup jendela visualisasi
    else:
        elapsed_time += 1

# Inisialisasi variabel global
robot_path = [
    # mulai dari home ke disaster zone terdekat cyan
    (50, 10), (50, 23), (80, 23), (80, 32), (62.5, 32), (62.5, 45),
    # lanjut dari disaster zone cyan ke camp zone cyan
    (62.5, 32), (50, 32), (50, 45), (60, 52.5), (50, 63), (50, 95),
    
]

robot_arrived_home = False
elapsed_time = 0
stop_timer_countdown = None
saved_objects = []

# Warna objek tetap sama, hanya zona yang berubah
object_colors = {
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

# Kordinat objek dari Disaster Zone dan Logistic Zone
pickup_coordinates = {
    'cyan': (62.5, 45),     # Disaster Zone Cyan
    'green': (35, 47.5),    # Disaster Zone Green
    'yellow': (50, 62),     # Disaster Zone Yellow
    'cyan_left': (4, 40),   # Logistic Zone Kiri Cyan
    'yellow_left': (4, 30), # Logistic Zone Kiri Yellow
    'green_left': (4, 20),  # Logistic Zone Kiri Green
    'cyan_right': (96, 20), # Logistic Zone Kanan Cyan
    'green_right': (96, 40),# Logistic Zone Kanan Green
    'yellow_right': (96, 50),# Logistic Zone Kanan Yellow
}

# kordinat objek diletakkan di Camp Zone
camp_zones_arrival = {
    'yellow': (15, 90),
    'green': (85, 90),
    'cyan': (50, 90)
}

# Setup visualisasi simulasi
fig, ax = plt.subplots(figsize=(8, 8))

# Menggambar robot sebagai lingkaran
robot = patches.Circle((50, 10), 2, color='blue')
ax.add_patch(robot)

# Menambahkan judul dan timer
ax.set_title("Simulasi Lapangan 2", fontsize=14, fontweight='bold')
timer_text = ax.text(70, 95, 'Timer: 0 s', horizontalalignment='center', fontsize=12)

draw_field(ax)
draw_objects(ax)
ani = FuncAnimation(fig, update, frames=len(robot_path)+ 5, interval=1000, blit=True, repeat=False)
plt.show()