f= imread('.\images_ch03\Fig0306(a)(bone-scan-GE).tif');
figure,imshow(f)
g= intrans(f,'stretch',mean2(im2double(f)),0.9); %call function intrans();
figure,imshow(g)
