import socket

if 'ryu' in socket.gethostname():
    from id_const_ryu import *
else:
    from id_const_for_commiting import *
