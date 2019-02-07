% linear model with multiple variables
% autompg data %
% x1 = cyl
% x2 = displacement 
myFit=LinearModel.fit(X,Y);
plot(myFit);
disp(myFit);
test = [1,1,1,1,1]; %test car info
est = predict(myFit, test); %what milage would be the result?
est
myFit2=LinearModel.stepwise(X,Y); %ignores irrelevant linear data
disp(myFit2);
plot(myFit2);