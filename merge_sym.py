import re, sys

def split(t):
    head = t[:t.index('(symbol ')]
    blocks, depth, start = {}, 0, None
    for i, ch in enumerate(t):
        if ch == '(':
            depth += 1
            if depth == 2 and t.startswith('(symbol ', i):
                start = i
        elif ch == ')':
            if depth == 2 and start is not None:
                b = t[start:i+1]
                blocks[re.match(r'\(symbol "([^"]+)"', b).group(1)] = b
                start = None
            depth -= 1
    return head, blocks

a_head, a = split(open('side_a.kicad_sym', encoding='utf-8').read())
_, b = split(open('side_b.kicad_sym', encoding='utf-8').read())

merged = dict(a)
for name, blk in b.items():
    if name in merged and merged[name] != blk:
        print(f"WARNING: '{name}' differs between sides, keeping side A")
    merged.setdefault(name, blk)

out = a_head + "\n\n  ".join(merged.values()) + "\n)\n"
open('merged.kicad_sym', 'w', encoding='utf-8', newline='\n').write(out)
print("Wrote", len(merged), "symbols:", ", ".join(merged))