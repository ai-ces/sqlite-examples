import sqlite3

veritabani = sqlite3.connect("veritabani.db")
imlec = veritabani.cursor()

tablo_yap = "CREATE TABLE IF NOT EXISTS personel(isim TEXT, soyisim TEXT, departman TEXT, maas INT)"

imlec.execute(tablo_yap)

veritabani.commit()

imlec.execute("INSERT INTO personel VALUES('abcd','efgh','IT',10)")

veritabani.commit()


def verileri_al():
    imlec.execute("SELECT * FROM personel")
    liste = imlec.fetchall()
    for i in liste:
        print(i)

verileri_al()

veritabani.close()