![Repo-Header](https://i.pinimg.com/originals/09/53/81/0953813004d675ca814403fbb649f8b7.png)
## About the Project
### Goals
The major goal of this project is to create a machine learning model that can predict a patient having diabetes or not. The model will base this on other diagnostic measures in the data, such as BMI and age. The data sample is for female patients at least 21 years of age or older with Pima Indian heritage.
### Background
### Deliverables
- Jupyter notebook with full analysis process
- Presentation on key insights and model performance
### Acknowledgments
Data from UCI Machine Learning [here](https://www.kaggle.com/uciml/pima-indians-diabetes-database).  
  - Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.
## Data Dictionary
### Included in Original Data
| Feature Name               | Description                                                              |
|----------------------------|--------------------------------------------------------------------------|
| Outcome                    | Binary class for diabetic patient or non-diabetic patient                |
| Pregnancies                | Number of times pregnant                                                 |
| Glucose                    | Plasma glucose concentration a 2 hours in an oral glucose tolerance test |
| Blood Pressure             | Diastolic blood pressure (mm Hg)                                         |
| Skin Thickness             | Triceps skin fold thickness (mm)                                         |
| Insulin                    | 2-Hour serum insulin (mu U/ml)                                           |
| BMI                        | Body mass index: weight in kg/(height in m)^2                            |
| Diabetes Pedigree Function | Measure of genetic influence                                             |
| Age                        | Age of patient in years                                                  |

### Features Created
Using pandas qcut to create equal bins or Kmeans to create clusters on one or two features. Clusters were split into dummy variables.

| Feature Name                | Description                                                                                 |
|-----------------------------|---------------------------------------------------------------------------------------------|
| age_bins                    | 4 bins based on Age: (21, 24] < (24, 29] < (29, 41] < (41, 81] labeled 1,2,3,4 respectively |
| bmi_bins                    | 3 bins based on BMI: (19, 29] < (29, 35] < (35, 67] labeled 1,2,3 respectively              |
| bp_bins                     | 3 bins based on blood pressure: (24, 68] < (68, 76] < (76, 122] labeled 1,2,3 respectively  |
| high_bmi_bp                 | Boolean if patient has BMI in levels 2 or 3 and Blood Pressure in level 3                   |
| age_bmi_cluster             | Cluster created on scaled train features Age and BMI                                        |
| pregnancy_cluster           | Cluster created on scaled train feature Pregnancies                                         |
| insulin_and_glucose_cluster | Cluster created on scaled train features Insulin and Glucose                                |

## Initial Thoughts & Hypotheses
### Thoughts
### Hypotheses
## Project Steps
### Acquire
### Prepare
### Explore
### Model
#### Final Model
| Model    | RandomForest | (max_depth=5, random_state=123)             | ['Glucose', 'Age', 'BMI', 'insulin_glucose_cluster', 'DiabetesPedigreeFunction'] |
|----------|--------------|---------------------------------------------|----------------------------------------------------------------------------------|
| DF       | Accuracy     | Recall on True Positive (actually diabetic) | Precision on True Positive (actually diabetic)                                   |
| Train    | 86%          | 69%                                         | 86%                                                                              |
| Validate | 79%          | 62%                                         | 76%                                                                              |
| Test     | 75%          | 57%                                         | 57%                                                                              |

### Conclusions
## How to Reproduce
### Steps
### Tools & Requirements
## Creator
[Bethany Thompson](https://github.com/ThompsonBethany01)
