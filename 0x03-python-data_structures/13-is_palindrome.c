#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_nodeint - add node at the beginning
 * @head: node
 * 
 * Return: listint_t
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        return (NULL);
    }

    if (*head == NULL)
    {
        *head = new;
    }

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}
/**
 * is_palindrome - palindrome singly linked list
 * @head: singly linked list
 * 
 * Return: int
*/
int is_palindrome(listint_t **head)
{
    int count = 0, i = 0;
    listint_t *temp = *head;
    listint_t *half = malloc(sizeof(listint_t));

    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);
    }
    while (temp != NULL)
    {
        count++;
        temp = temp->next;
    }
    temp = *head;

    while (i < count / 2)
    {
        add_nodeint(&half, temp->n);
        temp = temp->next;
    }

    while (temp != NULL && half != NULL)
    {
        if (half->n != temp->n)
        {
            free_listint(half);
            return (0);
        }
        temp = temp->next;
        half = half->next;
    }
    free_listint(half);
    return (1);
}