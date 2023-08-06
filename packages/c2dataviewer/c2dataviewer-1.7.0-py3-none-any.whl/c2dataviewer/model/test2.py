import pvaccess as pva

ch = pva.Channel('ec:Pva1:Image')
ch.setConnectionCallback(lambda x: print('connection:', x))
ch.asyncGet(None, lambda msg: print(msg), 'field()')
