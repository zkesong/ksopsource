# -*- coding=utf-8 -*-
import datetime

from pyhs2.haconnection import HAConnection


def get_emr_hive_conn():
    try:

        hosts = ["172.31.72.52", "172.31.72.54"]
        port = int(10000)
        conf = {"krb_host": "emr-header-1.cluster-12", "krb_service": "hive"}

        haConn = HAConnection(hosts=hosts,
                              port=port,
                              authMechanism="KERBEROS",
                              configuration=conf, timeout=60000000)
        conn = haConn.getConnection()
        print ("%s：成功连接hive！！！" % (datetime.datetime.now()))
        cur = conn.cursor()
        a = cur.execute('select * from hive_to.iris')
        b = cur.fetchall()
        print b
        print a
        conn.close()
    except Exception, e:
        print ("%s连接Hive数据库：%s" % (datetime.datetime.now(), e))
        # conn.close()
        # 抛出异常
        raise e


if __name__ == '__main__':
    get_emr_hive_conn()
