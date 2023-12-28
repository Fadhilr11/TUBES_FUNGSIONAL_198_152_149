def is_valid_number(number):
    return number.isdigit() and len(number) <= 12

def get_pembayaran_choice():
    print("\nMenu Pembayaran:")
    print("1. OVO")
    print("2. Go-Pay")
    print("3. Qris")

    pilihan_pembayaran = input("Pilih metode pembayaran (1/2/3): ")
    return pilihan_pembayaran

def main():
    pulsa = [
        "5.000",
        "10.000",
        "20.000",
        "35.000",
        "50.000",
        "75.000",
        "100.000",
        "200.000"
    ]

    paket = [
        "2GB",
        "4GB",
        "6GB",
        "8GB",
        "10GB",
        "12GB",
        "15GB",
        "20GB",
    ]

    nomor_hp = input("Masukkan nomor HP (maksimal 12 angka): ")
    
    if not is_valid_number(nomor_hp):
        print("Nomor HP tidak valid.")
        return

    pilihan_pembayaran = get_pembayaran_choice()

    def display_menu(options):
        print("\nMenu Pilihan:")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

    display_menu(["Pulsa", "Paket"])
    pilihan_menu = input("Pilih jenis layanan (1/2): ")

    if pilihan_menu == "1":
        display_menu(pulsa)
        pilihan_pulsa = input("Pilih nominal pulsa (1-8): ")
        
        if 1 <= int(pilihan_pulsa) <= len(pulsa):
            total_harga = int(pulsa[int(pilihan_pulsa) - 1])
            if pilihan_pembayaran:
                print(f"Anda telah memilih pulsa sebesar Rp {total_harga} untuk nomor {nomor_hp}.")
                print(f"Metode Pembayaran: {pilihan_pembayaran}")
                print("Pembayaran berhasil.")
            else:
                print("Pembayaran dibatalkan.")
        else:
            print("Pilihan pulsa tidak valid.")
    
    elif pilihan_menu == "2":
        display_menu(paket)
        pilihan_paket = input("Pilih paket data (1-8): ")

        if 1 <= int(pilihan_paket) <= len(paket):
            total_harga = int(paket[int(pilihan_paket) - 1].split("GB")[0]) * 10000  # Harga per GB
            if pilihan_pembayaran:
                print(f"Anda telah memilih paket data {paket[int(pilihan_paket) - 1]} untuk nomor {nomor_hp}.")
                print(f"Metode Pembayaran: {pilihan_pembayaran}")
                print("Pembayaran berhasil.")
            else:
                print("Pembayaran dibatalkan.")
        else:
            print("Pilihan paket data tidak valid.")
    
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
