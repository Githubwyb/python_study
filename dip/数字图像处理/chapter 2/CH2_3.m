%% 第二章 基本原理

%% im2bw 灰度图像变为二值图像
clc
clear

I = imread('.\images_ch02\liftingbody.png');
imshow(I)

BW = im2bw(I,0.46);

figure,imshow(BW)
