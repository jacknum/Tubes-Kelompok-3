def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def daftar_film():
    print("Daftar Film Yang Tayang: ")
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
    else:
        print("Film tidak valid.")
    else:
        print("Film tidak ada.")

def pesan_tiket(film, jam, hitung_kursi, kursi, pilihan_kursi):
    print("Tempat Duduk yang Tersedia:")
    print(kursi)
    n = 0
    while n < (hitung_kursi):
        pilih = input("Masukkan Nomor Kursi! : ")
        if pilih in kursi:
            kursi.remove(pilih)
            pilihan_kursi.append(pilih)
            n += 1
        elif pilih not in kursi:
            print("Kursi telah dipesan")
    print("Kursi berhasil dipesan")

    nama_pengunjung = input("Masukkan nama Anda: ")
    
    print("Transaksi berhasil!")
    print(f"Atas nama: {nama_pengunjung}")
    print(f"Film: {film}")
    print(f"Jam Tayang: {jam}")
    print("Kursi: ", end="")
    print(*pilihan_kursi, sep=", ")
    print("Total Pembayaran: Rp.", hitung_kursi * ambil_harga_film(film))

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
        print("\nSelamat Datang di Gabut Movie")
        daftar_film()
        pilihan_film = input("Pilih Nomor Film : ")
        lihat_waktu_tayang(pilihan_film)

        pilihan_waktu = input("Pilih Nomor Jam Tayang : ")
        hitung_kursi = int(input("Berapa Kursi Yang Ingin Anda Pesan? : "))
        while True:
            if pilihan_film == "1":
                pesan_tiket(pilihan_film, pilihan_waktu, hitung_kursi, kursi1)
                break
            elif pilihan_film == "1":
                pesan_tiket(pilihan_film, pilihan_waktu, hitung_kursi, kursi2)
                break
            elif pilihan_film == "1":
                pesan_tiket(pilihan_film, pilihan_waktu, hitung_kursi, kursi3)
                break
            elif pilihan_film == "1":
                pesan_tiket(pilihan_film, pilihan_waktu, hitung_kursi, kursi4)
                break
            else:
                print("Pilihan Anda Tidak Valid")
                continue