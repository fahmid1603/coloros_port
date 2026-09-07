import sys

p = sys.argv[1]
with open(p) as f:
    lines = f.readlines()

# Both occurrences are a single self-contained invoke-static call
# (void return, no move-result to clean up afterward) -- safe to
# delete the line wherever it appears in this file.
target = "invoke-static {v0, v1, v2}, Lcom/android/server/sensorprivacy/SensorPrivacyService$SensorPrivacyServiceImpl;->-$$Nest$muserSwitching(Lcom/android/server/sensorprivacy/SensorPrivacyService$SensorPrivacyServiceImpl;II)V"

kept = [l for l in lines if target not in l]
removed = len(lines) - len(kept)

if removed:
    with open(p, 'w') as f:
        f.writelines(kept)
print(f"----> removed {removed} userSwitching() call(s) from {p}")
