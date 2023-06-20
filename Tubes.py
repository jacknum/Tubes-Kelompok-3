def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def daftar_film():
    print("\nDaftar Film:")
    print("1. Sewu Dino (Rp. 30.000)")
    print("2. The Little Mermaid (Rp. 35.000)")
    print("3. The Big 4 (Rp. 40.000)")
    print("4. Hati Suhita (Rp. 30.000)")
    
def lihat_waktu_tayang(film):
    waktu = jam_tayang.get(film)
    if waktu is not None:
        insertion_sort(waktu)
        print("Jam Tayang:")
        for i, jam in enumerate(waktu):
            print(f"{i + 1}. {jam}")
        return True
    else:
        print("Film tidak valid.")
        return False
    
def pesan_tiket(film, jam, hitung_kursi, kursi_terpesan, pilihan_kursi):
    print("Tempat Duduk yang Tersedia:")
    for row in kursi:
        for seat in row:
            if seat in kursi_terpesan:
                print("X", end=" ") 
            else:
                print(seat, end=" ")
        print()
        
    pesanan_kursi = []
    for _ in range(hitung_kursi):
        while True:
            kursi_pilihan = int(input("Pilih kursi (masukkan nomor kursi): "))
            if kursi_pilihan in kursi_terpesan:
                print("Kursi telah dipilih dan dipesan.")
            elif kursi_pilihan < 1 or kursi_pilihan > len(kursi) * len(kursi[0]):
                print("Kursi tidak valid.")
            else:
                kursi_terpesan.append(kursi_pilihan)  # Menambahkan kursi yang terpesan
                pesanan_kursi.append(kursi_pilihan)
                break
            
    if len(pesanan_kursi) == hitung_kursi:
        pilihan_kursi.extend(pesanan_kursi)  # Menambahkan pesanan kursi ke dalam pilihan_kursi
        nama_pengunjung = input("Masukkan nama Anda: ")
        total_harga = hitung_kursi * ambil_harga_film(film)
        if hitung_kursi > 5:
            diskon = total_harga * 0.05  # Menghitung jumlah diskon (5% dari total harga)
            total_harga -= diskon  # Mengurangi jumlah diskon dari total harga
        print("\nTransaksi berhasil!")
        print(f"Atas nama: {nama_pengunjung}")
        print(f"Film: {film}")
        print(f"Jam Tayang: {jam}")
        print("Kursi: ", end="")
        print(*pilihan_kursi, sep=", ")
        print("Total Pembayaran: Rp.", total_harga)
    else:
        print("Jumlah kursi yang dipesan tidak sesuai dengan jumlah tiket.")
        return False
    
def ambil_harga_film(film):
    harga_film = {
        "1": 30000,
        "2": 35000,
        "3": 40000,
        "4": 30000
    }
    return harga_film.get(film, 0)

def main():
    while True:
        print("\n<======== Selamat Datang Di Gabut Chinema ========>")
        daftar_film()
        pilihan_film = input("Pilih nomor film: ")
        
        if lihat_waktu_tayang(pilihan_film):
            jam_choice = input("Pilih jam tayang: ")
            hitung_kursi = int(input("Berapa kursi yang Anda butuhkan? "))
            
            if pilihan_film in jam_tayang and jam_choice in jam_tayang[pilihan_film]:
                if pesan_tiket(pilihan_film, jam_choice, hitung_kursi, kursi_terpesan, pilihan_kursi):
                    break
            else:
                print("Pilihan film atau jam tayang tidak valid.")
        else:
            print("Pilihan film tidak valid.")
            
        restart = input("Apakah Anda ingin melanjutkan (y/n)? ")
        if restart.lower() != "y":
            print("<========Terima Kasih telah memesan. Happy Watching========>")
            break
        
jam_tayang = {
    "1": ["08:00", "16:00", "20:00"],
    "2": ["10:00", "13:00", "20:00"],
    "3": ["22:00", "15:00", "09:00"],
    "4": ["08:00", "20:00"]
}
kursi = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
]
pilihan_kursi = []
kursi_terpesan = []

main()
