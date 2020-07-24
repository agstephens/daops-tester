print('[WARN] Patched loader for clisops...libgeos needs right path...')

import sys
import os


cached_prefix = sys.prefix
sys.prefix = os.environ.get('CONDA_PREFIX')

import clisops.core as cops

sys.prefix = cached_prefix

