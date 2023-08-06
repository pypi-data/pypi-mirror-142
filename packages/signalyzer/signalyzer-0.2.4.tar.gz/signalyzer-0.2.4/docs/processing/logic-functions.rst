.. currentmodule:: signalyzer

.. testsetup:: *

    from signalyzer import *

.. _logic functions:

Logic Functions
===============

.. _all samples true:

All Samples True
----------------

You can test with the built-in function :func:`all` if **all** of the signal
:attr:`~Trace.samples` of a :ref:`signal trace <signal trace>` are ``True``.

   >>> all(Trace('Signal', [1, 1.0, True, 0x1, 0o1, 0b1]))
   True

   >>> all(Trace('Signal', [0, 1.0, True, 0x1, 0o1, 0b1]))
   False

.. _any sample true:

Any Sample True
---------------

You can test with the built-in function :func:`any` if **any** of the signal
:attr:`~Trace.samples` of a :ref:`signal trace <signal trace>` is ``True``.

   >>> any(Trace('Signal', [0, 0.0, False, 0x0, 0o0, 0b0]))
   False

   >>> any(Trace('Signal', [1, 0.0, False, 0x0, 0o0, 0b0]))
   True

.. _logical and:

Logical AND
-----------

You can logical AND the signal :attr:`~Trace.samples` of multiple
:ref:`signal traces <signal trace>` by calling the function :func:`logical_and`.

A new :class:`Trace` instance *labeled* with the preformed logic function
``'And'`` is returned.

    >>> # logical AND between binary signals
    >>> signal = Trace('Signal', [-1.0, -0.5, 0.0, 0.5, 1.0])
    >>> logical_and(signal != 0, signal > -1, signal < 1)
    Trace(label='And', samples=[0, 1, 0, 1, 0])

.. note::

  The *operands* should have the same length, otherwise only a subset of the
  signal :attr:`~Trace.samples` is returned!

.. plotly::

  import math
  from signalyzer import Trace, logical_and

  signal = Trace('Signal', [-1.0, -0.5, 0.0, 0.5, 1.0])
  trace = logical_and(signal != 0, signal > -1, signal < 1)
  go.Figure([signal.plot(), trace.digital.plot(mode='lines+markers')])

.. _logical or:

Logical OR
----------

You can logical OR the signal :attr:`~Trace.samples` of multiple
:ref:`signal traces <signal trace>` by calling the function :func:`logical_or`.

A new :class:`Trace` instance *labeled* with the preformed logic function
``'Or'`` is returned.

    >>> # logical OR between binary signals
    >>> signal = Trace('Signal', [-1.0, -0.5, 0.0, 0.5, 1.0])
    >>> logical_or(signal == 0 , signal < -0.5, signal > 0.5)
    Trace(label='Or', samples=[1, 0, 1, 0, 1])

.. note::

  The *operands* should have the same length, otherwise only a subset of the
  signal :attr:`~Trace.samples` is returned!

.. plotly::

  import math
  from signalyzer import Trace, logical_or

  signal = Trace('Signal', [-1.0, -0.5, 0.0, 0.5, 1.0])
  trace = logical_or(signal == 0 , signal < -0.5, signal > 0.5)
  go.Figure([signal.plot(), trace.digital.plot(mode='lines+markers')])

.. _priority encoder:

Priority Encoder
----------------

.. important::

  The *operands* are converted to :class:`int` before the operation is performed.

You can prioritize the ``Truth=1`` values of the **binary** signal
:attr:`~Trace.samples` of multiple :ref:`signal traces <signal trace>` by
calling the function :func:`priority` with the iterable *operands* in the
descending order to prioritize. This means the *highest* priority have the
``Truth=1`` values of the first provided operand.

The lowest priority number is determined by the number of the provided
*operands*.

A new :class:`Trace` instance *labeled* with the preformed logic function
``'Priority'`` is returned containing the priority numbers for the prioritized
the ``Truth=1`` values of the given *operands*.

    >>> # prioritize binary signals from left to right in descending order
    >>> signal = Trace('Signal', [-1.0, -0.5, 0.0, 0.5, 1.0])
    >>> priority(signal == 0, signal <= 0, signal >= 1)
    Trace(label='Priority', samples=[1, 1, 0, 3, 2])

    >>> # prioritize binary signals starting from 1 as highest priority number
    >>> signal = Trace('Signal', [-1.0, -0.5, 0.0, 0.5, 1.0])
    >>> priority(signal == 0, signal <= 0, signal >= 1, highest=1)
    Trace(label='Priority', samples=[2, 2, 1, 4, 3])

.. note::

  The *operands* should have the same length, otherwise only a subset of the
  signal :attr:`~Trace.samples` is returned!

.. plotly::

  import math
  from signalyzer import Trace, priority

  signal = Trace('Signal', [-1.0, -0.5, 0.0, 0.5, 1.0])
  trace = priority(signal == 0, signal <= 0, signal >= 1)
  go.Figure([signal.plot(), trace.digital.plot(mode='lines+markers')])
