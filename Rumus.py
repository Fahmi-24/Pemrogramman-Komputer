# Program rumus 
import math
import os


def pitch_awal(Ps,t,TT,dl):
    p_awal = math.ceil(Ps/(t*TT)+dl)

def tegangan_crushing_pressure_vessel():
    TC = float(input("Masukkan nilai dari tegangan crushing pressure vessel (N/mm^2) = "))
    return TC


def efisiensi():
    E = float(input("Masukkan nilai dari efisiensi rivet (%) = "))
    return E

def clear_console_except_title():
    """
    Membersihkan layar terminal dan langsung menampilkan judul kembali.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def diameter_pressure_vessel():
    D = float (input("Masukkan nilai dari diameter Pressure Vessel (mm) = "))
    return D

def banyak_kolom():
    n = int(input("Masukkan nilai dari banyak rivet = "))
    return n

def tekanan_pressure_vessel():
    P = float(input("Masukkan nilai dari tekanan pressure vessel (N/mm^2) = "))
    return P 

def tegangan_tarik_pressure_vessel():
    TT = float(input("Masukkan nilai dari tegangan tarik pressure vessel (N/mm^2) = "))
    return TT

def tegangan_tekan_pressure_vessel():
    TTek = float(input("Masukkan nilai dari tegangan tekan pressure vessel (N/mm^2) = "))
    return TTek

def tegangan_geser_pressure_vessel():
    TG = float(input("Masukkan nilai dari tegangan geser pressure vessel = "))
    return TG

def tearing_area(p, dl, t):   
    """
        Perhitungan untuk tearing area 
        p = pitch
        dl = diameter lubang 
        t = tebal plat
    """    
    As = (p - dl) * t
    return As

def tahanan_sobek(p, dl, t, TT):
    """
    Perhitungan tahanan sobek 
    p = pitch (mm)
    dl = diameter lubang (mm)
    t = tebal plat (mm)
    
    """
    Pt = (p - dl) * t
    return Pt

def luas_geser_single_shear(dl):
    '''
    Perhitungan luas geser single shear
    dl = diameter lubang (mm)
    '''
    As = ((math.pi/4)*(dl**2))
    return As

def luas_geser_double_shear(dl):
    '''
    Perhitungan luas geser double shear 
    dl = diameter lubang (mm)
    '''
    As = 1.875*(math.pi/4)*(dl**2)
    return As

def tahanan_geser_single(n, dl, TG):
    '''
    Perhitungan Tahanan Geser single 
    n = jumlah rivet 
    dl = diameter lubang (mm)
    TG = Tegangan Geser (N/mm^2)
    '''
    Ps = n * (math.pi) * (dl**2) * TG
    return Ps

def tahanan_geser_double(n, dl, TG):
    '''
    Perhitungan Tahanan Geser Double 
    n = jumlah rivet 
    dl = diameter lubang (mm)
    TG = Tegangan Geser (N/mm^2)
    '''
    Ps = n * 1.875 * (math.pi/4) * (dl**2) * TG
    return Ps

def luas_crushing_per_rivet(dl, t):
    '''
    Perhirungan luas crusing per rivet
    dl = diameter lubang (mm)
    t = tebal plat (mm)
    '''
    Ac = dl* t
    return Ac

def luas_crusing_semua_rivet(n, dl, t):
    '''
    Perhitungan luas crushing semua rivet 
    n = jumlah rivet (mm)
    dl = diameter lubang (mm)
    t = tebal plat (mm)
    '''
    Ac = n * dl * t
    return Ac

def tahanan_crushing(n, dl, t, TC):
    '''
    Perhitungan tahanan crushing
    n = jumlah rivet
    dl = diameter lubang (mm)
    t = tebal plat (mm)
    TC = tegangan crushing (N/mm^2)
    '''
    Pc = n * dl * t * TC
    return Pc

def tahanan_maximum(Pt, Ps, Pc):
    '''
    Perhitungan tahanan maximum dari ketiga kegagalan
    Pt = tahanan sobek (N/mm^2)
    Ps = tahanan geser (N/mm^2)
    Pc = tahanan crushing (N/mm^2)
    '''
    return max(Ps,Pt,Pc)

def tahanan_plat_tanpa_rivet(p, t, TT):
    '''
    Perhitungan tahanan plat tanpa rivet 
    p = pitch rivet (mm)
    t = tebal plat (mm)
    TT = tegangan tarik (N/mm^2)
    '''
    P = p * t * TT
    return P

def efisiensi_sambungan(Pt, Ps, Pc, p, t, TT):
    '''
    Perhitungan efisiensi rivet 
    '''
    P_max = max(Pt, Ps, Pc)  # Memanggil fungsi dengan parameter
    P_plat = tahanan_plat_tanpa_rivet(p, t, TT)  # Memanggil fungsi dengan parameter
    return P_max / P_plat  # Menghitung efisiensi

def tebal_plat_boiler(P, D, TT,E):
    '''
    Perhitungan tebal plat boiler 
    P = tekanan uap dalam boiler (N/mm^2)(MPa)
    D = diameter boiler (mm)
    TT = Tegangan Tarik (N/mm^2)
    Pt = Tahanan sobek (N/mm^2)
    Ps = Tahanan geser (N/mm^2)
    Pc = Tahanan geser (N/mm^2)
    p = pitch (mm)
    t = tebal plat (mm)
    '''
    t = ((P*D)/2*TT*E)+1
    return t

def diameter_rivet(t):
    '''
    Perhitungan diameter rivet
    '''
    dl = math.ceil(6*(math.sqrt(t)))
    return dl

def diameter_lubang(t):
    """
    Menentukan diameter lubang rivet dari tabel (IS:1928–1961)
    berdasarkan hasil perhitungan diameter_rivet(t).
    """
    # 1) Hitung diameter rivet teoretis
    dr = diameter_rivet(t)
    
    # 2) Tabel rivet (dictionary)
    RIVET_TABLE = {
        12: 13,
        14: 15,
        16: 17,
        18: 19,
        20: 21.5,
        22: 23.5,
        24: 25.5,
        27: 28.5,
        30: 31.5,
        32: 33.5,
        36: 37.5,
        39: 40.5,
        42: 44,
        48: 50
    }
    
    # Urutkan key agar kita bisa bandingkan dari terkecil ke terbesar
    sorted_keys = sorted(RIVET_TABLE.keys())  # [12, 14, 16, 18, 20, ...]

    # 3) Cari key pertama yang >= dr
    for key in sorted_keys:
        if key >= dr:
            return RIVET_TABLE[key]
    
    # 4) Jika tidak ada yang >= dr, kembalikan nilai terbesar
    return RIVET_TABLE[sorted_keys[-1]]



def pitch_maksimal(joint_type, t, n):
    '''
    Perhitungan Pitch Maksimal
    joint_type = Jenis sambungan ('Lap Joint', 'But Joint (Single Strap)', 'But Joint (Double Strap)')
    t = Tebal plat (mm)
    n = Banyak rivet per pitch length
    '''
    # Dictionary tabel nilai C
    C_values = {
        "Lap Joint": {1: 1.31, 2: 2.62, 3: 3.47, 4: 4.17, 5: None},
        "But Joint (Single Strap)": {1: 1.53, 2: 3.06, 3: 4.05, 4: None, 5: None},
        "But Joint (Double Strap)": {1: 1.75, 2: 3.50, 3: 4.63, 4: 5.52, 5: 6.00}
    }

    # Ambil nilai C berdasarkan jenis joint dan jumlah rivet
    C = C_values.get(joint_type, {}).get(n, None)
    
    # Cek apakah C tersedia
    if C is None:
        return "Nilai C tidak tersedia untuk kombinasi ini."

    # Hitung pitch maksimal
    pmax = C * t + 41.28
    return pmax

def pitch_back_zigzag_sama(p,d):
    '''
    Perhitungan pitch back

    '''
    pb = 0.33 * p + 0.67 * d
    return pb

def pitch_back_chain_sama(p,d):
    '''
    Perhitungan pitch back
    '''
    pb = 2 * d
    return pb

def pitch_back_zigzag_outer_setengah(p,d):
    '''
    Perhitungan pitch back
    '''
    pb = 0.2 * p + 1.15 * d
    return pb 

def pitch_back_chain_full(p,d):
    '''
    Perhitungan pitch back
    '''
    pb = 0.165 * p + 0.67 * d 
    return pb 

def tebal_single_strap_chain_riveting(t):
    '''
    Perhitungan tebal plat strap
    '''
    tebal_strap = 1.125 * t
    return tebal_strap

def tebal_single_strap_zigzag_riveting(t,p,d):
    '''
    Perhitungan tebal plat strap
    '''
    tebal_strap = 1.125 * t *((p-d)/(p-2*d))
    return tebal_strap

def tebal_double_strap_lebar_sama_chain_riveting(t):
    '''
    Perhitungan tebal plat strap 
    '''
    tebal_strap = 0.625 * t
    return tebal_strap

def tebal_double_strap_lebar_sama_zigzag_riveting(t,p,d):
    '''
    Perhitungan tebal plat strap
    '''
    tebal_strap = 0.625*t * ((p-d)/(p-2*d))
    return tebal_strap

def tebal_strap_lebar_berbeda_dalam_lebar(t):
    '''
    Perhitungan tebal strap
    '''
    tebal_strap = 0.75 * t
    return tebal_strap

def tebal_strap_lebar_berbeda_luar_sempit(t):
    '''
    Perhitungan tebal strap
    '''
    tebal_strap = 0.625 * t
    return tebal_strap

def margin(dl):
    '''
    Perhitungan margin
    '''
    margin = 1.5 * dl
    return margin

def jumlah_rivet(D,P,dl,TG):
    '''
    Perhitungan jumlah rivet
    '''
    n = ((D**2)*P)/((dl**2)*TG)
    return n

def jumlah_rivet_satu_baris(D,p):
    '''
    Perhitungan Jumlah Baris 
    '''
    jumlah = (math.pi*D)/p
    return jumlah

def overlap(jumlah_rivet_per_baris,pb,m):
    '''
    Perhitungan overlap
    '''
    overlap = (jumlah_rivet_per_baris-1)*pb+m
    return overlap