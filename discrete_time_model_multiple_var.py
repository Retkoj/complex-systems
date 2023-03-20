"""Exercises 4.5 - 4.6"""
import pylab as pylab


class DiscreteSimulationMultiVar:
    def __init__(self, x: float = 1., y: float = 1., a: float = 0.5, b: float = 0.):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.time_series_x: list = [self.x]
        self.time_series_y: list = [self.y]

    def update(self):
        """Updates x by multiplying the current value of x by a and adding b (y = axt + b)"""
        next_x = 0.5 * self.x + self.y
        next_y = -0.5 * self.x + self.y
        self.x = next_x
        self.y = next_y

    def observe(self):
        """Observe the current value of x and append to the time_series"""
        self.time_series_x.append(self.x)
        self.time_series_y.append(self.y)

    def plot_time_series(self):
        pylab.plot(self.time_series_x, 'b-')
        pylab.plot(self.time_series_y, 'g--')
        pylab.show()

    def plot_phase_space(self):
        pylab.plot(self.time_series_x, self.time_series_y)
        pylab.show()


if __name__ == '__main__':
    sim = DiscreteSimulationMultiVar()
    for _ in range(30):
        sim.update()
        sim.observe()

    sim.plot_time_series()
    sim.plot_phase_space()
