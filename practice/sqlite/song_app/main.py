from song import Music

# Örnek kullanım
music = Music()
while True:
    print("\n1. Şarkı Ekle\n2. Şarkı Sil\n3. Toplam Şarkı Süresini Hesapla\n4. Çıkış")
    choice = int(input("Seçiminizi yapın: "))

    if choice == 1:
        music.add_music()
    elif choice == 2:
        Music.delete_music()
    elif choice == 3:
        Music.calculate_total_duration()
    elif choice == 4:
        break
    else:
        print("Geçersiz seçim.")
