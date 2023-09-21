class Musik:
    def __init__(self, name, genre, durasi, penyanyi):
        self.name = name
        self.genre = genre
        self.durasi = durasi
        self.penyanyi = penyanyi
        self.is_playing = False

    def play(self):
        if not self.is_playing:
            print(f"Memutar lagu: {self.name} - {self.penyanyi}")
            self.is_playing = True
        else:
            print("Lagu sedang diputar.")

    def stop(self):
        if self.is_playing:
            print("Menghentikan pemutaran lagu.")
            self.is_playing = False
        else:
            print("Lagu sudah berhenti.")

    def informasi(self):
        print(
            f"Informasi Lagu:\nJudul: {self.name}\nGenre: {self.genre}\nDurasi: {self.durasi} detik\nPenyanyi: {self.penyanyi}")


# Membuat objek-objek dari kelas Musik
lagu1 = Musik("Halo", "Pop", 240, "Adele")
lagu2 = Musik("Bohemian Rhapsody", "Rock", 354, "Queen")
lagu3 = Musik("Nemen", "Hiphop", 435, "Gilga")
lagu4 = Musik("Rungkad", "Dangdut", 345, "Happy Asmara")
# Memanggil metode untuk memutar lagu
lagu4.play()

# Memanggil metode untuk memberhentikan pemutaran lagu
lagu4.stop()

# Menampilkan informasi lagu
lagu4.informasi()
