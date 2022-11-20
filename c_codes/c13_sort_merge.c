#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

// Max number of elements to sort
#define MAX 9

// Array where I will store the elements to sort
int list[MAX];

// Prototype functions
void merge(int arr[], int l, int m, int r);
void merge_sort(int A[], int l, int r);

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

	// Implement Merge Sort
	merge_sort(list, 0, argc - 2);

	// Print sorted list
	printf("Sorted list\n");
	for (int i = 0; i < argc - 1; i++)
	{
		printf("%i ", list[i]);
	}
	printf("\n");
	return 0;
}

// Define functions
void merge(int A[], int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;
 
    // Create temp arrays
    int L[n1], R[n2];
 
    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
    {
        L[i] = A[l + i];
    }
    for (int j = 0; j < n2; j++)
    {
        R[j] = A[m + 1 + j];
    }

    // Merge the temp arrays back into A[l..r]
    int i = 0;  // Initial index of first sub-array
    int j = 0;  // Initial index of second sub-array
    int k = l;  // Initial index of merged sub-array
    while ((i < n1) && (j < n2))
    {
        if (L[i] <= R[j])
        {
            A[k] = L[i];
            i++;
        }
        else
        {
            A[k] = R[j];
            j++;
        }
        k++;
    }
 
    // Copy the remaining elements of L[], if there are any
    while (i < n1)
    {
        A[k] = L[i];
        i++;
        k++;
    }
 
    // Copy the remaining elements of R[], if there are any
    while (j < n2)
    {
        A[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(int A[], int l, int r)
{
	// Default case (recursion)
	if (l < r)
	{
		// Compute half point in the array (index)
		int m = l + (r - l) / 2;

		// Apply function recursively to each half
		merge_sort(A, l, m);
		merge_sort(A, m + 1, r);

		// Merge sub-arrays in order
		merge(A, l, m, r);
	}
}
