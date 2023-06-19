def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def daftar_film():
    print("Daftar Film: ")
    print("1. Sewu Dino (Rp. 30.000)")
    print("2. The Little Mermaid (Rp. 35.000)")
    print("3. The Big 4 (Rp. 40.000)")
    print("4. Hati Suhita (Rp. 30.000)")
    
def waktu_tayang(film):
    waktu_tayang = {
        "1": ["08:00", "16:00", "20:00"],
        "2": ["10:00", "13:00", "20:00"],
        "3": ["22:00", "15:00", "09:00"],
        "4": ["08:00", "20:00"]
    }
    
waktu = waktu_tayang.get(film)
if waktu is not None:
    insertion_sort(waktu)
    print("Jam Tayang: ")
    for i, time in enumerate(times):
       print(f"{i + 1}. {time}")
else:
    print("Film tidak ada.")

#coba aja
#tambah aja
