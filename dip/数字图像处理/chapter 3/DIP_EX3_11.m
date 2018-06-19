%% 例3.11 使用函数 medfilt2 进行中值滤波P77
clc
clear

f = imread('.\images_ch03\Fig0318(a)(ckt-board-orig).tif');
figure,imshow(f)
title(1)

fn = imnoise(f, 'salt & pepper',0.2);
figure,imshow(fn)
%imfinfo(fn)
title(2)
gm = medfilt2(fn);
figure,imshow(gm)
%imfinfo(gm)
title(3)
gms = medfilt2(fn, 'symmetric');
figure,imshow(gms)
%imfinfo(gms)
title(4)

