import argparse
import logging
import importlib
from pathlib import Path
from ruamel.yaml import YAML

from pointevector.irs990 import validate, build_cache, build_index

def main():
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-f', type=Path, default='.config.yaml')
    args, _ = parser.parse_known_args()

    # Validate configuration
    config = validate(YAML(typ='safe').load(Path(args.config).read_text()))

    # Ensure cache index exists
    if not config['cache']['cache_directory'].joinpath('index.csv').exists():
        if not config['cache']['archive_directory'].joinpath('index.csv').exists():
            build_index(config, cache=False)
            logging.info('Could not find archive index, so building it...')
        logging.info('Could not find cache index, so building it...')
        build_cache(config)
        build_index(config)

    # Run plugins
    for plugin in config['plugins']:
        path = plugin['script'].relative_to('.')
        mod = '.'.join([*path.parent.parts, path.stem])
        p = importlib.import_module(mod)
        p.main(config, plugin)

# Execute
main()
