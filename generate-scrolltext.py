all_symbols = " ◢◣◤◥▄▀█"

phrase = "THE20C CAN HAZ AWESOME SCROLLER TOO - 6502 RULEZ"
phrase = 20*" " + phrase + 20*" "

char_lines = {
    # initialize with the space, which is the only codepoint that I'm making one LCD char wide
    " ": [" ", " ", " ", " "]
}

with open("chars.txt", 'r') as i_file:
    while l := i_file.readline():
        l = l.strip()
        c = [(i_file.readline().rstrip() + "    ")[:4] for n in range(4)]
        char_lines[l] = c

for ln in range(4):
    line = "".join(char_lines[c][ln] for c in phrase)
    print(";", line)

for ln in range(4):
    line = "".join(char_lines[c][ln] for c in phrase)
    print("scroll_linea_%d:" % ln)
    chars = []
    for c in line:
        n = all_symbols.find(c)
        chars.append("$%02x" % n)
    print("  .byte", ", ".join(chars))
