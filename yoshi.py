import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  MENAMPILKAN TOMBOL TAMBAHAN PADA TERMUX ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  Author : YOSHI TECH')
print('\t     Whatsapp : +1 507-596-1235')
print('\t Facebook : YOSHI')
print('\t Github : https://github.com/Zuck-Ker')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] Sedang mengambil file default termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] menambahkan File Tambahan..')
sleep(1)

key = "extra-keys = [['ESC','/','-','YOSHI','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Memproses  !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar nyet')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !! ^^'+c+'\n\WHATSAPP : +15075961235*\n\n')
