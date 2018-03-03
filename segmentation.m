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
