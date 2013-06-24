%
% for the 1-4 method all the combination processes
%
% stitch 4 individually
% stitch them all together into a mosaic
%

%%%%%%%%%%%%%%%%%%%%%%%% Combine A and b %%%%%%%%%%%%%%%%%%%%%%%%%%%%
AB = uint8(zeros(800,1000, 3));

[row,col,hei] = size(A);
xpos = 11;
ypos = 1;

AB(xpos:xpos+row-1,ypos:ypos+col-1,:) = A;

[row,col,hei] = size(b);
xpos = 1;
ypos = 992;
ycut = 103;

AB(xpos:xpos+row-1,ypos:ypos+col-ycut,:) = b(:,ycut:col,:);

% figure; imshow(AB);

%%%%%%%%%%%%%%%%%%%%%%%% Combine D and b %%%%%%%%%%%%%%%%%%%%%%%%%%%%
DB = uint8(zeros(1000,1000, 3));

[row,col,hei] = size(D);
ypos = 944;
xpos = 1;  % should be
ystart = 158.8174;

DB(ypos:ypos+row-ystart,xpos:xpos+col-1,:) = D(ystart:row,:,:);

[row,col,hei] = size(b);
ypos = 1;
xpos = 572.6564-431;
ymax = 944;

DB(ypos:ymax,xpos:xpos+col-1,:) = b(ypos:ymax,:,:);

% figure; imshow(DB);

%%%%%%%%%%%%%%%%%%%%%%% Combine AB and DB %%%%%%%%%%%%%%%%%%%%%%%%%%%
ABD = uint8(zeros(1000,1000, 3));

[row,col,hei] = size(DB);
ypos = 1;
xpos = 992-(572.6564-431)-103;

ABD(ypos:ypos+row-1,xpos:xpos+col-1,:) = DB;

[row,col,hei] = size(AB);
ypos = 1;
xpos = 1;
ymax = 944;

ABD(ypos:ymax,xpos:xpos+col-1,:) = AB(ypos:ymax,:,:);

% figure; imshow(ABD);

%%%%%%%%%%%%%%%%%%%%%%%% Combine C and ABD %%%%%%%%%%%%%%%%%%%%%%%%%%%%
ABCD = uint8(zeros(1000,1000, 3));

[row,col,hei] = size(ABD);
xpos = 1;
ypos = 1363-1196;

ABCD(xpos:xpos+row-1,ypos:ypos+col-1,:) = ABD(:,:,:);

[row,col,hei] = size(C);
xpos = 850;
ypos = 1;
xstart = 76;
ymax = 1201;

ABCD(xpos:xpos+row-xstart,ypos:ymax,:) = C(xstart:row,ypos:ymax,:);

figure; imshow(ABCD);
