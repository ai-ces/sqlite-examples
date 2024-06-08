import sqlite3

veritabani = sqlite3.connect("veratabani.db")
imlec = veritabani.cursor()

tablo_yap = "CREATE TABLE IF NOT EXIST personel (isim, soyisim, departman, maas)"

imlec.execute(tablo_yap)

veritabani.close()