measure_data = {'Word2Vec-LogisticRegression':
{
'roc_auc': [0.9332802833265021, 0.9363329975495067, 0.9382358451210476, 0.9387562110609853, 0.939024371528053, 0.9392711796169045, 0.9394406993387306, 0.9394720467015617],
'f1': [0.9395171790251705, 0.941059662269302, 0.9423463690808892, 0.9427049667076121, 0.9430303848705429, 0.943251031564078, 0.9433825067202246, 0.9433672332172375],
'accuracy': [0.9001027184661222, 0.9026719002059074, 0.9048778657495822, 0.9054593477415672, 0.9061524613445574, 0.9064865224716471, 0.9066206470244499, 0.9064865236792076]
 },
'BagOfWords-Tfidf-NaiveBayes':
{
'roc_auc': [0.912424049873255, 0.9150311684741165, 0.9171772616260864, 0.9210915426713733, 0.9204782646968325, 0.9207315447702286, 0.9221934292487767, 0.922351204663332],
'f1': [0.9173912765325758, 0.919891885813517, 0.9226491831398507, 0.9236741641033267, 0.9252496700430096, 0.9258045048580645, 0.9258288591750526, 0.9252860766816431],
'accuracy': [0.8556610533844067, 0.8605503310897937, 0.8659777726901834, 0.8678180203786496, 0.8709986799350204, 0.872057509594371, 0.8720158578640765, 0.8709287039309949]
},
'BagOfWords-Tfidf-LogisticRegression':
{
'roc_auc': [0.9413482835316218, 0.9475544499996493, 0.9515945730482188, 0.9532792241192874, 0.9541296549817414, 0.9548247624652427, 0.9552742408755623, 0.9553041900765399],
'f1': [0.9425362675839432, 0.9460997417699791, 0.948617474413138, 0.9496282489306888, 0.9503077693973742, 0.9507888516481807, 0.9511051426425673, 0.9511304991836615],
'accuracy': [0.9041622483742273, 0.9107434855002556, 0.9151929037648904, 0.9170073268941353, 0.9183543989779867, 0.9191808032571295, 0.9197081357832338, 0.9197048031706139]
},
'BagOfWords-CountVectorizer-LogisticRegression':
{
'roc_auc': [0.9174300146940487, 0.9295016580597183, 0.9369831933098434, 0.9396411679937913, 0.9418982078449852, 0.9432852559525994, 0.9438330442654413, 0.943654991785416],
'f1': [0.9388315983237304, 0.9428108574395102, 0.9456828842163989, 0.9469244637169227, 0.9478066585715984, 0.9485190602919774, 0.9488457266691629, 0.9488696908097087],
'accuracy': [0.8990972047582703, 0.9051544380649812, 0.9100195556290825, 0.9121230527817697, 0.9137683632500173, 0.9149679809135459, 0.9155427985922072, 0.9155336342312532]
},
'BagOfWords-CountVectorizer-NaiveBayes':
{
'roc_auc': [0.8877376174485199, 0.894690083817192, 0.8962203458094876, 0.9004002754865588, 0.9004246532789387, 0.8998439654499202, 0.9016417889313804, 0.902031761350795],
'f1': [0.9097952247127613, 0.9095687253232464, 0.9146765022199211, 0.9178701455824702, 0.9175544168345113, 0.9200207389168358, 0.92285885517488, 0.9245961233363124],
'accuracy': [0.8584326601826772, 0.8587225679703416, 0.8657819899299467, 0.8704729964367028, 0.8700398004098499, 0.8733254271972782, 0.8773216576193691, 0.8797425552136907]
},
'BagOfCentroids-RandomForest':
{
'roc_auc': [0.7978921627035666, 0.7948546399625078, 0.8108990388575589, 0.7873944088432193, 0.7882148056184825, 0.767567413377995, 0.7902300801152168, 0.7957396211186433],
'f1': [0.9019143166813439, 0.9018991382454565, 0.9051453563192483, 0.9038372787818276, 0.9034794924446977, 0.9028222034596155, 0.9032517253448821, 0.9045767991391219],
'accuracy': [0.8296110447239741, 0.8298209890006399, 0.8366363231785018, 0.8328866813519608, 0.8331615973608987, 0.8305774171633291, 0.8324209972645432, 0.8351218055248774]
},
'Word2Vec-RandomForest':
{
'roc_auc': [0.8745607146399506, 0.8843627077553977, 0.8935942260311737, 0.8969391770599436, 0.8996820297507725, 0.9009933472756672, 0.9020308689248654, 0.9026410389894594],
    'f1': [0.9187876721019305, 0.9216672251944167, 0.924199873856697, 0.9252093964532158, 0.9265148970748398, 0.9268621443711447, 0.927083319246529, 0.9269239312995875],
    'accuracy': [0.8601371418315603, 0.8656303902317766, 0.8701689455125106, 0.8720383500230419, 0.8746258623543713, 0.8753064790920516, 0.8756238787341976, 0.8751865174756027],
},
'BagOfWords-Tfidf-RandomForest':
{
    'roc_auc': [0.9056109539305205, 0.9161591193730726, 0.9224962208352206, 0.9258513278510717, 0.927918311474489, 0.9290795743335298, 0.9305299466830071, 0.9308711944465466],
    'f1': [0.9240871939301147, 0.9277230443270016, 0.9325226262250027, 0.9341070675062532, 0.93619983618388, 0.9370133143849517, 0.9376970076288956, 0.9377293070647662],
    'accuracy': [0.8689976236326163, 0.8759195875981627, 0.8850150275186306, 0.8879907479112176, 0.8919120024880264, 0.8934898336270374, 0.8946761234800628, 0.8946952833303801]
},
'BagOfWords-CountVectorizer-RandomForest':
{
    'roc_auc': [0.8994789973146688, 0.909326978066466, 0.9165210257384043, 0.9199945503982536, 0.921494610913235, 0.9229664557681617, 0.9241004011568871, 0.9247151608496066],
    'f1': [0.9237168532440085, 0.9273664342311769, 0.9315649260453954, 0.9330763189695622, 0.9350904555599678, 0.9358902637995743, 0.9364536220651744, 0.9364323165530677],
    'accuracy': [0.8684761275143633, 0.8753905929401595, 0.8833538935935991, 0.8861205128594011, 0.8899318020336606, 0.8914596489843368, 0.8924551662201213, 0.8923676939176014]
}
}
