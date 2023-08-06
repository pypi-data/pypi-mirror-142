import logging
import pandas as pd
import zipfile

from pointevector.irs990._validate_config import Config

def build(config: Config):
    archive_path = config['cache']['archive_directory']
    dim = config['partition_dimension']
    archive_index = pd.read_csv(archive_path.joinpath('index.csv'), dtype=str).set_index('ein')
    companies = pd.read_csv(config['company_map'], dtype=str).set_index('ein')
    reduced_index = pd.merge(companies, archive_index, on='ein')

    archives = {archive: zipfile.ZipFile(archive_path.joinpath(archive)) for archive in reduced_index.archive.unique()}
    partitions = companies[dim].str.split(';', expand=True).unstack().dropna().droplevel(-2)
    for partition in partitions.unique():
        filepath = config['cache']['cache_directory'].joinpath(f"{partition}.zip")
        partitioned_index = reduced_index[reduced_index[dim].str.split(';').apply(lambda i: partition in i)]
        with zipfile.ZipFile(filepath, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for _, filing in partitioned_index.iterrows():
                try:
                    data = archives[filing.archive].open(filing.filename).read()
                    z.writestr(zinfo_or_arcname=filing.filename, data=data)
                except zipfile.BadZipFile as e:
                    logging.warning(f"{e}: {filing.organization_name} {filing.style} {filing.archive} {filing.filename}")
