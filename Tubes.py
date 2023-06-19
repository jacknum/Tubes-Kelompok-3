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
    waktu_tayang = {
        "1": ["08:00", "23:00", "16:00"],
        "2": ["14:00", "10:00", "20:00"],
        "3": ["21:00", "15:00", "09:00"],
        "4": ["13:00", "19:00", "11:00"]
    }

    waktu = waktu_tayang.get(film)
    if waktu is not None:
        insertion_sort(waktu)
    print("Jam Tayang: ")
    for i, jam in enumerate(waktu):
        print(f"{i + 1}. {jam}")
    else:
        print("Film tidak ada.")

def book_tickets(film, jam, hitung_kursi):
    limit_kursi = 30
    tempat_duduk = list(range(1, limit_kursi + 1))
    kursi_pilihan = []

    if hitung_kursi > limit_kursi:
        print("Jumlah kursi melebihi batas.")
        return

    print("Tempat Duduk yang Tersedia:")
    print(tempat_duduk)

    for _ in range(hitung_kursi):
        kursi_pilihan_duduk = int(input("Pilih nomor kursi: "))

        if kursi_pilihan_duduk not in tempat_duduk:
            print("Kursi tidak tersedia.")
            return
        
        tempat_duduk.remove(kursi_pilihan_duduk)
        kursi_pilihan.append(kursi_pilihan_duduk)

    nama_penggunjung = input("Masukkan nama Anda: ")
    
