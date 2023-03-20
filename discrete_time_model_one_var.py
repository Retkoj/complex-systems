"""Exercises 4.5 - 4.6"""
import pylab as pylab


class DiscreteSimulation:
    def __init__(self, x: float = 1., a: float = 1.1, b: float = 0.):
        self.x = x
        self.a = a
        self.b = b
        self.time_series: list = [self.x]

    def update(self):
        """Updates x by multiplying the current value of x by a and adding b (y = axt + b)"""
        self.x = self.x * self.a + self.b

    def observe(self):
        """Observe the current value of x and append to the time_series"""
        self.time_series.append(self.x)

    def plot_time_series(self):
        pylab.plot(self.time_series)
        pylab.show()


if __name__ == '__main__':
    sim = DiscreteSimulation()
    for _ in range(30):
        sim.update()
        sim.observe()

    sim.plot_time_series()
