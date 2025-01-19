ascii_nb=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

ascii_text = ""
for nb in ascii_nb:
	ascii_text = ascii_text + chr(nb)

print(ascii_text)
