key = "Welcome To ISITDTU CTF"
local a =
    loadstring(
    (function(b, c)
        function bxor(d, e)
            local f = {{0, 1}, {1, 0}}
            local g = 1
            local h = 0
            while d > 0 or e > 0 do
                h = h + f[d % 2 + 1][e % 2 + 1] * g
                d = math.floor(d / 2)
                e = math.floor(e / 2)
                g = g * 2
            end
            return h
        end
        local function i(b)
            local j = {}
            local k = 1
            local l = b[k]
            while l >= 0 do
                j[k] = b[l + 1]
                k = k + 1
                l = b[k]
            end
            print(j)
            return j
        end
        local function m(b, c)
            if #c <= 0 then
                return {}
            end
            local k = 1
            local n = 1
            for k = 1, #b do
                b[k] = bxor(b[k], string.byte(c, n))
                n = n + 1
                if n > #c then
                    n = 1
                end
            end
            return b
        end
        local function o(b)
            local j = ""
            for k = 1, #b do
                j = j .. string.char(b[k])
            end
            return j
        end
        return o(m(i(b), c))
    end)(
        {
            1104,
            1428,
            1516,
            829,
            1304,
            1525,
            1358,
            1264,
            1162,
            1031,
            932,
            1432,
            1077,
            1258,
            899,
            890,
            1337,
            815,
            1506,
            1297,
            865,
            1540,
            1454,
            1482,
            1233,
            787,
            1572,
            1320,
            1316,
            1093,
            994,
            1054,
            1145,
            749,
            1309,
            948,
            1384,
            1228,
            942,
            1518,
            818,
            1187,
            908,
            1290,
            1449,
            1234,
            1419,
            768,
            1536,
            827,
            1175,
            1545,
            1005,
            1169,
            1171,
            1215,
            1380,
            1327,
            1369,
            1034,
            1554,
            978,
            799,
            903,
            1391,
            997,
            819,
            1230,
            1457,
            1333,
            766,
            777,
            921,
            1042,
            992,
            1225,
            765,
            904,
            769,
            964,
            1209,
            1447,
            840,
            790,
            981,
            950,
            1015,
            1273,
            1043,
            1173,
            1462,
            1334,
            1028,
            750,
            1520,
            972,
            1014,
            863,
            864,
            824,
            1168,
            1314,
            1194,
            1483,
            1480,
            974,
            1027,
            746,
            1416,
            1238,
            1521,
            949,
            1567,
            1099,
            1490,
            1079,
            1134,
            1427,
            848,
            1539,
            1068,
            1033,
            1284,
            907,
            811,
            1121,
            1362,
            1392,
            915,
            1319,
            1044,
            1004,
            1198,
            1534,
            776,
            869,
            764,
            762,
            1346,
            1299,
            1091,
            1183,
            1308,
            917,
            1430,
            1374,
            1163,
            786,
            1558,
            778,
            1371,
            820,
            1562,
            1353,
            1328,
            1002,
            1544,
            918,
            1513,
            1381,
            723,
            1303,
            1288,
            1263,
            1122,
            945,
            1083,
            886,
            1123,
            1085,
            1512,
            724,
            1261,
            1356,
            759,
            1345,
            752,
            1301,
            1127,
            785,
            1058,
            1366,
            1265,
            1165,
            1280,
            916,
            928,
            1213,
            1176,
            1095,
            748,
            1268,
            1156,
            1203,
            761,
            1098,
            1296,
            1489,
            1013,
            1006,
            1335,
            853,
            963,
            1224,
            779,
            1084,
            851,
            1370,
            1070,
            757,
            1443,
            788,
            1125,
            1564,
            760,
            875,
            1322,
            803,
            1221,
            774,
            1332,
            1128,
            783,
            728,
            1522,
            1341,
            1310,
            1236,
            1406,
            888,
            734,
            1281,
            1051,
            1435,
            1115,
            860,
            919,
            1497,
            1001,
            1394,
            1086,
            1307,
            729,
            789,
            1277,
            1479,
            1167,
            1188,
            1409,
            1429,
            1218,
            1063,
            1456,
            922,
            1298,
            1541,
            1402,
            1325,
            1408,
            1563,
            953,
            1017,
            952,
            1344,
            1326,
            1276,
            975,
            1352,
            923,
            791,
            1242,
            1285,
            1202,
            1158,
            976,
            1143,
            901,
            1078,
            1302,
            1237,
            1255,
            1232,
            784,
            1393,
            1021,
            835,
            1272,
            1019,
            1174,
            773,
            808,
            1460,
            960,
            968,
            1313,
            1474,
            1164,
            813,
            957,
            1287,
            850,
            1550,
            940,
            1231,
            1069,
            1141,
            874,
            1177,
            825,
            920,
            806,
            1458,
            859,
            1441,
            843,
            730,
            1549,
            954,
            1126,
            1398,
            1501,
            1485,
            1039,
            878,
            812,
            1131,
            961,
            1388,
            821,
            1349,
            846,
            1495,
            1472,
            990,
            937,
            914,
            993,
            1208,
            1509,
            1323,
            1414,
            781,
            1066,
            1367,
            807,
            1235,
            1072,
            1532,
            1220,
            1090,
            1340,
            1087,
            1294,
            1553,
            1153,
            1137,
            1431,
            1389,
            1470,
            832,
            735,
            1191,
            1331,
            897,
            736,
            1147,
            1080,
            1048,
            1436,
            732,
            984,
            1195,
            896,
            753,
            1568,
            1253,
            1365,
            1433,
            795,
            1140,
            1477,
            1511,
            866,
            894,
            1565,
            1210,
            1312,
            1081,
            910,
            1423,
            1206,
            1571,
            798,
            1160,
            1124,
            1339,
            1552,
            1088,
            1212,
            871,
            1378,
            1159,
            876,
            947,
            770,
            989,
            1016,
            941,
            939,
            1266,
            1426,
            973,
            1092,
            1216,
            1244,
            933,
            1397,
            1343,
            1142,
            1478,
            1361,
            1200,
            847,
            867,
            845,
            1324,
            1106,
            1360,
            991,
            1376,
            1505,
            1114,
            1199,
            1227,
            1569,
            1100,
            1010,
            1507,
            1029,
            1249,
            726,
            924,
            854,
            733,
            1157,
            1178,
            906,
            936,
            1450,
            1179,
            1395,
            1022,
            1089,
            969,
            1306,
            1025,
            1152,
            737,
            1486,
            1523,
            862,
            1049,
            1252,
            970,
            1112,
            882,
            1311,
            775,
            1403,
            740,
            1373,
            1424,
            1061,
            1045,
            1338,
            1514,
            930,
            1291,
            985,
            1466,
            1057,
            1060,
            982,
            879,
            1223,
            1411,
            1229,
            800,
            1570,
            1498,
            1166,
            1037,
            849,
            931,
            1274,
            1499,
            1074,
            912,
            1181,
            1451,
            1359,
            892,
            1330,
            1155,
            1260,
            986,
            1375,
            1471,
            1101,
            1404,
            1226,
            868,
            1204,
            1438,
            1257,
            1170,
            877,
            739,
            828,
            858,
            844,
            1154,
            855,
            1502,
            1538,
            885,
            1144,
            1105,
            979,
            796,
            1318,
            1364,
            1245,
            1110,
            841,
            744,
            1275,
            926,
            1097,
            743,
            1180,
            1011,
            1526,
            1407,
            1390,
            1246,
            1557,
            1351,
            1566,
            1425,
            935,
            1040,
            951,
            1192,
            1475,
            1293,
            988,
            1500,
            1342,
            1190,
            1508,
            1094,
            1434,
            1461,
            1254,
            1524,
            1368,
            1492,
            1410,
            1317,
            1548,
            1135,
            1133,
            1464,
            1556,
            1269,
            771,
            1096,
            756,
            938,
            1243,
            1052,
            1417,
            1056,
            1129,
            1207,
            1350,
            1289,
            1440,
            898,
            852,
            1515,
            738,
            1421,
            1161,
            967,
            1201,
            1321,
            927,
            1336,
            838,
            1399,
            1305,
            754,
            873,
            1064,
            1413,
            1453,
            1355,
            1372,
            887,
            1120,
            1256,
            1075,
            934,
            805,
            1038,
            995,
            1132,
            861,
            1510,
            1559,
            958,
            1459,
            1182,
            802,
            1065,
            1444,
            1149,
            856,
            1138,
            1382,
            971,
            1439,
            758,
            1012,
            946,
            741,
            1481,
            966,
            955,
            1387,
            1282,
            1119,
            1262,
            1059,
            725,
            943,
            889,
            1542,
            1046,
            780,
            1386,
            1448,
            1463,
            1000,
            782,
            804,
            727,
            839,
            857,
            834,
            891,
            880,
            1561,
            1003,
            1379,
            1503,
            1357,
            1279,
            1222,
            872,
            1130,
            913,
            842,
            881,
            1047,
            1007,
            1551,
            909,
            1118,
            925,
            1214,
            1136,
            900,
            1247,
            1197,
            1420,
            1468,
            814,
            826,
            998,
            1473,
            810,
            1109,
            1239,
            962,
            731,
            1494,
            1546,
            1292,
            1267,
            833,
            1555,
            1496,
            999,
            1259,
            1533,
            1217,
            1487,
            1251,
            1205,
            745,
            1531,
            929,
            1445,
            1529,
            1189,
            817,
            1020,
            822,
            977,
            -1,
            87,
            97,
            125,
            119,
            61,
            67,
            123,
            78,
            33,
            117,
            82,
            12,
            49,
            89,
            60,
            101,
            97,
            83,
            102,
            60,
            96,
            12,
            117,
            111,
            146,
            101,
            60,
            89,
            233,
            123,
            75,
            102,
            189,
            11,
            120,
            84,
            99,
            120,
            16,
            65,
            29,
            95,
            91,
            14,
            42,
            26,
            98,
            89,
            102,
            55,
            67,
            102,
            31,
            76,
            31,
            101,
            69,
            105,
            68,
            75,
            64,
            20,
            84,
            104,
            11,
            101,
            69,
            121,
            77,
            195,
            136,
            120,
            29,
            14,
            181,
            26,
            42,
            77,
            111,
            0,
            119,
            107,
            75,
            9,
            93,
            94,
            6,
            67,
            97,
            116,
            123,
            78,
            59,
            18,
            94,
            79,
            52,
            99,
            33,
            58,
            65,
            101,
            53,
            118,
            80,
            32,
            22,
            135,
            235,
            41,
            38,
            16,
            102,
            115,
            12,
            111,
            40,
            108,
            15,
            61,
            17,
            38,
            76,
            109,
            1,
            120,
            61,
            89,
            103,
            11,
            81,
            76,
            58,
            105,
            39,
            61,
            8,
            100,
            7,
            54,
            89,
            17,
            61,
            105,
            69,
            10,
            82,
            196,
            67,
            64,
            82,
            32,
            117,
            1,
            69,
            121,
            52,
            74,
            42,
            27,
            128,
            231,
            48,
            127,
            116,
            86,
            42,
            34,
            24,
            117,
            16,
            79,
            60,
            101,
            68,
            117,
            94,
            13,
            127,
            15,
            74,
            127,
            82,
            108,
            105,
            53,
            0,
            58,
            14,
            101,
            59,
            68,
            24,
            79,
            126,
            87,
            101,
            9,
            23,
            101,
            67,
            88,
            40,
            5,
            11,
            21,
            78,
            54,
            1,
            73,
            99,
            49,
            10,
            41,
            71,
            68,
            58,
            93,
            64,
            93,
            98,
            24,
            101,
            105,
            79,
            96,
            73,
            119,
            24,
            116,
            17,
            14,
            66,
            204,
            107,
            104,
            123,
            69,
            78,
            39,
            90,
            101,
            205,
            10,
            108,
            18,
            68,
            75,
            36,
            12,
            46,
            100,
            76,
            18,
            49,
            88,
            127,
            155,
            0,
            32,
            173,
            29,
            32,
            106,
            97,
            104,
            101,
            13,
            17,
            105,
            69,
            61,
            0,
            254,
            41,
            70,
            17,
            54,
            12,
            69,
            25,
            114,
            32,
            73,
            125,
            187,
            240,
            41,
            105,
            99,
            102,
            116,
            100,
            41,
            111,
            68,
            81,
            33,
            120,
            68,
            203,
            13,
            77,
            19,
            25,
            79,
            93,
            205,
            13,
            76,
            127,
            44,
            154,
            100,
            8,
            93,
            42,
            69,
            123,
            0,
            119,
            116,
            39,
            53,
            32,
            77,
            47,
            230,
            97,
            101,
            2,
            1,
            234,
            64,
            8,
            67,
            8,
            48,
            73,
            109,
            93,
            44,
            67,
            89,
            67,
            18,
            70,
            0,
            240,
            49,
            234,
            39,
            54,
            144,
            116,
            105,
            77,
            94,
            32,
            113,
            115,
            17,
            100,
            101,
            102,
            76,
            89,
            49,
            99,
            116,
            8,
            59,
            105,
            8,
            9,
            111,
            83,
            95,
            30,
            40,
            194,
            37,
            36,
            127,
            20,
            191,
            54,
            77,
            136,
            14,
            151,
            33,
            120,
            138,
            146,
            59,
            12,
            33,
            117,
            25,
            120,
            49,
            116,
            82,
            94,
            84,
            57,
            35,
            60,
            2,
            50,
            84,
            53,
            23,
            16,
            61,
            198,
            77,
            99,
            46,
            127,
            33,
            80,
            162,
            68,
            112,
            63,
            57,
            214,
            93,
            0,
            45,
            106,
            120,
            98,
            79,
            77,
            47,
            93,
            115,
            108,
            0,
            24,
            7,
            67,
            115,
            26,
            27,
            65,
            200,
            80,
            64,
            69,
            127,
            39,
            103,
            1,
            122,
            116,
            56,
            67,
            119,
            64,
            39,
            32,
            77,
            68,
            102,
            1,
            11,
            193,
            109,
            99,
            213,
            28,
            110,
            49,
            6,
            9,
            120,
            117,
            75,
            69,
            33,
            105,
            84,
            116,
            101,
            57,
            64,
            125,
            48,
            39,
            104,
            33,
            116,
            208,
            85,
            120,
            42,
            62,
            65,
            79,
            1,
            42,
            78,
            11,
            4,
            60,
            117,
            15,
            14,
            54,
            0,
            118,
            117,
            37,
            189,
            217,
            84,
            89,
            29,
            67,
            52,
            23,
            104,
            44,
            70,
            21,
            35,
            108,
            33,
            120,
            82,
            45,
            68,
            68,
            125,
            12,
            1,
            79,
            0,
            87,
            47,
            51,
            119,
            106,
            14,
            45,
            102,
            106,
            80,
            116,
            73,
            89,
            159,
            98,
            120,
            105,
            10,
            196,
            127,
            21,
            214,
            52,
            120,
            100,
            42,
            61,
            41,
            3,
            49,
            21,
            116,
            55,
            115,
            18,
            31,
            69,
            101,
            21,
            6,
            94,
            94,
            118,
            0,
            39,
            73,
            0,
            115,
            99,
            124,
            52,
            14,
            34,
            9,
            111,
            14,
            13,
            17,
            10,
            0,
            104,
            101,
            32,
            123,
            67,
            73,
            68,
            102,
            67,
            79,
            76,
            96,
            33,
            52,
            40,
            58,
            88,
            93,
            35,
            114,
            112,
            69,
            210,
            172,
            50,
            105,
            49,
            90,
            119,
            5,
            38,
            99,
            58,
            0,
            120,
            79,
            0,
            120,
            171,
            26,
            10,
            77,
            64,
            58,
            58,
            67,
            12,
            42,
            32,
            105,
            36,
            105,
            34,
            94,
            13,
            63,
            77,
            42,
            4,
            89,
            79,
            55,
            17,
            51,
            96,
            116,
            56,
            117,
            122,
            99,
            68,
            14,
            63,
            59,
            45,
            98,
            169,
            101,
            77,
            10,
            143,
            101,
            121,
            116,
            80,
            70,
            11,
            7,
            39,
            78,
            85,
            116,
            41,
            229,
            9,
            76,
            75,
            114,
            52,
            29,
            47,
            116,
            24,
            0,
            12,
            127,
            10,
            61,
            12,
            54,
            127,
            62,
            183,
            66,
            32,
            62,
            8,
            219,
            98,
            40,
            107,
            244,
            119,
            44,
            119,
            49,
            45,
            115,
            60,
            57,
            186,
            23,
            0,
            77,
            42,
            65,
            61,
            84,
            49,
            104,
            214,
            48,
            100,
            57,
            86,
            111,
            17,
            9,
            45,
            67,
            10,
            2,
            12,
            95,
            82,
            116,
            62,
            69,
            104,
            229,
            105,
            70,
            2,
            102,
            116,
            67,
            239,
            117,
            204,
            89,
            9,
            57,
            97,
            24,
            60,
            42,
            122,
            50,
            69,
            120,
            39,
            67,
            74,
            41,
            60,
            98,
            0,
            102,
            67,
            103,
            99,
            29,
            252,
            57,
            205,
            85,
            103,
            90,
            99,
            54,
            31,
            42,
            186,
            231,
            122,
            208,
            51,
            33,
            65,
            73,
            120,
            79,
            118,
            14,
            79,
            41,
            120,
            32,
            209,
            89,
            2,
            95,
            22,
            56,
            124,
            78,
            2,
            127,
            4,
            118,
            47,
            102,
            82,
            116,
            103,
            199,
            79,
            101,
            102,
            118,
            17,
            15,
            76,
            93,
            89,
            28,
            33,
            10
        },
        key
    )
)
if a then
    a()
else
    print("WRONG PASSWORD!")
end