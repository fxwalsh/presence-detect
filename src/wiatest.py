from wia import Wia
from PIL import Image
import StringIO
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('presence.cfg')

def publish_presence(name,result):
	buffer = StringIO.StringIO()
	fileName=name+'.png'
	if result[-8:]=='not home':
		fileName='x.png'
	print(fileName)
	buffer.write(open(fileName, 'rb').read())
	buffer.seek(0)

	wia = Wia()
	wia.access_token = config.get('wia.io','access_token')
	wia.Event.publish(name="temperature", data=21.5)
	wia.Event.publish(name=name, file=buffer)
	buffer.close()
