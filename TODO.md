# TODO List

* ### __Version 0.1 (BasicWorkingCondition)__

    *   Implement loading of data from csv: __[Done.]__

    *   Implement basic signals (price, sma and sharpe): __[Done.]__

    *   Implement basic benchmarks (correlation, beta and alpha): __[Done.]__

    *   Implement tests for all subroutines: __[Done.]__

*   ### __Version 0.2 (CurrentlyTentativelyTitled)__

    *   Extend loading of data to json: __[Done.]__

    *   Extend basic signals to include ema and largest drawdown: __[Done.]__

    *   Implement a base technical indicators: __[Done.]__

        1.  Number of dips in a period of time (by percent given): __[Done.]__

    *   Implement downloading of information (via tiingo initially)

*   ### __Version 0.3

    *   Rewrite all tests to be like `tests/test_data_from_csv.py` instead of the lazy tests we have now

    *   Extend `security_data.download()` to include a free-tier module as well

__Further down the line__

*   A Value at Risk modeler for a given equity (or portfolio of equities)
