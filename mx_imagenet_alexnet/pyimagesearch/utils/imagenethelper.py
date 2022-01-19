import numpy as np
import os

class ImageNetHelper:
    def __init__(self, config):
        self.config = config

        self.labelMappings = self.buildClassLabels()
        self.valBlacklist = self.buildBlacklist()

    def buildClassLabels(self):
        rows = open(self.config.WORD_IDS).read().strip().split('\n')
        labelMappings = {}

        for row in rows:
            wordID, label, hrLabel = row.split(' ')

            labelMappings[wordID] = int(label) - 1

        return labelMappings

    def buildBlacklist(self):
        rows = open(self.config.VAL_BLACKLIST).read()
        rows = set(rows.strip().split('\n'))

        return rows

    def buildTrainingSet(self):
        paths = []
        labels = []

        wordIDs = os.listdir(r'D:\Dataset\ImageNet\train')

        for wordID in wordIDs:
            path = os.path.sep.join([self.config.IMAGES_PATH,
                                     'train', wordID])
            images = os.listdir(path)
            for image in images:
                real_path = os.path.sep.join([path, image])
                label = self.labelMappings[wordID]
                paths.append(real_path)
                labels.append(label)

        return np.array(paths), np.array(labels)

    def buildValidationSet(self):
        paths = []
        labels = []

        valFilenames = os.listdir(r'D:\Dataset\ImageNet\val')

        valLabels = open(self.config.VAL_LABELS).read()
        valLabels = valLabels.strip().split('\n')

        for row, label in zip(valFilenames, valLabels):
            imageNum = int(row.split('_')[2].split('.')[0])

            if imageNum in self.valBlacklist:
                continue

            path = os.path.sep.join([self.config.IMAGES_PATH, "val", row])
            paths.append(path)
            labels.append(int(label) - 1)

        return np.array(paths), np.array(labels)



