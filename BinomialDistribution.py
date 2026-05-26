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
        size=10
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

def Ai_generated_prediction():
    matrix=np.random.binomial(
        n=15,
        p=0.8,
        size=50
    )
    print(f"The Prediction Avg-Values Are:{matrix.mean()}")
    print(f"The Prediction Max-Values Are:{matrix.max()}")
    print(f"The Prediction Min-Values Are:{matrix.min()}")
Ai_generated_prediction()

"""Mini Challenge:
Website Login Success Simulator”
Requirements:
generate 100 login attempts
5 trials
success probability = 0.6
Then print:
average successful logins
highest successful logins
lowest successful logins """

def website_login_simulator():
    login_attempts=np.random.binomial(
        n=5,
        p=0.6,
        size=100
    )
    print(f"The Avg Attempts:{login_attempts.mean()}")
    print(f"The Max Attempts:{login_attempts.max()}")
    print(f"The Min Attempts:{login_attempts.min()}")
website_login_simulator()