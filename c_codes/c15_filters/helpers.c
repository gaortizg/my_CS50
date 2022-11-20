#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int gray;
	
	// Loop through each pixel
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			// Compute average value of pixel
			gray = (int) (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3;

			// Assign average value to each channel on pixel
			image[i][j].rgbtBlue = gray;
			image[i][j].rgbtGreen = gray;
			image[i][j].rgbtRed = gray;
		}
	}
	return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
	int sepiaR, sepiaG, sepiaB;
	
	// Loop through each pixel
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			// Compute sepia colors for each channel
			sepiaR = (int) .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
			sepiaG = (int) .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
			sepiaB = (int) .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;

			// Sepia colors must be capped at 255
			if (sepiaR > 255)
			{
				sepiaR = 255;
			}
			else if (sepiaG > 255)
			{
				sepiaG = 255;
			}
			else if (sepiaB > 255)
			{
				sepiaB = 255;
			}

			// Assign new sepia colors to pixel;
			image[i][j].rgbtRed = sepiaR;
			image[i][j].rgbtGreen = sepiaG;
			image[i][j].rgbtBlue = sepiaB;
		}
	}
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
	// Create temp variable to store channels of a pixel before swapping
	RGBTRIPLE tmp;

	// Loop through all rows of the image
	for (int i = 0; i < height; i++)
	{
		// loop through half of the pixels in each row and swap pixels accordingly
		for (int j = 0; j <= width / 2; j++)
		{
			tmp = image[i][j];
			image[i][j] = image[i][width - 1 - j];
			image[i][width - 1 - j] = tmp;
		}
	}
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Copy original image into a temporary array.
	// This is necessary because once we make changes to original image,
	// then we will lose the original information of other pixels
	// to compute the average. Therefore, store original info in a temporary
	// array and use it to have always access to the original data
    RGBTRIPLE tmp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j] = image[i][j];
        }
    }
    
	// Loop through each pixel
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			// Initialize values to check if pixel is in corner or not
			int sumR, sumG, sumB;
			int counter;
			sumR = sumG = sumB = counter = 0;
			
			// loop to check if there are pixels around current pixel.
			// If there are pixels, then add RGB values.
			// If there are not pixels, then skip and continue to the next one
			for (int k = -1; k < 2; k++)
			{
			    for (int l = -1; l < 2; l++)
			    {
			        // Check if pixel outside rows
			        if ((i + k < 0) || (i + k > height))
			        {
			            continue;
			        }
			        
			        // Check if pixel outside columns
			        if ((j + l < 0) || (j + l > width))
			        {
			            continue;
			        }
			        
			        // Otherwise, add to sums
			        sumR += tmp[i + k][j + l].rgbtRed;
			        sumG += tmp[i + k][j + l].rgbtGreen;
			        sumB += tmp[i + k][j + l].rgbtBlue;
			        counter++;
			    }
			}
			
			// Compute average value to get blurred image
			image[i][j].rgbtRed = (int) sumR / counter;
			image[i][j].rgbtGreen = (int) sumG / counter;
			image[i][j].rgbtBlue = (int) sumB / counter;
		}
	}
    return;
}

// Detect edges on image
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Copy original image into a temporary array.
	// This is necessary because once we make changes to original image,
	// then we will lose the original information of other pixels
	// to compute the average. Therefore, store original info in a temporary
	// array and use it to have always access to the original data
    RGBTRIPLE tmp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j] = image[i][j];
        }
    }
    
    // Initialize kernel matrices
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    int red, green, blue;

	// Loop through each pixel
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			// Initialize values
			int sumRx, sumGx, sumBx;
			int sumRy, sumGy, sumBy;
			sumRx = sumGx = sumBx = 0;
			sumRy = sumGy = sumBy = 0;
			
			// loop to check if there are pixels around current pixel.
			// If there are pixels, then add RGB values.
			// If there are not pixels, then skip and continue to the next one
			for (int k = -1; k < 2; k++)
			{
			    for (int l = -1; l < 2; l++)
			    {
			        // Check if pixel outside rows
			        if ((i + k < 0) || (i + k > height))
			        {
			            continue;
			        }
			        
			        // Check if pixel outside columns
			        if ((j + l < 0) || (j + l > width))
			        {
			            continue;
			        }
			        
			        // Otherwise, add to sums
			        sumRx += Gx[k+1][l+1] * tmp[i + k][j + l].rgbtRed;
			        sumRy += Gy[k+1][l+1] * tmp[i + k][j + l].rgbtRed;
			        sumGx += Gx[k+1][l+1] * tmp[i + k][j + l].rgbtGreen;
			        sumGy += Gy[k+1][l+1] * tmp[i + k][j + l].rgbtGreen;
			        sumBx += Gx[k+1][l+1] * tmp[i + k][j + l].rgbtBlue;
			        sumBy += Gy[k+1][l+1] * tmp[i + k][j + l].rgbtBlue;
			    }
			}
			
			// Compute square root for each channel sqrt(Sumx^2 + Sumy^2)
			// Also make sure value is capped at 255
			red = (int) sqrt(sumRx * sumRx + sumRy * sumRy);
			green = (int) sqrt(sumGx * sumGx + sumGy * sumGy);
			blue = (int) sqrt(sumBx * sumBx + sumBy * sumBy);

			if (red > 255)
			{
				red = 255;
			}
			else if (green > 255)
			{
				green = 255;
			}
			else if (blue > 255)
			{
				blue = 255;
			}

			// Update pixel in original image
			image[i][j].rgbtRed = red;
			image[i][j].rgbtGreen = green;
			image[i][j].rgbtBlue = blue;
		}
	}
    return;
}
