# Daftar produk dan harga
produk = {"Piatos": 10000, "Kacang Kulit": 15000, "Coklat": 20000, "Oreo": 8000}

# Diskon berdasarkan jenis membershipBud
diskon = {"Silver": 0.05, "Gold": 0.10, "Platinum": 0.15}
print("Selamat Datang di Toko Sembako Surya")
namapelanggan = (input("Nama Pelanggan: "))

# Meminta pengguna untuk memilih jenis membership
print("Pilihan Membership:")
for index, membership in enumerate(diskon.keys(), start=1):
    print(f"{index}. {membership}")

try:
    pilihan_membership = int(input("Pilih jenis membership (masukkan nomor membership): "))
    if 1 <= pilihan_membership <= len(diskon):
        jenis_membership = list(diskon.keys())[pilihan_membership - 1]
        persentase_diskon = diskon[jenis_membership]
    else:
        print("Pilihan membership tidak valid.")
except ValueError:
    print("Masukan tidak valid. Harap masukkan nomor membership yang sesuai.")

banyakbelanja = int(input("Mau Belanja berapa jenis barang: "))
keranjang = [0 for i in range(banyakbelanja)]

for i in range(banyakbelanja):
    print("===============================")
    print(f"{namapelanggan}  ({membership})")
    print("===============================")
    # Menampilkan daftar produk
    print("Daftar Produk:")
    for index, (nama_produk, harga) in enumerate(produk.items(), start=1):
        print(f"{index}. {nama_produk}  IDR.{harga}")

    # Meminta pengguna untuk memilih produk
    try:
        
        pilihan_produk = int(input("Pilih produk (masukkan nomor produk): "))
        keranjang[i]= pilihan_produk
        if 1 <= pilihan_produk <= len(produk):
            nama_produk = list(produk.keys())[pilihan_produk - 1]
            harga_produk = produk[nama_produk]
        else:
            print("Pilihan produk tidak valid.")
    except ValueError:
        print("Masukan tidak valid. Harap masukkan nomor produk yang sesuai.")


total_harga=0

print("===============================")
print(f"{namapelanggan}  ({membership})")
print("===============================")
for i in range(banyakbelanja):
    nama_produk = list(produk.keys())[keranjang[i] - 1]
    harga_produk = produk[nama_produk]
    
    # Menghitung total belanjaan
    total_harga += harga_produk
    total_diskon = total_harga * persentase_diskon
    total_belanjaan = total_harga - total_diskon

    # Menampilkan total belanjaan kepada pengguna
    print(f"{i+1}. {nama_produk} harga IDR.{harga_produk}.")
# Menghitung total belanjaan
print("===============================")
total_diskon = total_harga * persentase_diskon
total_belanjaan = total_harga - total_diskon
print(f"Total belanjaan IDR{total_harga:.2f}")
print(f"Jenis membership: {jenis_membership} (Diskon {persentase_diskon * 100}%).")
print(f"Total belanjaan setelah diskon: IDR.{total_belanjaan:.2f}")
