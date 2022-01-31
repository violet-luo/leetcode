# 1. length = 4
# 2. no leading zero
# 3. 0 < IP < 255
def validateIPAddress(addressIP):
    ipv4 = addressIP.split('.')
    for ip in ipv4:
        if len(ipv4) == 4 and str(int(ip)) == ip and 0 <= int(ip) <= 255:
            continue
        else:
            return False
    return True
  
validateIPAddress('172.16.254.1')
validateIPAddress('172.16.254')
validateIPAddress('172.16.254.001')
validateIPAddress('172.16.256.1')
