![Repo-Header](https://i.pinimg.com/originals/09/53/81/0953813004d675ca814403fbb649f8b7.png)
## About the Project
### Goals
The major goal of this project is to create a machine learning model that can predict a patient having diabetes or not. The model will base this on other diagnostic measures in the data, such as BMI and age. The data sample is for female patients at least 21 years of age or older with Pima Native American heritage.
### Background
According to the U.S. Department of Health and Human Services [here](https://aspe.hhs.gov/report/diabetes-national-plan-action/importance-early-diabetes-detection),
> "Early detection and treatment of diabetes is an important step toward keeping people with diabetes healthy. It can help to reduce the risk of serious 
> complications such as premature heart disease and stroke, blindness, limb amputations, and kidney failure... Many people with type 2 diabetes have no signs or 
> symptoms, but do have risk factors... Early diagnosis of diabetes and pre-diabetes is important so that patients can begin to manage the disease early and 
> potentially prevent or delay the serious disease complications that can decrease quality of life."

### Deliverables
- Jupyter notebook with full analysis process
  - Title Data_Analysis within this repo; can also click [here](https://github.com/ThompsonBethany01/Predicting-Diabetes-Onset/blob/main/Data_Analysis.ipynb)
- Presentation on key insights and model performance
  - View Canva presentation [here](https://www.canva.com/design/DAEPT1-nivk/z_fSs84zumIo8slllAszCA/view?utm_content=DAEPT1-nivk&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu)
- Tableau Storybooks
  - Visualizing Clusters [here](https://public.tableau.com/profile/thompson.bethany.01#!/vizhome/ClustersWorkbook/Clusters?publish=yes)
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

##### Domain Knowledge
<details>
  <summary> Click to Expand </summary>
  
**Glucose**  
An oral glucose tolerance test measures blood glucose after not eating for at least 8 hours and 2 hours after drinking a glucose-containing beverage. This test is used to diagnose diabetes (200 mg/dl and above) or pre-diabetes (between 140 mg/dl and 199 mg/dl). [read more here](https://aspe.hhs.gov/report/diabetes-national-plan-action/importance-early-diabetes-detection)  

**Blood Pressure**  
High blood pressure means that blood is pumping through the heart and blood vessels with too much force. Over time, consistently high blood pressure tires the heart muscle and can enlarge it. Diabetes damages arteries and makes them targets for hardening, called atherosclerosis. That can cause high blood pressure. It is believed that factors such as MBI and diet contribute to both conditions. [read more here](https://www.healthline.com/health/type-2-diabetes/hypertension)

**Skin Thickness**  
Triceps (back side middle upperarm) - A skinfold caliper is used to assess the skinfold thickness, so that a prediction of the total amount of body fat can be made. This method is based on the hypothesis that the body fat is equally distributed over the body and that the thickness of the skinfold is a measure for subcutaneous fat. [read more here](https://nutritionalassessment.mumc.nl/en/skinfold-measurements)

**Insulin**  
During prolonged fasting, when the patient's glucose level is reduced to <40 mg/dL, an elevated insulin level plus elevated levels of proinsulin and C-peptide suggest insulinoma. Insulin levels generally decline in patients with type 1 diabetes mellitus. In the early stage of type 2 diabetes, insulin levels are either normal or elevated. In the late stage of type 2 diabetes, insulin levels decline. In normal individuals, insulin levels parallel blood glucose levels. [read more here](https://www.mayocliniclabs.com/test-catalog/Clinical+and+Interpretive/8664)

**BMI (Body Mass Index)**   
BMI is used to determine obesity along with the skinfold thickness test. The World Health Organization (WHO) defines BMI as weight in kilograms divided by the square of your height in metres (kg/m2). High BMI is a risk factor for diabetes. [read more here](https://www.qualityhealth.com/diabetes-articles/diabetes-your-body-mass-index-bmi)

**Diabetes Pedigree Function**  
The hereditary risk one might have with the onset of diabetes mellitus. [read more here](https://machinelearningmastery.com/case-study-predicting-the-onset-of-diabetes-within-five-years-part-1-of-3/)
 
</details>

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
Hypothesis  
> Null hypothesis:  
> Alternative hypothesis:  
> Results  

Hypothesis  
> Null hypothesis:  
> Alternative hypothesis:  
> Results  

Hypothesis  
> Null hypothesis:  
> Alternative hypothesis:  
> Results  

## Project Steps
### Acquire
### Prepare
### Explore
### Model
#### Final Model
| Model    | RandomForest | (max_depth=5, random_state=123)             | 'Glucose', 'Age', 'BMI', <br> 'insulin_glucose_cluster', 'DiabetesPedigreeFunction' |
|----------|--------------|---------------------------------------------|------------------------------------------------------------------------------|
| DF       | Accuracy     | Recall on Positive (predicting diabetic)    | Precision on Positive (predicting diabetic)                                  |
| Train    | 86%          | 75%                                         | 84%                                                                          |
| Validate | 78%          | 64%                                         | 73%                                                                          |
| Test     | 75%          | 63%                                         | 70%                                                                          |

![Random-Forest-Guide](https://i.pinimg.com/originals/7b/28/3f/7b283f5e05af1fd7f6ec949ceb847875.png)

### Conclusions
## How to Reproduce
### Steps
1. ~Go over this Readme.md file.~ ✅
2. Download Data_Analysis.ipynb, Prepare.py, and the dataset in your working directory.
3. Run this notebook.
### Tools Used
- Pandas version ___
- Matplotlib.pyplot version ___
- Seaborn version ___
## Creator
[Bethany Thompson](https://github.com/ThompsonBethany01)
