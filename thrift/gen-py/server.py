# -*- coding:utf-8 -*-    
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
# 根据实际的包结构去引入  
from Hello import HelloService  
  
# thrift的具体实现  
class HelloServiceHandler:  
    def __init__(self):  
        self.log = {}  
  
    def test(self,num,name):  
        return name + str(num)  
  
if __name__ == '__main__':  
    handler = HelloServiceHandler()  
    processor = TestService.Processor(handler)  
    transport = TSocket.TServerSocket(host='127.0.0.1',port=9090)  
    tfactory = TTransport.TBufferedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()  
  
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)  
    print 'python server:ready to start'  
    server.serve()  