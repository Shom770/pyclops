import shlex
import sys

print(shlex.split(
    " ".join(map(shlex.quote, sys.argv))
))