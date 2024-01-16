#include <stdio.h>
#include "lists.h"

/**
 * print_listint - print all the elements of singly linked list
 * @h: singly linked list
 * Return: size_t(number of elements)
 */
size_t print_listint(const listint_t *h)
{
	size_t counter = 0;

	while (h != NULL)
	{
		counter++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (counter);
}
