I = imread('.\images_ch03\Fig0303(a)(breast).tif');
% tform = maketform('affine',[2 0 0; 0 1 0; 0 0 1]);
% J = imtransform(I,tform);
% imview(I), imview(J)

figure;
subplot(121);imshow(I);
I=double(I);
I_mover=zeros(size(I));
H=size(I);
I_x=200;
I_y=200;
I_mover(I_x+1:H(1),I_y+1:H(2))=I(1:H(1)-I_x,1:H(2)-I_y);%ƽ�Ʊ仯
subplot(122);imshow(uint8(I_mover));
