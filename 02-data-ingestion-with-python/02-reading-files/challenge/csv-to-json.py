#! /usr/local/bin/python3

"""Convert from CSV format to JSON .jl format"""
import csv
import bz2
import json
from datetime import datetime
from collections import namedtuple

# named tuple for type conversion
Column = namedtuple('Column', 'src dest convert')


def parse_time(time):
    return datetime.strptime(time, format="%Y-%m-%d %H:%M:%S")


cols = [
    Column("VendorID", "vendor", int),
    Column("tpep_pickup_datetime", "pickup", str),
    Column("tpep_dropoff_datetime", "dropoff", str),
    Column("trip_distance", "distance", float),
    Column("tip_amount", "tip", float),
    Column("total_amount", "total", float)
]


def iso_convert(obj):
    if not isinstance(obj, datetime):
        return obj
    return obj.isoformat()


def iter_records(file_name):
    with bz2.open(file_name, 'rt') as fp:
        reader = csv.DictReader(fp)
        for csv_record in reader:
            jl_record = {}
            for col in cols:
                raw = csv_record[col.src]
                jl_record[col.dest] = col.convert(raw)
            yield jl_record


def main():
    filename = "taxi.csv.bz2"
    with open("taxi.jl", "w+") as jl:
        for record in iter_records(filename):
            dat = json.dumps(record, default=iso_convert)
            jl.write(f"{dat}\n")


if __name__ == '__main__':
    main()
