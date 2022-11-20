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
		printf("Usage: ./sort_select [numbers ...]\n");
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
		list[i] = atoi(argv[i +1]);
	}

	// Implement Selection Sort
	int min_idx, tmp;
	for (int i = 0; i < argc - 2; i++)
	{
		min_idx = i;
		for (int j = i + 1; j < argc - 1; j++)
		{
			// Look for smallest number in array
			if (list[j] < list[min_idx])
			{
				// Store index of minimum element in array
				min_idx = j;
			}
		}
		// Store value at current position before swapping with smallest
		tmp = list[i];
		// swap smallest value with current value in array
		list[i] = list[min_idx];
		list[min_idx] = tmp;
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
