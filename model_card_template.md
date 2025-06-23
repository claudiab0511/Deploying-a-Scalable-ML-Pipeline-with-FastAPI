# Model Card
This model was developed as part of the WGU Machine Learning DevOps course (D501).
It predicts whether a person earns more than $50k annually based on census data. 
The work follows the provided starter kit structure and adheres to the required implementation and documentation guidelines.

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- **Model Type:** Random Forest Classifier  
- **Library:** scikit-learn  
- **Task:** Binary classification (`<=50K` vs `>50K`)  
- **Version:** 1.0.1  
- **Random Seed:** 42 (for reproducibility)

## Intended Use
This model was built for educational purposes to demonstrate:
- Data preprocessing
- Model training and evaluation
- Inference
- Performance slicing
- CI/CD with GitHub Actions
- REST API deployment

It is **not** designed for real-world decision-making.


## Training Data
The model was trained on the cleaned version of `census.csv` dataset provided in the starter kit. 
The dataset includes both numerical and categorical features such as:
- `age`
- `education`
- `marital-status`
- `occupation`
- `relationship`
- `race`
- `sex`
- `native-country`
- `workclass`

### Preprocessing
- Categorical variables were processed using `OneHotEncoder`.  
- The label column (`salary`) was binarized using `LabelBinarizer`.  
- The dataset was split into 80% training and 20% testing.  
- Formatting issues were handled automatically during data preprocessing

## Evaluation Data
A 20% split of the original dataset was used as the evaluation set. 
The same preprocessing pipeline was applied, using trained encoders and 
label binarizers from the training phase.

In addition to the overall metrics, model performance was calculated for 
each unique value across all categorical features (e.g., race, education, 
workclass) using `performance_on_categorical_slice()`.

## Metrics
The model was evaluated on the following metrics:
- **Precision**
- **Recall**
- **F1 Score**

### Overall Test Performance:
- **Precision**: 0.7419  
- **Recall**: 0.6384  
- **F1 Score**: 0.6863  

The model's performance was also evaluated on **slices of the data** to assess fairness and 
stability across subgroups. For example:
- `workclass = Federal-gov`: Precision: 0.5000 | Recall: 0.4762 | F1: 0.4878  
- `workclass = Private`: Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000  
- Full slice-based performance can be found in `slice_output.txt`.

## Ethical Considerations
The dataset reflects real-world biases that may lead the model to produce unfair 
predictions across different demographic groups. Particular attention should be paid to:
- **Gender and racial bias**
- **Socioeconomic factors** encoded in job, education, and native-country features

The model should **not** be used in production without further fairness testing and 
mitigation. Predictions are based on limited demographic and employment data and should 
not be interpreted beyond the scope of this assignment.

## Caveats and Recommendations
- This model is trained on historical data and may **not generalize** well to new populations.
- Slice-level performance varies, and may indicate **potential model instability** on underrepresented groups.
- For any real-world use, retraining with updated data and deeper fairness analysis is highly recommended.
