#coding: utf-8
import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import scipy.misc

fw = open('history.txt', 'a+')
history = set()

def load_history(filename):
    f = open(filename)
    for line in f:
        line = line.strip()
        history.add(line)


def work():
    for root,dirnames,filenames in os.walk('/home/hcxy/Documents/hcxy/classfication/adni-processed/'):
        for filename in filenames:
            if filename.endswith('brain.nii.gz'):
                f = filename.split('_')[0].strip()
                if f in history:
                    continue
                print f
                if os.path.exists('/home/hcxy/Documents/hcxy/classfication/pic/' + f) == False:
                    os.mkdir('/home/hcxy/Documents/hcxy/classfication/pic/' + f)
                nil_img = nib.load(root + filename).get_data()
                for i in range(nil_img.shape[0]):
                    slice_0 = nil_img[i, :, :]
                    slice_0 = np.array(slice_0, dtype = np.int8)
                    scipy.misc.toimage(slice_0, cmin = 0, cmax = 255).save(
                        '/home/hcxy/Documents/hcxy/classfication/pic/' + f + '/' + str(i) + '_' + 'x' + '.jpg')
    print('x save done')
                
def main():
    load_history('history.txt')
    work()
  
if __name__ == '__main__':
    main()
