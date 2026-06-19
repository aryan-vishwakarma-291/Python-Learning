# from sklearn.model_selection import train_test_split , cross_val_score
# import numpy as np

# np.random.seed(42)
# X = np.random.randn(500,5)
# y = np.random.randint(0,2,500) 

# X_train , X_test , y_train , y_test = train_test_split(
#     X,y,test_size=0.2 , random_state=42 , stratify=y
# )
# print(f'Traning samples: {len(X_train)} | Test samples: {len(X_test)}')

# # 5-fold
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=50 , random_state=42)
# cv_scores = cross_val_score(model,X,y,cv=5, scoring='accuracy')
# print(f'CV Scores each fold: {cv_scores.round(3)}')
# print(f'Mean: {cv_scores.mean():.4f} += {cv_scores.std():.4f}')


# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt

# #data
# n_A , conv_A = 1000 , 52
# n_B, conv_B = 1000,68
# rate_A = conv_A / n_A
# rate_B = conv_B / n_B

# print(f'Version A conversion rate: {rate_A*100:.1f}%')
# print(f'Version B conversion rate: {rate_B*100:.1f}%')
# print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

# #chi-sqaure test for statistical significance

# table = [[conv_A, n_A-conv_A],[conv_B, n_B-conv_B]]
# chi2, p_value , dof , expected = stats.chi2_contingency(table)

# print(f'Chi-Square: {chi2:.4f}')
# print(f'P-value: {p_value:.4f}')
# print('Result:' , 'SIGNIFICANT - B is better!' if p_value<0.05 else 'NOT significant - could be random')
