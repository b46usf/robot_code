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
    kotak_atas = {'cyan': (50, 95), 'yellow': (85, 95), 'green': (15, 95)}
    for warna, (x, y) in kotak_atas.items():
        kotak = patches.Rectangle((x-5, y-5), 10, 10, linewidth=2, edgecolor='black', facecolor=warna)
        ax.add_patch(kotak)
    
    # Garis merah horizontal yang terbelah
    garis_merah_kiri = patches.Rectangle((10, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(garis_merah_kiri)
    
    garis_merah_kanan = patches.Rectangle((60, 70), 30, 5, linewidth=2, edgecolor='black', facecolor='red')
    ax.add_patch(garis_merah_kanan)
    
    ax.text(50, 72, 'Celah', horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    
    # Tiga kotak membentuk segitiga sama sisi di bagian tengah
    x_center = 50
    y_center = 50
    ax.add_patch(patches.Rectangle((x_center -3, y_center), 7, 7, linewidth=2, edgecolor='black', facecolor='yellow'))
    
    ax.add_patch(patches.Rectangle((x_center - 10 - 5, y_center -8), 7, 7, linewidth=2, edgecolor='black', facecolor='cyan'))
    
    ax.add_patch(patches.Rectangle((x_center + 14 - 5, y_center -8), 7, 7, linewidth=2, edgecolor='black', facecolor='green'))
    
    # Kotak merah dan kuning berada di samping kanan dan kiri secara vertikal
    ax.add_patch(patches.Rectangle((5 - 5, 50 - 3), 6, 6, linewidth=2, edgecolor='black', facecolor='yellow'))
    ax.add_patch(patches.Rectangle((94, 50 - 3), 6, 6, linewidth=2, edgecolor='black', facecolor='red'))
    ax.add_patch(patches.Rectangle((5 - 5, 50 - 12), 6, 6, linewidth=2, edgecolor='black', facecolor='green'))
    ax.add_patch(patches.Rectangle((94, 50 - 12), 6, 6, linewidth=2, edgecolor='black', facecolor='cyan'))
    ax.add_patch(patches.Rectangle((5 - 5, 50 - 21), 6, 6, linewidth=2, edgecolor='black', facecolor='red'))
    ax.add_patch(patches.Rectangle((94, 50 - 21), 6, 6, linewidth=2, edgecolor='black', facecolor='yellow'))
    ax.add_patch(patches.Rectangle((5 - 5, 50 - 30), 6, 6, linewidth=2, edgecolor='black', facecolor='cyan'))
    ax.add_patch(patches.Rectangle((94, 50 - 30), 6, 6, linewidth=2, edgecolor='black', facecolor='green'))
    
    # Menggambar konektor garis hitam dari HOME ke kotak merah dan kuning
    konektor = [
        # Konektor HOME ke titik cabang
        ((50, 10), (50, 23)),  # Vertikal dari HOME ke titik cabang
        
        # konektor DARI CABANG AWAL HOME BELOK KANAN
        ((50, 23), (94, 23)),  # HORIZONTAL BELOK KANAN
        
        # konektor DARI PERTIGAAN SATU BELOK KIRI
        ((80, 23), (80, 41)),  # VERTIKAL BELOK KIRI
       
        # konektor DARI PERTIGAAN DUA BELOK KIRI
        ((94, 32), (20, 32)),  # HORIZONTAL BELOK KIRI
        
        # konektor DARI PERTIGAAN TIGA BELOK KANAN
        ((50, 32), (50, 50)),  # HORIZONTAL NAIK KEATAS
        
         # konektor DARI PERTIGAAN EMPAT BELOK KANAN
         ((50, 45), (60, 52.5)),  # DIAGONAL NAIK KEATAS
         
         # konektor DARI PERTIGAAN EMPAT BELOK KANAN
         ((50, 45), (40, 52.5)),  # DIAGONAL NAIK KEATAS
         
         # konektor DARI PERTIGAAN LIMA BELOK KIRI
         ((40, 52.5), (50, 63)),  # DIAGONAL NAIK KEATAS
         
         # konektor DARI PERTIGAAN LIMA BELOK KIRI
         ((60, 52.5), (50, 63)),  # DIAGONAL NAIK KEATAS
         
         # konektor DARI PERTIGAAN ENAM BELOK KANAN
         ((50, 63), (50, 90)),  # VERTIKAL NAIK KEATAS
         
        # konektor DARI PERTIGAAN TUJUH BELOK KANAN
         ((50, 86), (85, 86)),  # HORIZONTAL KE KANAN
         
         # konektor DARI PERTIGAAN DELAPAN BELOK KIRI
         ((85, 86), (85, 90)),  # VERTIKAL KE ATAS
         
         # konektor DARI PERTIGAAN SEMBILAN BELOK KANAN
         ((50, 79), (85, 79)),  # HORIZONTAL KE KANAN
         
          # konektor DARI PERTIGAAN SEPULUH BELOK KANAN
         ((85, 79), (85, 86)),  # VERTIKAL KE KIRI
         
         # konektor DARI PERTIGAAN SEBELAS BELOK KIRI
        ((38.5, 32), (38.5, 42)),  # VERTIKAL KE ATAS
        
        # konektor DARI PERTIGAAN DUA BELAS BELOK KANAN
        ((62.5, 32), (62.5, 42)),  # VERTIKAL KE ATAS
        
        # konektor DARI PERTIGAAN TUJUH BELOK KIRI
         ((15, 86), (85, 86)),  # HORIZONTAL KE KIRI
         
         # konektor DARI PERTIGAAN TIGA BELAS BELOK KIRI
         ((15, 79), (85, 79)),  # HORIZONTAL KE KIRI
         
         # konektor DARI PERTIGAAN EMPAT BELAS BELOK KIRI
         ((15, 79), (15, 90)),  # VERTIKAL KE BAWAH
         
          # konektor DARI PERTIGAAN LIMA BELAS BELOK KIRI
         ((80, 41), (94, 41)),  # VERTIKAL KE ATAS
         
          # konektor DARI PERAPATAN SATU BELOK KIRI
        ((20, 50), (20, 23)),  # BELOK KANAN KIRI
        
         # konektor DARI PERAPATAN DUA BELOK KANAN
        ((20, 23), (6, 23)),  # BELOK KANAN
        
        # konektor DARI PERTIGAAN ENAM BELAS BELOK KIRI
         ((20, 41), (6, 41)),  # HORIZONTAL KE KIRI
         
         # konektor DARI PERTIGAAN TUJUH BELAS BELOK KIRI
         ((20, 50), (6, 50)),  # HORIZONTAL KE KIRI
        
        # Konektor dari titik cabang ke kotak merah
        # ((50, 20), (5, 20)),   # Horizontal dari titik cabang ke kotak merah
        # ((5, 20), (5, 50)),    # Vertikal dari titik cabang ke kotak merah
        
        # Konektor dari titik cabang ke kotak kuning
        # ((50, 20), (95, 20)),  # Horizontal dari titik cabang ke kotak kuning
        # ((95, 20), (95, 50)),  # Vertikal dari titik cabang ke kotak kuning
        
        # Konektor horizontal dari titik cabang ke kotak hijau
        # ((50, 20), (15, 20)),  # Horizontal dari titik cabang ke kotak hijau
        
        # Konektor horizontal dari titik cabang ke kotak cyan
        # ((50, 20), (85, 20)),  # Horizontal dari titik cabang ke kotak cyan
        
        # Konektor horizontal dari titik cabang ke kotak cyan
        # ((50, 20), (85, 20)),  # Horizontal dari titik cabang ke kotak cyan
    ]
    
    for (x_start, y_start), (x_end, y_end) in konektor:
        ax.plot([x_start, x_end], [y_start, y_end], color='black', linestyle='-', linewidth=1)
    
    # Menambahkan konektor horizontal dari percabangan grid 40 ke kotak hijau
    # ax.plot([35, 5], [40, 40], color='black', linestyle='-', linewidth=1)
    
    # Menambahkan konektor horizontal dari percabangan grid 40 ke kotak cyan
    # ax.plot([65, 95], [40, 40], color='black', linestyle='-', linewidth=1)
    
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
