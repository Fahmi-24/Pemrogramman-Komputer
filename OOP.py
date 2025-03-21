import math 
import Rumus as rumus 

class RivetJoint: # konstruktor 
    """
    Kelas dasar untuk Rivet Joint.
    Menyimpan parameter teknis:
      - Jenis rivet    : LapJoint,ButtJoint
      - Banyak kolom   : n
      - jenis_sambungan: chain_full, chain_sama, zigzag_sama, zigzag_outer_setengah 
      - jenis_shear    : single, double
      - P              : Tekanan Boiler (MPa)
      - TT             : Tegangan tekan/tarik (N/mm^2)
      - TG             : Tegangan geser (N/mm^2)
      - TC             : Tegangan crushing (N/mm^2)
      - efisiensi      : Efisiensi sambungan (%)
    """
    def __init__(self,jenis_rivet, banyak_kolom, jenis_sambungan, jenis_shear, P, TT, TG, TC, E,D):
        self.jenis_rivet = jenis_rivet
        self.banyak_kolom = banyak_kolom
        self.jenis_sambungan = jenis_sambungan
        self.jenis_shear = jenis_shear
        self.P = P
        self.TT = TT
        self.TG = TG
        self.TC = TC
        self.efisiensi = E
        self.D = D


class LapJoint(RivetJoint):
        '''
        Kelas untuk Lap Joint
        Menggunakan rumus untuk lap joint 1
        '''
        def tebal_plat_boiler(self):
             return rumus.tebal_plat_boiler(self.P,self.D,self.TT,self.efisiensi)
        
        def diameter_rivet(self):
             t = self.tebal_plat_boiler() # memanggil fungsi dari tebal_plat_boiler
             return rumus.diameter_rivet(t)
        def diameter_lubang(self):
             t = self.tebal_plat_boiler()
             dl = rumus.diameter_lubang(t)
             return dl
        def tahanan_geser_single(self):
             dl = self.diameter_lubang()
             return rumus.tahanan_geser_single(self.banyak_kolom,dl,self.TG)
        def tahanan_geser_double(self):
             dl = self.diameter_lubang()
             return rumus.tahanan_geser_double(self.banyak_kolom,dl,self.TG)
        
        def tahanan_geser(self):
             '''
             Mengambil nilai tahanan geser
             '''
             t = self.tebal_plat_boiler()
             if self.jenis_shear.lower() == "single":
                  return self.tahanan_geser_single()
             elif self.jenis_shear.lower() == "double":
                  return self.tahanan_geser_double()
             else:
                  raise ValueError("Nilai tidak dikenali")
        def pitch_awal(self):
            '''
            Menghitung nilai pitch 
            '''
            Ps = self.tahanan_geser()
            t = self.tebal_plat_boiler()
            d = self.diameter_rivet()
            p_awal = (Ps/(t*self.TG)) + d 
            return p_awal
        
        def pitch_max(self):
             '''
             Menghitung nilai pitch max
             '''
             t = self.tebal_plat_boiler()
             p_max = rumus.pitch_maksimal(self.jenis_sambungan,t,self.banyak_kolom)
             return p_max
        
        def pitch(self):
             '''
             Menghitung nilai dari pitch
             '''
             p = max(self.pitch_awal,self.pitch_max)
             return p 
        
        def pitch_back(self):
             '''
             Menghitung nilai dari pitch back 
             '''
             p = self.pitch()
             dl = self.diameter_lubang()
             if self.jenis_sambungan.lower() == "chain_sama":
                pb = rumus.pitch_back_chain_sama(p,dl)
                return pb
             elif self.jenis_sambungan.lower() == "chain_full":
                pb = rumus.pitch_back_chain_full(p,dl)
                return pb
             elif self.jenis_sambungan.lower() == "zigzag_sama":
                pb = rumus.pitch_back_zigzag_sama(p,dl)
                return pb
             elif self.jenis_sambungan.lower() == "zigzag_outer_setengah":
                pb = rumus.pitch_back_zigzag_outer_setengah(p,dl)
                return pb
             else:
                  raise ValueError("Masukkan nilai yang benar")
        
        def margin(self):
             dl = self.diameter_lubang()
             m = 1.5 * dl
             return m
        
        def tahanan_sobek(self):
             p = self.pitch()
             dl = self.diameter_lubang()
             t = self.tebal_plat_boiler()
             Pt = rumus.tahanan_sobek(p,dl,t,self.TT)
             return Pt
        
        def tahanan_crushing(self):
             n = self.banyak_kolom()
             dl = self.diameter_lubang()
             t = self.tebal_plat_boiler()
             Pc = n * dl * t * self.TC
             return Pc
        
        def tahanan_plat_tanpa_rivet(self):
             p = self.pitch()
             t = self.tebal_plat_boiler()
             P_tanpa_rivet = p * t * self.TT
             return P_tanpa_rivet
        
        def efisiensi_akhir(self):
             P_max = max(self.tahanan_crushing,self.tahanan_geser,self.tahanan_sobek)
             P_plat = self.tahanan_plat_tanpa_rivet()
             efisiensi = P_max/P_plat
             return efisiensi


        def menampilkan_data(self):
            d = self.diameter_rivet()
            dl = self.diameter_lubang()
            efisiensi = self.efisiensi_akhir()
            t = self.tebal_plat_boiler()
            print ("Perhitungan Lap Joint triple row zigzag single shear\n")
            print(5*"="+"Perhitungan Rivet"+5*"=")
            print(f"Diameter Rivet = {d} mm")
            print(f"Efisiensi sambungan = {efisiensi}%")
            print(f"Diameter Lubang = {dl} ")
            
            print("\n"+5*"="+"Perhitungan Pelat Boiler"+"="*5+"\n")
            print(f"Tebal Pelat = {t} mm")
    
