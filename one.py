temp = list()
t_end = time.time() + 10 
while time.time() < t_end:
    tn = telnetlib.Telnet("192.168.86.41", "23")
    tn.write("alien\n")
    tn.write("password\n")
    #print tn.read_until('Alien>')
    tn.write("get Taglist\r\n")
    time.sleep(1)
    record = tn.read_very_eager()
    query_tags   = re.findall('E200.*?\,',record)
    query_tags   = [re.sub('\,','',tag) for tag in query_tags]
    #print record
    #print type(record)
    temp.append(query_tags)
