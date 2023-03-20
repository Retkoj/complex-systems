"""Exercise 4.3 - 4.4"""
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum


class ColorState(Enum):
    RED = 'red'
    BLUE = 'blue'


@dataclass
class Component:
    state: ColorState

    @abstractmethod
    def state_transition_function(self, other_component):
        """Change state based on state of other component"""


class ComponentA(Component):
    def state_transition_function(self, other_state: ColorState):
        """Tries to be the same state as other_state"""
        if other_state != self.state:
            self.state = other_state


class ComponentB(Component):
    def state_transition_function(self, other_state: ColorState):
        """Tries to be the opposite state as other_state"""
        if other_state == self.state:
            self.state = ColorState.BLUE if self.state == ColorState.RED else ColorState.RED


def get_time_series(initial_color_a: ColorState = ColorState.BLUE, initial_color_b: ColorState = ColorState.BLUE,
                    n_times: int = 10) -> list[tuple]:
    """
    Produces a time series of (State A, State B) starting with an initial color condition
    per Component.

    :param initial_color_a:
    :param initial_color_b:
    :param n_times: int, length of time series
    :return: list[tuple], time series of (state A, state B)
    """
    component_a = ComponentA(initial_color_a)
    component_b = ComponentB(initial_color_b)

    time_series = []
    for _ in range(n_times):
        state_a, state_b = component_a.state, component_b.state
        time_series.append((state_a, state_b))
        component_a.state_transition_function(state_b)
        component_b.state_transition_function(state_a)
    return time_series


if __name__ == '__main__':
    time_series = get_time_series()
    for i, pair in enumerate(time_series):
        print(f"{i + 1}: State A: {pair[0].value} - State B: {pair[1].value}")
