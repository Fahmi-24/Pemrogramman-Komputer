# Program Backend
import Rumus as rumus
import math
import OOP

print ("="*5+"PERHITUNGAN RIVET"+"="*5)

# INPUT DATA 

while True:
    try:
        D = rumus.diameter_pressure_vessel()  # Meminta input ulang setiap iterasi
        if D <= 0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print("Masukkan nilai yang benar! Nilai harus lebih besar dari 0.")
        else:
            break  # Input valid, keluar dari loop
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print("Input tidak valid! Silahkan masukkan angka.")
    
while True:    
    try:
        P = rumus.tekanan_pressure_vessel()
        if P <=0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
            print("Masukkan nilai yang benar! Nilai harus lebih dari 0")
        else:
            break
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print("Input tidak valid! Silahkan masukkan angka")
        
while True:    
    try:
        TT = rumus.tegangan_tarik_pressure_vessel()
        if TT <=0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
            print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
            print("Masukkan nilai yang benar! Nilai harus lebih dari 0")
        else:
            break
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
        print("Input tidak valid! Silahkan masukkan angka")

while True:    
    try:
        TTek = rumus.tegangan_tekan_pressure_vessel()
        if TTek <=0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
            print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
            print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
            print("Masukkan nilai yang benar! Nilai harus lebih dari 0")
        else:
            break
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print("Input tidak valid! Silahkan masukkan angka")

while True:    
    try:
        TG = rumus.tegangan_geser_pressure_vessel()
        if TG <=0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
            print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
            print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
            print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
            print("Masukkan nilai yang benar! Nilai harus lebih dari 0")
        else:
            break
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
        print("Input tidak valid! Silahkan masukkan angka")

while True:    
    try:
        TC = rumus.tegangan_crushing_pressure_vessel()
        if TC <=0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
            print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
            print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
            print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
            print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
            print("Masukkan nilai yang benar! Nilai harus lebih dari 0")
        else:
            break
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
        print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
        print("Input tidak valid! Silahkan masukkan angka")


while True:    
    try:
        E = rumus.efisiensi()
        if E <=0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
            print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
            print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
            print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
            print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
            print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TC}")
            print("Masukkan nilai yang benar! Nilai harus lebih dari 0")
        else:
            break
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) ={P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
        print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
        print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TC}")
        print("Input tidak valid! Silahkan masukkan angka")

# Daftar pilihan yang valid

