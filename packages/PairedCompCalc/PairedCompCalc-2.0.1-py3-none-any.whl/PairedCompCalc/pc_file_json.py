"""This module defines class PairedCompFile to
read / write paired-comparison data in serialized json file format.
One file may include several PairedCompItem instances,
for one or more subjects and one or more test-conditions.

*** Version History:
* Version 2.0
2021-09-15, moved internal items property to local variable in  __iter__, save methods
2021-09-22, changed signature for method save

* Version 1.0
2018-09-25, first functional version
2018-12-08, PairedCompFile.save() method, creating safe file name to avoid over-writing
2019-03-30, PairedCompFile.save() with allow_over_write argument
"""

from pathlib import Path
import json
import logging

from . import __version__
from . import pc_base


logger = logging.getLogger(__name__)


class FileFormatError(pc_base.FileReadError):
    """Any type of input file format error"""


# ---------------------------------------------------------
class PairedCompFile(pc_base.PairedCompFile):
    """File storing paired-comparison experimental results
    from one or more listeners, in one or more test conditions,
    represented as a sequence of PairedCompItem instances.
    This class is used mainly to read / write a json file,
    as a flat sequence of PairedCompItem instances.
    """
    # def __init__(self, items=None, file_path, pcf, **kwargs):  # using super-class

    def __iter__(self):
        """Iterate over all items loaded from a file
        """
        path_test_cond = self.path_test_cond()
        items = self.load()
        # = list of all items in the file
        # for r in self.items:
        for r in items:
            # merge path test-cond with test-cond loaded from file:
            test_cond = path_test_cond.copy()
            test_cond.update(r.test_cond)
            r.test_cond = test_cond
            yield r

    def load(self):
        """Load paired-comparison data from given file.
        :return: items = generator of PairedCompItem instances loaded from file
        """
        try:
            with self.file_path.open() as f:
                file_dict = json.load(f)
            if 'PairedCompRecord' in file_dict.keys():
                # version 0.8 format
                file_dict = _update_version_format(file_dict['PairedCompRecord'])
            elif 'PairedCompFile' in file_dict.keys():
                file_dict = _update_version_format(file_dict['PairedCompFile'])
            # return [pc_base.PairedCompItem(**r) for r in file_dict['items']]
            return (pc_base.PairedCompItem(**r) for r in file_dict['items'])
        except (KeyError, json.decoder.JSONDecodeError):
            raise pc_base.FileReadError(f'File {self.file_path} does not contain PairedComp data')

    def save(self, items, allow_over_write=False):
        """Save self.items to file
        :param items: iterable of PairedCompItem instances
        :param allow_over_write: boolean switch, =True allows old file to be over-written
        :return: None

        2021-09-15, changed signature, input items here, not in __init__
        2021-09-22, changed signature, no file specificatian here, only in __init__
        """
        # dir = Path(dir)
        # dir.mkdir(parents=True, exist_ok=True)
        # # make sure it exists, create new hierarchy if needed
        # if file_name is None:
        #     if self.file_path is not None:
        #         file_name = self.file_path.name
        #     else:
        #         file_name = self.items[0].subject  # ****** NO **************
        # if allow_over_write:
        #     # no file-name check, over-write if file already exists
        #     file_path = (dir / file_name).with_suffix('.json')
        # else:
        #     file_path = pc_base.safe_file_path((dir / file_name).with_suffix('.json'))
        if not allow_over_write:
            self.file_path = pc_base.safe_file_path(self.file_path)
        # = non-existing file, to avoid over-writing
        self_dict = {'items': [i.__dict__ for i in items],
                     '__version__': __version__}
        with open(self.file_path, 'wt') as f:
            json.dump({'PairedCompFile': self_dict}, f, ensure_ascii=False, indent=1)
        # self.file_path = file_path


# ------------------------------------------------ internal module help functions

def _update_version_format(p_dict):
    """Update contents from an input json file to fit current file version
    :param p_dict: an old PairedCompRecord dict saved with an old package version
    :return: new_dict = dict with current file format
    """
    if p_dict['__version__'] < '0.9.0':
        try:
            subject = p_dict['subject']
            attr = p_dict['attribute']
            items = [{'subject': subject,
                      'attribute': attr,
                      'pair': r[0],
                      'response': r[1],
                      'test_cond': r[2]}
                     for r in p_dict['result']]
        except KeyError:
            raise FileFormatError('Error converting old "PairedCompRecord" file format')
        return {'items': items}
    # elif p_dict.__version__ < '1.0.0':  *** future
    #
    else:
        return p_dict  # no change for files in newer format
