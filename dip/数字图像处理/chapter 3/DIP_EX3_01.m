%% ������ ���ȱ任�Ϳռ��˲�

%% ʹ�ú��� imadjust Ŀ�ģ�ͻ�����Ǹ���Ȥ�����ȴ���ѹ���Ҷȼ��ĵͶ˲���չ�Ҷȼ��ĸ߶�
clc
clear

f = imread('.\images_ch03\Fig0303(a)(breast).tif');%Fig0303(a)(breast).tif
%imfinfo(f,[]);       %imfinfoMy(f)
figure,imshow(f,[]); %imshowMy(f)

g1 = imadjust(f,[0,1],[1,0]); % === imcomplement(f) �Ҷȷ�ת @ �Ҷȸ�Ƭ
%imshowMy(g1)
figure,imshow(g1,[]); %imfinfoMy(g1)

g2 = imadjust(f,[0.5,0.75],[0,1]); % ͻ�����Ǹ���Ȥ�����ȴ�
figure,imshow(g2,[]); %imshowMy(g2)
%imfinfoMy(g2)

g3 = imadjust(f,[],[],2); % ѹ���Ҷȼ��ĵͶ˲���չ�Ҷȼ��ĸ߶�
figure,imshow(g3,[]); %imshowMy(g3)
%imfinfoMy(g3)
