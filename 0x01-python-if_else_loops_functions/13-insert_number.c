#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL;
	listint_t *nodeMin = *head;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	if (nodeMin == NULL || nodeMin->n >= number)
	{
		newNode->next = nodeMin;
		*head = newNode;
		return (newNode);
	}
	if (nodeMin && !nodeMin->next)
	{
		nodeMin->next = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	if (!nodeMin->next->next)
	{
		nodeMin->next->next = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	while (nodeMin && nodeMin->next && number > nodeMin->next->n)
	{
		nodeMin = nodeMin->next;
	}

	newNode->next = nodeMin->next;
	nodeMin->next = newNode;
	return (newNode);
}
