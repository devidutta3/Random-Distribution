import numpy as np

"""Question-1: 
generate 5 random values
range: 1 to 100
using Uniform Distribution."""

def random_values():
    matrix=np.random.uniform(
        low=1,
        high=100,
        size=5
    )
    formatted_matrix = [f"{x:.2f}" for x in matrix]
    print(f"All The Generated Numbers:\n{formatted_matrix}")
random_values()
"""Question-2 
generate 20 student marks
range: 40 to 90 
highest marks
lowest marks""" 
def std_marks():
    marks=np.random.uniform(
        low=40,
        high=90,
        size=20
    )
    refined_marks=[f"{x:.2f}" for x in marks]
    print(f"Here Is The Generated Marks:\n{refined_marks}")
std_marks()

"""Write a Python program to:
generate 50 AI confidence scores
range: 0 to 1
average confidence
maximum confidence
minimum confidence
"""

def Ai_Confidence():
    scores=np.random.uniform(
        low=0,
        high=1,
        size=50
    )
    refined_scroes=[f"{x:.2f}" for x in  scores]
    print(f"Ai_confidence Scores:\n{refined_scroes}")
Ai_Confidence()

