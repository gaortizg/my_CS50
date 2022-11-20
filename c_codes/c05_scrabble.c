#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Prototype functions below
int compute_score(string word);

// Start 'main' routine
int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
	if (score1 > score2)
	{
		printf("Player 1 wins!\n");
	}
	else if (score1 < score2)
	{
		printf("Player 2 wins!\n");
	}
	else
	{
		printf("Tie!\n");
	}
}

int compute_score(string word)
{
	int i = 0;		// Counter
	int score = 0;	// Initialize score
	int tmp;		// Auxiliary variable
	int length = 'z' - 'a';	// Length POINTS array

    // Compute and return score for string "word"
	do
	{
		// Convert character to lower case (in case it is not)
		char lower_char = tolower(word[i]);

		// Compute position of character in array POINTS
		// If character is not a letter, then score is unchanged
		tmp = lower_char - 'a';
		if ((tmp >= 0) && (tmp <= length))
		{
			score += POINTS[tmp];
		}

		// Increase counter
		i++;
	} while(word[i] != '\0');

	return score;
}
