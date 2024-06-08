import sqlite3

veritabani = sqlite3.connect("veritabani.db")
imlec = veritabani.cursor()

tablo_yap = "CREATE TABLE IF NOT EXISTS personel(isim TEXT, soyisim TEXT, departman TEXT, maas INT)"

imlec.execute(tablo_yap)

veritabani.commit()

imlec.execute("INSERT INTO personel VALUES('abcd','efgh','IT',10)")

veritabani.commit()

isim = input("Ad:")
soyisim = input("Soyisim:")
departman = input("Departman:")
maas = int(input("Maas:"))

imlec.execute("INSERT INTO personel VALUES(?,?,?,?)", (isim,soyisim,departman,maas))

veritabani.commit()
veritabani.close()