%% �ڶ��� ����ԭ��
%%  ����ͼ��
clc
clear

f = imread('.\images_ch02\Fig0206(a)(rose-original).tif');% ����ͼ��
imshow(f)                                                 % ����ͼ��
print -f1 -dtiff -r300 hi_res_rose                        % ����ͼ��
