import os

references = """
. = 0x00000006; gUnknown_03000006 = .;
. = 0x00000008; gUnknown_03000008 = .;
. = 0x00000009; gUnknown_03000009 = .;
. = 0x0000000C; gUnknown_0300000C = .;
. = 0x00000010; gUnknown_03000010 = .;
. = 0x00000014; gUnknown_03000014 = .;
. = 0x00000018; gUnknown_03000018 = .;
. = 0x0000001A; gUnknown_0300001A = .;
. = 0x0000001C; gUnknown_0300001C = .;
. = 0x00000020; gUnknown_03000020 = .;
. = 0x00000021; gUnknown_03000021 = .;
. = 0x00000022; gUnknown_03000022 = .;
. = 0x00000023; gUnknown_03000023 = .;
. = 0x00000024; gUnknown_03000024 = .;
. = 0x00000025; gUnknown_03000025 = .;
. = 0x00000026; gUnknown_03000026 = .;
. = 0x00000028; gUnknown_03000028 = .;
. = 0x00000029; gUnknown_03000029 = .;
. = 0x0000002A; gUnknown_0300002A = .;
. = 0x0000002B; gUnknown_0300002B = .;
. = 0x0000002C; gUnknown_0300002C = .;
. = 0x0000002D; gUnknown_0300002D = .;
. = 0x0000002E; gUnknown_0300002E = .;
. = 0x0000002F; gUnknown_0300002F = .;
. = 0x00000030; gUnknown_03000030 = .;
. = 0x00000031; gUnknown_03000031 = .;
. = 0x00000032; gUnknown_03000032 = .;
. = 0x00000034; gUnknown_03000034 = .;
. = 0x00000035; gUnknown_03000035 = .;
. = 0x00000036; gUnknown_03000036 = .;
. = 0x00000038; gUnknown_03000038 = .;
. = 0x00000039; gUnknown_03000039 = .;
. = 0x0000003A; gUnknown_0300003A = .;
. = 0x0000003C; gUnknown_0300003C = .;
. = 0x0000003D; gUnknown_0300003D = .;
. = 0x0000003E; gUnknown_0300003E = .;
. = 0x0000003F; gUnknown_0300003F = .;
. = 0x00000040; gUnknown_03000040 = .;
. = 0x00000041; gUnknown_03000041 = .;
. = 0x00000042; gUnknown_03000042 = .;
. = 0x00000044; gUnknown_03000044 = .;
. = 0x00000046; gUnknown_03000046 = .;
. = 0x00000048; gUnknown_03000048 = .;
. = 0x00000049; gUnknown_03000049 = .;
. = 0x0000004A; gUnknown_0300004A = .;
. = 0x0000004B; gUnknown_0300004B = .;
. = 0x0000004C; gUnknown_0300004C = .;
. = 0x0000004D; gUnknown_0300004D = .;
. = 0x0000004E; gUnknown_0300004E = .;
. = 0x0000004F; gUnknown_0300004F = .;
. = 0x00000050; gUnknown_03000050 = .;
. = 0x00000051; gUnknown_03000051 = .;
. = 0x00000052; gUnknown_03000052 = .;
. = 0x00000054; gUnknown_03000054 = .;
. = 0x00000055; gUnknown_03000055 = .;
. = 0x00000056; gUnknown_03000056 = .;
. = 0x00000058; gUnknown_03000058 = .;
. = 0x00000059; gUnknown_03000059 = .;
. = 0x0000005A; gUnknown_0300005A = .;
. = 0x0000005B; gUnknown_0300005B = .;
. = 0x0000005C; gUnknown_0300005C = .;
. = 0x0000005D; gUnknown_0300005D = .;
. = 0x0000005E; gUnknown_0300005E = .;
. = 0x00000060; gUnknown_03000060 = .;
. = 0x00000061; gUnknown_03000061 = .;
. = 0x00000062; gUnknown_03000062 = .;
. = 0x00000063; gUnknown_03000063 = .;
. = 0x00000064; gUnknown_03000064 = .;
. = 0x00000065; gUnknown_03000065 = .;
. = 0x00000066; gUnknown_03000066 = .;
. = 0x00000068; gUnknown_03000068 = .;
. = 0x00000069; gUnknown_03000069 = .;
. = 0x0000006A; gUnknown_0300006A = .;
. = 0x0000006B; gUnknown_0300006B = .;
. = 0x0000006C; gUnknown_0300006C = .;
. = 0x0000006D; gUnknown_0300006D = .;
. = 0x0000006E; gUnknown_0300006E = .;
. = 0x00000070; gUnknown_03000070 = .;
. = 0x00000071; gUnknown_03000071 = .;
. = 0x00000072; gUnknown_03000072 = .;
. = 0x00000074; gUnknown_03000074 = .;
. = 0x00000075; gUnknown_03000075 = .;
. = 0x00000076; gUnknown_03000076 = .;
. = 0x00000078; gUnknown_03000078 = .;
. = 0x0000007A; gUnknown_0300007A = .;
. = 0x0000007C; gUnknown_0300007C = .;
. = 0x0000007D; gUnknown_0300007D = .;
. = 0x00000080; gUnknown_03000080 = .;
. = 0x00000081; gUnknown_03000081 = .;
. = 0x00000082; gUnknown_03000082 = .;
. = 0x00000084; gUnknown_03000084 = .;
. = 0x00000085; gUnknown_03000085 = .;
. = 0x00000086; gUnknown_03000086 = .;
. = 0x00000088; gUnknown_03000088 = .;
. = 0x00000089; gUnknown_03000089 = .;
. = 0x0000008A; gUnknown_0300008A = .;
. = 0x0000008C; gUnknown_0300008C = .;
. = 0x0000008D; gUnknown_0300008D = .;
. = 0x0000008E; gUnknown_0300008E = .;
. = 0x00000090; gUnknown_03000090 = .;
. = 0x00000091; gUnknown_03000091 = .;
. = 0x00000092; gUnknown_03000092 = .;
. = 0x00000094; gUnknown_03000094 = .;
. = 0x00000095; gUnknown_03000095 = .;
. = 0x00000098; gUnknown_03000098 = .;
. = 0x0000009C; gUnknown_0300009C = .;
. = 0x0000009E; gUnknown_0300009E = .;
. = 0x000000A0; gUnknown_030000A0 = .;
. = 0x000000A1; gUnknown_030000A1 = .;
. = 0x000000A2; gUnknown_030000A2 = .;
. = 0x000000A4; gUnknown_030000A4 = .;
. = 0x000000A8; gUnknown_030000A8 = .;
. = 0x000000A9; gUnknown_030000A9 = .;
. = 0x000000AA; gUnknown_030000AA = .;
. = 0x000000AC; gUnknown_030000AC = .;
. = 0x000000B0; gUnknown_030000B0 = .;
. = 0x000000B1; gUnknown_030000B1 = .;
. = 0x000000B2; gUnknown_030000B2 = .;
. = 0x000000B4; gUnknown_030000B4 = .;
. = 0x000000B5; gUnknown_030000B5 = .;
. = 0x000000B6; gUnknown_030000B6 = .;
. = 0x000000B8; gUnknown_030000B8 = .;
. = 0x000000BA; gUnknown_030000BA = .;
. = 0x000000BC; gUnknown_030000BC = .;
. = 0x000000BD; gUnknown_030000BD = .;
. = 0x000000BE; gUnknown_030000BE = .;
. = 0x000000BF; gUnknown_030000BF = .;
. = 0x000000C0; gUnknown_030000C0 = .;
. = 0x000000C1; gUnknown_030000C1 = .;
. = 0x000000C2; gUnknown_030000C2 = .;
. = 0x000000C4; gUnknown_030000C4 = .;
. = 0x000000C5; gUnknown_030000C5 = .;
. = 0x000000C8; gUnknown_030000C8 = .;
. = 0x000000CC; gUnknown_030000CC = .;
. = 0x000000D0; gUnknown_030000D0 = .;
. = 0x000000D1; gUnknown_030000D1 = .;
. = 0x000000D4; gUnknown_030000D4 = .;
. = 0x000000D6; gUnknown_030000D6 = .;
. = 0x000000D8; gUnknown_030000D8 = .;
. = 0x000000D9; gUnknown_030000D9 = .;
. = 0x000000DC; gUnknown_030000DC = .;
. = 0x000000E0; gUnknown_030000E0 = .;
. = 0x000000E1; gUnknown_030000E1 = .;
. = 0x000000E2; gUnknown_030000E2 = .;
. = 0x000000E4; gUnknown_030000E4 = .;
. = 0x000000E8; gUnknown_030000E8 = .;
. = 0x000000EB; gUnknown_030000EB = .;
. = 0x000000EC; gUnknown_030000EC = .;
. = 0x000000F0; gUnknown_030000F0 = .;
. = 0x000000F1; gUnknown_030000F1 = .;
. = 0x000000F2; gUnknown_030000F2 = .;
. = 0x000000F4; gUnknown_030000F4 = .;
. = 0x000000F6; gUnknown_030000F6 = .;
. = 0x000000F8; gUnknown_030000F8 = .;
. = 0x000000F9; gUnknown_030000F9 = .;
. = 0x000000FA; gUnknown_030000FA = .;
. = 0x000000FC; gUnknown_030000FC = .;
. = 0x000000FD; gUnknown_030000FD = .;
. = 0x000000FE; gUnknown_030000FE = .;
. = 0x00000100; gUnknown_03000100 = .;
. = 0x00000101; gUnknown_03000101 = .;
. = 0x00000102; gUnknown_03000102 = .;
. = 0x00000104; gUnknown_03000104 = .;
. = 0x00000105; gUnknown_03000105 = .;
. = 0x00000106; gUnknown_03000106 = .;
. = 0x0000010A; gUnknown_0300010A = .;
. = 0x0000010C; gUnknown_0300010C = .;
. = 0x0000010D; gUnknown_0300010D = .;
. = 0x0000010E; gUnknown_0300010E = .;
. = 0x00000110; gUnknown_03000110 = .;
. = 0x00000112; gUnknown_03000112 = .;
. = 0x00000114; gUnknown_03000114 = .;
. = 0x0000011C; gUnknown_0300011C = .;
. = 0x00000120; gUnknown_03000120 = .;
. = 0x00000121; gUnknown_03000121 = .;
. = 0x00000124; gUnknown_03000124 = .;
. = 0x00000128; gUnknown_03000128 = .;
. = 0x00000129; gUnknown_03000129 = .;
. = 0x0000012C; gUnknown_0300012C = .;
. = 0x00000130; gUnknown_03000130 = .;
. = 0x00000131; gUnknown_03000131 = .;
. = 0x00000132; gUnknown_03000132 = .;
. = 0x00000134; gUnknown_03000134 = .;
. = 0x0000013C; gUnknown_0300013C = .;
. = 0x0000013E; gUnknown_0300013E = .;
. = 0x00000140; gUnknown_03000140 = .;
. = 0x00000141; gUnknown_03000141 = .;
. = 0x00000142; gUnknown_03000142 = .;
. = 0x00000143; gUnknown_03000143 = .;
. = 0x00000144; gUnknown_03000144 = .;
. = 0x00000148; gUnknown_03000148 = .;
. = 0x0000014C; gUnknown_0300014C = .;
. = 0x0000014D; gUnknown_0300014D = .;
. = 0x0000014E; gUnknown_0300014E = .;
. = 0x00000150; gUnknown_03000150 = .;
. = 0x00000154; gUnknown_03000154 = .;
. = 0x00000155; gUnknown_03000155 = .;
. = 0x00000158; gUnknown_03000158 = .;
. = 0x00000159; gUnknown_03000159 = .;
. = 0x0000015C; gUnknown_0300015C = .;
. = 0x0000015D; gUnknown_0300015D = .;
. = 0x0000015E; gUnknown_0300015E = .;
. = 0x0000015F; gUnknown_0300015F = .;
. = 0x00000160; gUnknown_03000160 = .;
. = 0x00000161; gUnknown_03000161 = .;
. = 0x00000163; gUnknown_03000163 = .;
. = 0x00000164; gUnknown_03000164 = .;
. = 0x00000168; gUnknown_03000168 = .;
. = 0x00000169; gUnknown_03000169 = .;
. = 0x0000016C; gUnknown_0300016C = .;
. = 0x00000170; gUnknown_03000170 = .;
. = 0x00000174; gUnknown_03000174 = .;
. = 0x00000178; gUnknown_03000178 = .;
. = 0x0000017C; gUnknown_0300017C = .;
. = 0x00000180; gUnknown_03000180 = .;
. = 0x00000186; gUnknown_03000186 = .;
. = 0x00000188; gUnknown_03000188 = .;
. = 0x0000018C; gUnknown_0300018C = .;
. = 0x0000019C; gUnknown_0300019C = .;
. = 0x000001A0; gUnknown_030001A0 = .;
. = 0x000001A4; gUnknown_030001A4 = .;
. = 0x000001AC; gUnknown_030001AC = .;
. = 0x000001AD; gUnknown_030001AD = .;
. = 0x000001B0; gUnknown_030001B0 = .;
. = 0x000001B2; gUnknown_030001B2 = .;
. = 0x000001B4; gUnknown_030001B4 = .;
. = 0x000001B8; gUnknown_030001B8 = .;
. = 0x000001BC; gUnknown_030001BC = .;
. = 0x000001BD; gUnknown_030001BD = .;
. = 0x000001BE; gUnknown_030001BE = .;
. = 0x000001C0; gUnknown_030001C0 = .;
. = 0x000001C1; gUnknown_030001C1 = .;
. = 0x000001C2; gUnknown_030001C2 = .;
. = 0x000001C4; gUnknown_030001C4 = .;
. = 0x000001C8; gUnknown_030001C8 = .;
. = 0x000001C9; gUnknown_030001C9 = .;
. = 0x000001D4; gUnknown_030001D4 = .;
. = 0x000001D5; gUnknown_030001D5 = .;
. = 0x000001D8; gUnknown_030001D8 = .;
. = 0x000001D9; gUnknown_030001D9 = .;
. = 0x000001E0; gUnknown_030001E0 = .;
. = 0x000001E4; gUnknown_030001E4 = .;
. = 0x000001E8; gUnknown_030001E8 = .;
. = 0x000001EC; gUnknown_030001EC = .;
. = 0x000001F0; gUnknown_030001F0 = .;
. = 0x000001F2; gUnknown_030001F2 = .;
. = 0x000001F8; gUnknown_030001F8 = .;
. = 0x000001FC; gUnknown_030001FC = .;
. = 0x00000200; gUnknown_03000200 = .;
. = 0x00000201; gUnknown_03000201 = .;
. = 0x00000202; gUnknown_03000202 = .;
. = 0x00000203; gUnknown_03000203 = .;
. = 0x00000204; gUnknown_03000204 = .;
. = 0x00000205; gUnknown_03000205 = .;
. = 0x00000206; gUnknown_03000206 = .;
. = 0x0000020C; gUnknown_0300020C = .;
. = 0x00000210; gUnknown_03000210 = .;
. = 0x00000214; gUnknown_03000214 = .;
. = 0x0000021C; gUnknown_0300021C = .;
. = 0x00000228; gUnknown_03000228 = .;
. = 0x0000022C; gUnknown_0300022C = .;
. = 0x00000230; gUnknown_03000230 = .;
. = 0x00000234; gUnknown_03000234 = .;
. = 0x00000236; gUnknown_03000236 = .;
. = 0x00000238; gUnknown_03000238 = .;
. = 0x0000023A; gUnknown_0300023A = .;
. = 0x0000023C; gUnknown_0300023C = .;
. = 0x00000240; gUnknown_03000240 = .;
. = 0x00000244; gUnknown_03000244 = .;
. = 0x00000245; gUnknown_03000245 = .;
. = 0x00000246; gUnknown_03000246 = .;
. = 0x00000247; gUnknown_03000247 = .;
. = 0x00000248; gUnknown_03000248 = .;
. = 0x00000249; gUnknown_03000249 = .;
. = 0x0000024C; gUnknown_0300024C = .;
. = 0x00000250; gUnknown_03000250 = .;
. = 0x00000252; gUnknown_03000252 = .;
. = 0x00000253; gUnknown_03000253 = .;
. = 0x00000254; gUnknown_03000254 = .;
. = 0x00000258; gUnknown_03000258 = .;
. = 0x00000260; gUnknown_03000260 = .;
. = 0x0000026C; gUnknown_0300026C = .;
. = 0x00000270; gUnknown_03000270 = .;
. = 0x00000278; gUnknown_03000278 = .;
. = 0x0000027C; gUnknown_0300027C = .;
. = 0x0000027E; gUnknown_0300027E = .;
. = 0x00000280; gUnknown_03000280 = .;
. = 0x00000284; gUnknown_03000284 = .;
. = 0x00000288; gUnknown_03000288 = .;
. = 0x000002A0; gUnknown_030002A0 = .;
. = 0x000002A4; gUnknown_030002A4 = .;
. = 0x000002A8; gUnknown_030002A8 = .;
. = 0x000002A9; gUnknown_030002A9 = .;
. = 0x000002AA; gUnknown_030002AA = .;
. = 0x000002B0; gUnknown_030002B0 = .;
. = 0x000002B4; gUnknown_030002B4 = .;
. = 0x000002B6; gUnknown_030002B6 = .;
. = 0x000002CC; gUnknown_030002CC = .;
. = 0x000002D0; gUnknown_030002D0 = .;
. = 0x000002D4; gUnknown_030002D4 = .;
. = 0x000002D6; gUnknown_030002D6 = .;
. = 0x000002D8; gUnknown_030002D8 = .;
. = 0x000002DC; gUnknown_030002DC = .;
. = 0x000002DD; gUnknown_030002DD = .;
. = 0x000002E0; gUnknown_030002E0 = .;
. = 0x000002E4; gUnknown_030002E4 = .;
. = 0x00000300; gUnknown_03000300 = .;
. = 0x00000301; gUnknown_03000301 = .;
. = 0x0000030C; gUnknown_0300030C = .;
. = 0x00000310; gUnknown_03000310 = .;
. = 0x00000312; gUnknown_03000312 = .;
. = 0x00000314; gUnknown_03000314 = .;
. = 0x00000316; gUnknown_03000316 = .;
. = 0x00000317; gUnknown_03000317 = .;
. = 0x0000031C; gUnknown_0300031C = .;
. = 0x0000031E; gUnknown_0300031E = .;
. = 0x0000031F; gUnknown_0300031F = .;
. = 0x00000320; gUnknown_03000320 = .;
. = 0x00000321; gUnknown_03000321 = .;
. = 0x0000032C; gUnknown_0300032C = .;
. = 0x00000330; gUnknown_03000330 = .;
. = 0x00000338; gUnknown_03000338 = .;
. = 0x0000033C; gUnknown_0300033C = .;
. = 0x00000344; gUnknown_03000344 = .;
. = 0x0000034C; gUnknown_0300034C = .;
. = 0x00000350; gUnknown_03000350 = .;
. = 0x00000351; gUnknown_03000351 = .;
. = 0x00000358; gUnknown_03000358 = .;
. = 0x0000035B; gUnknown_0300035B = .;
. = 0x0000035C; gUnknown_0300035C = .;
. = 0x00000360; gUnknown_03000360 = .;
. = 0x00000363; gUnknown_03000363 = .;
. = 0x00000364; gUnknown_03000364 = .;
. = 0x0000036C; gUnknown_0300036C = .;
. = 0x0000036E; gUnknown_0300036E = .;
. = 0x00000370; gUnknown_03000370 = .;
. = 0x00000372; gUnknown_03000372 = .;
. = 0x00000374; gUnknown_03000374 = .;
. = 0x0000037C; gUnknown_0300037C = .;
. = 0x0000037E; gUnknown_0300037E = .;
. = 0x0000038C; gUnknown_0300038C = .;
. = 0x0000038E; gUnknown_0300038E = .;
. = 0x00000390; gUnknown_03000390 = .;
. = 0x00000394; gUnknown_03000394 = .;
. = 0x00000395; gUnknown_03000395 = .;
. = 0x00000396; gUnknown_03000396 = .;
. = 0x00000398; gUnknown_03000398 = .;
. = 0x000003A0; gUnknown_030003A0 = .;
. = 0x000003A4; gUnknown_030003A4 = .;
. = 0x000003A5; gUnknown_030003A5 = .;
. = 0x000003A6; gUnknown_030003A6 = .;
. = 0x000003AA; gUnknown_030003AA = .;
. = 0x000003AC; gUnknown_030003AC = .;
. = 0x000003B8; gUnknown_030003B8 = .;
. = 0x000003BA; gUnknown_030003BA = .;
. = 0x000003BB; gUnknown_030003BB = .;
. = 0x000003C0; gUnknown_030003C0 = .;
. = 0x000003C1; gUnknown_030003C1 = .;
. = 0x000003C3; gUnknown_030003C3 = .;
. = 0x000003C4; gUnknown_030003C4 = .;
. = 0x000003C5; gUnknown_030003C5 = .;
. = 0x000003C6; gUnknown_030003C6 = .;
. = 0x000003C7; gUnknown_030003C7 = .;
. = 0x000003C8; gUnknown_030003C8 = .;
. = 0x000003CA; gUnknown_030003CA = .;
. = 0x000003CC; gUnknown_030003CC = .;
. = 0x000003D4; gUnknown_030003D4 = .;
. = 0x000003D8; gUnknown_030003D8 = .;
. = 0x000003DC; gUnknown_030003DC = .;
. = 0x000003E4; gUnknown_030003E4 = .;
. = 0x000003FC; gUnknown_030003FC = .;
"""

vars_to_iwram = {}

for line in references.split(";\n"):
    if not line:
        continue

    var = line.split(';')[1].split("= .")[0].strip()
    offset = hex(int(var.split('gUnknown_03')[1], 16)).upper().replace('X', 'x')
    vars_to_iwram[var] = f"IWRAM_START + {offset}"


for code_file in os.listdir('asm'):
    if not code_file.endswith('.s'):
        continue

    new_data = ""

    with open("asm/" + code_file) as f_asm:
        new_data = "".join(f_asm.readlines())
    
    for var in vars_to_iwram:
        new_data = new_data.replace(var, vars_to_iwram[var])
    
    with open("asm/" + code_file, "w") as f_asm:
        f_asm.write(new_data)
