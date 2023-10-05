class Contact:
    # Mendefinisilkan nama dan nomor
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_name(self):
        # Lengkapi metode ini untuk mengembalikan nama kontak
        return self.name

    def get_phone(self):
        # Lengkapi metode ini untuk mengembalikan nomor telepon kontak
        return self.phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


class ContactList:
    def __init__(self):
        # Definisikan atribut/variabel daftar kontak dari fungsi init sebagai List.
        self.contacts = []

    def add_contact(self, contact):
        # Lengkapi metode ini untuk menambahkan kontak ke dalam daftar kontak
        self.contacts.append(contact)

    def delete_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.get_name() == name:
                self.contacts.remove(contact)
                found = True
                print(f"Kontak {name} sudah dihapus.")
                break
        if not found:
            print(f"Kontak dengan nama {name} tidak ditemukan.")

    def search_contact(self, name):
        found_contacts = []

        for contact in self.contacts:
            if contact.get_name() == name:
                found_contacts.append(contact)

        if found_contacts:
            print(f"Kontak dengan nama {name} ditemukan:")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"Kontak dengan nama {name} tidak ditemukan.")

    def display_contacts(self):
        if not self.contacts:
            print("Daftar kontak kosong.")
        else:
            print("Daftar kontak:")
            for contact in self.contacts:
                print(
                    f"Nama: {contact.get_name()}, Nomor Telepon: {contact.get_phone()}")


# Membuat objek daftar kontak
contact_list = ContactList()

while True:
    print("\nMenu:")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Kontak")
    print("5. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        name = input("Masukkan nama kontak: ")
        phone = input("Masukkan nomor telepon kontak: ")
        contact = Contact(name, phone)
        contact_list.add_contact(contact)
        print(f"Kontak {name} telah ditambahkan.")

    elif choice == "2":
        name = input("Masukkan nama kontak yang akan dihapus: ")
        # Panggil metode untuk menghapus kontak berdasarkan nama
        contact_list.delete_contact(name)

    elif choice == "3":
        name = input("Masukkan nama kontak yang akan dicari: ")
        # Panggil metode untuk mencari kontak berdasarkan nama
        contact_list.search_contact(name)

    elif choice == "4":
        # Panggil metode untuk menampilkan semua kontak
        contact_list.display_contacts()

    elif choice == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
