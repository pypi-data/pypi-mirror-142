from time import perf_counter
from tachymeter.util import format_time


class Tachyon:
    def __init__(self, f=None, label=None, running=False):
        self.startTime = None
        self.endTime = None
        self.f = f
        self.label = label or (f and f.__name__)
        self.running = False
        if running:
            self.start()

    def __enter__(self):
        self.running = True
        self.startTime = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.endTime = perf_counter()
        self.running = False

    def __call__(self, *args, **kwargs):
        if self.f is None:
            raise Exception(
                "A Tachyon should only be called when used as a decorator!")
        self.startTime = perf_counter()
        res = self.f(*args, **kwargs)
        self.endTime = perf_counter()
        self.print()
        return res

    def start(self):
        self.startTime = perf_counter()
        self.running = True

    def stop(self):
        self.endTime = perf_counter()
        self.running = False

    def pause(self):
        raise NotImplementedError()

    def split(self, split_label):
        raise NotImplementedError()

    def loop(self):
        raise NotImplementedError()

    @property
    def duration(self):
        if self.startTime is None:
            raise Exception("Timer has not been started!")
        if self.endTime is None:
            raise Exception("Timer has not finished!")
        return self.endTime - self.startTime

    def print(self):
        label = self.label or "Tachyon"
        print(f"{label}: done in {format_time(self.duration)}")
