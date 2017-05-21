make

use example:

train:
./word2vec -train segmentation_result_train.txt -output vectors.txt -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -thread 12 -binary 1

obtain the vector
./vector vectors.bin

obtain the closest distance word
./distance vector.bin

More information about the scripts is provided at https://code.google.com/p/word2vec/

