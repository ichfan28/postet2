from prettytable import PrettyTable

produk_tembakau = []
pembeli_tembakau = []
id_produk_tembakau = 1

def tambah_produk_tembakau():
    global id_produk_tembakau
    nama_produk = input("Masukkan nama tembakau: ")
    harga_produk = float(input("Masukkan harga tembakau: "))
    produk_tembakau.append({"ID": id_produk_tembakau, "Nama": nama_produk, "Harga": harga_produk})
    id_produk_tembakau += 1
    print("Tembakau telah ditambahkan.")

def tampilkan_produk_tembakau():
    if not produk_tembakau:
        print("Tidak ada tembakau yang tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Tembakau", "Harga"]
        for p in produk_tembakau:
            table.add_row([p["ID"], p["Nama"], p["Harga"]])
        print(table)

def transaksi_pembeli_tembakau():
    tampilkan_produk_tembakau()
    if not produk_tembakau:
        return
    produk_id = int(input("Pilih ID tembakau yang ingin dibeli (0 untuk keluar): "))
    if produk_id == 0:
        return
    jumlah = int(input("Masukkan jumlah tembakau yang ingin dibeli: "))
    for p in produk_tembakau:
        if p["ID"] == produk_id:
            total_harga = p["Harga"] * jumlah
            pembeli_tembakau.append({"Tembakau": p["Nama"], "Jumlah": jumlah, "Total Harga": total_harga})
            print("Transaksi berhasil.")
            return
    print("Tembakau dengan ID tersebut tidak ditemukan.")

def riwayat_pembeli_tembakau():
    if not pembeli_tembakau:
        print("Belum ada transaksi.")
    else:
        table = PrettyTable()
        table.field_names = ["Tembakau", "Jumlah", "Total Harga"]
        for transaksi in pembeli_tembakau:
            table.add_row([transaksi["Tembakau"], transaksi["Jumlah"], transaksi["Total Harga"]])
        print(table)

def main_tembakau():
    while True:
        print("\nSelamat datang di TOKO PENJUALAN TEMBAKAU")
        print("Menu:")
        print("1. Admin")
        print("2. Pembeli")
        print("3. Keluar")
        pilihan = input("Pilih peran (1/2/3): ")
        
        if pilihan == "1":
            print("\nMenu Admin:")
            print("1. Tambah Tembakau")
            print("2. Lihat Tembakau")
            print("3. Kembali")
            admin_pilihan = input("Pilih tindakan (1/2/3): ")
            if admin_pilihan == "1":
                tambah_produk_tembakau()
            elif admin_pilihan == "2":
                tampilkan_produk_tembakau()
            elif admin_pilihan == "3":
                continue
            else:
                print("Pilihan tidak valid.")

        elif pilihan == "2":
            print("\nMenu Pembeli:")
            print("1. Beli Tembakau")
            print("2. Lihat Riwayat Transaksi")
            print("3. Kembali")
            pembeli_pilihan = input("Pilih tindakan (1/2/3): ")
            if pembeli_pilihan == "1":
                transaksi_pembeli_tembakau()
            elif pembeli_pilihan == "2":
                riwayat_pembeli_tembakau()
            elif pembeli_pilihan == "3":
                continue
            else:
                print("Pilihan tidak valid.")

        elif pilihan == "3":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_tembakau()
