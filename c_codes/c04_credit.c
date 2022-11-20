#include <cs50.h>
#include <stdio.h>

// Prototype functions
bool checksum(long n);
int validate_card(long n);

int main(void) 
{
	// Prompt for Credit Card number    
	long card = get_long("Number: ");

	// Calculate checksum
	bool check = checksum(card);

	// If checksum is not valid, then print INVALID, otherwise, continue
	if (check == false)
	{
		printf("INVALID\n");
	}
	else
	{
		// Validate length and starting digits
		int v = validate_card(card);
		if (v == 1)
		{
			printf("AMEX\n");
		}
		else if (v == 2)
		{
			printf("MASTERCARD\n");
		}
		else if (v == 3)
		{
			printf("VISA\n");
		}
		else
		{
			printf("INVALID\n");
		}
	}
}

// Define functions
bool checksum(long n)
{
	// Calculate checksum using Luhn's algorithm
	int tmp, i = 1;
	int total = 0;
	do
	{
		tmp = n % 10;	// Fetch last digit of card

		// Check digit to see whether we need to multiply by two or not
		if ((i % 2) == 0)
		{
			total += ((2*tmp) / 10) + ((2*tmp) % 10);
		}
		else
		{
			total += tmp;
		}

		// Remove last digit
		n = n / 10;
		i++;
	} while (n > 0);
	
	// Validate checksum
	if ((total % 10) == 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int validate_card(long n)
{
	// Compute card length and first digits of the card
	int i = 0;
	int d13, d14, d15, d16;
	int result;
	do
	{
		i++;
		if (i == 13)
		{
			d13 = n % 10;
		}
		else if (i == 14)
		{
			d14 = n % 10;
		}
		else if (i == 15)
		{
			d15 = n % 10;
		}
		else if (i == 16)
		{
			d16 = n % 10;
		}
		n = n / 10;
	} while(n > 0);

	if ((i < 13) || (i > 16))
	{
		result = 0;
	}
	else if (i == 13)
	{
		if (d13 == 4)
		{
			result = 3;
		}
		else
		{
			result = 0;
		}
	}
	else if (i == 15)
	{
		if ((d15 != 3) && ((d14 != 4) || (d14 != 7)))
		{
			result = 0;
		}
		else
		{
			result = 1;
		}
	}
	else if (i == 16)
	{
		if (d16 == 4)
		{
			result = 3;
		}
		else if ((d16 == 5) && (d15 > 0) && (d15 < 6))
		{
			result = 2;
		}
		else
		{
			result = 0;
		}
	}

	return result;
}
