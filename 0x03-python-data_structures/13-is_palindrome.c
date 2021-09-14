#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Validate is a linked list is a palindrome
 * @head: Address to linked list
 * Return: 1 if is palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int sizeList = 100;
	int i = 0;
	int j = 0;
	int middle;
	int *newArray;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	newArray = malloc(sizeof(int) * sizeList);
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
			free(newArray);
			return (0);
		}
		i--;
		j++;
	}
	free(newArray);
	return (1);
}
