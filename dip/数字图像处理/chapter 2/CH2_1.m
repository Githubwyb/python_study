%% �ڶ��� ����ԭ��

%% imshow �����̬��Χ��С����
clc
clear

I = imread('.\images_ch02\Fig0203(a)(chest-xray).tif');
figure,subplot(121),imshow(I),subplot(122),imhist(I) 
axis tight

% ��̬��Χ�ϵ�
class(I)
min(I(:))  
max(I(:))

figure,imshow(I,[])
