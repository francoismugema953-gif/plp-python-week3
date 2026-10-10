# Grade and Statistics Reporter Assignment

* `grade_reporter.py`: Processes a list of student scores, assigns letter grades, counts passes and failures, and calculates the overall rounded class average.
* `stats_analyzer.py`: *(Placeholder)* Analyzes extended dataset metrics including minimum, maximum, and median values.

The hardest bug to find in Part B was a silent logical error where an accumulation variable was initialized inside the loop instead of outside, causing it to reset on every iteration. We knew something was wrong because the program ran successfully without throwing any syntax or runtime exception, but the final summary output displayed wildly incorrect, abnormally low values instead of the true total.
