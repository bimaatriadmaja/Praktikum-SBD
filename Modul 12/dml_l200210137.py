#### L200210137_Bima Triadmaja
##
#### SELECT :
##from datetime import date, datetime, timedelta
##import mysql.connector
##
##cnx = mysql.connector.connect(
##    user='root',
##    host='localhost',
##    password='',
##    database='l200210137_bimastore')
##cursor = cnx.cursor()
##tanggal = datetime.now().date()
##query = ("""SELECT nama_pegawai, jabatan from pegawai
##where nama_pegawai like '%a%'""")
##cursor.execute(query)
##results = cursor.fetchall()
##for data in results:
##    print(data)
##
##cursor.close()
##cnx.close()


#### INSERT :
##from datetime import date, datetime, timedelta
##import mysql.connector
##
##cnx = mysql.connector.connect(
##    user='root',
##    host='localhost',
##    password='',
##    database='l200210137_bimastore')
##cursor = cnx.cursor()
##tanggal = datetime.now().date()
##
##insert = (""" insert into transaksi
##                        (id_transaksi,pembeli_id_pembeliFK,
##                        tanggal_transaksi,jumlah_transaksi)
##                        VALUES (%s,%s,%s,%s)""")
##data = ('202305113', 'PM113', '2023-06-30', '72000')
##cursor.execute(insert,data)
##cnx.commit()
##print("{} data telah ditambahkan". format(cursor.rowcount))
##
##cursor.close()
##cnx.close()


#### UPDATE :
##from datetime import date, datetime, timedelta
##import mysql.connector
##
##cnx = mysql.connector.connect(
##    user='root',
##    host='localhost',
##    password='',
##    database='l200210137_bimastore')
##cursor = cnx.cursor()
##tanggal = datetime.now().date()
##
##update = ("""update pegawai set nama_pegawai = 'Fernando'
##where id_pegawai = 'PG025'""")
##cursor.execute(update)
##cnx.commit()
##print("{} data telah di update". format(cursor.rowcount))
##
##cursor.close()
##cnx.close()


## DELETE :
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    host='localhost',
    password='',
    database='l200210137_bimastore')
cursor = cnx.cursor()
tanggal = datetime.now().date()

delete = ("""DELETE FROM cabang_toko WHERE id_cabang = 'BS10'""")
cursor.execute(delete)
cnx.commit()
print("{} data telah dihapus". format(cursor.rowcount))

cursor.close()
cnx.close()
