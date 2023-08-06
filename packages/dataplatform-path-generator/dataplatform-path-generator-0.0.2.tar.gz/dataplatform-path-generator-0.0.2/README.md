# Path generator for dataplatform files in cloud storage

This library generates the path to write files to in cloud storage, partitioned into the prefix, source, optionally type, and then finally the day. Arguments:

* *prefix*: "the prefix of the cloud storage location of your files, usually the top level bucket
* *source*: the type of files to output.
* *date*: the execution date in isoformat
* *type* (Optional): a subset of source, if the source has multiples types

Example usage:

```  
from pathgenerator import path

output_path = path.generate_path('gs://dataplatform-raw', 'salesforce', "2022-03-11T12:12:12+00:00", "account")
```

Output

```  
gs://dataplatform-raw/source=salesforce/type=account/year=2022/month=3/day=11
```