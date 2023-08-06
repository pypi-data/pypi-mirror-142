# Aviv AWS CostExplorer

Aims to provide a quick and comprehensive interface to AWS costexplorer api.
This is useful to extract cost and usage (aka CAU) data, save it and to make it available for reporting and analysis.

## Requirements

- python >= 3.8
- boto3
- Access to AWS ce:cost_and_usage

## Usage

```shell
pip install aviv-aws-costexplorer

# Install additional libraries required to save/read data on AWS S3: pandas, awswrangler
pip install aviv-aws-costexplorer[datastore]
```

Sample code

```python
from aviv_aws_costexplorer import costreporter

cr = costreporter.CostReporter()
costs = cr.get_cost_and_usage()
# Will print you last 3 months costs
print(costs)

from aviv_aws_costexplorer import datastore
ds = datastore.DataStore(database='test', bucket='my-s3-bucket')
ds.to_parquet(data=costs, path='monthly/last3', database='monthly')

# Show it nicely
import pandas as pd
df = pd.DataFrame(costs)
df.head()


# Store on S3 and make it available through Athena (uses awswrangler)

```

## Development

```bash
pipenv install -d
```

## Test, Build, Release

We typically follow the [standard python packaging and distribution](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives) process to release this package.

```bash
# Run tests
pipenv run pytest -v tests/

# Build python package
python3 -m pip install --upgrade build
python3 -m build

# Release on testpypi
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

Note: the Pypi release is also done during the CICD process.

## Contribute

Yes please! Send us your PR's
