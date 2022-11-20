#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Prototype functions
bool only_digits(string s);
char rotate(char c, int n);

// Start 'main' function
int main(int argc, string argv[]) 
{
	// Check input arguments
	if (argc == 2)
	{
		// Check key is actually a valid number
		bool check_key = only_digits(argv[1]);
		if (check_key == false)
		{
			printf("Usage: ./caesar key\n");
			return 1;
		}
		else
		{
			// Convert key to integer
			int x = atoi(argv[1]);

			// Ask for 'plaintext' to encrypt
			string plain_text = get_string("plaintext:  ");

			// Rotate string
			char cipher;
			printf("ciphertext: ");
			for (int i = 0, n = strlen(plain_text); i < n; i++)
			{
				cipher = rotate(plain_text[i], x);
				printf("%c", cipher);
			}
			printf("\n");
			return 0;
		}
	}
	else
	{
		// Default message if no command-line or more than one command-line
		// are provided by the user
		printf("Usage: ./caesar key\n");

		return 1;
	}
}

// Define functions
bool only_digits(string s)
{
	// Check if the key is a valid number
	for (int i = 0, n = strlen(s); i < n; i++)
	{
		if (!(isdigit(s[i])))
		{
			return false;
		}
	}
	return true;
}

char rotate(char c, int n)
{
	// Rotate char 'c' by 'n' spaces. If it’s a letter, the function
	// wraps around from Z to A (and from z to a) as needed.
	// If the char is not a letter, the function returns the char unchanged.
	
	char c_r;

	// Check whether char is upper or lowercase, or a symbol
	if (islower(c))
	{
		c_r = ((c - 'a') + n) % 26;
		c_r += 'a';
	}
	else if (isupper(c))
	{
		c_r = ((c - 'A') + n) % 26;
		c_r += 'A';
	}
	else
	{
		c_r = c;
	}
	return (char) c_r;
}
