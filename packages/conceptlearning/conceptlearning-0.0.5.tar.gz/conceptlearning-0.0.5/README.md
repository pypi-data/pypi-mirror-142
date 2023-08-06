# Concept Learning
This module contains functions to concept learning algorithms

# Installation 
Run the following command to install:
```python
    pip install conceptlearning
```
# Parameters
## data
    The training dataset consisting of featues and outcomes of type list

# Attributes
```
    # for Candidate Elimination Algorithm
    candidate_elimination() 

    # for Find S Algorithm
    initialize_hypothesis() 
    find_s() 
```
# Usage 
```python 
    from conceptlearning.CandidateEliminationAlgorithm import CandidateElimination
    ce = CandidateElimination(data)
    ce.candidate_elimination()

    from concetplearning.FindSAlgorithm import FindS
    fs = FindS(data)
    fs.initialize_hypothesis()
    fs.find_s()
```