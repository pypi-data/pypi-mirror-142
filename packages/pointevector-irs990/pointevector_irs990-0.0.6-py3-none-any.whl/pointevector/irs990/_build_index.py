import io
import pandas as pd
from pathlib import Path
import zipfile

from pointevector.irs990._validate_config import Config
from pointevector.xml_parser import ParserConfig, parse

def _gen_filings(directory: Path):
    for archive in directory.glob('*.zip'):
        with zipfile.ZipFile(archive) as z:
            for filename in z.filelist:
                yield (archive.name, filename, z.open(filename).read())

def _worker(item, indexer: ParserConfig):
    archive, file_info, content = item
    results = parse(config=indexer, data=io.BytesIO(content))
    results['archive'] = archive
    results['filename'] = file_info.filename
    return results

def build(config: Config, cache: bool=True) -> pd.DataFrame:
    directory = config['cache']['cache_directory'] if cache else config['cache']['archive_directory']
    df = pd.DataFrame.from_records(_worker(item, config['cache']['parser_configuration']) for item in _gen_filings(directory))
    df.to_csv(directory.joinpath('index.csv'), index=False)
