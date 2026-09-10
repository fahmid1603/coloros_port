import sys

OLD = """on property:ro.boot.hardware=qcom && property:persist.radio.multisim.config=dsds
    stop qti-modem-daemon-0
    stop qti-modem-daemon-1
    start qti-modem-daemon-0
    start qti-modem-daemon-1"""

NEW = """on property:ro.boot.hardware=qcom && property:persist.radio.multisim.config=dsds
    stop qti-modem-daemon-0
    stop qti-modem-daemon-1
    start qti-modem-daemon-0
    setprop persist.vendor.radio.daemon1_delay_trigger 1

on property:persist.vendor.radio.daemon1_delay_trigger=1
    start qti-modem-daemon-1
    setprop persist.vendor.radio.daemon1_delay_trigger 0"""

def main(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(OLD)
    print(f"matches found: {count}")
    if count != 1:
        print("ERROR: expected exactly 1 match. Not patching.")
        sys.exit(1)
    content = content.replace(OLD, NEW)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("----> subsys_daemon.rc race-condition patch applied (dsds trigger de-raced)")

if __name__ == "__main__":
    main(sys.argv[1])
