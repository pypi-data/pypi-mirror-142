.. currentmodule:: signalyzer

.. testsetup:: *

    from signalyzer import *

.. _moving event counter:

Moving Event Counter
====================

You can count the occurrences of a sample *value* over a number of signal
samples by calling the method :meth:`~Trace.moving_events`.

A new :class:`Trace` instance *labeled* with the performed transformation
``'events'`` is returned.

  >>> # counts the ones in the moving window samples
  >>> Trace('Signal', [0, 1, 0, 1, 0, 0, 0, 1, 1, 1]).moving_events(size=3)
  Trace(label='Signal:events', samples=[0, 1, 1, 2, 1, 1, 0, 1, 2, 3])

  >>> # counts the zeros in the moving window samples
  >>> Trace('Signal', [0, 1, 0, 1, 0, 0, 0, 1, 1, 1]).moving_events(3, value=0)
  Trace(label='Signal:events', samples=[1, 1, 2, 1, 2, 2, 3, 2, 1, 0])

.. note::

  The `moving event counter`_ uses ``None`` as the *preset* value to generate
  the windows for the first *number* of signal :class:`~Trace.samples`.

.. plotly::

  from signalyzer import Trace

  signal = Trace('Signal', [0, 1, 0, 1, 0, 0, 0, 1, 1, 1])
  trace = signal.moving_events(3)
  fig = go.Figure([signal.digital.plot(),
                   trace.digital.plot(mode='lines+markers')])
  fig.show()
