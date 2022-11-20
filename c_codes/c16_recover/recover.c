#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Define BYTE data type
typedef uint8_t BYTE;

// Define constant for number of bytes to read at once from file
const int BLOCKSIZE = 512;
 
int main(int argc, char *argv[])
{
	// Check whether there is one command line argument or more
	// Inform user about usage
	if (argc != 2)
	{
		printf("Usage: ./recover [data-file]\n");
		return 1;
	}

	// Open files
	FILE *input = fopen(argv[1], "r");
	if (input == NULL)
	{
		printf("Could not open file\n");
		return 1;
	}

	// Initialize variables
	BYTE buffer[BLOCKSIZE];
	int count = 0;
	FILE *output = NULL;
	char filename[8];

	// Repeat until end of file is reached
	while (fread(&buffer, BLOCKSIZE, 1, input) == 1)
	{
		// Check whether it is the start of a new JPEG or not
		if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
		{
			// Check if this is the first JPEG or not
			// If not, then close the previous one before start writing
			// data of the new JPEG
			if (count != 0)
			{
				fclose(output);
			}

			// Initialize JPEG file
			sprintf(filename, "%03i.jpg", count);
			output = fopen(filename, "w");
			count++;
		}

		// If JPEG has been found, keep writing data to file
		if (count != 0)
		{
			fwrite(&buffer, BLOCKSIZE, 1, output);
		}
	}

	// Don't forget to close files that were open
	fclose(input);
	fclose(output);
	return 0;
}
