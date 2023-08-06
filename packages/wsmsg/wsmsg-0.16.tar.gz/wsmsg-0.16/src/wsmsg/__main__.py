import sys, os, asyncio, socket, json, logging, shlex
from uuid import uuid4
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from signal import SIGTERM, SIGINT

from .server import Server
from .client import Client
from .common import Message

log = logging.getLogger(__package__)

async def server(args: Namespace):
    if args.host is None:
        args.host = '0.0.0.0'
    try:
        server = Server(args.host, args.port, args.key)
        server.loop.add_signal_handler(SIGINT, server._stop.set)
        server.loop.add_signal_handler(SIGTERM, server._stop.set)
        await server.run()
    except Exception as e:
        return str(e)

async def subscribe(args: Namespace):
    if len(args.args) < 1:
        return("[ERROR] you must provide a channel name")
    if args.host is None:
        args.host = '127.0.0.1'
    try:
        endpoint = f"{socket.getfqdn()}-{str(os.getpid())}"
        client = Client(endpoint, args.host, args.port, args.key)
        await client.connect()
        channel = args.args[0]
        subject = '*'
        if len(args.args) > 1:
            subject = args.args[1]
        async def handler(client: Client, msg: Message):
            print(args.delim.join([msg.uid.hex(), msg.subject, json.dumps(msg.data)]), flush=True)
        await client.subscribe(channel, subject, handler)
        stop = asyncio.Event()
        client.loop.add_signal_handler(SIGINT, stop.set)
        client.loop.add_signal_handler(SIGTERM, stop.set)
        log.debug("Waiting for signal...")
        await stop.wait()
        await client.unsubcribe(channel)
    except Exception as e:
        return str(e)

async def publish(args: Namespace):
    if len(args.args) < 3:
        return("[ERROR] you must provide a channel, subject, and data")
    if args.host is None:
        args.host = '127.0.0.1'
    try:
        endpoint = f"{socket.getfqdn()}-{str(os.getpid())}"
        client = Client(endpoint, args.host, args.port, args.key, False)
        await client.connect()
        channel, subject, data = args.args
        if args.reference is not None:
            args.reference = bytes.fromhex(args.reference)
        await client.publish(
            Message(uuid4().bytes, args.reference, channel, subject, json.loads(data))
        )
        await client.done()
        await asyncio.sleep(0.01)
    except Exception as e:
        return str(e)

async def request(args: Namespace):
    if len(args.args) < 3:
        return("[ERROR] you must provide a channel, subject, and data")
    if args.host is None:
        args.host = '127.0.0.1'
    try:
        endpoint = f"{socket.getfqdn()}-{str(os.getpid())}"
        client = Client(endpoint, args.host, args.port, args.key, False)
        await client.connect()
        channel, subject, data = args.args
        reply = await client.request(
            Message(uuid4().bytes, None, channel, subject, json.loads(data)),
            args.timeout
        )
        if '.exception' in reply.subject:
            return(str(reply.data))
        print(json.dumps(reply.data))
    except asyncio.TimeoutError:
        return "[ERROR] request timed out"
    except Exception as e:
        return str(e)

if __name__ == "__main__":

    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument('command', type=str, choices=['server', 'subscribe', 'publish', 'request'], metavar="command", 
        help="one of {server, subscribe, publish, request}")
    parser.add_argument('args', nargs="*", 
        help="command arguments:\nsubscribe <channel> (subject)\npublish <channel> <subject> <data: json>\nrequest <channel> <subject> <data: json>")
    parser.add_argument('--host', '-H', type=str, metavar='<string>',
        help="host name or IP address to use for communication")
    parser.add_argument('--port', '-p', type=int, metavar='<integer>', default=1234, 
        help="TCP port to use for communication (1234)")
    parser.add_argument('--key', '-k', type=str, metavar='<string>',
        help="authentication key")
    parser.add_argument('--reference', '-r', type=str, metavar='<hexstr>',
        help="reference message uid to use for 'publish' command")
    parser.add_argument('--delim', type=str, metavar='<character>', default=' ',
        help="delimiter for the output of 'subscribe' command (' ')")
    parser.add_argument('--timeout', type=int, metavar='<integer>', default=5,
        help="timeout in seconds for the 'request' command (5)")
    parser.add_argument('--quiet', '-q', action='store_true')
    parser.add_argument('--debug', '-D', action='store_true')
    args = parser.parse_args()

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO
    
    if not args.quiet:
        logging.basicConfig()
        logging.getLogger(__package__).setLevel(level)

    sys.exit(asyncio.run(globals()[args.command](args)))
