import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from collections import deque

# Fungsi untuk menggambar lapangan
def gambar_lapangan():
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Mengatur batas grid
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    # Area HOME
    area_home = patches.Rectangle((45, 5), 10, 10, linewidth=2, edgecolor='black', facecolor='white')
    ax.add_patch(area_home)
    ax.text(50, 10, 'HOME', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')
    
    # Kotak berwarna di atas (mewakili camp atau target)
    kotak_atas = {'cyan': (50, 85), 'yellow': (85, 85), 'green': (15, 85)}
    for warna, (x, y) in kotak_atas.items():
        kotak = patches.Rectangle((x-5, y-5), 10, 10, linewidth=2, edgecolor='black', facecolor=warna)
        ax.add_patch(kotak)
    
    # Garis merah horizontal yang terbelah
    garis_merah_kiri = patches.Rectangle((10, 60), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(garis_merah_kiri)
    
    garis_merah_kanan = patches.Rectangle((60, 60), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(garis_merah_kanan)
    
    ax.text(50, 62, 'Celah', horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    
    # Tiga kotak membentuk segitiga sama sisi di bagian tengah
    x_center = 50
    y_center = 40
    ax.add_patch(patches.Rectangle((x_center - 5, y_center), 10, 10, linewidth=2, edgecolor='black', facecolor='yellow'))
    
    ax.add_patch(patches.Rectangle((x_center - 15 - 5, y_center - 5), 10, 10, linewidth=2, edgecolor='black', facecolor='green'))
    
    ax.add_patch(patches.Rectangle((x_center + 15 - 5, y_center - 5), 10, 10, linewidth=2, edgecolor='black', facecolor='cyan'))
    
    # Kotak merah dan kuning berada di samping kanan dan kiri secara vertikal
    ax.add_patch(patches.Rectangle((5 - 5, 50 - 5), 10, 10, linewidth=2, edgecolor='black', facecolor='red'))
    ax.add_patch(patches.Rectangle((95 - 5, 50 - 5), 10, 10, linewidth=2, edgecolor='black', facecolor='yellow'))
    
    # Menggambar konektor garis hitam dari HOME ke kotak merah dan kuning
    konektor = [
        # Konektor HOME ke titik cabang
        ((50, 10), (50, 20)),  # Vertikal dari HOME ke titik cabang
        
        # Konektor dari titik cabang ke kotak merah
        ((50, 20), (5, 20)),   # Horizontal dari titik cabang ke kotak merah
        ((5, 20), (5, 50)),    # Vertikal dari titik cabang ke kotak merah
        
        # Konektor dari titik cabang ke kotak kuning
        ((50, 20), (95, 20)),  # Horizontal dari titik cabang ke kotak kuning
        ((95, 20), (95, 50)),  # Vertikal dari titik cabang ke kotak kuning
        
        # Konektor horizontal dari titik cabang ke kotak hijau
        ((50, 20), (15, 20)),  # Horizontal dari titik cabang ke kotak hijau
        
        # Konektor horizontal dari titik cabang ke kotak cyan
        ((50, 20), (85, 20)),  # Horizontal dari titik cabang ke kotak cyan
    ]
    
    for (x_start, y_start), (x_end, y_end) in konektor:
        ax.plot([x_start, x_end], [y_start, y_end], color='black', linestyle='-', linewidth=1)
    
    # Menambahkan konektor horizontal dari percabangan grid 40 ke kotak hijau
    ax.plot([35, 5], [40, 40], color='black', linestyle='-', linewidth=1)
    
    # Menambahkan konektor horizontal dari percabangan grid 40 ke kotak cyan
    ax.plot([65, 95], [40, 40], color='black', linestyle='-', linewidth=1)
    
    # Menonaktifkan grid
    ax.grid(False)

    # Judul dan rasio aspek
    ax.set_title("Simulasi Lapangan Robot", fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    
    return fig, ax

# Fungsi untuk memperbarui posisi robot
def gambar_robot(ax, robot_patch, x, y):
    robot_patch.center = (x, y)
    plt.draw()

# Fungsi BFS untuk menemukan jalur terpendek
def bfs(start, goal, graph):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        (vertex, path) = queue.popleft()
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Fungsi untuk menggerakkan robot mengikuti rute
def gerak_robot(ax, robot_patch, rute):
    for (x, y) in rute:
        gambar_robot(ax, robot_patch, x, y)
        plt.pause(0.1)

# Fungsi simulasi utama
def simulasi():
    fig, ax = gambar_lapangan()
    
    # Membuat robot
    robot_patch = patches.Circle((50, 10), 3, linewidth=1, edgecolor='black', facecolor='orange')
    ax.add_patch(robot_patch)
    plt.draw()

    # Definisikan graf (node dan edge)
    graph = {
        (50, 10): [(50, 20)],
        (50, 20): [(50, 10), (5, 20), (95, 20), (15, 20), (85, 20)],
        (5, 20): [(50, 20), (5, 50)],
        (95, 20): [(50, 20), (95, 50)],
        (15, 20): [(50, 20), (15, 50)],
        (85, 20): [(50, 20), (85, 50)],
        (5, 50): [(5, 20), (5, 50)],
        (95, 50): [(95, 20), (95, 50)],
        (15, 50): [(15, 20), (15, 50)],
        (85, 50): [(85, 20), (85, 50)],
        (5, 50): [(5, 50)],
        (15, 50): [(15, 50)],
        (25, 85): [(25, 50)],
        (25, 50): [(25, 85), (85, 50), (15, 50)],
        (85, 50): [(25, 50), (85, 85)],
        (85, 85): [(85, 50), (25, 30)],
        (25, 30): [(85, 85), (25, 85)],
        (25, 85): [(25, 30), (15, 30)],
        (15, 30): [(25, 85), (15, 85)],
        (15, 85): [(15, 30), (85, 30)],
        (85, 30): [(15, 85), (85, 85)],
        (50, 10): [(50, 20)],
    }

    # Tentukan urutan pengambilan kotak
    rute_kotak = [
        (50, 10), (25, 50), (25, 85), # Ambil Kotak Cyan
        (25, 85), (15, 50), (15, 85), # Ambil Kotak Kuning
        (15, 85), (85, 50), (85, 85), # Ambil Kotak Hijau
        (85, 85), (25, 30), (25, 85), # Ambil Logistik Cyan
        (25, 85), (15, 30), (15, 85), # Ambil Logistik Kuning
        (15, 85), (85, 30), (85, 85), # Ambil Logistik Hijau
        (85, 85), (50, 10)            # Kembali ke HOME
    ]

    # Gerakkan robot sesuai rute
    gerak_robot(ax, robot_patch, rute_kotak)
    
    # Tunggu selama 5 detik
    plt.pause(5)
    
    plt.show()

# Menjalankan simulasi
simulasi()
