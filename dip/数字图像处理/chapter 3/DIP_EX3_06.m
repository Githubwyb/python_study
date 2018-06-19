%% Àı3.6 Ö±·½Í¼Æ¥Åä
clc
clear
f = imread('.\images_ch03\Fig0310(a)(Moon Phobos).tif');%»ğĞÇµÄÎÀĞÇ(»ğÎÀ1)Í¼Ïñ
subplot(121),imshow(f),subplot(122),imhist(f)
ylim('auto')
%imfinfo(f)

[g T] = histeq(f,256);
figure,subplot(121),imshow(g),subplot(122),imhist(g)
ylim('auto')

% ¶ÔÓ¦±ä»»
x = linspace(0,1,256);
figure,plot(x,T)
axis([0 1 0 1])

