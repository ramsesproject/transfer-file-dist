from __future__ import division
from scipy.stats import rv_discrete
import random
import numpy as np
from matplotlib import pyplot as plt

'''
Generate a list of file size by given a total dataset size
the generated file size will follow the file size distribution 
extracted from about 3.2 billion files transferred by using Globus online in 2017
'''
def gen_filesize_list_globusonline(dataset_size):
    hist = np.load('globusonline-hist.npy')
    num = range(hist.shape[0])
    random_variable = rv_discrete(values=(num, hist))
    total = 0
    res = []
    while total < dataset_size:
        _bin = random_variable.rvs(size=1)[0]
        _one = random.randint(2**_bin, 2**(_bin + 1))
        total += _one
        res.append(_one)
    return res

def filesize_globusonline_cmp(fs_list):
    fsize_r_hist = np.load('globusonline-hist.npy')
    fsize_r_hist = fsize_r_hist / np.sum(fsize_r_hist)
     
    fsize_g = np.log2(fs_list).astype('int')
    fsize_g_hist = np.array([fsize_g[fsize_g==s].shape[0]/fsize_g.shape[0] for s in range(fsize_r_hist.shape[0])])

    jsd = 0.5 * np.sum([_p * np.log2(_p / _q) for _p, _q in zip(fsize_g_hist, fsize_r_hist) if _p != 0]) + \
          0.5 * np.sum([_p * np.log2(_p / _q) for _p, _q in zip(fsize_r_hist, fsize_g_hist) if _q != 0])
    
    plt.figure(figsize=(8.9, 5))
    plt.bar(np.arange(fsize_r_hist.shape[0]), 100.*fsize_r_hist, align='edge', color='g', hatch='\\', width=-.35, label='Real')
    plt.bar(np.arange(fsize_g_hist.shape[0]), 100.*fsize_g_hist, align='edge', color='y', hatch='o', width=.35, label='Generated')  
    plt.xlim((-.5, fsize_g_hist.shape[0]-.5))
    plt.xticks(range(0, fsize_g_hist.shape[0], 5), [r'$2^{%d}$' % d for d in range(0, fsize_g_hist.shape[0], 5)])
    plt.legend(loc=0, fontsize=16)
    plt.xlabel('File size (byte)', fontsize=18)
    plt.ylabel('Frequency (%)', fontsize=18)
    plt.title('Jensen-Shannon Divergence: %.4f' % (jsd))
    
    plt.show()
    plt.close()

'''
Generate a list of file size by given a total dataset size
the generated file size will follow the file size distribution 
extracted from about 5.4 billion files transferred by using Globus GridFTP in 2017
Specifically, include 'globusonline-fxp', 'globus-url-copy', 'libglobus_ftp_client', 
and 'fts_url_copy'. brief introduction about the dataset and transfer tools are available 
in our paper https://doi.org/10.1145/3208040.3208053
'''
def gen_filesize_list_gridftp(dataset_size):
    hist = np.load('gridftp-all-hist.npy')
    num = range(hist.shape[0])
    random_variable = rv_discrete(values=(num, hist))
    total = 0
    res = []
    while total < dataset_size:
        _bin = random_variable.rvs(size=1)[0]
        _one = random.randint(2**_bin, 2**(_bin + 1))
        total += _one
        res.append(_one)
    return res

def filesize_gridftp_cmp(fs_list):
    fsize_r_hist = np.load('gridftp-all-hist.npy')
    fsize_r_hist = fsize_r_hist / np.sum(fsize_r_hist)
     
    fsize_g = np.log2(fs_list).astype('int')
    fsize_g_hist = np.array([fsize_g[fsize_g==s].shape[0]/fsize_g.shape[0] for s in range(fsize_r_hist.shape[0])])

    jsd = 0.5 * np.sum([_p * np.log2(_p / _q) for _p, _q in zip(fsize_g_hist, fsize_r_hist) if _p != 0]) + \
          0.5 * np.sum([_p * np.log2(_p / _q) for _p, _q in zip(fsize_r_hist, fsize_g_hist) if _q != 0])

    plt.figure(figsize=(8.9, 5))
    plt.bar(np.arange(fsize_r_hist.shape[0]), 100.*fsize_r_hist, align='edge', color='g', hatch='\\', width=-.35, label='Real')
    plt.bar(np.arange(fsize_g_hist.shape[0]), 100.*fsize_g_hist, align='edge', color='y', hatch='o', width=.35, label='Generated')  
    plt.xlim((-.5, fsize_g_hist.shape[0]-.5))
    plt.xticks(range(0, fsize_g_hist.shape[0], 5), [r'$2^{%d}$' % d for d in range(0, fsize_g_hist.shape[0], 5)])
    plt.legend(loc=0, fontsize=16)
    plt.xlabel('File size (byte)', fontsize=18)
    plt.ylabel('Frequency (%)', fontsize=18)
    plt.title('Jensen-Shannon Divergence: %.4f' % (jsd))
    
    plt.show()
    plt.close()
    
if __name__ == '__main__':
    np.random.seed(2018)
    fs_list_gridftp = gen_filesize_list_gridftp(4e10)
    filesize_gridftp_cmp(fs_list_gridftp)

    fs_list_globusonline = gen_filesize_list_globusonline(1e10)
    filesize_globusonline_cmp(fs_list_globusonline)
