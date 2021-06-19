from autobahn.asyncio.component import Component
from autobahn.asyncio.component import run

comp = Component(
    transports=u"ws://localhost:8080/ws",
    realm=u"realm1",
)

@comp.on_join
async def joined(session, details):
    print("session ready")

@comp.subscribe("tcp.data")
def handle_tcp_data(message):
    print("received tcp data: {}".format(message))

if __name__ == "__main__":
    run([comp])