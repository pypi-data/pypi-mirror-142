# wsmsg Package

## Overview
**Websockets** are used, and the server will accept all authenticated connections to an endpoint root (default '/'). Authentication is via an HTTP bearer token on initial connection. Each node attaches to an **endpoint** specified in the connection URI. For example: `wss://<host>:<port>/<endpoint>`. **Channels** receive (and queue) **messages**. **Subscriptions** bind an endpoint to one or more channels. **Subjects** can be used to filter messages in a subscription. Message delivery is at most once, with flow control and no guaranteed persistence.
## Flow Diagram
```
Publish Channel  Routing     Endpoint 
-------+--------+-----------+-------------
      / Queue -> Forward \ / Queue -> Node
Node <  Queue -> Forward  X         / Node
      \ Queue -> Forward / \ Queue <  Node
                                    \ Node
```

## Message Format
_Messages are sent/received as a msgpack array_
* **uid**: bytes  
  _Binary-safe unique id of message - recommand ULID as bytes_
* **channel**: str  
  _Channel this message will be sent to_
* **subject**: str  
  _Subject of message_
* **reference**: bytes  
  _Binary-safe id of message that this references_
* **data**: any  
  _Subject-defined message data_

### Python
`Message = NamedTuple('Message', uid=bytes, channel=str, subject=str, reference=bytes, data=any)`  
```
class Message(NamedTuple):
    uid: bytes
    channel: str
    subject: str
    reference: bytes
    data: any
    def __repr__(self):
        elements = [
            str(ulid.from_bytes(self.uid)),
            self.channel,
            self.subject,
            str(ulid.from_bytes(self.reference)) if self.reference else None,
            repr(self.data)
        ]
        return "Message(%s)" % ', '.join(elements)
```

## System Messages
_The 'system' channel has ultimate priority (100) over all other channels._  
_If there are any queued messages in the system queue, no other channels will forward._

### Commands
* **ack**  
  _Acknowledge message receipt, not forwarded._  
  _Ack'd message uid should be in the refercence field._  
  _Next message for connection will not be dequeued or sent_  
  _until previous message was ackowledged._ 
* **subcribe**
    * **channel** (endpoint: str, channel_pattern: str, subject_pattern: str)  
      _Subscribe endpoint to channel pattern with subject pattern filter._
    * **message** (endpoint: str, message_uid: bytes, expires: int)  
      _Subscribe endpoint to any messages that reference the message uid until the expiration (unix timestamp)._
* **unsubscribe** (endpoint: str, channel_pattern: str)  
    * **channel** (endpoint: str, channel_pattern: str)  
      _Unsubscribe endpoint from patterns matching pattern._  
      _Includes any subject filters._
    * **message** (endpoint: str, message_uid: bytes)  
      _Unsubscribe endpoint to any messages that reference the message uid._
* **pause**  
  _Pause all message transmissions._  
  _Messages can still be received and system commands processed._
* **resume**  
  _Resume message transmissions._
* **stop**  
  _Cleanly stop and shutdown server._  
  _Pending messages are persisted._ 
* **channel**
    * **create** (channel: str)  
      _Create channel queue._
    * **size** (channel: str, size: int)  
      _Set max size of channel queue. Old messages are dropped when full_
    * **priority** (channel: str, priority: int)  
      _Set channel priority. Higher is better, range 0-99. Default of zero._
* **endpoint**
    * **create** (endpoint: str)  
      _Create endpoint queue_
    * **size** (endpoint: str, size: int)  
      _Set max size of endpoint queue. Old messages are dropped when full_

### System Events
* **stopping**
  _Server is shutting down (in one second), no more messages will be delivered_
* **node**
    * **joined** (endpoint, uid)
    * **left** (endpoint, uid)
* **endpoint**
    * **created** (endpoint)
    * **sized** (channel: str)
* **channel**
    * **created** (channel: str)
    * **sized** (channel: str)
    * **prioritized** (channel: str)

## Misc

### Router
* Until stop
    * Wait for next message
    * For each subscriber
        * Push message to node Queue

### Route Map?
```
class Route NamedTuple('Route', router=Router, dest=set[UUID])
RouteMap = dict[UUID, Route]

routes: RouteMap = 
{
    <channel>: <route>, 
    ...
}

while True:
    msg = channel.get()
    for node in routes[channel].dest:
      forward_message(msg, node)
```
    
## Examples

### Task Queue
_By connecting all nodes to one endpoint, each node will get a fair shair of the messages in the 'order' channel with the subject 'submitted'._
```
All nodes connects to ws://<host>:<port>/group1
node1 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, ('group1', 'orders', 'submitted'))
node2 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, ('group1', 'orders', 'submitted'))
node3 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, ('group1', 'orders', 'submitted'))
```

### Fanout
_By using one endpoint per node, each node will get a copy of the messages in the 'order' channel with the subject 'submitted'._
```
Each node connects to ws://<host>:<port>/<node id>
node1 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<node id>, 'orders', 'submitted'))
node2 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<node id>, 'orders', 'submitted'))
node3 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<node id>, 'orders', 'submitted'))
```

### Direct Delivery
_If each node subscribes to a unique addressable channel, messages can be routed to each node by the sender._  
_To send a message to a single node, use channel 'node.<node id>' with any subject._  
_To send a message to all nodes, additionally subscribe all nodes to a 'nodes' channel and send to that._
```
Each node connects to ws://<host>:<port>/<node id>
node1 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<node id>, 'node.<node id>', '*'))
node2 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<node id>, 'node.<node id>', '*'))
node3 -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<node id>, 'node.<node id>', '*'))
```
### RPC
_Advantages: Less messages to send, supports heavy RPC traffic through server._  
_Disadvantages: Need to know what reply channel and subjects will be used, large number of channel subscriptions can slow down message forwarding._  
```
Connect to ws://<host>:<port>/<id>
node -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<id>, 'order', 'created'))
node -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<id>, 'order', 'exception'))
...
# Generate uid
Register Queue with RX task/thread for reference=uid
node -> Message(uid, 'order', 'submitted', None, None, Check)
...
node <- Message(<message uid>, 'order', 'created', uid, None, <check uid>)
RX task/thread matches and puts message(s) in Queue
...
Get result(s) with timeout from Queue
Resend if needed or show error on exception
Unregister Queue from RX task/thread
```

### RPC - Streamlined
_Advantages: message subscription matching is much faster, RTT should be lower. No need to know what reply subject may be._  
_Disadvantages: more messages to send, total throughput may be lower if heavy use of RPC._  
_Notes: If you set the message subscription expiration, no need to unsubscribe._  
```
server -> Message(ulid.new().bytes, 'system', 'subscribe.channel', None, (<endpoint>, 'rpc', 'order.*'))
server -> Message(ulid.new().bytes, 'system', 'channel.priority', None, ('rpc', 99))
server -> Message(ulid.new().bytes, 'system', 'endpoint.size', None, (<endpoint>, 10))
...
Connect to ws://<host>:<port>/<id>
...
Generate uid
Register Queue with RX task/thread for reference=uid
node -> Message(ulid.new().bytes, 'system', 'subscribe.message', None, (<id>, uid, <timeout>))
node -> Message(uid, 'rpc', 'order.get.request', None, Check)
...
node <- Message(<message uid>, 'rpc', 'order.get.reply', uid, None, <check uid>)
RX task/thread matches and puts message(s) in Queue
...
Get result(s) with timeout from Queue
Resend if needed or show error on exception
Unregister Queue from RX task/thread
```

