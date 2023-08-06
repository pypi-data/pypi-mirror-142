import time
import pvapy_plugins as pvap
import argparse as argp

data_calls = 0
def data_callback(data):
    global data_calls
    data_calls += 1
#    print('data callback called')

def status_callback(status, msg):
    print('status callback called ',status, ':' , msg)

if __name__ == "__main__":
#    argparser = argp.ArgumentParser()
#    argparser.add_argument('pv')
#    argparser.add_argument('--rate', dest='rate')
#    args = argparser.parse_args()

    pv = 'ec:Pva1:Image'
    startcounter = data_calls
    ds = pvap.DataSource()
    ds.update_device(pv)
    ds.set_data_callback(data_callback)
    ds.set_status_callback(status_callback)

    print('starting')
    ds.start()

    time.sleep(5)
    assert(ds.channel.state == pvap.Channel.State.CONNECTED)
    assert(data_calls > startcounter)
    print('received {} objs'.format(data_calls - startcounter))
    startcounter = data_calls

    print('------')
    print('change rate')
    ds.update_framerate(3)
    time.sleep(5)
    assert(ds.channel.state == pvap.Channel.State.CONNECTED)
    assert(data_calls > startcounter)
    print('received {} objs'.format(data_calls - startcounter))

    print('------')
    startcounter = data_calls
    print('change to unlimited rate')
    ds.update_framerate(None)
    time.sleep(5)
    assert(ds.channel.state == pvap.Channel.State.CONNECTED)
    assert(data_calls > startcounter)
    print('received {} objs'.format(data_calls - startcounter))

    print('------')
    print('stopping source')
    startcounter = data_calls
    ds.stop()
    time.sleep(5)
    assert(ds.channel.state == pvap.Channel.State.DISCONNECTED)
    print('received {} objs'.format(data_calls - startcounter))

    print('------')
    print('change to bogus pv')
    startcounter = data_calls
    ds.update_device('foobar')
    ds.start()
    
    time.sleep(20)
    assert(ds.channel.state == pvap.Channel.State.FAILED_TO_CONNECT)
    print('received {} objs'.format(data_calls - startcounter))

    print('------')
    print('change back')
    startcounter = data_calls
    ds.update_device(pv)
    ds.start()
    
    time.sleep(5)
    print('received {} objs'.format(data_calls - startcounter))
    assert(ds.channel.state == pvap.Channel.State.CONNECTED)
    assert(data_calls > startcounter)
    print('------')
    
    ds.stop()
    assert(ds.channel.state == pvap.Channel.State.DISCONNECTED)
    
