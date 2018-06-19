%% 第二章 基本原理
%% imabsdiff 计算两幅图像间的绝对差
clc
clear

I = imread('.\images_ch02\tire.tif');
figure,imshow(I,[]);                         %imshow(I,[]);
J = uint8(filter2(fspecial('gaussian'), I));
figure,imshow(J,[]);                         %imshow(J,[]);
K = imabsdiff(I,J);
figure,imshow(K,[]);                         %[] = scale data automatically
