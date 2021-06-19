import asyncio


class EchoServerProtocol(asyncio.Protocol):
    def __init__(self, cb_session=None):
        super().__init__()
        self.cb_session = cb_session

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        # publish received data to crossbar
        if self.cb_session:
            self.cb_session.publish("tcp.data", message)

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

