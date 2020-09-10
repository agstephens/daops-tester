projects = {
    'cmip6': {
        'start_dir': '/badc/cmip6/data/cmip6',
        'base': '/badc/cmip6/data',
        'prefacets': 3,
        'facets': 'badc cmip6 data mip_era activity_id institution_id source_id experiment_id member_id table_id variable_id grid_label version'.split(),
        'facet_picks': {'ensemble': 'r1i1p1'},
        'wildcards': ['institution', 'model']
    },
    'c3s-cmip5': {
        'start_dir': '/group_workspaces/jasmin2/cp4cds1/vol1/data/c3s-cmip5',
        'base': '/group_workspaces/jasmin2/cp4cds1/vol1/data',
        'var_index': -2,
        'freq_index': 5,
        'prefacets': 6,
        'facets': '_ _ _ _ _ activity product institute model experiment frequency realm mip_table ensemble_member variable version'.split(),
        'facet_picks': {'ensemble': 'r1i1p1'},
        'wildcards': ['institution', 'model']
    }
}
