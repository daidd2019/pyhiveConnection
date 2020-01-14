# pyhiveConnection
support hive zookeeper HA mode(based on pyhive and kazoo)) \
pass username,password,databasename,zkhosts,port and return pyhive DB-API connection
# requirements
pyhive>=0.5 \
kazoo
## client for centos
yum install -y cyrus-sasl-plain cyrus-sasl-devel cyrus-sasl-gssapi  cyrus-sasl-md5
pip install thrift
pip install sasl
pip install thrift_sasl
pip install PyHive
pip install kazoo


## client for ubuntu
sudo apt-get install python-pip
sudo apt-get install sasl2
sudo apt-get install sasl2-bin
sudo apt-get install libsasl2-modules-gssapi-mit
sudo pip install thrift
sudo pip install sasl
sudo pip install thrift_sasl
sudo pip install PyHive
sudo pip install kazoo


# example
```python
from pyhiveConnection import hiveConnector
conn = hiveConnector.KRBZKConnect('default')
cursor=conn.cursor()
cursor.execute("show databases")
for result in cursor.fetchall():
    print(result)
cursor.close()
conn.close()
```

#deploy 
sudo python setup.py install