from pixels import pixelList


r_values = 0
g_values = 0
b_values = 0

for pixel in pixelList:
    r_values += pixel[0]
    g_values += pixel[1]
    b_values += pixel[2]

average_r = int(r_values / len(pixelList))
average_g = int(g_values / len(pixelList))
average_b = int(b_values / len(pixelList))

print(average_r, average_g, average_b)
# 221 222 213
