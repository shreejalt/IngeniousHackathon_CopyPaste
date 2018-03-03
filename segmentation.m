clc;    % Clear command window.
close all;
A=imread('C:\Users\Hp\Desktop\aaa.jpeg');

I2 = imresize(A,[800 800]);

%Converts the image to gray scale
grey = rgb2gray(I2);

%Gives the thresold of the image by Otsu
level = graythresh(grey);

%Black and White
BW = im2bw(grey, level);

%Invert BW
bin_im = imcomplement(BW);

%Delete CC with area<30
bin_im = bwareaopen(bin_im,30);
bw1 = bin_im;

%Label the connected components
[Label,Total]=bwlabel(bw1,8);

%Rectangle containing the region
Sdata=regionprops(Label,'BoundingBox');
for i=1:Total  
%Crop all the Images 
    Img = imcrop(bw1,Sdata(i).BoundingBox);
    Name = strcat('Object Number:',num2str(i));
    pathname1 = 'C:\Users\Hp\Desktop\images';
    baseFileName1 = sprintf('Img%d.jpg',i);
    fullFileName1 = fullfile(pathname1,baseFileName1);
    imwrite(Img,fullFileName1);
end
