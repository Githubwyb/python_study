%% �ڶ��� ����ԭ��
%% imabsdiff ��������ͼ���ľ��Բ�
clc
clear

I = imread('.\images_ch02\tire.tif');
figure,imshow(I,[]);                         %imshow(I,[]);
J = uint8(filter2(fspecial('gaussian'), I));
figure,imshow(J,[]);                         %imshow(J,[]);
K = imabsdiff(I,J);
figure,imshow(K,[]);                         %[] = scale data automatically
