import random
import time

# Terminal ekranı boyutları
WIDTH = 80
HEIGHT = 40

# Boş bir kanvas oluştur
canvas = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Karakterler
characters = ['0', '1']

# Matris döngüsü
while True:
    # Matris etkisi oluştur
    for i in range(HEIGHT):
        for j in range(WIDTH):
            canvas[i][j] = random.choice(characters)

    # Kanvası yazdır
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(canvas[i][j], end='')
        print()
    
    # 50ms bekle
    time.sleep(0.05)

    # Ekranı temizle
    print('\033[H\033[J', end='')
