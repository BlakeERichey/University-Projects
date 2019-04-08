%LABELS ----IMPORT AS TABLE----
%'Alcohol',        'MalicAcid',  'Ash', 'AlcalinityOfAsh',    'Magnesium', 
%'TotalPhenols',   'Flavanoids', 'NonflavanoidPhenols',       'Proanthocyanins', 
%'ColorIntensity', 'Hue',        'OD280_OD315OfDilutedWines', 'Proline'
predictorNames = {'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13'};
predictors = datasetTable(:,predictorNames);    %determines dependent variables
predictors = table2array(varfun(@double, predictors));
response = datasetTable.Class;  %independent variable. E.g. Wine determined from dependent variables

X = predictors; %dependent values, magnesium etc
Y = response;   %the guess we are trying to evaluate, Which wine corresponds

B = datasetTable[:1] == 1