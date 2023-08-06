# Input/Output utilities
import csv
import random
from dataclasses import dataclass
from typing import List


@dataclass
class Dataset:
    samples: List[List[float]]
    labels: List[int]

    @property
    def num_attributes(self) -> int:
        return len(self.samples[0])

    @property
    def num_classes(self) -> int:
        return len(set(self.labels))

    def __str__(self) -> str:
        return f"{type(self).__name__}(classes={self.num_classes}, num_attr={self.num_attributes})"


def _parse_data(sample_data: List[List[str]], shuffle_data: bool = True) -> Dataset:
    samples = []
    labels = []
    if shuffle_data:
        random.shuffle(sample_data)
    for row in sample_data:
        samples.append([float(i) for i in row[:-1]])
        labels.append(int(row[-1]))
    return Dataset(samples, labels)


# File reading
def read_csv(file_path: str) -> Dataset:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_lines = list(csv_reader)
    return _parse_data(csv_lines[1:])


# file writing
