import sys
from pyhiveConnection import hiveConnector
conn = hiveConnector.KRBZKConnect('default')
if conn == 0:
    sys.exit(1)
cursor=conn.cursor()
cursor.execute("show databases")
for result in cursor.fetchall():
    print(result)
cursor.close()
conn.close()
