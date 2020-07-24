import pytest

import xarray as xr

from daops_tester.clisops_loader import cops


ds = None


def setup_module():
    global ds
    ds = xr.open_dataset('/badc/cmip5/data/cmip5/output1/MPI-M/MPI-ESM-LR/esmControl/day/ocean/day/r1i1p1/latest/tos/tos_day_MPI-ESM-LR_esmControl_r1i1p1_18500101-18591231.nc', use_cftime=True)
    

def _stat(x, stat, is_time=False):
    r = eval(f'x.values.{stat}()')
    if is_time:
        r = r.strftime()
    return r


def _min(x, is_time=False):
    return _stat(x, 'min', is_time)


def _max(x, is_time=False):
    return _stat(x, 'max', is_time)

    
def test_clisops_subset_bbox_i_j_grid():
    res = cops.subset_bbox(ds['tos'], lon_bnds=(55, 88), lat_bnds=(-10, 20), start_date='1850-01-01T12:00:00', end_date='1850-04-01T12:00:00')

    lat = res.lat
    lon = res.lon
    tm = res.time

    assert(_min(lat) > -15 and _max(lat) < 25)
    assert(_min(lon) > 50  and _max(lon) < 95)
    assert(_min(tm, True)  == '1850-01-01 12:00:00' and _max(tm, True) == '1850-04-01 12:00:00')


@pytest.mark.xfail(reason="Subset crossing Greenwich Meridian when data is 0-360 not implemented.")
def test_clisops_subset_bbox_i_j_grid_fail_over_0_longitude():
    res = cops.subset_bbox(ds['tos'], lon_bnds=(-50, 50), lat_bnds=(-10, 20), start_date='1850-01-01T12:00:00', end_date='1850-04-01T12:00:00')

    print(res.lat.min(), res.lat.max())
    print(res.lon.min(), res.lon.max())
    print(res.time.min(), res.time.max())
    print('LON IS WRONG IN SECOND ONE!')


def teardown_module():
    ds.close()

