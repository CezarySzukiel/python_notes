from stat import *

permission = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH
print(bin(permission)) # 0b110100100
permission |= S_IWGRP
print(bin(permission)) # 0b110110100

