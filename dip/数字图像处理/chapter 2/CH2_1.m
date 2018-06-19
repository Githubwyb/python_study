%% 第二章 基本原理

%% imshow 解决动态范围较小问题
clc
clear

I = imread('.\images_ch02\Fig0203(a)(chest-xray).tif');
figure,subplot(121),imshow(I),subplot(122),imhist(I) 
axis tight

% 动态范围较低
class(I)
min(I(:))  
max(I(:))

figure,imshow(I,[])
