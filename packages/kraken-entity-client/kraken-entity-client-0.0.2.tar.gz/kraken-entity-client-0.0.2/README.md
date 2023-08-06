# Kraken Entity Client


## Overview
Class to interact with kraken db as entity

## How to use

```
from kraken_entity_client.kraken_entity_client import Kraken_entity_client as K
```

# Set api url 
(only have to do it once, will be reused as env variable for other instances)

```
k1 = K()
k1.set_api_url('https://krakenengine.tactik8.repl.co/api')
```

# Get record

```
k1 = K()
k1.record_type = 'schema:test'
k1.record_id = 'id_of_record'
k1.get()
record = k1.record
```

# Post record

```
k1 = K()
k1.record = record
k1.post()
```


