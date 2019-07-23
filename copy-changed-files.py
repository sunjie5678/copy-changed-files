from subprocess import check_output
import sys

out = check_output(["ntpq", "-p"])

print(out)