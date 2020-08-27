import glob
import os

import xarray as xr

from dachar.utils.character import get_coords
from daops_tester.settings import projects


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


def merge_domains(d1, d2, f1, f2):
    if set(d1.keys()) != set(d2.keys()):
        raise Exception(f'Domains are different for files: \n\t{f1}\n\t{f2}')

    d = {}

    for key in d1.keys():
        d[key] = {}
        d1c = d1[key]
        d2c = d2[key]

        for prop in ('value', 'units', 'length', 'id', 'max', 'min', 'calendar'):
            if prop in d1c and prop not in d2c:
                raise Exception(f'Coords are different across domain: \n\t{d1c}\n\t{d2c}')

        if d1c.get('calendar', None) != d2c.get('calendar', None):
            raise Exception(f'Calendars differ between files: \n\t{f1}\n\t{f2}')

        mn = d1c.get('min', d1c.get('value'))
        mx = d2c.get('max', d2c.get('value'))
      
        d[key] = {'id': d1c['id'], 'range': (mn, mx), 'units': d1c.get('units', None)}

    return d
             

def get_file_domain(fpath):
    ds = xr.open_dataset(fpath, use_cftime=True)
    
    var_id = os.path.basename(fpath).split('_')[0]
    coords = get_coords(ds[var_id])
    return coords
    
x = get_file_domain('/badc/cmip5/data/cmip5/output1/MIROC/MIROC-ESM/esmControl/day/ocean//day/r1i1p1/latest/tos/tos_day_MIROC-ESM_esmControl_r1i1p1_18500101-18691231.nc')


def get_ds_domain(f1, f2):
    d1 = get_file_domain(f1)
    d2 = get_file_domain(f2)

    return merge_domains(d1, d2, f1, f2)


def get_common_domain(sample_id, proj):

    ds_dirs = get_ds_dirs(sample_id, proj)
    file_pairs = [get_file_pairs(_) for _ in ds_dirs]

    domains = []
 
    for f1, f2 in file_pairs:
        dmn = get_ds_domain(f1, f2)
        domains.append((dmn, f1, f2))

    return domains

pth = 'cmip5/output1/MIROC/MIROC-ESM/esmControl/day/ocean//day/r1i1p1/latest/tos'.replace('/', '.')
pth = 'cmip5/output1/*/*/esmControl/day/ocean//day/r1i1p1/latest/tos'.replace('/', '.')

d = get_common_domain(pth, 'cmip5')
for dmn, f1, f2 in d:
    print(f1, f2)
    print(dmn)
    print()
    
