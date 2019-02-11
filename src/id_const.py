import socket

hostname = socket.gethostname()
if 'ryu' in hostname:
    from id_const_ryu import *
elif 'sample' in hostname:
    from id_const_sample import *
else:
    from id_const_for_commiting import *
