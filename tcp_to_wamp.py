import asyncio

from autobahn.asyncio.component import Component
from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.component import run

from echo_server import EchoServerProtocol

class TcpToWamp(ApplicationSession):

    async def onJoin(self, details):
        self.log.info("joined")
        print("details", details)

        loop = asyncio.get_running_loop()

        self.server = await loop.create_server(
            lambda: EchoServerProtocol(cb_session=self),
            '127.0.0.1', 8888)

    def onLeave(self, details):
        self.log.info("left")
        if self.server:
            self.server.close()
            self.server = None


comp = Component(
    transports = {
        "url": "ws://localhost:8080/ws"
    },
    realm="realm1",
    session_factory=TcpToWamp
)

if __name__ == "__main__":
    run([comp])