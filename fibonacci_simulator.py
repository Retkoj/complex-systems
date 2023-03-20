"""Exercises 4.8"""
import pylab as pylab


class FibonacciSimulator:
    def __init__(self, x: float = 1., y: float = 0.):
        self.x = x
        self.y = y
        self.time_series_x: list = [self.x]
        self.time_series_y: list = [self.y]

    def update(self):
        """Updates x by multiplying the current value of x by a and adding b (y = axt + b)"""
        next_x = self.x + self.y
        next_y = self.x
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
    sim = FibonacciSimulator()
    for _ in range(30):
        sim.update()
        sim.observe()

    sim.plot_time_series()
    sim.plot_phase_space()
