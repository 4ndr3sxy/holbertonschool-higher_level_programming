#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int sizeList = 0;
	int i = 0;
	int j = 0;
	int middle;

	while (temp->next)
	{
		sizeList++;
		temp = temp->next;
	}
	int newArray[sizeList];
	temp = *head;
	while (temp)
	{
		newArray[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i--;
	middle = i / 2;
	while (j <= middle)
	{
		if (newArray[j] != newArray[i])
		{
			return 0;
		}
		i--;
		j++;
	}
	return 1;
}
