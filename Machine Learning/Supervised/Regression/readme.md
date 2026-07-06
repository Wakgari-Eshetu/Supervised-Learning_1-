│     ├── Regression
│     │     ├── Linear Regression
│     │     ├── Multiple Linear Regression
│     │     ├── Polynomial Regression
│     │     ├── Ridge Regression
│     │     ├── Lasso Regression
│     │     ├── Elastic Net
notebook/
│
├── 01_data_understanding.ipynb
├── 02_eda.ipynb
├── 03_data_cleaning.ipynb
├── 04_feature_engineering.ipynb
├── 05_model_training.ipynb
├── 06_model_evaluation.ipynb
└── experiments/

01_data_understanding.ipynb
Load dataset
Verify dataset source and version
Display first and last rows
Check dataset shape
Inspect column names
Inspect data types
Check memory usage
Generate summary statistics
Identify target variable
Understand business problem
Review data dictionary (if available)
Classify problem (Regression/Classification)
Separate features (X) and target (y)
Identify numerical, categorical, datetime, boolean columns
Identify identifier columns (ID)
Check unique values per column
Check cardinality of categorical features
Detect duplicate rows
Detect duplicate columns
Detect constant (single-value) columns
Detect near-constant columns
Check missing values count
Check missing values percentage
Identify obvious data quality issues
Document initial observations
📓 02_eda.ipynb
   Target Variable
Missing values
Summary statistics
Distribution
Histogram
KDE plot
Boxplot
Skewness
Kurtosis
Outlier inspection
Decide whether transformation is needed
   Numerical Features
Summary statistics
Distribution plots
Histograms
KDE plots
Boxplots
Skewness
Kurtosis
Missing value visualization
Correlation matrix
Correlation heatmap
Feature-target correlation
Pair plots (selected features)
Outlier detection
Multicollinearity inspection
   Categorical Features
Frequency tables
Missing values
Cardinality
Bar plots
Count plots
Category imbalance
Relationship with target
Rare category detection
   Mixed Analysis
Numerical vs Target
Categorical vs Target
Numerical vs Numerical
Categorical vs Categorical
Numerical vs Categorical
General Findings
Strong predictors
Weak predictors
Redundant variables
Data imbalance
Initial preprocessing decisions
📓 03_data_cleaning.ipynb
Create working copy
Remove duplicate rows
Remove duplicate columns
Drop irrelevant columns
Drop identifier columns
Drop high-missing columns
Correct data types
Fix inconsistent values
Standardize categorical labels
Handle missing numerical values
Handle missing categorical values
Handle datetime issues
Handle invalid values
Handle impossible values
Handle outliers (if appropriate)
Verify cleaned dataset
Compare before vs after cleaning
Save cleaned dataset
📓 04_feature_engineering.ipynb
Feature Creation
Create new numerical features
Create interaction features
Aggregate features
Ratio features
Date/time derived features
Domain-specific features
Feature Transformation
Log transformation
Square root transformation
Box-Cox/Yeo-Johnson (if needed)
Encoding
Label Encoding
One-Hot Encoding
Ordinal Encoding
Frequency Encoding (if needed)
Target Encoding (if appropriate)
Scaling
StandardScaler
MinMaxScaler
RobustScaler
Normalizer (if appropriate)
Feature Selection
Remove low variance features
Correlation-based selection
Statistical feature selection
Model-based feature selection
Recursive Feature Elimination (RFE)
Remove multicollinearity
Final Checks
Verify feature matrix
Verify target alignment
Save processed dataset
📓 05_model_training.ipynb
Split train/validation/test sets
Build preprocessing pipeline
Define baseline model
Train baseline model
Train multiple candidate models
Cross-validation
Hyperparameter tuning
Feature importance extraction
Model comparison
Select best model
Save trained model
Save preprocessing pipeline
Save training metadata
Record training time
Set random seed for reproducibility
📓 06_model_evaluation.ipynb
Performance
Evaluate training performance
Evaluate validation performance
Evaluate test performance
Metrics (Regression)
MAE
MSE
RMSE
RMSLE (if applicable)
R²
Adjusted R² (if applicable)
Error Analysis
Residual analysis
Residual plots
Prediction vs Actual plot
Error distribution
Largest prediction errors
Model Diagnostics
Overfitting check
Underfitting check
Bias-variance analysis
Generalization assessment
Interpretation
Feature importance
SHAP (optional)
Permutation importance (optional)
Final Outputs
Compare all models
Select final model
Save evaluation results
Document strengths
Document limitations
Recommend future improvements
📁 experiments/
Test new preprocessing methods
Test different imputers
Test different encoders
Test different scalers
Test feature selection methods
Test feature engineering ideas
Try different train/test splits
Compare algorithms
Compare hyperparameters
Try ensemble methods
Test stacking/blending
Prototype new ideas
Temporary visualizations
Ablation studies
Failed experiments
Notes and observations