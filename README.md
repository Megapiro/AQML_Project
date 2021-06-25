# AQML_Project

Benchmarks for the max2sat testing are taken from [here](http://maxsat.ia.udl.cat/benchmarks/)

results can be found [here](http://maxsat.ia.udl.cat/detailed/complete-ms-random-table.html)

we report them for simpplicity: (we report only the best optimal result from the best solver for the benchmark)

| Label |                                            Meaning                                           |
|:-----:|:--------------------------------------------------------------------------------------------:|
| S     | Solution {OPTIMUM FOUND or OPT \| UNSATISFIABLE or UNSAT \| UNKNOWN \| Not available or N/A} |
| O     | Best solution found                                                                          |
| T     | CPU time (TO for Time Out)                                                                   |


|     Instance file name     |         Best solver         | OUR (Simulation) | OUR (Real) |
|:--------------------------:|:---------------------------:|:----------------:|:----------:|
| s2v120c1200-1.cnf          | S = OPT O = 161 T = 5.65    |  O = 324         |   O = 300  |
| s2v120c1200-2.cnf          | S = OPT O = 159 T = 8.40    |                  |            |
| s2v120c1200-3.cnf          | S = OPT O = 160 T = 2.70    |                  |            |
| s2v120c1300-1.cnf          | S = OPT O = 180 T = 14.94   |                  |            |
| s2v120c1300-2.cnf          | S = OPT O = 172 T = 6.29    |                  |            |
| s2v120c1300-3.cnf          | S = OPT O = 173 T = 5.96    |                  |            |
| s2v120c1400-1.cnf          | S = OPT O = 197 T = 17.17   |                  |            |
| s2v120c1400-2.cnf          | S = OPT O = 191 T = 10.06   |                  |            |
| s2v120c1400-3.cnf          | S = OPT O = 189 T = 8.30    |                  |            |
| s2v120c1500-1.cnf          | S = OPT O = 211 T = 8.00    |                  |            |
| s2v120c1500-2.cnf          | S = OPT O = 213 T = 27.02   |                  |            |
| s2v120c1500-3.cnf          | S = OPT O = 207 T = 6.18    |                  |            |
| s2v120c1600-1.cnf          | S = OPT O = 233 T = 24.19   |                  |            |
| s2v120c1600-2.cnf          | S = OPT O = 239 T = 85.74   |                  |            |
| s2v120c1600-3.cnf          | S = OPT O = 233 T = 29.73   |                  |            |
| s2v120c1700-1.cnf          | S = OPT O = 257 T = 51.12   |                  |            |
| s2v120c1700-2.cnf          | S = OPT O = 248 T = 66.38   |                  |            |
| s2v120c1700-3.cnf          | S = OPT O = 239 T = 5.69    |                  |            |
| s2v120c1800-1.cnf          | S = OPT O = 291 T = 383.01  |                  |            |
| s2v120c1800-2.cnf          | S = OPT O = 262 T = 16.59   |                  |            |
| s2v120c1800-3.cnf          | S = OPT O = 279 T = 64.81   |                  |            |
| s2v120c1900-1.cnf          | S = OPT O = 293 T = 64.83   |                  |            |
| s2v120c1900-2.cnf          | S = OPT O = 296 T = 144.99  |                  |            |
| s2v120c1900-3.cnf          | S = OPT O = 294 T = 88.19   |                  |            |
| s2v120c2000-1.cnf          | S = OPT O = 307 T = 27.04   |  O = 486         | O = 487    |
| s2v120c2000-2.cnf          | S = OPT O = 321 T = 651.59  |                  |            |
| s2v120c2000-3.cnf          | S = OPT O = 307 T = 71.32   |                  |            |
| s2v120c2100-1.cnf          | S = OPT O = 336 T = 64.23   |                  |            |
| s2v120c2100-2.cnf          | S = OPT O = 336 T = 691.62  |                  |            |
| s2v120c2100-3.cnf          | S = OPT O = 332 T = 214.08  |                  |            |
| s2v120c2200-1.cnf          | S = OPT O = 358 T = 446.53  |                  |            |
| s2v120c2200-2.cnf          | S = OPT O = 371 T = 1530.60 |                  |            |
| s2v120c2200-3.cnf          | S = OPT O = 359 T = 336.23  |                  |            |
| s2v120c2300-1.cnf          | S = OPT O = 380 T = 384.48  |                  |            |
| s2v120c2300-2.cnf          | S = OPT O = 383 T = 599.46  |                  |            |
| s2v120c2300-3.cnf          | S = OPT O = 365 T = 80.14   |                  |            |
| s2v120c2400-1.cnf          | S = OPT O = 389 T = 154.85  |                  |            |
| s2v120c2400-2.cnf          | S = OPT O = 402 T = 958.04  |                  |            |
| s2v120c2400-3.cnf          | S = OPT O = 380 T = 41.53   |                  |            |
| s2v120c2500-1.cnf          | S = OPT O = 418 T = 256.04  |                  |            |
| s2v120c2500-2.cnf          | S = N/A O = N/A T = TO      |                  |            |
| s2v120c2500-3.cnf          | S = OPT O = 425 T = 898.11  |                  |            |
| s2v120c2600-1.cnf          | S = OPT O = 439 T = 877.77  |  O = 671         | O = 663    |
| s2v120c2600-2.cnf          | S = N/A O = N/A T = TO      |                  |            |
| s2v120c2600-3.cnf          | S = OPT O = 440 T = 447.94  |                  |            |
| s2v140c1200-1.cnf          | S = OPT O = 144 T = 6.48    |                  |            |
| s2v140c1200-2.cnf          | S = OPT O = 155 T = 156.32  |                  |            |
| s2v140c1200-3.cnf          | S = OPT O = 155 T = 17.66   |                  |            |
| s2v140c1300-1.cnf          | S = OPT O = 162 T = 23.75   |                  |            |
| s2v140c1300-2.cnf          | S = OPT O = 171 T = 109.37  |                  |            |
| s2v140c1300-3.cnf          | S = OPT O = 168 T = 30.82   |                  |            |
| s2v140c1400-1.cnf          | S = OPT O = 182 T = 46.33   |                  |            |
| s2v140c1400-2.cnf          | S = OPT O = 178 T = 24.86   |                  |            |
| s2v140c1400-3.cnf          | S = OPT O = 193 T = 144.40  |                  |            |
| s2v140c1500-1.cnf          | S = OPT O = 205 T = 145.96  |                  |            |
| s2v140c1500-2.cnf          | S = OPT O = 199 T = 129.94  |                  |            |
| s2v140c1500-3.cnf          | S = OPT O = 212 T = 450.64  |                  |            |
| s2v140c1600-1.cnf          | S = OPT O = 221 T = 99.13   |                  |            |
| s2v140c1600-2.cnf          | S = OPT O = 221 T = 160.58  |                  |            |
| s2v140c1600-3.cnf          | S = OPT O = 226 T = 246.25  |                  |            |
| s2v140c1700-1.cnf          | S = N/A O = N/A T = TO      |                  |            |
| s2v140c1700-2.cnf          | S = OPT O = 242 T = 206.76  |                  |            |
| s2v140c1700-3.cnf          | S = OPT O = 236 T = 69.70   |                  |            |
| s2v140c1800-1.cnf          | S = OPT O = 254 T = 324.26  |                  |            |
| s2v140c1800-2.cnf          | S = OPT O = 257 T = 132.36  |                  |            |
| s2v140c1800-3.cnf          | S = OPT O = 255 T = 67.50   |                  |            |
| s2v140c1900-1.cnf          | S = N/A O = N/A T = TO      |                  |            |
| s2v140c1900-2.cnf          | S = OPT O = 273 T = 53.78   |                  |            |
| s2v140c1900-3.cnf          | S = OPT O = 278 T = 268.61  |                  |            |
| s2v140c2000-1.cnf          | S = OPT O = 298 T = 535.22  |                  |            |
| s2v140c2000-2.cnf          | S = OPT O = 308 T = 1178.33 |                  |            |
| s2v140c2000-3.cnf          | S = OPT O = 296 T = 269.67  |                  |            |
| s2v140c2100-1.cnf          | S = OPT O = 293 T = 33.99   |                  |            |
| s2v140c2100-2.cnf          | S = OPT O = 310 T = 190.04  |                  |            |
| s2v140c2100-3.cnf          | S = OPT O = 319 T = 593.53  |                  |            |
| s2v140c2200-1.cnf          | S = OPT O = 336 T = 1014.50 |                  |            |
| s2v140c2200-2.cnf          | S = OPT O = 332 T = 952.96  |                  |            |
| s2v140c2200-3.cnf          | S = OPT O = 329 T = 397.21  |                  |            |
| s2v140c2300-1.cnf          | S = N/A O = N/A T = TO      |                  |            |
| s2v140c2300-2.cnf          | S = N/A O = N/A T = TO      |                  |            |
| s2v140c2300-3.cnf          | S = OPT O = 352 T = 880.10  |                  |            |
| s2v140c2400-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v140c2400-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v140c2400-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v140c2500-1.cnf          | S = OPT O = 393 T = 837.06  |||
| s2v140c2500-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v140c2500-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v140c2600-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v140c2600-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v140c2600-3.cnf          | S = OPT O = 406 T = 961.82  |||
| s2v160c1200-1.cnf          | S = OPT O = 142 T = 43.42   |||
| s2v160c1200-2.cnf          | S = OPT O = 133 T = 8.96    |||
| s2v160c1200-3.cnf          | S = OPT O = 143 T = 86.49   |||
| s2v160c1300-1.cnf          | S = OPT O = 167 T = 337.15  |||
| s2v160c1300-2.cnf          | S = OPT O = 139 T = 2.90    |||
| s2v160c1300-3.cnf          | S = OPT O = 157 T = 86.01   |||
| s2v160c1400-1.cnf          | S = OPT O = 166 T = 36.36   |||
| s2v160c1400-2.cnf          | S = OPT O = 164 T = 38.99   |||
| s2v160c1400-3.cnf          | S = OPT O = 167 T = 21.86   |||
| s2v160c1500-1.cnf          | S = OPT O = 183 T = 14.22   |||
| s2v160c1500-2.cnf          | S = OPT O = 200 T = 905.90  |||
| s2v160c1500-3.cnf          | S = OPT O = 184 T = 62.16   |||
| s2v160c1600-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c1600-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c1600-3.cnf          | S = OPT O = 213 T = 743.89  |||
| s2v160c1700-1.cnf          | S = OPT O = 226 T = 659.70  |||
| s2v160c1700-2.cnf          | S = OPT O = 230 T = 572.97  |||
| s2v160c1700-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c1800-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c1800-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c1800-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c1900-1.cnf          | S = OPT O = 261 T = 1241.31 |||
| s2v160c1900-2.cnf          | S = OPT O = 262 T = 1480.92 |||
| s2v160c1900-3.cnf          | S = OPT O = 264 T = 995.23  |||
| s2v160c2000-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2000-2.cnf          | S = OPT O = 272 T = 92.52   |||
| s2v160c2000-3.cnf          | S = OPT O = 282 T = 790.73  |||
| s2v160c2100-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2100-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2100-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2200-1.cnf          | S = OPT O = 310 T = 642.57  |||
| s2v160c2200-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2200-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2300-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2300-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2300-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2400-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2400-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2400-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2500-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2500-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2500-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2600-1.cnf          | S = OPT O = 392 T = 1596.27 |||
| s2v160c2600-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v160c2600-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1200-1.cnf          | S = OPT O = 134 T = 147.86  |||
| s2v180c1200-2.cnf          | S = OPT O = 130 T = 79.94   |||
| s2v180c1200-3.cnf          | S = OPT O = 131 T = 156.38  |||
| s2v180c1200-4.cnf          | S = OPT O = 128 T = 135.96  |||
| s2v180c1300-1.cnf          | S = OPT O = 153 T = 646.96  |||
| s2v180c1300-2.cnf          | S = OPT O = 138 T = 43.39   |||
| s2v180c1300-3.cnf          | S = OPT O = 150 T = 165.80  |||
| s2v180c1300-4.cnf          | S = OPT O = 149 T = 288.42  |||
| s2v180c1400-1.cnf          | S = OPT O = 165 T = 433.80  |||
| s2v180c1400-2.cnf          | S = OPT O = 165 T = 514.80  |||
| s2v180c1400-3.cnf          | S = OPT O = 156 T = 133.24  |||
| s2v180c1400-4.cnf          | S = OPT O = 160 T = 245.56  |||
| s2v180c1500-1.cnf          | S = OPT O = 184 T = 1633.85 |||
| s2v180c1500-2.cnf          | S = OPT O = 180 T = 1434.90 |||
| s2v180c1500-3.cnf          | S = OPT O = 179 T = 291.29  |||
| s2v180c1500-4.cnf          | S = OPT O = 181 T = 406.46  |||
| s2v180c1600-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1600-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1600-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1600-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1700-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1700-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1700-3.cnf          | S = OPT O = 209 T = 1066.08 |||
| s2v180c1700-4.cnf          | S = OPT O = 206 T = 266.32  |||
| s2v180c1800-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1800-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1800-3.cnf          | S = OPT O = 232 T = 1359.50 |||
| s2v180c1800-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1900-1.cnf          | S = OPT O = 245 T = 657.85  |||
| s2v180c1900-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1900-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c1900-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2000-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2000-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2000-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2000-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2100-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2100-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2100-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2100-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2200-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2200-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2200-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v180c2200-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1200-1.cnf          | S = OPT O = 118 T = 133.09  |||
| s2v200c1200-2.cnf          | S = OPT O = 127 T = 332.19  |||
| s2v200c1200-3.cnf          | S = OPT O = 125 T = 475.72  |||
| s2v200c1200-4.cnf          | S = OPT O = 115 T = 29.65   |||
| s2v200c1200-5.cnf          | S = OPT O = 117 T = 148.82  |||
| s2v200c1200-6.cnf          | S = OPT O = 127 T = 275.54  |||
| s2v200c1200-7.cnf          | S = OPT O = 112 T = 17.12   |||
| s2v200c1300-1.cnf          | S = OPT O = 144 T = 655.54  |||
| s2v200c1300-2.cnf          | S = OPT O = 143 T = 874.62  |||
| s2v200c1300-3.cnf          | S = OPT O = 121 T = 62.43   |||
| s2v200c1300-4.cnf          | S = OPT O = 139 T = 306.59  |||
| s2v200c1300-5.cnf          | S = OPT O = 142 T = 572.57  |||
| s2v200c1300-6.cnf          | S = OPT O = 134 T = 517.50  |||
| s2v200c1300-7.cnf          | S = OPT O = 128 T = 32.98   |||
| s2v200c1400-1.cnf          | S = OPT O = 156 T = 756.32  |||
| s2v200c1400-2.cnf          | S = OPT O = 147 T = 156.52  |||
| s2v200c1400-3.cnf          | S = OPT O = 150 T = 182.12  |||
| s2v200c1400-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1400-5.cnf          | S = OPT O = 153 T = 342.49  |||
| s2v200c1400-6.cnf          | S = OPT O = 145 T = 115.08  |||
| s2v200c1400-7.cnf          | S = OPT O = 142 T = 135.26  |||
| s2v200c1500-1.cnf          | S = OPT O = 165 T = 177.97  |||
| s2v200c1500-2.cnf          | S = OPT O = 165 T = 388.23  |||
| s2v200c1500-3.cnf          | S = OPT O = 165 T = 759.47  |||
| s2v200c1500-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1500-5.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1500-6.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1500-7.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1600-1.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1600-2.cnf          | S = OPT O = 178 T = 307.70  |||
| s2v200c1600-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1600-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1600-5.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1600-6.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1600-7.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1700-1.cnf          | S = OPT O = 193 T = 146.26  |||
| s2v200c1700-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1700-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1700-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1700-5.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1700-6.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1700-7.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1800-1.cnf          | S = OPT O = 206 T = 383.34  |||
| s2v200c1800-2.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1800-3.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1800-4.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1800-5.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1800-6.cnf          | S = N/A O = N/A T = TO      |||
| s2v200c1800-7.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-1.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-10.cnf         | S = N/A O = N/A T = TO      |||
| s3v110c1000-2.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-3.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-4.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-5.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-6.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-7.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1000-8.cnf          | S = OPT O = 26 T = 1427.23  |||
| s3v110c1000-9.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-1.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-10.cnf         | S = N/A O = N/A T = TO      |||
| s3v110c1100-2.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-3.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-4.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-5.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-6.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-7.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-8.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c1100-9.cnf          | S = N/A O = N/A T = TO      |||
| s3v110c700-1.cnf           | S = OPT O = 11 T = 57.81    |||
| s3v110c700-10.cnf          | S = OPT O = 9 T = 11.36     |||
| s3v110c700-2.cnf           | S = OPT O = 12 T = 107.37   |||
| s3v110c700-3.cnf           | S = OPT O = 10 T = 27.60    |||
| s3v110c700-4.cnf           | S = OPT O = 11 T = 41.32    |||
| s3v110c700-5.cnf           | S = OPT O = 10 T = 28.59    |||
| s3v110c700-6.cnf           | S = OPT O = 11 T = 52.64    |||
| s3v110c700-7.cnf           | S = OPT O = 9 T = 17.50     |||
| s3v110c700-8.cnf           | S = OPT O = 11 T = 57.96    |||
| s3v110c700-9.cnf           | S = OPT O = 10 T = 42.96    |||
| s3v110c800-1.cnf           | S = OPT O = 17 T = 315.01   |||
| s3v110c800-10.cnf          | S = OPT O = 14 T = 73.99    |||
| s3v110c800-2.cnf           | S = OPT O = 17 T = 411.69   |||
| s3v110c800-3.cnf           | S = OPT O = 15 T = 167.31   |||
| s3v110c800-4.cnf           | S = OPT O = 18 T = 256.45   |||
| s3v110c800-5.cnf           | S = OPT O = 17 T = 243.27   |||
| s3v110c800-6.cnf           | S = OPT O = 18 T = 434.56   |||
| s3v110c800-7.cnf           | S = OPT O = 16 T = 210.59   |||
| s3v110c800-8.cnf           | S = OPT O = 17 T = 482.74   |||
| s3v110c800-9.cnf           | S = OPT O = 16 T = 142.61   |||
| s3v110c900-1.cnf           | S = OPT O = 22 T = 782.05   |||
| s3v110c900-10.cnf          | S = OPT O = 21 T = 614.51   |||
| s3v110c900-2.cnf           | S = OPT O = 22 T = 1038.44  |||
| s3v110c900-3.cnf           | S = OPT O = 17 T = 77.23    |||
| s3v110c900-4.cnf           | S = OPT O = 21 T = 483.81   |||
| s3v110c900-5.cnf           | S = OPT O = 22 T = 537.59   |||
| s3v110c900-6.cnf           | S = OPT O = 23 T = 764.33   |||
| s3v110c900-7.cnf           | S = OPT O = 21 T = 849.63   |||
| s3v110c900-8.cnf           | S = OPT O = 22 T = 601.91   |||
| s3v110c900-9.cnf           | S = N/A O = N/A T = TO      |||
| s3v70c1000-1.cnf           | S = OPT O = 47 T = 123.08   |||
| s3v70c1000-2.cnf           | S = OPT O = 43 T = 56.66    |||
| s3v70c1000-3.cnf           | S = OPT O = 45 T = 78.94    |||
| s3v70c1000-4.cnf           | S = OPT O = 47 T = 122.22   |||
| s3v70c1000-5.cnf           | S = OPT O = 42 T = 47.84    |||
| s3v70c1100-1.cnf           | S = OPT O = 56 T = 331.47   |||
| s3v70c1100-2.cnf           | S = OPT O = 55 T = 227.34   |||
| s3v70c1100-3.cnf           | S = OPT O = 53 T = 136.06   |||
| s3v70c1100-4.cnf           | S = OPT O = 52 T = 169.47   |||
| s3v70c1100-5.cnf           | S = OPT O = 53 T = 184.75   |||
| s3v70c1200-1.cnf           | S = OPT O = 66 T = 752.93   |||
| s3v70c1200-2.cnf           | S = OPT O = 63 T = 322.68   |||
| s3v70c1200-3.cnf           | S = OPT O = 65 T = 608.15   |||
| s3v70c1200-4.cnf           | S = OPT O = 67 T = 1011.74  |||
| s3v70c1200-5.cnf           | S = OPT O = 65 T = 544.98   |||
| s3v70c1300-1.cnf           | S = OPT O = 75 T = 1139.98  |||
| s3v70c1300-2.cnf           | S = OPT O = 74 T = 946.71   |||
| s3v70c1300-3.cnf           | S = OPT O = 70 T = 708.07   |||
| s3v70c1300-4.cnf           | S = OPT O = 68 T = 316.19   |||
| s3v70c1300-5.cnf           | S = OPT O = 70 T = 650.70   |||
| s3v70c1400-1.cnf           | S = OPT O = 78 T = 705.64   |||
| s3v70c1400-2.cnf           | S = OPT O = 83 T = 1309.01  |||
| s3v70c1400-3.cnf           | S = OPT O = 79 T = 990.89   |||
| s3v70c1400-4.cnf           | S = OPT O = 75 T = 284.52   |||
| s3v70c1400-5.cnf           | S = OPT O = 82 T = 1062.63  |||
| s3v70c1500-1.cnf           | S = N/A O = N/A T = TO      |||
| s3v70c1500-2.cnf           | S = OPT O = 89 T = 1182.99  |||
| s3v70c1500-3.cnf           | S = OPT O = 86 T = 893.82   |||
| s3v70c1500-4.cnf           | S = N/A O = N/A T = TO      |||
| s3v70c1500-5.cnf           | S = N/A O = N/A T = TO      |||
| s3v70c700-1.cnf            | S = OPT O = 21 T = 5.00     |||
| s3v70c700-2.cnf            | S = OPT O = 21 T = 7.06     |||
| s3v70c700-3.cnf            | S = OPT O = 25 T = 14.14    |||
| s3v70c700-4.cnf            | S = OPT O = 24 T = 13.83    |||
| s3v70c700-5.cnf            | S = OPT O = 22 T = 4.61     |||
| s3v70c800-1.cnf            | S = OPT O = 31 T = 27.20    |||
| s3v70c800-2.cnf            | S = OPT O = 34 T = 81.33    |||
| s3v70c800-3.cnf            | S = OPT O = 30 T = 16.76    |||
| s3v70c800-4.cnf            | S = OPT O = 28 T = 15.14    |||
| s3v70c800-5.cnf            | S = OPT O = 31 T = 26.16    |||
| s3v70c900-1.cnf            | S = OPT O = 39 T = 67.52    |||
| s3v70c900-2.cnf            | S = OPT O = 38 T = 59.97    |||
| s3v70c900-3.cnf            | S = OPT O = 39 T = 53.09    |||
| s3v70c900-4.cnf            | S = OPT O = 39 T = 54.46    |||
| s3v70c900-5.cnf            | S = OPT O = 40 T = 87.16    |||
| s3v90c1000-1.cnf           | S = OPT O = 34 T = 241.17   |||
| s3v90c1000-2.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1000-3.cnf           | S = OPT O = 39 T = 1687.82  |||
| s3v90c1000-4.cnf           | S = OPT O = 34 T = 264.05   |||
| s3v90c1000-5.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1000-6.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1000-7.cnf           | S = OPT O = 38 T = 963.23   |||
| s3v90c1100-1.cnf           | S = OPT O = 44 T = 1495.14  |||
| s3v90c1100-2.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1100-3.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1100-4.cnf           | S = OPT O = 43 T = 1729.54  |||
| s3v90c1100-5.cnf           | S = OPT O = 44 T = 1781.90  |||
| s3v90c1100-6.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1100-7.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1200-1.cnf           | S = OPT O = 47 T = 1783.02  |||
| s3v90c1200-2.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1200-3.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1200-4.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1200-5.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1200-6.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1200-7.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1300-1.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1300-2.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1300-3.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1300-4.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1300-5.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1300-6.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c1300-7.cnf           | S = N/A O = N/A T = TO      |||
| s3v90c700-1.cnf            | S = OPT O = 16 T = 32.64    |||
| s3v90c700-2.cnf            | S = OPT O = 17 T = 42.27    |||
| s3v90c700-3.cnf            | S = OPT O = 15 T = 19.32    |||
| s3v90c700-4.cnf            | S = OPT O = 18 T = 52.16    |||
| s3v90c700-5.cnf            | S = OPT O = 16 T = 26.75    |||
| s3v90c700-6.cnf            | S = OPT O = 18 T = 59.07    |||
| s3v90c700-7.cnf            | S = OPT O = 18 T = 63.00    |||
| s3v90c800-1.cnf            | S = OPT O = 22 T = 111.53   |||
| s3v90c800-2.cnf            | S = OPT O = 23 T = 132.89   |||
| s3v90c800-3.cnf            | S = OPT O = 23 T = 138.70   |||
| s3v90c800-4.cnf            | S = OPT O = 20 T = 47.16    |||
| s3v90c800-5.cnf            | S = OPT O = 24 T = 242.87   |||
| s3v90c800-6.cnf            | S = OPT O = 26 T = 447.20   |||
| s3v90c800-7.cnf            | S = OPT O = 24 T = 199.84   |||
| s3v90c900-1.cnf            | S = OPT O = 28 T = 142.76   |||
| s3v90c900-2.cnf            | S = OPT O = 28 T = 190.45   |||
| s3v90c900-3.cnf            | S = OPT O = 32 T = 545.30   |||
| s3v90c900-4.cnf            | S = OPT O = 28 T = 219.32   |||
| s3v90c900-5.cnf            | S = OPT O = 25 T = 55.30    |||
| s3v90c900-6.cnf            | S = OPT O = 30 T = 341.01   |||
| s3v90c900-7.cnf            | S = OPT O = 27 T = 153.47   |||
| HG-3SAT-V250-C1000-1.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-10.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-100.cnf | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-11.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-12.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-13.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-14.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-15.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-16.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-17.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-18.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-19.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-2.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-20.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-21.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-22.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-23.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-24.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-3.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-4.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-5.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-6.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-7.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-8.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V250-C1000-9.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-1.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-10.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-100.cnf | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-11.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-12.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-13.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-14.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-15.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-16.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-17.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-18.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-19.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-2.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-20.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-21.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-22.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-23.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-24.cnf  | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-3.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-4.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-5.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-6.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-7.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-8.cnf   | S = N/A O = N/A T = TO      |||
| HG-3SAT-V300-C1200-9.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V100-C900-14.cnf   | S = OPT O = 2 T = 844.23    |||
| HG-4SAT-V100-C900-19.cnf   | S = OPT O = 2 T = 1458.20   |||
| HG-4SAT-V100-C900-2.cnf    | S = OPT O = 2 T = 872.23    |||
| HG-4SAT-V100-C900-20.cnf   | S = OPT O = 2 T = 694.04    |||
| HG-4SAT-V100-C900-23.cnf   | S = OPT O = 2 T = 523.58    |||
| HG-4SAT-V100-C900-4.cnf    | S = OPT O = 2 T = 962.72    |||
| HG-4SAT-V100-C900-7.cnf    | S = OPT O = 2 T = 992.69    |||
| HG-4SAT-V150-C1350-1.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-10.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-100.cnf | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-11.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-12.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-13.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-14.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-15.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-16.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-17.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-18.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-19.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-2.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-20.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-21.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-22.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-23.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-24.cnf  | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-3.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-4.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-5.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-6.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-7.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-8.cnf   | S = N/A O = N/A T = TO      |||
| HG-4SAT-V150-C1350-9.cnf   | S = N/A O = N/A T = TO      |||