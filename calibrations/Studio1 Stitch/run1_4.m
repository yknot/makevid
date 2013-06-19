%
% for the 1-4 method all the combination processes
%
% stitch 4 individually
% stitch them all together into a mosaic
%


%%%%%%%%%%%%%%%%%%%%%%%% Combine a and b %%%%%%%%%%%%%%%%%%%%%%%%%%%%
base_min_Ab = min(base_points_Ab);
input_min_Ab = min(input_points_Ab);

xdiff = base_min_Ab(2)-input_min_Ab(2);

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
ypos = input_min_Ab(1);  % should be 992
ycut = base_min_Ab(1);  % should be 103

AB(xpos:xpos+row-1,ypos:ypos+col-ycut,:) = b(:,ycut:col,:);

% figure; imshow(AB);


%%%%%%%%%%%%%%%%%%%%%%%% Combine d and b %%%%%%%%%%%%%%%%%%%%%%%%%%%%
base_max_Db = base_points_Db(max(find(base_points_Db==max(base_points_Db(:)))),:);
index = base_points_Db(find(input_points_Db==base_min_Db(1)))
input_min_Db = input_points_Db(index,:);

DB = uint8(zeros(1000,1000, 3));

[row,col,hei] = size(D);
ypos = 1;
xpos = 1;  % should be

DB(xpos:xpos+row-1,ypos:ypos+col-1,:) = D;

[row,col,hei] = size(b);
ypos = 1;
xpos = 1;
xcut = base_max_Db(2);  % should be

DB(xpos:xcut,ypos:ypos+col-1,:) = b(1:xcut,:,:);

figure; imshow(DB);


%%%%%%%%%%%%%%%%%%%%%%%% Combine c and D %%%%%%%%%%%%%%%%%%%%%%%%%%%%
% base_min_cD = base_points_cD(min(find(base_points_cD==min(base_points_cD(1)))),:);
% input_min_cD = input_points_cD(min(find(input_points_cD==min(input_points_cD(1)))),:);

% xdiff = base_min_cD(2)-input_min_cD(2);

% CD = uint8(zeros(960,2274, 3));

% [row,col,hei] = size(D);
% if xdiff > 0
%   xpos = xdiff;
% else
%   xpos = 1;
% end
% ypos = 1;

% DB(xpos:xpos+row-1,ypos:ypos+col-1,:) = D;

% [row,col,hei] = size(c);
% if xdiff < 0
%   xpos = 0-xdiff; % should be 31;
% else 
%   xpos = 1;
% end   
% ypos = input_min_cD(1);  % should be 1094
% ycut = base_min_cD(1);  % should be 88

% CD(xpos:xpos+row-1,ypos:ypos+col-ycut,:) = c(:,ycut:col,:);

% figure; imshow(CD);
