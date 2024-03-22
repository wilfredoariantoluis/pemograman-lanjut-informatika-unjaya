def tampilkan_profile_mahasiswa(**kwargs):
    print("Profile Mahasiswa UNJANI Yogyakarta")
    for key, value in kwargs.items():
        print(f"{key.capitalize()} : {value}")

# Main program
nama = input("Nama: ")
nim = input("NIM: ")
prodi = input("Prodi: ")
hobi = input("Hobi: ")

tampilkan_profile_mahasiswa(Nama=nama, NIM=nim, Prodi=prodi, Hobi=hobi)
