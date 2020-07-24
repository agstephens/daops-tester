import os
import re
import random

from .settings import projects


def select_item(dr, proj):
    """[summary]

    Ctrl+Shift+2 - to create docstring

    Args:
        dr ([type]): [description]

    Returns:
        [type]: [description]
    """    
    items = os.listdir(dr)

    # Remove files and '.' files
    items = [_ for _ in items if not _.startswith('.') and
               _ not in ('latest', 'files') and
               not os.path.isfile(os.path.join(dr, _))]

    facets = projects[proj]['facets']
    current_facet = facets[len(dr.strip('/').split('/'))]

    facet_picks = projects[proj]['facet_picks']
    facet_value = facet_picks.get(current_facet, None)

    if facet_value in items:
        return facet_value

    return random.choice(items)


def get_path(dr, proj, stop_on=r'vd{8}'):
    """[summary]

    Args:
        dr ([type], optional): [description].
        stop_on (str, optional): [description]. Defaults to 'v\d{8}'.

    Returns:
        [type]: [description]
    """
    item = select_item(dr, proj)
    path = os.path.join(dr, item)

    print(f'Resolving path: {path}')

    if re.match(stop_on, item):
        return path

    return get_path(path)


def patch_path(path, proj):
    """Takes a completed path (drs ID) for a dataset and generalises it to 
    include "*" values for facets based on project config.

    Args:
        path ([type]): [description]
        proj ([type]): [description]
    """    
    prj = projects[proj]
    path_parts = path.strip('/').split('/')
    facets = prj['facets']

    if len(path_parts) != len(facets):
        raise Exception(f'Facets and path are different lengths: {facets}, {path}')

    wildcards = prj['wildcards']
    sample_id = ''

    for i, facet in enumerate(facets):
        if i < prj['prefacets']: continue

        value = wildcards.get(facet, path_parts[i])
        sample_id += f'{value}.'

    sample_id = sample_id.rstrip('.')
    return sample_id


def get_random_sample(proj):

    eg_path = get_path(projects[proj]['start_dir'], proj)
    sample_id = patch_path(eg_path, proj)
    return sample_id
    