import pytest

from balanceBinarySearchTree.solution import Solution
from core.dataStructure.TreeNode import to_bst, to_array


@pytest.mark.parametrize("input, expected",
                         [
                             # ([41, 20, 65, 11, 29, 50, None, None, None, 26, None, None, 55, 23],
                             #   [41, 20, 55, 11, 26, 50, 65, None, None, 23, 29]),
                             # ([1, None, 2, None, 3, None, 4, None, None],
                             #  [3, 1, 4, None, 2]),
                             # ([1, None, 15, 14, 17, 7, None, None, None, 2, 12, None, 3, 9, None, None, None, None, 11],
                             #  [9, 2, 14, 1, 3, 11, 15, None, None, None, 7, None, 12, None, 17]),
                             ([57097, 35790, 72149, 17771, 49554, 70055, 84593, 2509, 30090, 43067, 51437, 67162, 71423, 78075, 89163, 2032, 5790, 22021, 31730, 38889, 49174, 50760, 55559, 57920, 67300, 70204, 71570, 74049, 84090, 87060, 98928, 96, 2057, 5652, 9391, 18171, 29925, 30953, 31805, 36213, 41536, 46324, 49374, 50424, 51158, 51655, 56064, 57153, 63771, None, 67616, None, 71228, None, 71943, 72866, 76874, 82381, 84418, 85880, 88034, 92447, 99495, None, 777, None, 2226, 4575, 5715, 9047, 10325, 17995, 20050, 27067, 29979, 30619, 31030, 31796, 34775, 36160, 37596, 40797, 42149, 43341, 47005, 49265, None, 50351, 50604, 51055, 51220, 51466, 51850, 55935, 57045, None, 57307, 62969, 64863, 67363, 69954, 70911, 71231, 71865, None, 72808, 72895, 76203, 77360, 79632, 82736, 84135, 84540, 84935, 86359, 87613, 88325, 91371, 97921, 99179, 99888, 323, 1438, None, None, 3644, 5021, 5698, 5786, 7627, 9093, 10022, 12341, 17841, 18118, 19767, 21727, 26860, 27274, None, None, 30117, 30844, None, 31220, None, None, 34093, 35369, 35976, None, 36907, 38460, 39644, 40889, 41728, 43028, 43261, 44980, 46788, 47714, None, 49302, 49791, 50412, None, 50661, 51022, 51153, None, None, 51458, 51526, 51782, 53109, 55762, 55991, 56969, None, 57182, 57765, 60384, 63070, 64556, 65335, None, None, 67822, None, 70861, 71086, None, None, 71649, None, 72194, 72814, None, 74039, 75981, 76292, 77099, 78050, 79305, 82030, 82383, 83437, None, 84308, 84450, 84577, 84851, 85705, 86335, 86619, 87366, 88026, 88123, 88428, 89225, 91399, 93884, 98695, 99004, 99363, 99646, 99946, 133, 589, 1375, 1789, 3220, 3950, 4579, 5451, None, None, None, None, 5894, 8132, None, 9208, 9575, 10215, 10803, 13344, 17807, 17932, 18088, 18128, 18620, 19821, 21370, 21865, 23187, None, 27193, 27979, 30101, 30553, 30742, None, 31114, 31290, 32717, 34400, 34804, 35633, None, 36056, 36484, 36985, 37982, 38803, None, 40009, 40816, 41430, 41672, None, 42961, None, 43099, None, 43637, 45979, 46476, 46972, 47310, 48102, None, 49351, 49620, 50344, None, None, None, 50676, 50885, None, 51106, None, None, None, None, 51544, 51740, None, 52683, 55188, None, None, None, None, 56493, None, None, None, 57434, 57798, 58744, 60554, 63032, 63215, 64271, 64625, 65013, 66427, 67668, 67853, 70500, None, None, None, None, None, None, 72278, None, None, 73616, 74045, 74192, None, 76285, 76501, 76997, None, 77468, None, 79172, 79624, 81883, 82311, None, 82633, 83207, 83807, None, None, None, None, None, None, None, None, 85076, None, 86224, None, 86593, 86767, 87235, None, 87935, None, None, 88222, None, 88925, 89181, 89303, None, 92398, 93000, 96977, 97948, 98754, None, 99152, 99313, None, 99611, 99855, 99924, 99956, None, None, 485, 645, 1222, None, 1788, 1938, 2797, 3466, 3896, 4093, None, 5019, 5283, 5498, None, 7079, 7757, 8180, None, None, None, 9984, 10201, 10288, 10440, 11377, 13163, 16435, None, None, None, None, 18016, None, None, None, 18450, 18630, None, 20031, 21278, 21560, None, None, 22458, 25006, 27145, None, 27350, 28399, None, None, None, None, 30631, None, 31067, None, None, 31650, 32348, 33093, 34206, 34570, None, 34955, None, None, None, None, None, 36758, None, 37351, 37629, 38167, None, None, 39965, 40242, None, None, 41309, 41474, None, None, 42902, 42977, None, 43181, 43489, 44262, 45429, 46180, 46462, 46709, 46929, 46996, 47043, 47605, 47753, 49159, None, None, None, None, 49823, None, None, None, 50812, None, None, None, None, None, None, 51753, 52480, 52925, 53884, 55398, 56437, 56584, None, 57737, None, 57829, None, 58829, None, 62950, 63007, 63035, None, 63297, 64262, 64529, None, 64842, None, 65109, 66172, 66584, None, 67780, None, 69373, None, 70716, None, 72365, 73234, 73980, None, None, 74106, 74777, None, None, 76375, 76793, None, None, None, None, 78091, 79192, None, None, 80165, 82005, 82291, None, 82611, 82695, 83156, 83280, 83449, 83902, 84988, 85647, None, 86303, 86478, None, 86656, 87029, None, None, None, 88002, None, 88289, 88602, 89108, None, None, 89237, 89930, 91599, 92405, 92888, 93220, 96638, 97489, None, 98311, None, None, None, None, None, 99318, None, None, None, None, None, None, None, None, 408, None, None, 739, 925, 1263, 1631, None, None, None, 2775, 2979, 3328, 3574, None, None, 4023, 4335, 4824, None, 5126, 5435, None, None, 6123, 7493, None, 7845, None, 8401, None, None, 10148, 10214, None, None, None, 10681, 11191, 12091, 12546, None, 14158, 17322, None, 18066, None, 18491, None, 19332, None, None, 20912, 21306, 21447, None, 22285, 23169, 24267, 25495, None, None, 27286, 27391, 28381, 29593, None, None, None, None, 31476, None, 32198, 32501, 32842, 33769, None, 34373, None, 34623, 34811, 35218, 36531, None, 37187, None, None, 37779, 38157, 38238, None, None, 40121, 40599, 41150, None, None, None, 42379, None, None, 43007, None, None, None, None, 43848, 44862, 45181, 45466, 46149, 46316, 46330, None, 46637, None, 46875, None, None, None, None, 47116, 47320, 47617, None, None, 48378, None, None, 50038, None, None, None, None, 52154, 52672, 52923, 53000, 53592, 55048, None, None, 56192, None, 56563, 56749, None, None, None, None, None, 58847, 62668, None, None, None, None, None, None, None, 64121, None, 64371, None, None, None, 65057, 65142, 66051, None, 66520, 66859, 67712, 67783, 68107, 69407, None, None, 72304, 72738, 73175, 73610, 73759, 74021, None, 74177, 74528, 75105, None, 76480, 76744, 76828, None, 78902, 79187, 79208, 80071, 80743, 81990, 82021, 82289, None, 82393, None, None, None, 83107, 83198, None, 83319, None, None, None, None, None, None, 85560, None, None, None, None, 86588, None, None, 86880, None, None, None, None, None, 88459, None, None, None, None, None, 89609, 90495, 91498, 91723, None, None, 92673, None, 93076, 93480, 95986, 96734, 97362, 97523, 97952, None, None, None, None, None, None, None, None, 1192, None, None, None, 1766, 2712, None, 2881, 3186, 3315, 3433, 3513, None, None, None, 4334, 4493, 4761, 5005, 5060, 5250, None, None, None, 7033, 7433, None, None, 8038, 8296, 9024, None, None, None, None, 10545, None, 10853, None, 11747, None, None, 12808, 14001, 16398, 17017, 17679, None, None, None, 18574, 19253, 19514, 20360, 21045, None, 21354, None, 21558, 22231, 22455, 22863, None, 23727, 24679, 25342, 26580, None, None, None, None, None, None, 29496, 29628, 31465, 31496, None, None, None, 32663, None, 33079, 33121, 33969, 34311, None, 34620, None, None, 34834, None, 35268, None, None, None, None, 37754, None, None, None, None, 38370, None, 40129, 40308, 40733, None, 41227, 42311, 42556, 42984, None, 43728, 44015, 44288, 44889, 45008, 45275, None, 45953, None, None, None, None, None, None, 46528, 46684, 46790, 46909, None, None, None, 47456, None, None, 48272, 48916, None, 50158, 52044, 52179, None, None, 52909, None, 52980, 53087, 53508, 53646, 54885, 55149, None, None, 56520, None, None, None, None, 59841, 61771, 62908, None, None, None, None, 65016, None, None, None, 65609, None, 66511, None, 66703, 67023, None, None, None, None, 67916, 69110, None, 69879, None, None, 72603, None, None, None, 73374, None, None, 73831, 74013, None, None, None, 74203, 74747, 74916, 75589, None, None, 76505, None, None, None, 78736, 79054, None, None, None, None, 79726, 80148, 80365, 81507, None, None, 82014, None, 82065, None, None, 82443, 82855, None, None, None, 83306, None, None, None, None, None, None, None, None, None, 89580, 89679, 90001, 90515, None, None, 91699, 91933, 92481, 92817, None, 93126, 93239, 93601, 94099, 96454, 96649, 96967, 96988, None, None, 97782, None, 97963, None, None, 1657, None, 2517, None, 2848, 2882, 3126, None, 3299, None, 3410, None, None, None, None, None, 4430, None, 4722, 4767, None, None, 5036, None, None, None, 6188, 7066, None, None, None, None, None, None, 8550, None, 10485, 10582, None, None, None, 11879, 12623, 12909, 13739, 14031, 14425, 16420, 16622, 17319, 17599, 17740, None, None, 18828, None, 19359, 19671, 20349, 20752, None, 21153, None, None, None, None, 22062, 22264, 22287, None, 22464, 22888, 23681, 23934, 24597, 24969, 25044, None, 26019, None, 28846, None, 29612, 29918, None, None, None, None, None, None, 32852, None, None, 33282, 33842, 33980, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 40462, None, None, None, 41262, None, 42337, None, 42818, None, None, None, 43735, 43932, 44256, None, 44741, None, None, None, 45112, 45211, 45420, 45539, None, None, None, None, None, None, 46873, None, None, None, 47470, None, None, 48733, None, None, None, None, None, None, 52181, None, None, None, None, 53047, None, 53270, 53561, 53600, 53812, 54243, None, None, None, None, None, 59327, 59890, 61462, 61993, None, None, None, None, None, 65741, None, None, None, None, 66909, 67139, None, 67990, 69021, 69350, 69833, 69908, 72447, 72621, None, 73585, None, None, None, None, 74202, 74455, 74553, None, None, None, 75182, None, None, 76734, 78366, 78870, None, None, None, 79914, 80081, None, 80244, 80519, 81266, 81704, None, None, None, None, None, None, None, 82909, None, None, 89421, None, 89610, None, 89972, 90249, None, 91338, None, None, 91763, 92208, None, None, None, None, None, 93163, None, None, 93517, None, 94017, 94171, 96019, None, None, None, None, None, None, None, 97537, None, None, None, None, None, None, 2558, None, None, None, None, None, None, None, None, 3380, None, None, None, None, None, None, None, None, None, None, 6719, None, None, 8492, 8978, None, 10498, None, None, None, None, None, 12656, None, None, 13587, 13981, None, None, 14175, 15204, None, None, 16496, 17013, None, None, 17558, None, None, 17768, 18704, 18951, 19353, 19421, None, None, 20187, None, 20631, 20838, None, 21253, 22042, 22131, None, None, None, None, None, 22540, None, 23105, 23196, None, None, None, None, None, 24903, None, None, 25283, 25650, 26425, None, 29041, None, None, 29679, None, None, None, 33278, 33532, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 44602, None, None, 45165, None, None, None, None, None, None, None, None, None, 47478, None, None, None, 52219, None, None, 53255, 53446, None, None, 53596, None, 53753, None, 54032, None, 59190, 59717, None, 60119, 60674, 61749, 61955, 62093, None, 66003, 66880, None, 67050, None, None, None, 68455, None, None, None, 69513, None, None, None, None, 72499, None, 72688, None, None, None, None, None, None, None, 74646, 75123, None, 76580, None, 78136, 78703, None, None, 79758, None, None, None, None, None, 80496, 80602, None, 81283, None, None, None, None, None, None, None, None, None, None, 90026, None, 91316, None, None, 91804, 92106, 92305, None, None, None, 93562, 93907, 94083, None, 95935, 96002, 96175, None, None, None, None, None, None, 6386, 6780, None, None, 8723, None, None, None, None, None, None, 13630, None, None, None, None, 14525, 16069, None, None, None, None, 17373, 17585, None, None, None, None, 18902, None, None, None, None, None, 20062, 20221, 20561, None, 20778, 20892, None, 21271, None, None, 22104, 22182, None, 22785, None, None, 23192, 23212, None, None, None, None, None, None, None, None, None, None, None, None, 33277, None, None, 33765, 44598, 44630, None, None, None, None, None, None, None, None, None, None, None, None, 53738, None, 53955, None, 58938, None, 59472, 59759, 59967, None, 60641, 60755, None, 61753, 61786, None, None, 62176, None, None, None, None, 67043, None, 68380, 68853, None, 69704, None, None, None, None, None, None, None, None, None, 76669, None, None, None, None, None, 79805, None, None, None, None, None, 81332, None, 90039, 91224, None, None, None, None, 92199, None, 92335, None, None, None, 93920, None, None, 94585, None, None, None, 96039, 96404, None, 6705, None, 6847, None, None, None, None, 14458, 15126, 15530, 16170, None, None, None, None, None, None, None, 20074, None, 20343, 20470, None, None, None, 20847, None, None, None, None, None, None, None, None, None, None, None, None, 23622, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 59460, 59707, None, 59832, None, 60047, None, None, None, 60990, None, None, None, None, None, 62454, None, None, None, None, None, 69001, 69644, None, None, None, None, None, None, None, None, None, 91116, None, None, None, None, None, None, None, 94383, 95405, None, None, 96372, 96422, None, None, None, None, None, None, 14668, None, None, 15731, None, None, None, None, None, None, None, None, 20842, None, None, None, None, None, None, None, None, None, None, None, 60835, None, 62201, 62461, None, None, None, None, 90596, 91187, None, 94554, 94825, 95658, None, None, None, None, 14533, 14748, 15578, None, None, None, None, None, None, None, None, None, None, 91076, None, None, None, None, 94695, 95219, 95429, 95814, None, 14574, None, None, None, None, None, None, None, None, 95186, None, None, None, 95804, None, None, None, 94841, None, None, None, None, 95132 ],
                              [50604,22540,75981,11191,38238,63035,88325,5005,18450,31290,45112,55991,69833,82289,93907,2848,7845,15578,20778,27193,34400,42556,47043,52923,59759,66880,72866,79192,84593,91371,96649,1438,3574,5790,9984,13739,17585,19671,21560,24597,29918,33079,36160,40797,43728,46330,49159,51526,53646,57434,61753,65016,67853,71649,74106,76997,80496,83198,86619,89679,92447,95405,98754,645,2057,3299,4430,5283,6847,8723,10440,12623,14525,16496,17932,18902,20221,21253,22182,23192,25495,28399,30631,31805,33769,34955,37351,40009,41474,43028,44598,45466,46790,47617,49791,51055,52154,53255,54885,56584,58847,60554,62454,64271,66051,67300,69021,70716,72447,73759,74646,76505,78366,79805,81704,82611,83902,85880,87613,89181,90515,91933,93163,94554,96019,97537,99495,323,1192,1788,2558,2979,3410,4023,4722,5036,5652,6386,7433,8296,9093,10214,10582,11879,13163,14158,14748,16170,17319,17768,18088,18620,19353,20050,20470,20892,21354,22042,22287,22888,23681,25006,26580,27350,29593,30101,31030,31496,32663,33278,34093,34775,35633,36758,37779,38803,40308,41227,42149,42961,43261,44015,44862,45211,46149,46637,46929,47456,48272,49351,50344,50760,51220,51753,52480,53000,53561,53884,55398,56437,57097,57829,59460,59967,60835,61993,62950,63297,64625,65335,66520,67043,67712,68380,69407,69954,71228,72194,72688,73374,74021,74203,75105,76292,76744,78050,78902,79624,80148,81266,82014,82381,82855,83319,84418,85076,86359,87029,88034,88602,89421,90026,91187,91699,92305,92888,93517,94083,94841,95814,96404,96988,97952,99179,99888,96,485,777,1263,1657,1938,2509,2775,2881,3186,3328,3466,3896,4334,4575,4767,5019,5126,5451,5715,6123,6719,7066,7627,8132,8492,9024,9391,10148,10288,10498,10803,11377,12341,12808,13587,14001,14425,14574,15204,15731,16420,17013,17373,17679,17807,18016,18128,18491,18704,19253,19421,19821,20074,20349,20631,20842,21045,21278,21447,21865,22104,22264,22458,22785,23169,23212,23934,24903,25283,26019,27067,27274,27979,29041,29628,29979,30553,30844,31114,31465,31730,32348,32842,33121,33532,33969,34311,34620,34811,35268,35976,36484,36985,37629,38157,38370,39644,40129,40599,40889,41309,41672,42337,42818,42984,43099,43489,43848,44262,44630,44980,45165,45420,45953,46316,46476,46709,46875,46996,47310,47478,47753,48733,49265,49554,50038,50412,50661,50885,51153,51458,51655,51850,52181,52683,52925,53087,53446,53596,53753,54032,55149,55762,56064,56520,56969,57182,57765,58744,59190,59707,59841,60119,60674,61462,61786,62176,62668,63007,63070,64121,64529,64863,65109,65741,66427,66703,66909,67139,67616,67783,67990,68853,69350,69644,69879,70204,70911,71423,71943,72304,72603,72808,73175,73610,73980,74045,74192,74528,74777,75182,76203,76480,76669,76828,77360,78091,78736,79172,79208,79726,80071,80244,80602,81332,81990,82030,82291,82393,82695,83107,83280,83449,84135,84540,84935,85647,86303,86588,86767,87235,88002,88222,88428,89108,89237,89609,89972,90249,91076,91316,91498,91763,92199,92398,92673,93076,93239,93601,93920,94171,94695,95186,95658,95986,96175,96454,96967,97489,97921,98311,99004,99318,99646,99946,None,133,408,589,739,925,1222,1375,1631,1766,1789,2032,2226,2517,2712,2797,None,2882,3126,3220,3315,3380,3433,3513,3644,3950,4093,4335,4493,4579,4761,4824,None,5021,5060,5250,5435,5498,5698,5786,5894,6188,6705,6780,7033,7079,7493,7757,8038,8180,8401,8550,8978,9047,9208,9575,10022,10201,10215,10325,10485,10545,10681,10853,None,11747,12091,12546,12656,12909,13344,13630,13981,14031,14175,14458,14533,14668,15126,15530,None,16069,16398,16435,16622,17017,17322,17558,17599,17740,17771,17841,17995,18066,18118,18171,None,18574,18630,18828,18951,19332,19359,19514,19767,20031,20062,20187,20343,20360,20561,20752,20838,20847,20912,21153,21271,21306,21370,21558,21727,22021,22062,22131,22231,22285,22455,22464,None,22863,23105,23187,23196,23622,23727,24267,24679,24969,25044,25342,25650,26425,26860,27145,None,27286,27391,28381,28846,29496,29612,29679,29925,30090,30117,30619,30742,30953,31067,31220,None,31476,31650,31796,32198,32501,32717,32852,33093,33277,33282,33765,33842,33980,34206,34373,34570,34623,34804,34834,35218,35369,35790,36056,36213,36531,36907,37187,37596,37754,37982,38167,None,38460,38889,39965,40121,40242,40462,40733,40816,41150,41262,41430,41536,41728,42311,42379,None,42902,42977,43007,43067,43181,43341,43637,43735,43932,44256,44288,44602,44741,44889,45008,None,45181,45275,45429,45539,45979,46180,46324,46462,46528,46684,46788,46873,46909,46972,47005,47116,47320,47470,47605,47714,48102,48378,48916,49174,49302,49374,49620,49823,50158,50351,50424,None,50676,50812,51022,51106,51158,51437,51466,51544,51740,51782,52044,52179,52219,52672,52909,None,52980,53047,53109,53270,53508,53592,53600,53738,53812,53955,54243,55048,55188,55559,55935,None,56192,56493,56563,56749,57045,57153,57307,57737,57798,57920,58829,58938,59327,59472,59717,59832,59890,60047,60384,60641,60755,60990,61749,61771,61955,62093,62201,62461,62908,62969,63032,None,63215,63771,64262,64371,64556,64842,65013,65057,65142,65609,66003,66172,66511,66584,66859,None,67023,67050,67162,67363,67668,67780,67822,67916,68107,68455,69001,69110,69373,69513,69704,None,69908,70055,70500,70861,71086,71231,71570,71865,72149,72278,72365,72499,72621,72738,72814,72895,73234,73585,73616,73831,74013,74039,74049,74177,74202,74455,74553,74747,74916,75123,75589,None,76285,76375,76501,76580,76734,76793,76874,77099,77468,78075,78136,78703,78870,79054,79187,None,79305,79632,79758,79914,80081,80165,80365,80519,80743,81283,81507,81883,82005,82021,82065,None,82311,82383,82443,82633,82736,82909,83156,83207,83306,83437,83807,84090,84308,84450,84577,84851,84988,85560,85705,86224,86335,86478,86593,86656,86880,87060,87366,87935,88026,88123,88289,None,88459,88925,89163,89225,89303,89580,89610,89930,90001,90039,90495,90596,91116,91224,91338,91399,91599,91723,91804,92106,92208,92335,92405,92481,92817,93000,93126,93220,93480,93562,93884,None,94017,94099,94383,94585,94825,95132,95219,95429,95804,95935,96002,96039,96372,96422,96638,96734,96977,97362,97523,97782,97948,97963,98695,98928,99152,99313,99363,99611,99855,99924,99956])
                         ])
def test(input, expected):
    input_tree = str(to_bst(input))

    print(input_tree)
    # actual_tree = Solution().balanceBST(input_tree)
    # actual = to_array(actual_tree)

  #  assert actual == expected