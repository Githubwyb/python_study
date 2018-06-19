%% 第二章 基本原理
%%  保存图像
clc
clear

f = imread('.\images_ch02\Fig0206(a)(rose-original).tif');% 读入图像
imshow(f)                                                 % 读入图像
print -f1 -dtiff -r300 hi_res_rose                        % 保存图像
