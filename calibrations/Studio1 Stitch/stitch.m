%
% atttempt at a stitching script
% 
% develop parameters based on this to apply in batch
%
clear
load('base.mat')

% if not loading the .mat file need to run all these steps
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% open files
% a = imread('Studio1-1-out.png', 'png');
% b = imread('Studio1-4-out.png', 'png');
% c = imread('Studio1-3-out.png', 'png');
% d = imread('Studio1-2-out.png', 'png');

%% get the control points
% cpselect(a,b);
% cpselect(c,d);

%% create the transform
% TFORMab = cp2tform(input_points_ab, base_points_ab, 'projective');
% TFORMcd = cp2tform(input_points_cd, base_points_cd, 'projective');

%% transform the a image
% A = imtransform(a, TFORMab);
% C = imtransform(c, TFORMcd);

%% make new control points based on the transformed input image A
% cpselect(A, b);
% cpselect(C, d);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% run for a and b

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

figure; imshow(AB);

%% run for c and d

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

figure; imshow(CD);