import os

for root,dirs,files in os.walk("/home"):
    for filename in files:
        print(filename)