while True:
    pilihan_valid = ["chain_full", "chain_sama", "zigzag_sama", "zigzag_outer_setengah"]
    jenis_sambungan = input("Jenis Sambungan (chain_full, chain_sama, zigzag_sama, zigzag_outer_setengah) = ")
    
    if jenis_sambungan in pilihan_valid:
        print(f"Anda memilih {jenis_sambungan}.")
        break
    else:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) = {P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
        print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
        print(f"Masukkan nilai dari tegangan crushing pressure vessel (N/mm^2) = {TC}")
        print(f"Masukkan nilai dari efisiensi rivet (%) = {E}")
        print("Masukkan nilai yang benar! Nilai harus ada dalam pilihan:", ", ".join(pilihan_valid))

while True:
    list_joint = ["LapJoint","ButtJoint"]
    jenis_rivet = input("Masukkan jenis rivet (LapJoint/ButtJoint) = ")
    if jenis_rivet in list_joint:
        print(f"Anda memilih rivet {jenis_rivet}")
        break
    else:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) = {P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
        print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
        print(f"Masukkan nilai dari tegangan crushing pressure vessel (N/mm^2) = {TC}")
        print(f"Masukkan nilai dari efisiensi rivet (%) = {E}")
        print(f"Jenis Sambungan (chain_full, chain_sama, zigzag_sama, zigzag_outer_setengah) = {jenis_sambungan}")
        print("Masukkan nilai yang benar! Nilai harus ada dalam pilihan:")

while True:    
    try:
        n = rumus.banyak_kolom()
        if n <=0:
            rumus.clear_console_except_title()
            print("=== Pressure Vessel Calculator ===\n")
            print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
            print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) = {P}")
            print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
            print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
            print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
            print(f"Masukkan nilai dari tegangan crushing pressure vessel (N/mm^2) = {TC}")
            print(f"Masukkan nilai dari efisiensi rivet (%) = {E}")
            print(f"Jenis Sambungan (chain_full, chain_sama, zigzag_sama, zigzag_outer_setengah) = {jenis_sambungan}")
            print(f"Masukkan jenis rivet (LapJoint/ButtJoint) = {jenis_rivet}")
            print("Masukkan nilai yang benar! Nilai harus ada dalam pilihan:")
        else:
            break
    except ValueError:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) = {P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
        print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
        print(f"Masukkan nilai dari tegangan crushing pressure vessel (N/mm^2) = {TC}")
        print(f"Masukkan nilai dari efisiensi rivet (%) = {E}")
        print(f"Jenis Sambungan (chain_full, chain_sama, zigzag_sama, zigzag_outer_setengah) = {jenis_sambungan}")
        print(f"Masukkan jenis rivet (LapJoint/ButtJoint) = {jenis_rivet}")
        print("Masukkan nilai yang benar! Nilai harus ada dalam pilihan:")

while True:
    list_shear = ["single","double"]
    jenis_shear = input("Masukkan jenis tahanan geser (single/double) = ")
    if jenis_shear in list_shear:
        print(f"Anda memilih rivet {jenis_shear}")
        break
    else:
        rumus.clear_console_except_title()
        print("=== Pressure Vessel Calculator ===\n")
        print(f"Masukkan nilai dari diameter Pressure Vessel (mm) = {D}")
        print(f"Masukkan nilai dari tekanan pressure vessel (N/mm^2) = {P}")
        print(f"Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = {TT}")
        print(f"Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = {TTek}")
        print(f"Masukkan nilai dari tegangan geser pressure vessel (N/mm^2) = {TG}")
        print(f"Masukkan nilai dari tegangan crushing pressure vessel (N/mm^2) = {TC}")
        print(f"Masukkan nilai dari efisiensi rivet (%) = {E}")
        print(f"Jenis Sambungan (chain_full, chain_sama, zigzag_sama, zigzag_outer_setengah) = {jenis_sambungan}")
        print(f"Masukkan jenis rivet (LapJoint/ButtJoint) = {jenis_rivet}")
        print(f"Masukkan jenis tahanan geser (single/double) = {jenis_shear}")
        print("Masukkan nilai yang benar! Nilai harus ada dalam pilihan:")



# NILAI YANG DIKETAHUI 
print("\n"+"="*5+"DIKETAHUI"+"="*5)
print(f"\nNilai diameter yang valid: {D} mm\n")
print(f"NIlai tekanan yang valid: {P} N/mm^2\n")
print(f"Nilai Tegangan tarik yang valid: {TT} N/mm^2\n")
print(f"Nilai Tegangan tekan yang valid: {TTek} N/mm^2\n")
print(f"Nilai Tegangan geser yang valid: {TG} N/mm^2\n")
print(f"Nilai Efisiensi yang valid: {E}%\n")
print(f"Jenis Sambungan = {jenis_sambungan}\n")
print(f"Jenis Rivet = {jenis_rivet}\n")
print(f"Banyak Kolom = {n}\n")
print(f"Jenis Tahanan Geser = {jenis_shear}\n")

# NILAI YANG DIHITUNG 
if jenis_rivet == "LapJoint":
    lap_joint = OOP.LapJoint(jenis_rivet,n,jenis_sambungan,jenis_shear,P,TT,TG,TC,E,D)
    tebal_plat = OOP.LapJoint.tebal_plat_boiler(lap_joint)
    diameter_rivet = OOP.LapJoint.diameter_rivet(lap_joint)
    diameter_lubang = OOP.LapJoint.diameter_lubang(lap_joint)
    tahanan_geser = OOP.LapJoint.tahanan_geser(lap_joint)





