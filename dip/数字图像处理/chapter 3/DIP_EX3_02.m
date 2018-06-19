
%% ��3.2 ʹ�ö����任   ��С��̬��Χ
clc
clear

f = imread('.\images_ch03\Fig0305(a)(spectrum).tif');
%imfinfo(f)

subplot(121),imshow(f),subplot(122),imhist(f),axis tight

g = im2uint8(mat2gray(log(1 + double(f))));
figure,subplot(121),imshow(g),subplot(122),imhist(g),axis tight
title('ʹ�ö����任��С��̬��Χ')
%imfinfo(g)
% axis([0 255 0 4000])

% �Աȶ�����任
m = 5;
E = 10;
h = im2uint8(mat2gray(1./(1 + (m./(double(f) + eps)).^E)));
%imfinfo(h)
figure,subplot(121),imshow(h),subplot(122),imhist(h),axis tight
title('ʹ�öԱȶ�����任')
