from pyhiveConnection import hiveConnector
conn = hiveConnector.KRBZKConnect('default')
cursor=conn.cursor()
cursor.execute("show databases")
for result in cursor.fetchall():
    print(result)
cursor.close()
conn.close()
