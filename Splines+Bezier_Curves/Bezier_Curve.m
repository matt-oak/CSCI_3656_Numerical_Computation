%Points: (1,1), (2,3), (3,2), (4,1)

%Interval for parametric equations
u = linspace(0, 1);

%Bezier curves in parametric equation form
x = ((1-u).^3) + (6*u).*((1-u).^2) + (9*u.^2).*(1-u) + 4*u.^3;
y = ((1-u).^3) + (9*u).*((1-u).^2) + (6*u.^2).*(1-u) + u.^3;

%Plot parametric equations
plot(x, y);
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