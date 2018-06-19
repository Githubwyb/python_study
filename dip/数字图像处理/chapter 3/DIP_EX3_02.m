
%% 例3.2 使用对数变换   减小动态范围
clc
clear

f = imread('.\images_ch03\Fig0305(a)(spectrum).tif');
%imfinfo(f)

subplot(121),imshow(f),subplot(122),imhist(f),axis tight

g = im2uint8(mat2gray(log(1 + double(f))));
figure,subplot(121),imshow(g),subplot(122),imhist(g),axis tight
title('使用对数变换减小动态范围')
%imfinfo(g)
% axis([0 255 0 4000])

% 对比度拉伸变换
m = 5;
E = 10;
h = im2uint8(mat2gray(1./(1 + (m./(double(f) + eps)).^E)));
%imfinfo(h)
figure,subplot(121),imshow(h),subplot(122),imhist(h),axis tight
title('使用对比度拉伸变换')
