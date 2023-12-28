class PengirimanLogistik:
    def __init__(self):
        self.tarif_per_kg = 5000  # Tarif per kilogram
        self.tarif_dimensi = 0.1  # Tarif per cm3
        self.biaya_per_jarak = 20000  # Biaya per jarak

    def hitung_jarak(self, tujuan_awal, tujuan_akhir):
        kota = [
            "Kota Surabaya",
            "Kota Blitar",
            "Kota Kediri",
            "Kota Madiun",
            "Kota Malang",
            "Kota Batu",
            "Kota Mojokerto",
            "Kota Pasuruan",
            "Kota Probolinggo"
        ]
        jarak = abs(kota.index(tujuan_awal) - kota.index(tujuan_akhir))
        return jarak

    def cek_tarif(self, tujuan_awal, tujuan_akhir, berat_barang, tinggi_barang, lebar_barang):
        volume_barang = tinggi_barang * lebar_barang * 1  # 1 di sini hanya contoh pengali volume
        biaya_berat = berat_barang * self.tarif_per_kg
        biaya_dimensi = volume_barang * self.tarif_dimensi
        total_biaya = biaya_berat + biaya_dimensi

        jarak = self.hitung_jarak(tujuan_awal, tujuan_akhir)
        biaya_jarak = jarak * self.biaya_per_jarak
        total_biaya += biaya_jarak

        print("\n--- Informasi Barang ---")
        print(f"Tujuan: {tujuan_awal} -> {tujuan_akhir}")
        print(f"Jarak: {jarak} kota")
        print(f"Biaya Jarak: Rp {biaya_jarak}")
        print("--- Rincian Biaya ---")
        print(f"Biaya Berat: Rp {biaya_berat}")
        print(f"Biaya Dimensi: Rp {biaya_dimensi}")
        print(f"Total Biaya: Rp {total_biaya}")

def cek_menu(kota):
    print("Daftar kota yang tersedia:")
    for idx, k in enumerate(kota, start=1):
        print(f"{idx}. {k}")

    try:
        idx_awal = int(input("Masukkan nomor kota tujuan awal: ")) - 1
        idx_akhir = int(input("Masukkan nomor kota tujuan akhir: ")) - 1

        tujuan_awal = kota[idx_awal]
        tujuan_akhir = kota[idx_akhir]

        berat_barang = float(input("Masukkan berat barang (kg): "))
        tinggi_barang = float(input("Masukkan tinggi barang (cm): "))
        lebar_barang = float(input("Masukkan lebar barang (cm): "))

        return tujuan_awal, tujuan_akhir, berat_barang, tinggi_barang, lebar_barang
    except (ValueError, IndexError):
        print("Input tidak valid. Pastikan Anda memasukkan nomor kota yang sesuai.")
        return None, None, None, None, None

def main():
    kota = [
        "Kota Surabaya",
        "Kota Blitar",
        "Kota Kediri",
        "Kota Madiun",
        "Kota Malang",
        "Kota Batu",
        "Kota Mojokerto",
        "Kota Pasuruan",
        "Kota Probolinggo"
    ]

    print("Selamat datang di Layanan Logistik")
    logistik = PengirimanLogistik()

    while True:
        print("\nPilih menu:")
        print("1. Cek Tarif")
        print("2. Keluar")
        pilihan = input("Masukkan pilihan (1/2): ")

        if pilihan == '1':
            tujuan_awal, tujuan_akhir, berat_barang, tinggi_barang, lebar_barang = cek_menu(kota)
            if tujuan_awal is not None:
                logistik.cek_tarif(tujuan_awal, tujuan_akhir, berat_barang, tinggi_barang, lebar_barang)
        elif pilihan == '2':
            print("Terima kasih telah menggunakan layanan logistik.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
