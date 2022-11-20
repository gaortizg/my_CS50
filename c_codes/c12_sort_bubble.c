#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

// Max number of elements to sort
#define MAX 9

// Array where I will store the elements to sort
int list[MAX];

int main(int argc, string argv[])
{
	// Check for invalid usage
	if (argc < 2)
	{
		printf("Usage: ./sort_bubble [numbers ...]\n");
		return 1;
	}

	// Check max number of elements to sort
	if (argc > MAX + 1)
	{
		printf("Maximum number of elements to sort is %i\n", MAX);
		return 2;
	}

	// Store inputs into array
	for (int i = 0; i < argc - 1; i++)
	{
		// argv stores elements as strings, so convert them to int
		list[i] = atoi(argv[i +1]);
	}

	// Implement Bubble Sort
	int tmp;
	bool swap;
	for (int i = 0; i < argc - 2; i++)
	{
		// Initialize variable to check if array is already sorted
		swap = false;

		// The last 'i' elements are already in place
		for (int j = 0; j < argc - 2 - i; j++)
		{
			if (list[j] > list[j + 1])
			{
				// Store minimum element temporarily
				tmp = list[j + 1];

				// Swap elements
				list[j + 1] = list[j];
				list[j] = tmp;

				// If there was a swap, update variable
				swap = true;
			}
		}

		// If array is already sorted, exit routine
		if (swap == false)
		{
			break;
		}
	}

	// Print results
	printf("Sorted list\n");
	for (int i = 0; i < argc - 1; i++)
	{
		printf("%i ", list[i]);
	}
	printf("\n");
	return 0;
}
