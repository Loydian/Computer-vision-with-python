from os import path

BASE_PATH = r"D:\Dataset\ImageNet"

IMAGES_PATH = BASE_PATH
DEVKIT_PATH = path.sep.join([BASE_PATH, r"devkit\data"])

WORD_IDS = path.sep.join([DEVKIT_PATH, 'map_clsloc.txt'])

VAL_LABELS = path.sep.join([DEVKIT_PATH, 'ILSVRC2015_clsloc_validation_ground_truth.txt'])
VAL_BLACKLIST = path.sep.join([DEVKIT_PATH, 'ILSVRC2015_clsloc_validation_blacklist.txt'])

NUM_CLASSES = 1000
NUM_TEST_IMAGES = 50 * NUM_CLASSES

MX_OUTPUT = r'D:\Dataset\ImageNet'
TRAIN_MX_LIST = path.sep.join([MX_OUTPUT, r'lists\train.lst'])
VAL_MX_LIST = path.sep.join([MX_OUTPUT, r'lists\val.lst'])
TEST_MX_LIST = path.sep.join([MX_OUTPUT, r'lists\test.lst'])

TRAIN_MX_REC = path.sep.join([MX_OUTPUT, r'rec\train.rec'])
VAL_MX_REC = path.sep.join([MX_OUTPUT, r'rec\val.rec'])
TEST_MX_REC = path.sep.join([MX_OUTPUT, r'rec\test.rec'])

DATASET_MEAN = path.sep.join([MX_OUTPUT, r'output\imagenet_mean.json'])

BATCH_SIZE = 32
NUM_DEVICES = 1





