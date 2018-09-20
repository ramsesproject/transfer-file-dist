# distribution4file-transfer
A file size distribution based on more than 40 billion files transferred by real users.

function **gen_filesize_list_globusonline** can be used to Generate a list of file size by given a total dataset size, and the generated file size will follow the file size distribution extracted from about 3.2 billion files transferred by using Globus online in 2017

function **gen_filesize_list_gridftp** can be used to generate a list of file size by given a total dataset size, the generated file size will follow the file size distribution extracted from about 5.4 billion files transferred by using Globus GridFTP in 2017. Specifically, include 'globusonline-fxp', 'globus-url-copy', 'libglobus_ftp_client',  and 'fts_url_copy'. brief introduction about the dataset and transfer tools are available  in our paper https://doi.org/10.1145/3208040.3208053

This distribution can be used to generate dataset to profile and benchmark file transfer tools, and/or optimization to existing transfer tools.
