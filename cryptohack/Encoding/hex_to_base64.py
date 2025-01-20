from base64 import b64encode

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte_data = bytes.fromhex(hex_string)
encoded64 = b64encode(byte_data)

print(encoded64)
