import qrcode
from wifi_f import wifi


def handle():
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    data = "Wi-Fi şəbəkəsinə bağlı deyilsiniz."
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()


if wifi(b='ad') != '00x0':
    wifi_data = "WIFI:T:WPA;S:{};P:{};;".format(wifi(b='ad'), wifi(b='sifre'))
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(wifi_data)
    qr.make(fit=True)

    qr_kod = qr.make_image(fill_color="black", back_color="white")
    qr_kod.show()
else:
    handle()
