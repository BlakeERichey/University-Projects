x=[1 8 11 4 3];
y = [3 9 11 5 2 ];
myFit=LinearModel.fit(x,y);
plot(myFit);
disp(myFit);

Estimate = predict(myFit, 6); %if x is 6 y is? 6.552
