# PipeRider Python SDK

PipeRider SDK is a python library to manipulate your project resources on the PipeRider.

## Configuration

Before using the sdk, you need a `api key` to authenticate with the api server. Visit the user settings page and
generate your api key:

* https://app.piperider.io/settings

When the api key available, set it to the environment:

```bash
export PIPERIDER_API_KEY=<user_api_key>
```

Or setup it with help function:

```python
from PipeRider.api.http_client import set_api_key

set_api_key('api-key')
```

## Install

```bash
pip install piperider-python-sdk
```

## Usage

First, start a new project `my-pipe-rider`

```python
import PipeRider

project = PipeRider.project('my-pipe-rider')
```

Then, create a run to keep ML project settings:

```python
with project.runs.create(name='Awesome Run') as run:
    run.config = {'learning_rate': 0.02,
                  'architecture': 'CNN',
                  'dataset': 'TKNV-users', }

    run.params = {
        'batch_size': 64,
        'epoch': 100,
        'learning_rate': 0.005
    }
```

Don't forget to link dataset, it is useful when reviewing how a model built:

```python
run.add_dataset('golden-dataset')
```

The `run` could be used logging metrics and mark the final result:

```python

offset = random.random() / 5
for ii in range(2, 10):
    acc = 1 - 2 ** -ii - random.random() / ii - offset
    loss = 2 ** -ii + random.random() / ii + offset
    # 2️⃣ Log metrics from your script to PipeRider
    run.log({"acc": acc, "loss": loss})

# the final metrics
run.metrics = {"acc": 0.987, "loss": 0.123}
```

You also could add comment to the **timeline**:

```python
project.comment('it is a good idea.')
```

Finally, mark the run as winner if it was so outstanding:

```python
run.win()
```