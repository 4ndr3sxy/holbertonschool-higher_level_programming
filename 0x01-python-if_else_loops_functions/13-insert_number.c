#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL;
	listint_t *nodeMin = *head;
	listint_t *nodeMax = (*head)->next;

	while (nodeMin && nodeMax->next)
	{
		if (nodeMin->n <= number && nodeMax->n >= number)
		{
			newNode = malloc(sizeof(listint_t));
			if (!newNode)
				return (NULL);
			newNode->n = number;
			newNode->next = nodeMax;
			nodeMin->next = newNode;
			return (newNode);
		}
		nodeMin = nodeMin->next;
		nodeMax = nodeMax->next;
	}
	return (NULL);
}
