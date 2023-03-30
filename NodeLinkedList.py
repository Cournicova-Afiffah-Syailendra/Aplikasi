class Node:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add_data(self):
        name = input("Masukkan nama siswa: ")
        year = input("Masukkan tahun lulus SMP: ")
        new_node = Node(name, year)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        print()
        print("Data berhasil ditambahkan\n")
    
    def delete_data(self):
        if self.is_empty():
            print("Anda belum mengisikan data\n")
        else:
            name = input("Masukkan nama siswa yang ingin dihapus: ")
            if self.head.name == name:
                self.head = self.head.next
                print()
                print("Data berhasil dihapus\n")
            else:
                current = self.head
                while current.next != None:
                    if current.next.name == name:
                        current.next = current.next.next
                        print()
                        print("Data berhasil dihapus\n")
                        break
                    current = current.next
                else:
                    print()
                    print("Data tidak ditemukan\n")
    
    def insert_data(self):
        if self.is_empty():
            print("Anda belum mengisikan data\n")
        else:
            name = input("Masukkan nama siswa yang ingin disisipkan: ")
            year = input("Masukkan tahun lulus siswa yang ingin disisipkan: ")
            new_node = Node(name, year)
            position = int(input("Masukkan posisi sisipan: "))
            if position == 1:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for i in range(position-2):
                    if current.next != None:
                        current = current.next
                    else:
                        print()
                        print("Posisi sisipan tidak valid\n")
                        return
                new_node.next = current.next
                current.next = new_node
            print()
            print("Data berhasil disisipkan\n")
    
    def display_data(self):
        if self.is_empty():
            print("Anda belum mengisikan data\n")
        else:
            current = self.head
            print("-------------------------------------------------")
            print("|\t    Nama\t\t|  Tahun Lulus  |")
            print("-------------------------------------------------")

            while current != None:
                print("|" + current.name + "\t|  " + "   " + current.year + "      |")
                current = current.next
                print("-------------------------------------------------")
            print("")
            
linked_list = LinkedList()

while True:
    print("--------------------------------------")
    print("=== Aplikasi Pendaftaran Siswa SMA ===")
    print("--------------------------------------")
    print("| 1. Tambah Data                     |")
    print("| 2. Hapus Data                      |")
    print("| 3. Sisipkan Data                   |") 
    print("| 4. Tampilkan Data                  |")
    print("| 5. Keluar                          |")
    print("======================================")

    

    try:
        choice = int(input("Masukkan pilihan: "))
        print("")

        if choice == 1:
            linked_list.add_data()
        elif choice == 2:
            linked_list.delete_data()
        elif choice == 3:
            linked_list.insert_data()
        elif choice == 4:
            linked_list.display_data()
        elif choice == 5:
            break
        else:
            print("Pilihan tidak valid\n")
    except ValueError:
        print("")
        print("Input harus berupa angka antara 1-5")
        print("")

