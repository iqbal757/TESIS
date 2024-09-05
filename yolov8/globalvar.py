global causes_data_file
global empty
global err_internal
global err_upload_file
global class_name

data_file = ''
empty = ''


err_internal = 'Error : Hasil Klasifikasi Tidak Bisa Ditampilkan, Terjadi Kesalahan Internal !!'
err_upload_file = 'Error : Kesalahan Terjadi Saat Unggah File Dataset, Periksa Kembali File Dataset !!'
err_empty = 'Error : Input Lirik Lagu Tidak Boleh Kosong, Silakan Diisi Terlebih Dahulu !!'
succ_train = 'Proses Latih Ulang Sistem Klasifikasi BERHASIL Dilakukan, Silakan Melakukan Klasifikasi Lirik Lagu'
succ_test = 'Hasil Klasifikasi Lirik Lagu Berasal Dari Daerah : '

global FILE_DATASET
FILE_DATASET = 'data\/data_lirik_lagu.csv'

global FILE_TRAIN
FILE_TRAIN= 'data\/train.bin'

global SET_SAMPLE_RATE
SET_SAMPLE_RATE = 48000

global EXT
EXT = 'wav'

global K_VALUE
K_VALUE = 5
