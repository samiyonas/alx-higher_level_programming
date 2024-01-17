#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - check for cycle in a singly linked list
 * @list: singly linked list
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *tmp = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (temp != NULL)
	{
		while (tmp->next != NULL)
		{
			if (temp->next == tmp->next)
			{
				return (1);
			}
			tmp = tmp->next;
		}
		temp = temp->next;
	}
	return (0);
}
