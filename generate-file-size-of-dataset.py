from scipy.stats import rv_discrete
import random
import numpy as np

'''
Generate a list of file size by given a total dataset size
the generated file size will follow the file size distribution 
extracted from about 3.2 billion files transferred by using Globus online in 2017
'''
def gen_filesize_list_globus(dataset_size):
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

if __name__ == '__main__':
    print gen_filesize_list_globus(12e6)
    print gen_filesize_list_gridftp(122e6)