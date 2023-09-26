class ContactList:
    def __init__(self):
        # Definisikan atribut/variabel daftar kontak dari fungsi init sebagai List.
        self.contacts = []

    def add_contact(self, contact):
        # Lengkapi metode ini untuk menambahkan kontak ke dalam daftar kontak
        self.contacts.append(contact)

    def delete_contact(self, name):
        # Lengkapi metode ini untuk menghapus kontak berdasarkan nama
        deleted = False
        for contact in self.contacts:
            if contact.get_name() == name:
                self.contacts.remove(contact)
                deleted = True
                print(f"Kontak {name} telah dihapus.")
                break
        if not deleted:
            print(f"Kontak dengan nama {name} tidak ditemukan.")

    def search_contact(self, name):
        # Lengkapi metode ini untuk mencari kontak berdasarkan nama
        found = False
        for contact in self.contacts:
            if contact.get_name() == name:
                print(f"Nama: {contact.get_name()}\nNomor Telepon: {contact.get_phone()}")
                found = True
                break
        if not found:
            print(f"Kontak dengan nama {name} tidak ditemukan.")

    def display_contacts(self):
        # Lengkapi metode ini untuk menampilkan semua kontak dalam daftar
        if not self.contacts:
            print("Daftar kontak kosong.")
        else:
            for contact in self.contacts:
                print(contact)

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
        contact = contact(name, phone)
        contact_list.add_contact(contact)
        print(f"Kontak {name} telah ditambahkan.")

    elif choice == "2":
        name = input("Masukkan nama kontak yang akan dihapus: ")
        contact_list.delete_contact(name)

    elif choice == "3":
        name = input("Masukkan nama kontak yang akan dicari: ")
        contact_list.search_contact(name)

    elif choice == "4":
        contact_list.display_contacts()

    elif choice == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
