import subprocess
def wifi(b):
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'interface'])
    data = data.decode('utf-8', errors="backslashreplace")
    data = data.split('\n')
    SSID = [b.split(":")[1][1:-1] for b in data if "SSID" in b]

    if SSID:
        try:
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', SSID[0], 'key=clear'])

            data = data.decode('utf-8', errors="backslashreplace")
            data = data.split('\n')

            data = [b.split(":")[1][1:-1] for b in data if "Key Content" in b]

            try:
                ad = SSID[0]
                sifre = data[0]
                if b == 'ad':
                    return ad
                elif b=='sifre':
                    return sifre

            except IndexError:

                return "{}\n".format(SSID[0])


        except subprocess.CalledProcessError:
           
            return "Kodlaşdırma xətası baş verdi"
    else:
        
        return "00x0"
    
