%% ��3.5 ֱ��ͼ���⻯ Ĭ��Ϊ64
clc
clear
f = imread('.\images_ch03\Fig0308(a)(pollen).tif');
subplot(121),imshow(f),subplot(122),imhist(f)
ylim('auto')
%imfinfo(f)

g = histeq(f,256);
figure,subplot(121),imshow(g),subplot(122),imhist(g)
ylim('auto')
%imfinfo(g)

g = histeq(f,128);
figure,subplot(121),imshow(g),subplot(122),imhist(g)
ylim('auto')
%imfinfo(g)

g = histeq(f);  % Ĭ��Ϊ64
figure,subplot(121),imshow(g),subplot(122),imhist(g)
ylim('auto')
%imfinfo(g)

g = histeq(f,8);
figure,subplot(121),imshow(g),subplot(122),imhist(g)
ylim('auto')
%imfinfo(g)