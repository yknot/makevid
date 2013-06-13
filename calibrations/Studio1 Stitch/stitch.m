%
% atttempt at a stitching script
% 
% develop parameters based on this to apply in batch
%

% if not loading the .mat file need to run all these steps
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% open files
% a = imread('Studio1-1-out.png', png);
% b = imread('Studio1-4-out.png', png);

%% get the control points
% cpselect(a,b);

%% create the transform
% TFORM = cp2tform(input_points, base_points, 'projective');

%% transform the a image
% A = imtransform(a, TFORM);

%% make new control points based on the transformed input image A
% cpselect(A, b);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

load

base_min1 = min(base_points1);
input_min1 = min(input_points1);


C = uint8(zeros(960,2274, 3));

[r,c,h] = size(A);
xpos = base_min1(2)-input_min1(2);   % shoule be 11
ypos = 1;

C(xpos:xpos+r-1,ypos:ypos+c-1,:) = A;

[r,c,h] = size(b);
xpos = 1;
ypos = input_min1(1);  % should be 992
ycut = base_min1(1);  % should be 103

C(xpos:xpos+r-1,ypos:ypos+c-ycut,:) = b(:,ycut:c,:);

figure; imshow(C);
