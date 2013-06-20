%
% for the 1-4 method all the combination processes
%
% stitch 4 individually
% stitch them all together into a mosaic
%


%%%%%%%%%%%%%%%%%%%%%%%% Combine a and b %%%%%%%%%%%%%%%%%%%%%%%%%%%%
% base_min_Ab = min(base_points_Ab);
% input_min_Ab = min(input_points_Ab);

% xdiff = base_min_Ab(2)-input_min_Ab(2);

% AB = uint8(zeros(1000,1000, 3));

% [row,col,hei] = size(A);
% if xdiff > 0
%   xpos = xdiff;   % should be 11
% else
%   xpos = 1;
% end
% ypos = 1;

% AB(xpos:xpos+row-1,ypos:ypos+col-1,:) = A;

% [row,col,hei] = size(b);
% if xdiff < 0
%   xpos = 0-xdiff;
% else
%   xpos = 1;
% end
% ypos = input_min_Ab(1);  % should be 992
% ycut = base_min_Ab(1);  % should be 103

% AB(xpos:xpos+row-1,ypos:ypos+col-ycut,:) = b(:,ycut:col,:);

% figure; imshow(AB);


%%%%%%%%%%%%%%%%%%%%%%%% Combine d and b %%%%%%%%%%%%%%%%%%%%%%%%%%%%

% DB = uint8(zeros(1000,1000, 3));

% [row,col,hei] = size(D);
% ypos = 944;
% xpos = 1;  % should be
% ystart = 158.8174;

% DB(ypos:ypos+row-ystart,xpos:xpos+col-1,:) = D(ystart:row,:,:);

% [row,col,hei] = size(b);
% ypos = 1;
% xpos = 572.6564-431;
% ymax = 944;

% DB(ypos:ymax,xpos:xpos+col-1,:) = b(ypos:ymax,:,:);

% figure; imshow(DB);


%%%%%%%%%%%%%%%%%%%%%%% Combine AB and DB %%%%%%%%%%%%%%%%%%%%%%%%%%%
% ABD = uint8(zeros(1000,1000, 3));


% [row,col,hei] = size(DB);
% ypos = 1;
% xpos = 992-(572.6564-431)-103;

% ABD(ypos:ypos+row-1,xpos:xpos+col-1,:) = DB;

% [row,col,hei] = size(AB);
% ypos = 1;
% xpos = 1;  % should be
% ymax = 944;

% ABD(ypos:ymax,xpos:xpos+col-1,:) = AB(ypos:ymax,:,:);


% figure; imshow(ABD);



%%%%%%%%%%%%%%%%%%%%%%%% Combine c and ABD %%%%%%%%%%%%%%%%%%%%%%%%%%%%
ABCD = uint8(zeros(1000,1000, 3));

[row,col,hei] = size(ABD);
xpos = 1;
ypos = 1363-1196;  % should be
% xmax = 837;

ABCD(xpos:xpos+row-1,ypos:ypos+col-1,:) = ABD(:,:,:);

[row,col,hei] = size(C);
xpos = 850;
ypos = 1;
xstart = 76;
ymax = 1201;

ABCD(xpos:xpos+row-xstart,ypos:ymax,:) = C(xstart:row,ypos:ymax,:);

figure; imshow(ABCD);
