%% �ڶ��� ����ԭ��
%% imcomplement ��ͼ����
clc
clear

bw = imread('.\images_ch02\text.png');
bw2 = imcomplement(bw);
subplot(1,2,1),imshow(bw)
subplot(1,2,2),imshow(bw2)
