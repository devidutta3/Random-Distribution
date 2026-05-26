import numpy as np
"""Question 1-> generate 5 binomial values
number of trials = 10
probability = 0.5
Then print all generated values."""
def generated_value():
    matrix=np.random.binomial(
        n=10,
        p=0.5,
        size=5
    )
    print(f"The Generated Values Are :\n{matrix}")
generated_value()

"""Question ->2 
simulate exam pass results
20 trials
probability of passing = 0.7
generate results for 10 students
Then print:
maximum passes
minimum passes"""
def exam_simulator():
    results=np.random.binomial(
        n=20,
        p=0.7,
        size=20
    )
    print(f"simulate exam pass results 20 trials are :\n{results} ")
    print(f"simulate exam max-pass results 20 trials are :\n{results.max()} ")
    print(f"simulate exam min-pass results 20 trials are :\n{results.min()} ")
exam_simulator()
"""Question -> 3
 generate 50 AI prediction success values
number of trials = 15
success probability = 0.8
Then print:
average success
highest success
lowest success"""

