from enum import Enum
from pathlib import Path
from typing_extensions import TypedDict, NotRequired
from typing import Dict, Tuple
from ruamel.yaml import YAML

from pointevector.xml_parser import ParserConfig, validate as validate_parser_config

def _check_for_unknown_keys(cls, config: Dict):
    for key in config:
        if key not in cls.__annotations__:
            raise TypeError(f"Unknown key in {cls} configuration: {key}")

def _check_if_paths_exist(cls, config: Dict):
    for k, v in cls.__annotations__.items():
        if v == Path:
            config[k] = Path(config[k])
            if not config[k].exists():
                raise OSError(f"Could not find path to '{k}'")

def _validate_parser(path: str) -> ParserConfig:
    config_path = Path(path)
    if not config_path.exists():
        raise OSError('Could not find path to parser_configuration')

    return validate_parser_config(YAML(typ='safe').load(config_path.read_text()))

class CacheConfig(TypedDict):
    archive_directory: Path
    parser_configuration: ParserConfig
    cache_directory: Path

def _validate_cache(config: Dict) -> CacheConfig:
    _check_for_unknown_keys(CacheConfig, config)
    _check_if_paths_exist(CacheConfig, config)
    if not config['archive_directory'].is_dir():
        raise TypeError('archive_directory must be a directory')
    if not config['cache_directory'].is_dir():
        raise TypeError('cache_directory must be a directory')
    config['parser_configuration'] = _validate_parser(config['parser_configuration'])

class RankMetric(Enum):
    unknown=0
    total_expenses=1

class RankConfig(TypedDict):
    metrics: Tuple[RankMetric]
    parser_configuration: ParserConfig
    override: NotRequired[Path]

def _validate_rank(config: Dict) -> RankConfig:
    _check_for_unknown_keys(RankConfig, config)
    config['metrics'] = tuple(RankMetric[metric] for metric in config['metrics'])
    config['parser_configuration'] = _validate_parser(config['parser_configuration'])
    if 'override' in config:
        config['override'] = Path(config['override'])
        if not config['override'].exists():
            raise OSError('Could not find path to "override"')
        if not config['override'].is_file():
            raise TypeError('override must be a file')

class CompensationConfig(TypedDict):
    parser_configuration: ParserConfig

def _validate_compensation(config: Dict) -> CompensationConfig:
    _check_for_unknown_keys(CompensationConfig, config)
    config['parser_configuration'] = _validate_parser(config['parser_configuration'])

class Config(TypedDict):
    output: Path
    company_map: Path
    partition_dimension: NotRequired[str]
    earliest_year: int
    latest_year: NotRequired[int]
    cache: CacheConfig
    rank: NotRequired[RankConfig]
    compensation: NotRequired[CompensationConfig]
    
def validate(config: Dict) -> Config:
    _check_for_unknown_keys(Config, config)
    config['output'] = Path(config['output'])
    config['company_map'] = Path(config['company_map'])
    if 'partition_dimension' in config:
        config['partition_dimension'] = str(config['partition_dimension'])
    config['earliest_year'] = int(config['earliest_year'])
    if 'latest_year' in config:
        config['latest_year'] = int(config['latest_year'])
    _validate_cache(config['cache'])
    if 'rank' in config:
        _validate_rank(config['rank'])
    if 'compensation' in config:
        _validate_compensation(config['compensation'])
    return config
