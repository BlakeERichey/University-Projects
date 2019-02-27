predictorNames = {'Alcohol', 'MalicAcid', 'Ash', 'AlcalinityOfAsh', 'Magnesium', 'TotalPhenols', 'Flavanoids', 'NonflavanoidPhenols', 'Proanthocyanins', 'ColorIntensity', 'Hue', 'OD280_OD315OfDilutedWines', 'Proline'};
predictors = datasetTable(:,predictorNames);    %determines dependent variables
predictors = table2array(varfun(@double, predictors));
response = datasetTable.Class;  %independent variable. E.g. Wine determined from dependent variables

X = predictors; %dependent values, magnesium etc
Y = response;   %the guess we are trying to evaluate, Which wine corresponds

S = std(X);
M = mean(X);
V = var(X);

%***Scatter Plot***
plotmatrix(X);

%***Parallel Coords***
%x axis in parallelcoords plot
labels = {'Alcohol', 'MalicAcid', 'Ash', 'AlcalinityOfAsh', 'Magnesium', 'TotalPhenols', 'Flavanoids', 'NonflavanoidPhenols', 'Proanthocyanins', 'ColorIntensity', 'Hue', 'OD280_OD315OfDilutedWines', 'Proline'};

%parallel coordinate plot
parallelcoords(X, 'Group', Y, 'Labels', labels);
S;
M;
V;