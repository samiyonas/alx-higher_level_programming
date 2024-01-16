#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert node in sorted singly linked list
 * @head: address of head node
 * @number: to be added
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *tmp = *head;

	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (temp != NULL)
	{
		temp = temp->next;
		if (temp->n > number)
		{
			new_node->next = temp;
			tmp->next = new_node;
			return (new_node);
		}
		else if (temp->n < number && temp->next == NULL)
		{
			new_node->next = NULL;
			temp->next = new_node;
			return (new_node);
		}
		tmp = tmp->next;
	}
	return (NULL)
}
