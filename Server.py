def find_ip(Mlength):
    ip = []
    total = []
    with open(file, 'r') as f:
        for line in f:
            for i in range(Mlength):
                if line[i] == '-' or line[i] == ' ':
                    pass
                else:
                    ip.append(line[i])
            if ip not in total:
                total.append(ip)
            ip = []
    
    return len(ip)


def find_in_file(to_find, file, prnt_line = False):
    total = 0
    with open(file, 'r') as f:
        for line in f:
            if to_find in line:
                total += 1
                if prnt_line == True:
                    print(line)
            else:
                pass
        
    return total 


print(find_in_file("\x04\x01\x00P\xC6\xCE\x0Eu0\x00", 'access.log', True))