import datetime

class Hotel:
    def __init__(self, nama, harga_per_kamar, lokasi):
        self.nama = nama
        self.harga_per_kamar = harga_per_kamar
        self.lokasi = lokasi

hotels = [
    Hotel("Hotel Fave", 150000, "Kota Surabaya"),
    Hotel("Hotel Kartika", 300000, "Kota Surabaya"),
    Hotel("Hotel Santika", 450000, "Kota Surabaya"),
    Hotel("Hotel Rayz UMM", 500000, "Kota Malang"),
    Hotel("Hotel Harris", 200000, "Kota Malang"),
    Hotel("Hotel Kapal Garden", 250000, "Kota Malang"),
    Hotel("Hotel Whiz", 350000, "Kota Pasuruan"),
    Hotel("Hotel Bromo", 400000, "Kota Pasuruan"),
    Hotel("Hotel Swiss Belinn", 200000, "Kota Pasuruan")
]

def pilih_lokasi(daftar_hotel):
    daftar_lokasi = list(set([hotel.lokasi for hotel in daftar_hotel]))
    return daftar_lokasi

def hotel_di_lokasi(lokasi, daftar_hotel):
    return list(filter(lambda hotel: hotel.lokasi == lokasi, daftar_hotel))

def hotel_booking(daftar_hotel):
    lokasi_terpilih = pilih_lokasi(daftar_hotel)

    if not lokasi_terpilih:
        return "Nomor lokasi tidak valid."

    lokasi_hotel_terpilih = hotel_di_lokasi(lokasi_terpilih[0], daftar_hotel)

    if not lokasi_hotel_terpilih:
        return "Tidak ada hotel di lokasi yang dipilih."

    return lokasi_hotel_terpilih[0]

def main():
    hasil_booking = hotel_booking(hotels)
    if isinstance(hasil_booking, Hotel):
        print(f"Anda telah memesan {hasil_booking.nama} di {hasil_booking.lokasi} dengan harga {hasil_booking.harga_per_kamar}")
    else:
        print(hasil_booking)

if __name__ == "__main__":
    main()
