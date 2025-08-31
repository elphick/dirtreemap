"""
A demo of dirtreemap
"""
import os
from pathlib import Path

from directory_treemap import DirectoryTreemap

scan_dir: Path = Path(os.path.expanduser("~"))

if __name__ == '__main__':
    dtm: DirectoryTreemap = DirectoryTreemap(base_path=scan_dir,
                                             output_dir=Path("."),
                                             parallel=True)
    dtm.scan()
    dtm.generate_treemap(title='Demo Directory Treemap',
                         max_depth=4,
                         max_files=25)
    dtm.save_report()
    dtm.open_report()
