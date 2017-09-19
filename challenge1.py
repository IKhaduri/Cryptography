import codecs
import binascii
a = str(input()).strip()
print(bytes.decode(binascii.b2a_base64(codecs.decode(a, "hex_codec"))))
