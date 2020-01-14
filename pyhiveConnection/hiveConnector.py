from kazoo.client import KazooClient
from pyhive import hive
import random


def KRBZKConnect(database):
    zkhost = "dn-02.hadoop.citic:2181,dn-01.hadoop.citic:2181,dn-03.hadoop.citic:2181"
    znodeName = "/hiveserver2"
    serviceKeyword = "serverUri"
    return ConnKRB(zkhost, znodeName, serviceKeyword, database)


# connect hive by pyhive and return cursor
def ConnKRB(zkhost, znodeName, serviceKeyword, database):
    hostList = discoveryThriftSerivcehost(zkhost, znodeName, serviceKeyword)
    hostLength = hostList.__len__()
    random.seed()
    isConnected = False
    while isConnected is False and hostLength > 0:
        index = random.randint(0, hostLength - 1)
        hostStr = hostList.pop(index).split(":")
        try:
            conn = hive.Connection(host=hostStr[0], port=int(hostStr[1]), database=database, auth='KERBEROS',
                                   kerberos_service_name="hive")
            isConnected = True
        except:
            isConnected = False
            if hostLength > 1:
                print("ERROR:Can not connect " + hostStr[0] + ":" + hostStr[1] + " .try another thrift server...")
            else:
                print("ERROR:Can not connect hiveserver2, please check the connection config and the hiveserver")
                return 0
        hostLength -= 1
    return conn


# discovery the thrfit service host list
def discoveryThriftSerivcehost(zkhost, znodeName, serviceKeyword):
    zkClient = KazooClient(hosts=zkhost)
    zkClient.start()
    # get the children name of zonde
    result = zkClient.get_children(znodeName)
    zkClient.stop()
    hostList = list()
    for item in result:
        for subitem in item.split(";"):
            lst = subitem.split("=")
            if lst[0] == serviceKeyword:
                hostList.append(lst[1])
    return hostList
