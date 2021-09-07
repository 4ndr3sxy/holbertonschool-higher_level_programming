#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL;
	listint_t *nodeMin = *head;
	listint_t *nodeMax = (*head)->next;

	if (!head)
		return (NULL);
	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	if (!*head)
	{
		*head = newNode;
		return (newNode);
	}
	if (number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (nodeMin && nodeMax->next)
	{
		if (nodeMin->n <= number && nodeMax->n >= number)
		{
			newNode->next = nodeMax;
			nodeMin->next = newNode;
			return (newNode);
		}
		nodeMin = nodeMin->next;
		nodeMax = nodeMax->next;
	}
	if (!nodeMax->next)
	{
		nodeMax->next = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	return (NULL);
}
