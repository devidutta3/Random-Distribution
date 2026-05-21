import numpy as np
print("--------- Question 1 ----------")

"""Question 1-> Generate:
5 random values
mean = 100
std deviation = 10"""

def random_values():
    matrix=np.random.normal(
        loc=100,
        scale=10,
        size=5
    )
    print(f"The Generated Random Values Are:\n{matrix}")
    
random_values()

print("--------- Question 2 ----------")

"""Question 2 -> Generate:

20 student marks
mean = 70
std deviation = 5
Print:
highest marks
lowest marks"""
def  marks():
    std_marks=np.random.normal(
        loc=70,
        scale=5,
        size=20
    )
    print(f"The Generated Student Marks : \n {std_marks}")
    print(f"The Highest Mark Is:\n{std_marks.max()}")
    print(f"The Lowest Mark Is:\n{std_marks.min()}")
marks()


print("--------- Question 3 ----------")
"""Question 3 -> Generate:

50 AI accuracy scores
mean = 85
std deviation = 3
Then print:
average accuracy
minimum accuracy
maximum accuracy"""
def ai_accuracy():
    scores=np.random.normal(
        loc=85,
        scale=3,
        size=50
    )
    print(f"The Average Accuracy:\n{scores.mean()}")
    print(f"The Highest Accuracy Is:\n{scores.max()}")
    print(f"The Lowest Accuracy Is:\n{scores.min()}")
ai_accuracy()

