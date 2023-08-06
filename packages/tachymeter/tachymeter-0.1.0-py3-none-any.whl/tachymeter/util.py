def format_time(dt):
    """
    Formats a time with the closest relevant unit.
    Replicates functionality of inbuilt timeit formatting.

    :param dt: (float) time in seconds to be formatted
    """
    units = {"nsec": 1e-9, "usec": 1e-6, "msec": 1e-3, "sec": 1.0}
    precision = 3
    scales = [(scale, unit) for unit, scale in units.items()]
    scales.sort(reverse=True)
    for scale, unit in scales:
        if dt >= scale:
            break
    return "%.*g %s" % (precision, dt / scale, unit)
