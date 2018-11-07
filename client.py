import sys
sys.path.append('./gen-py')

from hello import HelloWorld
from hello.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket('localhost',9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = HelloWorld.Client(protocol)

transport.open()##open the transport pipline
pingrespond = client.ping() #RPC request
sayrespond = client.say('hello')#RPC
print(pingrespond)
print('\n{}'.format(sayrespond))
transport.close()#close the pipline