from typing import List

import numpy as np


def extract_classes(element_list: List[int]) -> set:
    return set(element_list)


def calculate_input(input_values: List[float], weights: List[float]) -> float:
    return sum(x * w for x, w in zip(input_values, weights))


def calculate_number_of_hidden_nodes(num_inputs: int, num_outputs: int) -> int:
    return round(np.array([num_inputs, num_outputs]).prod() ** 0.5)
