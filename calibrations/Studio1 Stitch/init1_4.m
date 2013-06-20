%
%  For use with the 1_4 method
%  all the initializations if neccessary uncomment
%
%

%%%%%%%%%%%%%%%%%%%%%%%%% Camera 1 and 4 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% open files
% a = imread('Studio1-1-out.png', 'png');
% b = imread('Studio1-4-out.png', 'png');

%% get the control points
% cpselect(a,b);

%% create the transform
% TFORMab = cp2tform(input_points_ab, base_points_ab, 'projective');

%% transform the a image
% A = imtransform(a, TFORMab);

%% make new control points based on the transformed input image A
% cpselect(A, b);


%%%%%%%%%%%%%%%%%%%%%%%%% Camera 2 and 4 %%%%%%%%%%%%%%%%%%%%%%%%%%%
%% open files
% d = imread('Studio1-2-out.png', 'png');

%% get the control points
% cpselect(d,b);

%% create the transform
% TFORMdb = cp2tform(input_points_db, base_points_db, 'projective');

%% transform the a image
% D = imtransform(d, TFORMdb);

%% make new control points based on the transformed input image A
% cpselect(D, b);


%%%%%%%%%%%%%%%%%%%%%%%%% Camera 3 and 124 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% open files
% c = imread('Studio1-3-out.png', 'png');

%% get the control points
% cpselect(c,ABD);

%% create the transform
% TFORMcABD = cp2tform(input_points_cABD, base_points_cABD, 'projective');

%% transform the a image
% C = imtransform(c, TFORMcABD);

%% make new control points based on the transformed input image C
% cpselect(C, ABD);
