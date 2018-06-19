%% 第三章 亮度变换和空间滤波

%% 使用函数 imadjust 目的：突出我们感兴趣的亮度带·压缩灰度级的低端并扩展灰度级的高端
clc
clear

f = imread('.\images_ch03\Fig0303(a)(breast).tif');%Fig0303(a)(breast).tif
%imfinfo(f,[]);       %imfinfoMy(f)
figure,imshow(f,[]); %imshowMy(f)

g1 = imadjust(f,[0,1],[1,0]); % === imcomplement(f) 灰度反转 @ 灰度负片
%imshowMy(g1)
figure,imshow(g1,[]); %imfinfoMy(g1)

g2 = imadjust(f,[0.5,0.75],[0,1]); % 突出我们感兴趣的亮度带
figure,imshow(g2,[]); %imshowMy(g2)
%imfinfoMy(g2)

g3 = imadjust(f,[],[],2); % 压缩灰度级的低端并扩展灰度级的高端
figure,imshow(g3,[]); %imshowMy(g3)
%imfinfoMy(g3)
