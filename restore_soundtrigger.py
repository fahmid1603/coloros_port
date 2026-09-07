import sys

soundtrigger_block = '''    <hal format="hidl">
        <name>android.hardware.soundtrigger</name>
        <transport>hwbinder</transport>
        <version>2.3</version>
        <interface>
            <name>ISoundTriggerHw</name>
            <instance>default</instance>
        </interface>
        <fqname>@2.3::ISoundTriggerHw/default</fqname>
    </hal>
'''

p = sys.argv[1]
with open(p) as f:
    c = f.read()

if "android.hardware.soundtrigger" in c:
    print("already present, not adding")
    sys.exit(0)

marker = "</manifest>"
idx = c.rfind(marker)
if idx == -1:
    print("ERROR: </manifest> not found")
    sys.exit(1)

c2 = c[:idx] + soundtrigger_block + c[idx:]
with open(p, 'w') as f:
    f.write(c2)
print("soundtrigger HAL entry restored")
