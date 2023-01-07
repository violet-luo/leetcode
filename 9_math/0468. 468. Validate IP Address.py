# 1. length = 4 (.123.123.123.123.)
# 2. no leading zero
# 3. 0 < IP < 255
# 4. non numeric
def validateIPAddress(addressIP):
    ipv4 = addressIP.split('.')
    for num in ipv4:
        if not num.isnumeric():
            return False
        
    for ip in ipv4:
        if len(ipv4) == 4 and str(int(ip)) == ip and 0 <= int(ip) <= 255:
            continue
        else:
            return False
    return True
