
from pyhs2.connections import Connection
import time
import logging

logging.basicConfig(filename = '/var/log/python-client.log',
                    level = logging.WARN, filemode = 'a',
                    format = '%(asctime)s - %(levelname)s - (%(pathname)s,%(lineno)s)  - %(message)s')  

class HAConnection():
    #connection = None
    
    def __init__(self, hosts = None, port = 10000, authMechanism = None, user = None,
                 password = None, database = None, configuration = None, timeout = 10000):
        if hosts is None:
            raise ValueError('hosts is None .')
        
        if isinstance(hosts, list):
            hosts = tuple(hosts)
        elif isinstance(hosts, tuple):
            pass
        else:
            raise ValueError('hosts is not a tuple or a list .')
        
        isConnectted = False
        for i in range(0, 10):
            for host in hosts:
                try:
                    self.connection = Connection(host, port, authMechanism, user, password,
                                                 database, configuration, timeout)
                    isConnectted = True
                    logging.debug("Connect to hive server successful!")
                    break
                except Exception, e:
                    logging.warning("Failed to connect host : %s ,error message is : %s" % (host, e))
                    continue
            if isConnectted:
                break
            else:
                time.sleep(1)
        
        if not isConnectted:
            logging.error("Failed to connect hive server.")
            raise HAConnectionError("Failed to connect hive server.")
        
    def getConnection(self):
        return self.connection
        
    def close(self):
        if self.connection is not None:
            self.connection.close()
            
    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback):
        if self.connection is not None:
            self.connection.close()
        
class HAConnectionError(Exception):
    def __init__(self, value):
        self.value = value
      
    def __str__(self):  
        return repr(self.value)
    
