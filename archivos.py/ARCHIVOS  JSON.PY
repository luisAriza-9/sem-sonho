import json
fd = open ("LUCHO\\lista.json", "w")
lst = [{"nombre":"lucho", "edada" : 23}
{"nombre":"lucho", "edada" : 23}
{"nombre":"mario", "edada" : 23}
{"nombre":"daniel", "edada" : 23}
{"nombre":" Elquin", "edada" : 23}] 


json. dump (lst, fd)
fd.close()