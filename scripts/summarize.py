"""Read every JUnit XML in a directory and print a Markdown table. Standard library only."""
import glob
import sys
import xml.etree.ElementTree as ET

rows = []
for path in sorted(glob.glob(sys.argv[1] + "/*.xml")):
    suite = ET.parse(path).getroot()
    if suite.tag == "testsuites":
        suite = suite[0]
    rows.append((path.rsplit("/", 1)[-1], suite.get("tests"), suite.get("failures"), suite.get("errors")))

print("| file | tests | failures | errors |")
print("|---|---|---|---|")
for r in rows:
    print("| " + " | ".join(r) + " |")
print(f"\n{len(rows)} result files")
