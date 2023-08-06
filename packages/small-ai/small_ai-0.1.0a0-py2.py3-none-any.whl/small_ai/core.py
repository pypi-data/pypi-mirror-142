# Base/Abstract definitions
import abc
from dataclasses import dataclass
from typing import Any
from typing import Optional
from typing import Tuple
from typing import Callable

import numpy
import scipy.special

from .exceptions import UrecognizedActivationFunction
from .helpers import calculate_number_of_hidden_nodes


@dataclass
class Neuron:
    bias: float = 0.0
    weight: float = 0.0
    value: float = 0.0


class BaseNeuralNetwork(abc.ABC):
    @abc.abstractmethod
    def train(self, *args, **kwargs) -> None:
        """Abstract definition for training method"""
        pass

    @abc.abstractmethod
    def predict(self) -> int:
        """Abstract definition for network querying method.

        Returns:
            int: class representation as integer
        """
        pass

    @abc.abstractmethod
    def get_accuracy(self):
        """Abstract definition for accuracy reporting"""
        pass

    @abc.abstractmethod
    def _assemble_network(self) -> None:
        """Abstract definition for network assembling helper"""
        pass

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.__dict__})"


class FeedForwardNeuralNetwork(BaseNeuralNetwork):

    AVAILABLE_ACTIVATION_FUNC = ("sigmoid", "hiper")

    def __init__(
        self,
        input_nodes: int,
        output_nodes: int,
        learning_rate: float = 0.3,
        weights=Optional[numpy.ndarray],
        activation: str = "sigmoid",
    ) -> None:
        self._input_nodes = input_nodes
        self._output_nodes = output_nodes
        self._hidden_nodes = calculate_number_of_hidden_nodes(
            self._input_nodes, self._output_nodes
        )
        self._learning_rate = learning_rate
        # generate weights for input to hidden layer transitions
        self._weights_ih = self._generate_random_weights(
            self._input_nodes, self._hidden_nodes
        )
        # generate weights for hidden to input layer transitions
        self._weights_ho = self._generate_random_weights(
            self._hidden_nodes, self._output_nodes
        )
        if activation not in self.AVAILABLE_ACTIVATION_FUNC:
            raise UrecognizedActivationFunction(
                f"The activation function '{activation}' is not recognized. Options are [sigmoid,hiper]"
            )
        self._activation_func = self.__set_activation_func(activation)

        # numpy.where(x < 0, numpy.exp(x)/(1 + numpy.exp(x)), 1/(1 + numpy.exp(-x)))

    def __set_activation_func(self, activation_func: str) -> Callable[[float], float]:
        if activation_func == "sigmoid":
            # TODO: replace this with numpy call, removing scipy dependency
            return lambda x: scipy.special.expit(x)
        return lambda x: numpy.tanh(x)

    def predict(self, input_list) -> int:
        inputs = numpy.array(input_list, ndmin=2).T
        _, final_outputs = self.__feed_forward(inputs)

        return final_outputs

    def __feed_forward(self, inputs) -> Tuple[numpy.ndarray, numpy.ndarray]:
        hidden_inputs = numpy.dot(self._weights_ih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self._activation_func(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self._weights_ho, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self._activation_func(final_inputs)
        return hidden_outputs, final_outputs

    def train(
        self, input_list, labels, epochs: int = 100, error_tolerance: float = 10**-5
    ) -> None:
        epoch_counter = 0
        inputs = numpy.array(input_list, ndmin=2).T
        targets = numpy.array(labels, ndmin=2).T

        while epoch_counter < epochs:
            # calculate the signals emerging from hidden layer
            hidden_outputs, final_outputs = self.__feed_forward(inputs)
            # calculate errors
            output_errors = targets - final_outputs
            hidden_errors = numpy.dot(self._weights_ho.T, output_errors)
            # weight update
            self._weights_ho += self._learning_rate * numpy.dot(
                (output_errors * final_outputs * (1.0 - final_outputs)),
                numpy.transpose(hidden_outputs),
            )
            self._weights_ih += self._learning_rate * numpy.dot(
                (hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                numpy.transpose(inputs),
            )
            epoch_counter += 1

    @staticmethod
    def _generate_random_weights(
        num_inputs: int, num_outputs: int
    ) -> numpy.ndarray[Any, numpy.dtype[numpy.float64]]:
        """Generates random weight matrix using normal distribution (-1.0, 1.0)

        Args:
            num_inputs (int): number of outputs for the current layer
            num_outputs (int): number of inputs for the next layer

        Returns:
            numpy.ndarray[float]: _description_
        """
        return numpy.random.normal(
            0.0, pow(num_inputs, -1.0), (num_outputs, num_inputs)
        )

    def _assemble_network(self):
        pass

    def get_accuracy(self):
        pass
