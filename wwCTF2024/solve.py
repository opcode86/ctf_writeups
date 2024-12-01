from z3 import *

array_1 = [252, 174, 221, 116, 74, 140, 110, 29]
array_2 = [166, 74, 96, 96, 218, 220, 56, 111]

password = [BitVec("c_{}".format(i), 32) for i in range(38)]

s = Solver()

for i in range(38):
    s.add(password[i] >= 0, password[i] <= 255)

s.add(103569 == (69 * ((69 + (array_2[0] * (array_1[0] ^ ((password[37]) + (password[0]))))) ^ ((array_2[0] + (array_1[0] * (password[1] ^ password[0]))) ^ 14))))
s.add(1410273 == (213 * ((57 + (array_2[1] * (array_1[1] ^ ((password[0]) + (password[1]))))) ^ ((array_2[1] + (array_1[1] * (password[2] ^ password[1]))) ^ 188))))
s.add(1194466 == (182 * ((38 + (array_2[2] * (array_1[2] ^ ((password[1]) + (password[2]))))) ^ ((array_2[2] + (array_1[2] * (password[3] ^ password[2]))) ^ 236))))
s.add(3304794 == (254 * ((248 + (array_2[3] * (array_1[3] ^ ((password[2]) + (password[3]))))) ^ ((array_2[3] + (array_1[3] * (password[4] ^ password[3]))) ^ 83))))
s.add(4250975 == (115 * ((101 + (array_2[4] * (array_1[4] ^ ((password[3]) + (password[4]))))) ^ ((array_2[4] + (array_1[4] * (password[5] ^ password[4]))) ^ 168))))
s.add(1434672 == (144 * ((162 + (array_2[5] * (array_1[5] ^ ((password[4]) + (password[5]))))) ^ ((array_2[5] + (array_1[5] * (password[6] ^ password[5]))) ^ 205))))
s.add(1657074 == (151 * ((125 + (array_2[6] * (array_1[6] ^ ((password[5]) + (password[6]))))) ^ ((array_2[6] + (array_1[6] * (password[7] ^ password[6]))) ^ 245))))
s.add(792390 == (61 * ((139 + (array_2[7] * (array_1[7] ^ ((password[6]) + (password[7]))))) ^ ((array_2[7] + (array_1[7] * (password[8] ^ password[7]))) ^ 49))))
s.add(55890 == (243 * ((182 + (array_2[0] * (array_1[0] ^ ((password[7]) + (password[8]))))) ^ ((array_2[0] + (array_1[0] * (password[9] ^ password[8]))) ^ 72))))
s.add(468292 == (44 * ((152 + (array_2[1] * (array_1[1] ^ ((password[8]) + (password[9]))))) ^ ((array_2[1] + (array_1[1] * (password[10] ^ password[9]))) ^ 239))))
s.add(4570092 == (222 * ((128 + (array_2[2] * (array_1[2] ^ ((password[9]) + (password[10]))))) ^ ((array_2[2] + (array_1[2] * (password[11] ^ password[10]))) ^ 121))))
s.add(4415362 == (226 * ((209 + (array_2[3] * (array_1[3] ^ ((password[10]) + (password[11]))))) ^ ((array_2[3] + (array_1[3] * (password[12] ^ password[11]))) ^ 32))))
s.add(4538278 == (122 * ((209 + (array_2[4] * (array_1[4] ^ ((password[11]) + (password[12]))))) ^ ((array_2[4] + (array_1[4] * (password[13] ^ password[12]))) ^ 222))))
s.add(209304 == (24 * ((39 + (array_2[5] * (array_1[5] ^ ((password[12]) + (password[13]))))) ^ ((array_2[5] + (array_1[5] * (password[14] ^ password[13]))) ^ 34))))
s.add(1588748 == (161 * ((235 + (array_2[6] * (array_1[6] ^ ((password[13]) + (password[14]))))) ^ ((array_2[6] + (array_1[6] * (password[15] ^ password[14]))) ^ 69))))
s.add(3339440 == (208 * ((58 + (array_2[7] * (array_1[7] ^ ((password[14]) + (password[15]))))) ^ ((array_2[7] + (array_1[7] * (password[16] ^ password[15]))) ^ 49))))
s.add(952128 == (72 * ((214 + (array_2[0] * (array_1[0] ^ ((password[15]) + (password[16]))))) ^ ((array_2[0] + (array_1[0] * (password[17] ^ password[16]))) ^ 118))))
s.add(2922543 == (117 * ((19 + (array_2[1] * (array_1[1] ^ ((password[16]) + (password[17]))))) ^ ((array_2[1] + (array_1[1] * (password[18] ^ password[17]))) ^ 252))))
s.add(312864 == (16 * ((249 + (array_2[2] * (array_1[2] ^ ((password[17]) + (password[18]))))) ^ ((array_2[2] + (array_1[2] * (password[19] ^ password[18]))) ^ 134))))
s.add(929380 == (31 * ((191 + (array_2[3] * (array_1[3] ^ ((password[18]) + (password[19]))))) ^ ((array_2[3] + (array_1[3] * (password[20] ^ password[19]))) ^ 63))))
s.add(8851407 == (197 * ((156 + (array_2[4] * (array_1[4] ^ ((password[19]) + (password[20]))))) ^ ((array_2[4] + (array_1[4] * (password[21] ^ password[20]))) ^ 109))))
s.add(1846515 == (155 * ((125 + (array_2[5] * (array_1[5] ^ ((password[20]) + (password[21]))))) ^ ((array_2[5] + (array_1[5] * (password[22] ^ password[21]))) ^ 28))))
s.add(2953720 == (220 * ((33 + (array_2[6] * (array_1[6] ^ ((password[21]) + (password[22]))))) ^ ((array_2[6] + (array_1[6] * (password[23] ^ password[22]))) ^ 253))))
s.add(3463992 == (237 * ((205 + (array_2[7] * (array_1[7] ^ ((password[22]) + (password[23]))))) ^ ((array_2[7] + (array_1[7] * (password[24] ^ password[23]))) ^ 207))))
s.add(1280928 == (44 * ((101 + (array_2[0] * (array_1[0] ^ ((password[23]) + (password[24]))))) ^ ((array_2[0] + (array_1[0] * (password[25] ^ password[24]))) ^ 249))))
s.add(127560 == (30 * ((5 + (array_2[1] * (array_1[1] ^ ((password[24]) + (password[25]))))) ^ ((array_2[1] + (array_1[1] * (password[26] ^ password[25]))) ^ 159))))
s.add(197301 == (13 * ((208 + (array_2[2] * (array_1[2] ^ ((password[25]) + (password[26]))))) ^ ((array_2[2] + (array_1[2] * (password[27] ^ password[26]))) ^ 163))))
s.add(386910 == (18 * ((36 + (array_2[3] * (array_1[3] ^ ((password[26]) + (password[27]))))) ^ ((array_2[3] + (array_1[3] * (password[28] ^ password[27]))) ^ 227))))
s.add(114738 == (39 * ((226 + (array_2[4] * (array_1[4] ^ ((password[27]) + (password[28]))))) ^ ((array_2[4] + (array_1[4] * (password[29] ^ password[28]))) ^ 64))))
s.add(742775 == (55 * ((23 + (array_2[5] * (array_1[5] ^ ((password[28]) + (password[29]))))) ^ ((array_2[5] + (array_1[5] * (password[30] ^ password[29]))) ^ 158))))
s.add(501690 == (42 * ((17 + (array_2[6] * (array_1[6] ^ ((password[29]) + (password[30]))))) ^ ((array_2[6] + (array_1[6] * (password[31] ^ password[30]))) ^ 206))))
s.add(4778284 == (196 * ((78 + (array_2[7] * (array_1[7] ^ ((password[30]) + (password[31]))))) ^ ((array_2[7] + (array_1[7] * (password[32] ^ password[31]))) ^ 59))))
s.add(272085 == (55 * ((11 + (array_2[0] * (array_1[0] ^ ((password[31]) + (password[32]))))) ^ ((array_2[0] + (array_1[0] * (password[33] ^ password[32]))) ^ 96))))
s.add(1371072 == (192 * ((79 + (array_2[1] * (array_1[1] ^ ((password[32]) + (password[33]))))) ^ ((array_2[1] + (array_1[1] * (password[34] ^ password[33]))) ^ 122))))
s.add(2206236 == (148 * ((32 + (array_2[2] * (array_1[2] ^ ((password[33]) + (password[34]))))) ^ ((array_2[2] + (array_1[2] * (password[35] ^ password[34]))) ^ 236))))
s.add(4155088 == (161 * ((215 + (array_2[3] * (array_1[3] ^ ((password[34]) + (password[35]))))) ^ ((array_2[3] + (array_1[3] * (password[36] ^ password[35]))) ^ 123))))
s.add(11333348 == (247 * ((90 + (array_2[4] * (array_1[4] ^ ((password[35]) + (password[36]))))) ^ ((array_2[4] + (array_1[4] * (password[37] ^ password[36]))) ^ 182))))
s.add(2257580 == (130 * ((116 + (array_2[5] * (array_1[5] ^ ((password[36]) + (password[37]))))) ^ ((array_2[5] + (array_1[5] * (password[0] ^ password[37]))) ^ 182))))

if s.check() == sat:
    m = s.model()
    sol = ''.join([chr(m[password[i]].as_long()) for i in range(38)])
    print("Password:", sol) # wwf{m45h1r0_w41fu_>_<_50_cu73~~_4hw4_}
else:
    print("No solution found.")
