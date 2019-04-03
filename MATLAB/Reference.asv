%OUTPUT
x = 3;
x;  %semicolon to supress output

%INPUT
%x = input('Change x value: '); %strings must be in ' ' 
%x;

%FOR STATEMENTS
%print x: //0,1,2,3,4,5 inclusive both sides
for n = 0:5
    x = n;
end


%IF STATEMENT
if x == 5
    x = x * 5;   %x = 25
end

if x ~= 5   %not statement ~
    x / 5;   %ans = 5 (x = 25 still)
end

%ARRAYS
z = ones(5); %create 5x5 matrix of all 1s
z = zeros(5); %create 5x5 matrix of all 0s

A = [1 4 ; 2 5 ; 3 6]; %custom array 3x2

size(A); %3 2

%access array index
%arrays start at 1, not 0
A(1, 2); %ans = 4

%FUNCTIONS
%this file, being named Reference.h is a function called 'Reference'

%add;
avg([1,2,3, 7, 11]) %prints 4.8
%can also do sub functions in a file:
%these must be the end of the file (akin to prototyping)
function add
x = input('X value: ')
y = input('Y value: ')
'X + Y'
(x+y)
end

function avg(n)
sum(n)/length(n)
end