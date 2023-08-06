

# Table of Contents

1. [Background](#L1-background)
2. [Log variables / output messages](#L2-log-things)
3. [Run a command with realtime stdout](#L2-run-cmd01)
4. [Run a command with blocked stdout](#L2-run-cmd02)
5. [Print with Color](#L2-color)
6. [Handle network interface addresses](#L2-network-addresses)

# Background <a name="L1-background" />

Q: What exactly is this module called [`z2`][1]?

A: Various code bites to keep my python code DRY.

## Log variables / output messages <a name="L2-log-things" />

```python
## LogIt() is implemented by loguru.
##  loguru is a complete python logging rewrite.
##
##  See https://github.com/Delgan/loguru

from z2.utils import LogIt

LogIt().info("You forgot to eat your corn flakes")
```

## Run a command with streaming realtime stdout <a name="L2-zrun-cmd01" />

There are a couple of `zrun` recipies to consider...

1. Run three pings and see output in realtime.

- `realtime=True` allows you to watch individual pings as they happen...
- add all stdout to a list

```python
from z2.process import zrun

## Call z2.process.zrun()...
## - Watch individual pings as they happen... like you ran it in bash / zsh / ??
## - add all output to a list
output = list(zrun("ping -c3 172.16.1.1", print_stdout=True, realtime=True))

print(output)
```

2. Run non-stop pings and act on individual pings.

- `realtime=True` allows you to watch individual pings as they happen...
- add all stdout to a list

```python
from datetime import datetime
import errno

from z2.process import zrun

def act_on_ping(condition=None, now=datetime.now()):
    assert isinstance(condition, str)

    if condition=="foo":
        # Do something...
        pass

    # Much more here...


## Call z2.process.zrun()...
## - Watch individual pings as they happen... like you ran it in bash / zsh / ??
## - add all output to a list

for ii in zrun("ping -c5 -O 172.16.1.1", print_stdout=True, realtime=True):

    if isinstance(ii, str):
        output.append(ii)

    if isinstance(ii, str) and "no answer" in ii.lower():
        # Lost a ping -> "no answer yet for icmp_seq=1"
        #     do something here
        act_on_ping(condition="ping_timeout")

    elif isinstance(ii, int) and ii==errno.EWOULDBLOCK:
        # This is normal while waiting on ping stdout...
        print("    errno.EWOULDBLOCK")
        pass

print(output)
```

## Run a command with blocked stdout <a name="L2-zrun-cmd02" />

1. Run three pings with blocked stdout

- `realtime=False` blocks stdout
- results are returned in a `list()`

```python
from z2.process import zrun

## Call z2.process.zrun()...
## - stdout is blocked during cmd execution
## - return all output as a list of strings
output = list(zrun("ping -c3 172.16.1.1", print_stdout=True, realtime=False))

print(output)
```

## Print with Color <a name="L2-color" />

```python
from z2.strings import C

# Print with green, orange
print(C.GREEN + "Hello" + C.YELLOW + " World" + C.ENDC)
```

## Handle network interface addresses <a name="L2-network-addresses" />

Most network interfaces take an IPv4 or IPv6 address format with a network
mask or a mask-length.  However, when you try to store both address and
mask in Python stdlib, you hit a problem.  `IPv4Address()` does not process a
mask, and `IPv4Network()` does not store "host-bits".  Consider the following:

```python

>>> # IPv4Address() and IPv4Network() are from python stdlib.
>>> from ipaddress import IPv4Address, IPv4Network
>>> intfAddr = IPv4Address("1.1.1.200/24")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/python37/lib/python3.7/ipaddress.py", line 1300, in __init__
    raise AddressValueError("Unexpected '/' in %r" % address)
ipaddress.AddressValueError: Unexpected '/' in '1.1.1.200/24'
>>>
>>>
>>> ### IPv4Network() does not store "host bits", only "network bits".
>>> ### As such, IPv4Network() is **useless** to hold network devices'
>>> ### real-life needs (to store the interface address and mask).
>>>
>>> intfAddr = IPv4Network("1.1.1.200/24")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/python37/lib/python3.7/ipaddress.py", line 1536, in __init__
    raise ValueError('%s has host bits set' % self)
ValueError: 1.1.1.200/24 has host bits set
>>> intfAddr = IPv4Network("1.1.1.200/24", strict=False)
>>> intfAddr
IPv4Network('1.1.1.0/24')
>>> ### Above ^^^^^^ we see that IPv4Network() strips .200 from the
>>> ### address.

Keeping the interface address and mask is supported out of the box with
z2.IPv4Obj(). See below...

>>> from z2 import IPv4Obj
>>> intfAddr = IPv4Obj("1.1.1.200/24")
>>>
>>> intfAddr
<IPv4Obj 1.1.1.200/24>
>>>
```

  [1]: https://github.com/mpenning/z2
