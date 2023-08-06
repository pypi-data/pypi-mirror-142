# coding=utf-8
#!/usr/bin/env python3
import uuid


def ascii_to_hex_str(ascii):
    li = []
    ascii = ascii.replace(' ', '')
    for c in ascii:
        li.append('%02X' % ord(c))
    return ' '.join(li)

def hex_str_to_ascii(hex_str, seg='', s_count=2):
    hex_li = hex_str.split(' ')
    len_li = len(hex_li)
    li = []
    j = 0
    s = ''
    for i in range(len_li):
        s += chr(int(hex_li[i], 16))
        j += 1
        if j == s_count:
            li.append(s)
            s = ''
            j = 0
    else:
        if s:
            li.append(s)
    return seg.join(li)

def xhr_code(ins):
    li = ins.split(' ')
    n_li = [int(x, 16) for x in li]
    tmp = 0
    for n in n_li:
        tmp = tmp ^ n
    return '%02X' % tmp

def split_str(s, sep=' '):
    li = []
    tmp = ''
    for i in range(len(s)):
        tmp += s[i]
        i += 1
        if i % 2 == 0:
            li.append(tmp)
            tmp = ''
    else:
        if tmp:
            li.append(tmp)
    return sep.join(li)

def sum_code(ins):
    if isinstance(ins, str):
        li = ins.split(' ')
    else:
        li = ins
    n_li = [int(x, 16) for x in li]
    return '%02X' % (sum(n_li) % 256)

def to_sign_int(val_str):
    val_str = val_str.replace(' ', '')
    b_len = len(val_str) * 4
    if len(val_str) < int(b_len/4):
        return '0'
    val_str = val_str[:int(b_len/4)]
    val_num = int(val_str, 16)
    s_num = eval('0b1' + (b_len -1) * '0')
    v_num = eval('0b0' + (b_len - 1) * '1')
    symbol = val_num & s_num
    if symbol == 0:
        return val_num & v_num
    else:
        return - (((val_num & v_num) ^ v_num) + 1)

from ctypes import *
def convert(s):
    i = int(s, 16)  # convert from hex to a Python int
    cp = pointer(c_int(i))  # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return float('%.3f' % fp.contents.value)  # dereference the pointer, get the float

def to_char_with_2(st):
    res = chr(int(st))
    return res

def get_mac_addr():
    mac_addr = uuid.UUID(int=uuid.getnode()).hex[-12]
    mac_addr = split_str(mac_addr, '-')
    return mac_addr