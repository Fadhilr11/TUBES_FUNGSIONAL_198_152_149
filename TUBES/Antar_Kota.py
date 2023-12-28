def hitung_jarak(tujuan_awal, tujuan_akhir, kota):
    return abs(kota.index(tujuan_awal) - kota.index(tujuan_akhir))

def hitung_harga(jarak, jumlah_penumpang):
    return jarak * 10000 * jumlah_penumpang

def buat_detail_perjalanan(titik_awal, titik_tujuan, tanggal_keberangkatan, jumlah_penumpang, nama_kereta, total_harga, metode_pembayaran):
    return f"Anda akan melakukan perjalanan dari {titik_awal} ke {titik_tujuan} pada tanggal {tanggal_keberangkatan} dengan {jumlah_penumpang} penumpang.\nKereta: {nama_kereta}\nTotal Harga tiket: Rp {total_harga}\nMetode Pembayaran: {metode_pembayaran}\nPembayaran Lunas"

def proses_pembayaran(total_harga):
    print("\nPilih metode pembayaran:")
    print("1. M-Banking")
    print("2. Go-Pay")
    print("3. OVO")

    metode_pembayaran = input("Masukkan pilihan metode pembayaran: ")

    if metode_pembayaran == "1":
        return "M-Banking"
    elif metode_pembayaran == "2":
        return "Go-Pay"
    elif metode_pembayaran == "3":
        return "OVO"
    else:
        print("Pilihan tidak valid.")
        return None

def antar_kota(kota, kereta):
    print("\nDaftar Kota:")
    for idx, k in enumerate(kota, 1):
        print(f"{idx}. {k}")

    pilihan_awal = int(input("Masukkan nomor kota asal: "))
    pilihan_tujuan = int(input("Masukkan nomor kota tujuan: "))

    if 1 <= pilihan_awal <= len(kota) and 1 <= pilihan_tujuan <= len(kota):
        titik_awal = kota[pilihan_awal - 1]
        titik_tujuan = kota[pilihan_tujuan - 1]
        tanggal_keberangkatan = input("Masukkan tanggal keberangkatan: ")
        jumlah_penumpang = int(input("Masukkan jumlah penumpang: "))

        jarak = hitung_jarak(titik_awal, titik_tujuan, kota)
        harga = hitung_harga(jarak, jumlah_penumpang)

        print("\nDaftar Kereta:")
        for idx, k in enumerate(kereta, 1):
            print(f"{idx}. {k}")

        pilihan_kereta = int(input("Masukkan nomor kereta: "))
        if 1 <= pilihan_kereta <= len(kereta):
            nama_kereta = kereta[pilihan_kereta - 1]
            total_harga = harga * jumlah_penumpang
            metode_pembayaran = proses_pembayaran(total_harga)
            journey_details = buat_detail_perjalanan(titik_awal, titik_tujuan, tanggal_keberangkatan, jumlah_penumpang, nama_kereta, total_harga, metode_pembayaran)

            if metode_pembayaran:
                konfirmasi = input(
                    f"Apakah Anda ingin membayar Rp {total_harga} dengan {metode_pembayaran}? (y/n): ")
                if konfirmasi.lower() == 'y':
                    print("\nPembayaran berhasil.")
                    return journey_details
                else:
                    print("\nPembayaran dibatalkan.")
                    return "Perjalanan dibatalkan."
            else:
                return "Perjalanan dibatalkan. Metode pembayaran tidak valid."
        else:
            print("Nomor kereta tidak valid.")
    else:
        print("Nomor kota tidak valid.")

    return journey_details

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
    kereta = [
        "KA Cikuray",
        "KA Argo Bromo Anggrek",
        "KA Ciremai",
        "KA Sindoro",
        "KA Pangrango",
        "KA Argo Muria",
        "KA Argo Wilis",
        "KA Argo Lawu"
    ]
    
    journey_info = antar_kota(kota, kereta)
    print(journey_info)

if __name__ == "__main__":
    main()
