import socket as s
import os
from os import system, name

os.system("clear")
print("----------------------------------------");
print("> IP CHECKER <")
print("CONTOH DOMAIN www.google.com");
print("Creator: rndwst\n");

domain = str(input("DOMAIN:"))

print("Nih ngab ip dari domain yang lu minta");
print(f'===>> {s.gethostbyname(domain)} <<====');
print(f'===>> {domain} <<===\n\n');
print("----------------------------------------");
