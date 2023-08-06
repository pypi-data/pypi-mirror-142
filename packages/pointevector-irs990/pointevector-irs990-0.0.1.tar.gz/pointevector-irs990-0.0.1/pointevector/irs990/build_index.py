import io
import pandas as pd
from pathlib import Path
from ruamel.yaml import YAML
import zipfile

from pointevector.xml_parser import parse

def _gen_filings(directory: Path):
    for archive in directory.glob('*.zip'):
        with zipfile.ZipFile(archive) as z:
            for filename in z.filelist:
                yield (archive, filename, z.open(filename).read())

def _worker(item, indexer: Path):
    archive, file_info, content = item
    results = parse(
        config=YAML(typ='safe').load(indexer.read_text()),
        data=io.BytesIO(content),
    )
    results['archive'] = archive
    results['filename'] = file_info.filename
    return results

def build(directory: Path, indexer: Path) -> pd.DataFrame:
    df = pd.DataFrame.from_records(_worker(item, indexer) for item in _gen_filings(directory))
    df.to_csv(directory.joinpath('index.csv'), index=False)
