%% ��3.6 ֱ��ͼƥ��
clc
clear
f = imread('.\images_ch03\Fig0310(a)(Moon Phobos).tif');%���ǵ�����(����1)ͼ��
subplot(121),imshow(f),subplot(122),imhist(f)
ylim('auto')
%imfinfo(f)

[g T] = histeq(f,256);
figure,subplot(121),imshow(g),subplot(122),imhist(g)
ylim('auto')

% ��Ӧ�任
x = linspace(0,1,256);
figure,plot(x,T)
axis([0 1 0 1])

