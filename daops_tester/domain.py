import glob

import xarray as xr


from .settings import 


def get_ds_dirs(sample_id, proj):
    prj = projects[proj]
    basedir = prj['base']

    pattn = f'{basedir}/{sample_id.replace(".", "/")}'
    dirs = glob.glob(pattn)

    return dirs


def get_file_pairs(dr):
    """Returns first and last file (which might be the same).

    Args:
        dr ([type]): [description]

    Returns:
        [type]: [description]
    """
    files = glob.glob(f'{dr}/*.nc')
    return files[0], files[-1]


def merge_domains(d1, d2):
    

def get_file_domain(fpath):


def get_ds_domain(f1, f2):
    d1 = get_file_domain(f1)

    if f1 == f2:
        return d1

    d2 = get_file_domain(f2)

    return merge_domains(d1, d2)


def get_common_domain(sample_id, proj):

    ds_dirs = get_ds_dirs(sample_id, proj)
    file_pairs = [get_file_pairs(_) for _ in ds_dirs]

    domains = [get_ds_domain(*_) for _ in file_pairs]