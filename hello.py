key = 777777777
key_bin_list = [int(x) for x in bin(key)[2:].zfill(32)]
print(key_bin_list)
print(len(key_bin_list))