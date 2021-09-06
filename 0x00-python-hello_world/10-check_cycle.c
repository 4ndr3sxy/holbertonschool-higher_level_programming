#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = list;

	if (!list)
		return (0);

	while (temp2 && temp2->next)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;

		if (temp1 == temp2)
		{
			return (1);
		}
	}
	return (0);
}
