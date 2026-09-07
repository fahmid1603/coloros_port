import re, sys
p = sys.argv[1]
with open(p) as f:
    c = f.read()
c2 = re.sub(r'\s*<hal format="hidl">\s*<name>android\.hardware\.soundtrigger</name>.*?</hal>', '', c, flags=re.S)
with open(p, 'w') as f:
    f.write(c2)
print(f"soundtrigger HAL entries removed: {c != c2}")
