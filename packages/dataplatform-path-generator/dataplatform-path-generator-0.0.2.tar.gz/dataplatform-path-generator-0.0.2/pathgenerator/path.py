import os
from datetime import datetime



def generate_path(prefix, source, dt, type=None):

    partitions = dict(
        source=source
    )
    
    if type:
        partitions.update(type=type)
    
    execution_date = datetime.fromisoformat(dt)

    date_dict = dict(
        year=execution_date.year,
        month=execution_date.month,
        day=execution_date.day,
    )

    partitions.update(**date_dict)

    partition_path = '/'.join([f'{k}={v}' for k,v in partitions.items()])
    return os.path.join(prefix, partition_path)


