%% 第二章 基本原理
%% imcomplement 对图像求补
clc
clear

bw = imread('.\images_ch02\text.png');
bw2 = imcomplement(bw);
subplot(1,2,1),imshow(bw)
subplot(1,2,2),imshow(bw2)
