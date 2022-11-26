import time

arr = [288768, 169985, 133120, 483338, 491530, 307210, 393229, 26638, 10253, 110608, 368662, 419862, 458775, 30, 266271, 249887, 389151, 264226, 219169, 180262, 284713, 18478, 174127, 223279, 108592, 327732, 270389, 198710, 194612, 69689, 356410, 321597, 81983, 313408, 469056, 413761, 387139, 325701, 458822, 319559, 172103, 421961, 149578, 497738, 383051, 178253, 221263, 430162, 63573, 41050, 63579, 424026, 395360, 376930, 344165, 252008, 223340, 118893, 116845, 346220, 45170, 14454, 356471, 379000, 479354, 356475, 36988, 110717, 53374, 442494, 452736, 362626, 370820, 65669, 75910, 465033, 444554, 231568, 110737, 313494, 86168, 100508, 137374, 407710, 407711, 356514, 385189, 299173, 252408, 229546, 356525, 463022, 465074, 284851, 139445, 364727, 174264, 153787, 12475, 252091, 221372, 80064, 127171, 454853, 397510, 258257, 469208, 45272, 495833, 35041, 258274, 418019, 59620, 82150, 51431, 301294, 393455, 258289, 315634, 282865, 190708, 348407, 450808, 264442, 45306, 248058, 491773, 407804, 426241, 26883, 14596, 383236, 395526, 20748, 321810, 223509, 12565, 403734, 80152, 307482, 440602, 241953, 446753, 227623, 403752, 231719, 151851, 323884, 319789, 278828, 221487, 305456, 196912, 24886, 350519, 192824, 325946, 223548, 397630, 92480, 405824, 149824, 82245, 186697, 483658, 18763, 174412, 495947, 270669, 104783, 186704, 149841, 188753, 270676, 55637, 57686, 239959, 305494, 229722, 61790, 414047, 201058, 131427, 213348, 47458, 98660, 477540, 217449, 299370, 2413, 282990, 22895, 493936, 221549, 436595, 192883, 483704, 27001, 250235, 29053, 61821, 145791, 139649, 409988, 342405, 418182, 92550, 346501, 207241, 100746, 485771, 461195, 143758, 391567, 326035, 160155, 82336, 96678, 496045, 434608, 201140, 471477, 33209, 27067, 29117, 266685, 303553, 254402, 231875, 12741, 303558, 405959, 424391, 16841, 215502, 29135, 20945, 461266, 45523, 307667, 137685, 190933, 352729, 328154, 231905, 475617, 301538, 436718, 168430, 111088, 387569, 487924, 428533, 322038, 84470, 260598, 119289, 340471, 342523, 217595, 107005, 381438, 416246, 139770, 186881, 207369, 498187, 156176, 227861, 119318, 250391, 193047, 94746, 348700, 193057, 174626, 365093, 90662, 420395, 74285, 125489, 475698, 483894, 346680, 248376, 369209, 277051, 367161, 293432, 401988, 440902, 299590, 408136, 88646, 289356, 211535, 100945, 307795, 297556, 475731, 129620, 266835, 31322, 41563, 420443, 483937, 45666, 96866, 279138, 53857, 402022, 293473, 92770, 82533, 485998, 66161, 455284, 174714, 256635, 238204, 182909, 303743, 307846, 162438, 400011, 8843, 250514, 309908, 43671, 49817, 410266, 170651, 127644, 55965, 385699, 152232, 469674, 297643, 453292, 117418, 451242, 74417, 383669, 176825, 53947, 451260, 252604, 438972, 205503, 109252, 344773, 371406, 332494, 328401, 53972, 21204, 322262, 248534, 25302, 58073, 408282, 455388, 152288, 101096, 19178, 412395, 90860, 318194, 148212, 357109, 447222, 379639, 105208, 252662, 338684, 408317, 156414, 232198, 453383, 408328, 498443, 23310, 66319, 107280, 492308, 381717, 340758, 330520, 135961, 394010, 113435, 252699, 236313, 486170, 432922, 258851, 148259, 359205, 322346, 267053, 486189, 178996, 232244, 138037, 404282, 379707, 287553, 383815, 207689, 496458, 19274, 246606, 308048, 291667, 293715, 115544, 400217, 201560, 52059, 195422, 95072, 236386, 469860, 457573, 426854, 349030, 418664, 459626, 271216, 424819, 445301, 271223, 416632, 11130, 58238, 359295, 441217, 86914, 144259, 269189, 328583, 160653, 197517, 27533, 74641, 347029, 318358, 168855, 19352, 13215, 119714, 414629, 322471, 64424, 318375, 43946, 43948, 353198, 304048, 271281, 314292, 244662, 482231, 256952, 426939, 3005, 484285, 447424, 54210, 486342, 238535, 132040, 80843, 93134, 318415, 353231, 467924, 107477, 156630, 291800, 336858, 351195, 21468, 250846, 306143, 201696, 386016, 111586, 148453, 222182, 209894, 115686, 197609, 363497, 218091, 216041, 177134, 429039, 207860, 312310, 472056, 285691, 224251, 248832, 277505, 17409, 136195, 64516, 252933, 279557, 37895, 238601, 347147, 398348, 447501, 463892, 105492, 465942, 89110, 300058, 496668, 312355, 222245, 388136, 187433, 363563, 189484, 418860, 298031, 257073, 109621, 76855, 171066, 201788, 50237, 164926, 287808, 336961, 459845, 201799, 396360, 37959, 490572, 332877, 27727, 42065, 445527, 148569, 68702, 314462, 390239, 435300, 470116, 392300, 50285, 169070, 455788, 214128, 54385, 148594, 439411, 406642, 463989, 62581, 287856, 310392, 406650, 416892, 126078, 343167, 337025, 488578, 423045, 35977, 406666, 224395, 255117, 478350, 349327, 418961, 169105, 31892, 5269, 302231, 148636, 64668, 187551, 255138, 322726, 421034, 289963, 453806, 320687, 122031, 76977, 484530, 494771, 193715, 79032, 355513, 335037, 453821, 144575, 421054, 236739, 66757, 117961, 238798, 154831, 9423, 177365, 214229, 13527, 70872, 435417, 324825, 103642, 117981, 191709, 296163, 7400, 148715, 496877, 81135, 290033, 70898, 355570, 140533, 335094, 326903, 255224, 468215, 204021, 447739, 105724, 216310, 437504, 15618, 9480, 347401, 87306, 265485, 15630, 294159, 355600, 312592, 134418, 339218, 345362, 167189, 23830, 199960, 359705, 193818, 451867, 441628, 468249, 138521, 171291, 341281, 118051, 251172, 25893, 374054, 36135, 163108, 21801, 46377, 58671, 271664, 15665, 218415, 64818, 468274, 70965, 142646, 228662, 154934, 310584, 19769, 372022, 435516, 349501, 83260, 120127, 173370, 499009, 142662, 496967, 261446, 7500, 468307, 30044, 304482, 40290, 91492, 30053, 181607, 294247, 50535, 300392, 7531, 93548, 335214, 367983, 255345, 361841, 85362, 79217, 413045, 79218, 449908, 480634, 494972, 394622, 28030, 466302, 218495, 130433, 294275, 339332, 269700, 1411, 368007, 322953, 458122, 157067, 216462, 345488, 105872, 56726, 277911, 48536, 386463, 282016, 181671, 32168, 243113, 409007, 91567, 220596, 140726, 322999, 36280, 40376, 495033, 259517, 443842, 42435, 19906, 58821, 406982, 167365, 263626, 359885, 370127, 83409, 374228, 40405, 13781, 171480, 175578, 437724, 124382, 275935, 417246, 15842, 165347, 308715, 24043, 331245, 22000, 181745, 415218, 310771, 146930, 65012, 134641, 341495, 253427, 71161, 130555, 278015, 200194, 105987, 97797, 413190, 15879, 97803, 407054, 413199, 130576, 134670, 386582, 484887, 40473, 423455, 437793, 153124, 265767, 439850, 251436, 136753, 431666, 300594, 495156, 337461, 106036, 423479, 58936, 138810, 384573, 386624, 7747, 480836, 398919, 431690, 460364, 325197, 425550, 388685, 165458, 153177, 138842, 61019, 130652, 388702, 319072, 3682, 224867, 398949, 58990, 218736, 46704, 419442, 499321, 493181, 278142, 448129, 93833, 405130, 415373, 355984, 292497, 460432, 378516, 233109, 358039, 89753, 315035, 161436, 181917, 269986, 403107, 59044, 269989, 126632, 374444, 138931, 249527, 464567, 159417, 388792, 95931, 91835, 356027, 493242, 153276, 48834, 126658, 333508, 458437, 376516, 216775, 173774, 370383, 116433, 429777, 227027, 52948, 216789, 390873, 315104, 319204, 36583, 63208, 259817, 34539, 136941, 437998, 22256, 204528, 55028, 263924, 370428, 134910, 124672, 366341, 280327, 325388, 34580, 401173, 237333, 202519, 196379, 376607, 36640, 386848, 79648, 208673, 487204, 485159, 132904, 294698, 50991, 386866, 470837, 51007, 423746, 89923, 83781, 89925, 374600, 196430, 53075, 380755, 151387, 91996, 339805, 57181, 149344, 337770, 307050, 489326, 249712, 264049, 200564, 167798, 362360, 69497, 188282, 434046, 57214, 300928, 262017, 10115, 458627, 343941, 483208, 401288, 161680, 173970, 65427, 302995, 264085, 165784, 241560, 483226, 311194, 352158, 79775, 391076, 159653, 380839, 94120, 309161, 440238, 436144, 475059, 321460, 130999, 417722, 341950, 292802, 108485, 151494, 327623, 18376, 88009, 452557, 477134, 110545, 208854, 366553, 165850, 327643, 436190, 194527, 311264, 268258, 118755, 456674, 227304, 339949, 165870, 393197, 337908, 403448, 47098, 317436]
keys = [237333, 357001, 317436]

start = time.time()
for key in keys:
    exist = False
    for i in range(len(arr)):
        if arr[i] == key:
            print("%d exists in #%d" % (key, i))
            exist = True
    if not exist:
        print("%d does not exist" % key)
print("Running time: %.9f seconds" % (time.time() - start))