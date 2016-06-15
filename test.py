line = 'asdf fjdk; afed, fjedk, asdef , foo'
import re
line_new = re.split(r'[;,\s]\s*', line)
''.join(v + d for v, d in zip(values, delimiters))
