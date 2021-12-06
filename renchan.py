import os
from os import system, name

os.system("clear")
print("----------------------------------------");
print("\033[1;32;40m > IP CHECKER <")
print("\033[1;32;40m CONTOH DOMAIN www.google.com");
print("\033[1;32;40m Creator: RenChan\n");

domain = str(input("DOMAIN:"))

print("Nih ngab ip dari domain yang lu minta");
print(f'===>> {s.gethostbyname(domain)} <<====');
print(f'===>> {domain} <<===\n\n');
print("----------------------------------------");
