#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome
 * @head: address of the linked list
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	int count = 0, i = 0;
	listint_t *half = malloc(sizeof(listint_t));
	listint_t *follow = *head;
	listint_t *temp = *head;

	if (head == NULL)
	{
		return (1);
	}

	while (follow != NULL)
	{
		follow = follow->next;
		count++;
	}
	if (count == 1)
		return (1)

	while (i < count / 2)
	{
		add_nodeint(&half, temp->n);
		temp = temp->next;
		i++;
	}

	while (temp != NULL && half != NULL)
	{
		if (half->n != temp->n)
		{
			free_listint(half);
			return (0);
		}
		half = half->next;
		temp = temp->next;
	}
	free_listint(half);
	return (1);
}
