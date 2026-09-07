import re, sys

p = sys.argv[1]
with open(p) as f:
    c = f.read()

before = c

# Each service start is a self-contained, trace-bookended block:
#   const-string v0, "<TraceName>"
#   invoke-virtual {v2, v0}, ...;->traceBegin(...)V
#   ... get service manager, load class, call startService ...
#   invoke-virtual {v2}, ...;->traceEnd()V
# Safe to remove wholesale: v0/v3 get freshly reassigned by whatever
# code follows in every case observed, v1/v2 (SystemServer instance,
# trace helper) are untouched.
for trace_name in ("StartSoundTriggerMiddlewareService", "StartSoundTrigger"):
    pattern = (
        r'\n\s*const-string v0, "' + re.escape(trace_name) + r'"\n'
        r'.*?'
        r'invoke-virtual \{v2\}, Lcom/android/server/utils/TimingsTraceAndSlog;->traceEnd\(\)V\n'
    )
    c2 = re.sub(pattern, '\n', c, count=1, flags=re.S)
    if c2 == c:
        print(f"----> WARNING: block for '{trace_name}' not found, nothing removed")
    else:
        print(f"----> removed startService block: {trace_name}")
    c = c2

if c != before:
    with open(p, 'w') as f:
        f.write(c)
