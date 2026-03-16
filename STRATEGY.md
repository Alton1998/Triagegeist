# Approach and Strategy to solving the problem

## What we want?
Need an AI Agent that can take in a natural language version of a patients condition and then structure it for a triage agent to provide a triage acquity

```mermaid
flowchart TD

A[Patient Natural Language Input<br>I have severe chest pain and shortness of breath]

B[NLP Intake Agent]

C1[Text Cleaning<br>Normalize text]
C2[Medical Entity Extraction<br>Symptoms Duration Severity]
C3[Clinical Concept Mapping<br>SNOMED ICD Mapping]
C4[Risk Feature Extraction<br>Age Severity Vitals]

D[Structured Patient Representation<br>JSON or Feature Vector]

E[Triage Acuity Prediction Agent<br>ML Model or Rules]

F[Triage Output<br>ESI or CTAS Level]

G[Explanation Layer<br>Highlight risk symptoms]

A --> B
B --> C1
C1 --> C2
C2 --> C3
C3 --> C4
C4 --> D
D --> E
E --> F
E --> G
```
## Creating the Triage agent 

To create the triage agent we experiment with the following approaches
:

1. Basic Uncertainty from Softmax
2. Predictive Entropy
3. Monte Carlo Dropout
4. Deep Ensembles
5. Bayesian Neural Networks
6. Calibration (ECE)
7. Conformal prediction

We will experiment with the following models
1. Ordinal Logistic Regress
2. SVM
3. Random Forest
4. Naive Bayes
5. KNN
6. Decision Trees
7. DNN

To create a model we will be using the following features:
1. PULSE
2. RESPR
3. BPSYS
4. BPDIAS
5. ARREMS
6. INJURY
7. IMMEDR
8. POPCT
9. PAINSCALE
10. RFV1 
11. RACEUN
12. ETHUN
13. SEEN72
 
