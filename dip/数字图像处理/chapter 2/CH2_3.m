%% �ڶ��� ����ԭ��

%% im2bw �Ҷ�ͼ���Ϊ��ֵͼ��
clc
clear

I = imread('.\images_ch02\liftingbody.png');
imshow(I)

BW = im2bw(I,0.46);

figure,imshow(BW)
