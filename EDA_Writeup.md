Here is a **cleaned and more formal version** of your EDA write-up. I preserved your findings but improved grammar, clarity, and logical flow so it reads more like a report.

---

## Exploratory Data Analysis (EDA)

An initial overview of the dataset shows that it contains **over 913 columns**, indicating a highly detailed record of emergency department (ED) visits. The **target variable representing triage acuity is `IMMEDR`**.

### Demographics

Analysis of patient demographics shows that the **largest proportion of ED visits comes from individuals aged 25–44 years**. In addition, **female patients account for a higher number of visits than male patients**.

From an ethnicity perspective, the majority of visits are from **non-Hispanic or Latino patients**, with **White patients representing the largest racial group** in the dataset.

### Reasons for Visit

The most frequent reasons for ED visits include:

* Abdominal pain, cramps, or spasms
* Chest pain
* Fever
* Shortness of breath
* Headache
* Vomiting
* Psychological concerns
* Back or leg pain
* Injury or trauma

Most visits were **non-injury related**. However, there is a noticeable gender pattern:

* **Non-injury related visits are more common among female patients**,
* **Injury-related visits are more common among male patients**.

### Diagnoses

The most frequently recorded diagnoses include:

* COVID-19
* Chest pain
* Abdominal pain
* Upper respiratory infections
* Joint pain
* Viral infections
* Fever
* Muscle cramps

### Triage Acuity Distribution

The majority of visits were assigned a **triage acuity level of 3**, indicating moderate urgency.

Average patient age tends to be **higher for patients assigned triage acuity levels 1, 2, and 3**, suggesting that more severe cases are often associated with older patients.

For each triage acuity level, the most common presenting complaints were:

| Triage Level | Code  | Most Common Complaint                       |
| ------------ | ----- | ------------------------------------------- |
| 1            | 14150 | Shortness of breath or respiratory distress |
| 2            | 10501 | Chest pain                                  |
| 3            | 15451 | Abdominal pain                              |
| 4            | 14400 | Cough                                       |
| 5            | 45550 | Follow-up and administrative reasons        |

### Mode of Arrival

The **majority of patients arrive at the ED as walk-ins (approximately 81%)**, while **about 18% arrive by ambulance**.

Patients arriving by ambulance are **more likely to receive higher triage acuity scores**, reflecting the more severe nature of their conditions. Additionally, **patients arriving by ambulance have a higher rate of hospital admission** compared to walk-in patients.

### Wait Times

Wait times vary significantly by both **mode of arrival** and **triage acuity level**:

* **Ambulance arrivals generally experience shorter wait times than walk-in patients.**
* **Patients with higher triage acuity levels (more severe conditions) have shorter wait times**, as expected in a triage-based prioritization system.

### Vital Signs and Clinical Indicators

Clinical indicators such as **temperature, blood pressure, and respiratory rate** appear to correlate with triage acuity. Patients with:

* **High body temperature**
* **Elevated blood pressure**
* **Abnormally low or high respiratory rates**

were more likely to be assigned **higher triage acuity levels**.

Furthermore, patients with **higher systolic blood pressure and lower diastolic pressure** were observed to have a **higher likelihood of hospital admission**.

---

