%
%  For use with the 2_2 method
%  all the initializations if neccessary uncomment
%
%

%%%%%%%%%%%%%%%%%%%%%%%%% Camera 1 and 4 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% open files
a = imread('Studio1-1-out.png', 'png');
b = imread('Studio1-4-out.png', 'png');

%% get the control points
cpselect(a,b);

%% create the transform
TFORMab = cp2tform(input_points_ab, base_points_ab, 'projective');

%% transform the a image
A = imtransform(a, TFORMab);

%% make new control points based on the transformed input image A
cpselect(A, b);

%%%%%%%%%%%%%%%%%%%%%%%%% Camera 2 and 3 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% open files
c = imread('Studio1-3-out.png', 'png');
d = imread('Studio1-2-out.png', 'png');

%% get the control points
cpselect(c,d);

%% create the transform
TFORMcd = cp2tform(input_points_cd, base_points_cd, 'projective');

%% transform the a image
C = imtransform(c, TFORMcd);

%% make new control points based on the transformed input image C
cpselect(C, d);



%%%%%%%%%%%%%%%%%%%%%%%%% Combine 2 and 2 %%%%%%%%%%%%%%%%%%%%%%%%%%%
%% get the control points
cpselect(AB,CD);

%% create the transform
TFORMabcd = cp2tform(input_points_abcd, base_points_abcd, 'affine');

%% transform the a image
ab = imtransform(AB, TFORMabcd);

%% make new control points based on the transformed input image A
cpselect(ab, CD);
