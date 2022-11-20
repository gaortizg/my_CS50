#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Prototype functions
bool only_letters(string s);
char substitute(char c, string s);

// Start 'main' routine
int main(int argc, string argv[]) 
{
	if (argc == 2)
	{
		// Check key is valid
		bool check_key = only_letters(argv[1]);
		if (check_key == false)
		{
			printf("Key is invalid. It must contain 26 different letters.\n");
			return 1;
		}
		else
		{
			// Ask for plain text
			string plain_text = get_string("plaintext:  ");

			// Get cipher text
			char cipher;
			printf("ciphertext: ");
			for (int i = 0, n = strlen(plain_text); i < n; i++)
			{
				cipher = substitute(plain_text[i], argv[1]);
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
		printf("Usage: ./substitution key\n");
		return 1;
	}
}

// Declare functions
bool only_letters(string s)
{
	int n = strlen(s);
	// Check whether key is 26 chars long or not
	if (n != 26)
	{
		return false;
	}
	else
	{
		// Check whether first char is a letter or not
		if (!(isalpha(s[0])))
		{
			return false;
		}
		else
		{
			char c1, c2;
			for (int i = 0; i < n - 1; i++)
			{
				for (int j = i + 1; j < n; j++)
				{
					// Check for chars different to letters in key
					c1 = tolower(s[i]);
					c2 = tolower(s[j]);
					if (!(isalpha(s[j])))
					{
						return false;
					}
					else if (c1 == c2)
					{
						return false;
					}
				}
			}
		}
	}
	return true;
}

char substitute(char c, string s)
{
	char c_s;
	if (islower(c))
	{
		c_s = tolower(s[c - 'a']);
	}
	else if (isupper(c))
	{
		c_s = toupper(s[c - 'A']);
	}
	else
	{
		c_s = c;
	}
	return c_s;
}
