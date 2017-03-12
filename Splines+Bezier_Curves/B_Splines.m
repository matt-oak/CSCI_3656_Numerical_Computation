%Points: (1,1), (2,3), (3,2), (4,1)

%Interval for parametric equations
u = linspace(0, 1);

%Parametric equations for middle segment
x = (1/6)*((1-u).^3) + (1/3)*(3*u.^3-6*u.^2+4) + (1/2)*(-3*u.^3+3*u.^2+3*u+1) + (2/3)*u.^3;
y = (1/6)*((1-u).^3) + (1/2)*(3*u.^3-6*u.^2+4) + (1/3)*(-3*u.^3+3*u.^2+3*u+1) + (1/6)*u.^3;

%Parametric equations for left-most segment
x2 = (1/6)*((1-u).^3) + (1/6)*(3*u.^3-6*u.^2+4) + (1/3)*(-3*u.^3+3*u.^2+3*u+1) + (1/2)*u.^3;
y2 = (1/6)*((1-u).^3) + (1/6)*(3*u.^3-6*u.^2+4) + (1/2)*(-3*u.^3+3*u.^2+3*u+1) + (1/3)*u.^3;

%Parametric equations for right-most segment
x3 = (1/3)*((1-u).^3) + (1/2)*(3*u.^3-6*u.^2+4) + (2/3)*(-3*u.^3+3*u.^2+3*u+1) + (2/3)*u.^3;
y3 = (1/2)*((1-u).^3) + (1/3)*(3*u.^3-6*u.^2+4) + (1/6)*(-3*u.^3+3*u.^2+3*u+1) + (1/6)*u.^3;

%Plot middle, left-most, and then right-most segments
plot(x, y);
hold on
plot(x2, y2);
hold on
plot(x3, y3);
hold on

%Plot points
plot(1, 1, 'r*');
text(1, 1, ' Point 1');
hold on
plot(2, 3, 'r*');
text(2, 3, ' Point 2');
hold on
plot(3, 2, 'r*');
text(3, 2, ' Point 3');
hold on
plot(4, 1, 'r*');
text(4, 1, ' Point 4');