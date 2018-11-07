import sys
sys.path.append('./gen-py')

from hello import HelloWorld
from hello.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol 
from thrift.server import TServer

class HelloWorldHandler():
	def __init__(self):
		pass
	def ping(self):
		return 'pong!'
	def say(self,message):
		ret = "server received: "+ message
		print(ret)
		return ret

if __name__ =='__main__':
	handler = HelloWorldHandler()#build your own handler 
	processor  = HelloWorld.Processor(handler) ##get a processor from a handler that you built
	transport = TSocket.TServerSocket('localhost',9090) #get a server transport
	tfactory = TTransport.TBufferedTransportFactory() ##get a transport factory
	pfactory = TBinaryProtocol.TBinaryProtocolFactory() ##get a protocol factory

	server  = TServer.TSimpleServer(processor,transport,tfactory,pfactory) #get a server from the settings

	print("begin the server on localhost,9090")
	server.serve()
	print("Suspend the service on localhost,9090")

