projects = {
    'cmip5': {
        'start_dir': '/badc/cmip5/data/cmip5',
        'base': '/badc/cmip5/data'
        'prefacets': 3,
        'facets': 'badc cmip6 data project mip institution model experiment ensemble table variable grid version'.split(),
        'facet_picks': {'ensemble': 'r1i1p1'},
        'wildcards': ['institution', 'model']
    }
}

