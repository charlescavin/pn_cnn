# author  : Charles Cavin <charles@cavinAI.com>
# license : MIT

import glob


SEARCH_PATH = "/data8/pn/dcm/files/p*/p*/s*/*.dcm"

num_dcms = len(glob.glob(SEARCH_PATH, recursive=True))
print(f"The number of dcm files found: {num_dcms}")
