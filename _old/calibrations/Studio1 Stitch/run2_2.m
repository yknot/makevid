%
% for the 2-2 method all the combination processes
%
% this combines a and b as well as c and d
% then combines the 2 images into a 4 image mosaic
%


%%%%%%%%%%%%%%%%%%%%%%%% Combine a and b %%%%%%%%%%%%%%%%%%%%%%%%%%%%
base_min_ab1 = min(base_points_ab1);
input_min_ab1 = min(input_points_ab1);

xdiff = base_min_ab1(2)-input_min_ab1(2);

AB = uint8(zeros(960,2274, 3));

[row,col,hei] = size(A);
if xdiff > 0
  xpos = xdiff;   % should be 11
else
  xpos = 1;
end
ypos = 1;

AB(xpos:xpos+row-1,ypos:ypos+col-1,:) = A;

[row,col,hei] = size(b);
if xdiff < 0
  xpos = 0-xdiff;
else
  xpos = 1;
end
ypos = input_min_ab1(1);  % should be 992
ycut = base_min_ab1(1);  % should be 103

AB(xpos:xpos+row-1,ypos:ypos+col-ycut,:) = b(:,ycut:col,:);

% figure; imshow(AB);




%%%%%%%%%%%%%%%%%%%%%%%% Combine c and d %%%%%%%%%%%%%%%%%%%%%%%%%%%%
base_min_cd1 = base_points_cd1(min(find(base_points_cd1==min(base_points_cd1(1)))),:);
input_min_cd1 = input_points_cd1(min(find(input_points_cd1==min(input_points_cd1(1)))),:);

xdiff = base_min_cd1(2)-input_min_cd1(2);

CD = uint8(zeros(960,2274, 3));

[row,col,hei] = size(C);
if xdiff > 0
  xpos = xdiff;
else
  xpos = 1;
end
ypos = 1;

CD(xpos:xpos+row-1,ypos:ypos+col-1,:) = C;

[row,col,hei] = size(d);
if xdiff < 0
  xpos = 0-xdiff; % should be 31;
else 
  xpos = 1;
end   
ypos = input_min_cd1(1);  % should be 1094
ycut = base_min_cd1(1);  % should be 88

CD(xpos:xpos+row-1,ypos:ypos+col-ycut,:) = d(:,ycut:col,:);

% figure; imshow(CD);


%%%%%%%%%%%%%%%%%%%%%% Combine top and bot %%%%%%%%%%%%%%%%%%%%%%%%%%
base_min_abcd1 = base_points_abcd1(min(find(base_points_abcd1==min(base_points_abcd1(1)))),:);
input_min_abcd1 = input_points_abcd1(min(find(input_points_abcd1==min(input_points_abcd1(1)))),:);

ydiff = base_min_abcd1(1)-input_min_abcd1(1);

ABCD = uint8(zeros(960,2274, 3));

[row,col,hei] = size(ab);
if ydiff > 0
  ypos = ydiff;
else
  ypos = 1;
end
xpos = 1;

ABCD(xpos:xpos+row-1,ypos:ypos+col-1,:) = ab;

[row,col,hei] = size(CD);
if ydiff < 0
  ypos = 0-ydiff; % should be 852.75
else 
  ypos = 1;
end   
xpos = input_min_abcd1(2);  % should be 
xcut = base_min_abcd1(2);  % should be 

ABCD(xpos:xpos+row-xcut,ypos:ypos+col-1,:) = CD(xcut:row,:,:);

figure; imshow(ABCD);