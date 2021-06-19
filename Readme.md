# Tcp to Wamp

> Minimal example of running tcp server and wamp component in the same asyncio event loop

## Setup

```shell
# run crossbar router
docker run -it -p 8080:8080 crossbario/crossbar
```

Run tcp to wamp:

```shell
python tcp_to_wamp.py
```

This will connect to crossbar router and create a tcp server.
Messages send to the tcp server will be published to crossbar router.


Run the wamp listener:

```shell
python wamp_listener.py
```

This will listen to incoming wamp messages.


Run the tcp sender:

```shell
python tcp_sender.py
```

This will send a message over tcp to the server running in `tcp_to_wamp.py`.


The tcp messages will be received by the server of `tcp_to_wamp.py` and then published
to the crossbar router. `wamp_listener.py` receives these messages.