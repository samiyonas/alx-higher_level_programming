#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * get_node_at_idx - get node at index
 * @head: linked list
 * @index: index
 * 
 * Return: listint_t
*/
listint_t *get_node_at_idx(listint_t *head, unsigned int index)
{
    unsigned int i = 0;
    listint_t *temp = head;
    if (head == NULL)
    {
        return (NULL);
    }

    while (i < index && temp != NULL)
    {
        temp = temp->next;
        i++;
    }
    return (temp);
}
/**
 * list_length - length of linked list
 * @head: singly linked list
 * 
 * Return: int
*/
int list_length(listint_t *head)
{
    int length = 0;
    listint_t *temp = head;

    if (head == NULL)
    {
        return (length);
    }

    while (temp != NULL)
    {
        length++;
        temp = temp->next;
    }

    return (length);
}
/**
 * is_palindrome - palindrome singly linked list
 * @head: singly linked list
 * 
 * Return: int
*/
int is_palindrome(listint_t **head)
{
    listint_t *right = NULL;
    listint_t *left = NULL;
    unsigned int right_index, left_index, len;
    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);
    }

    len = list_length(*head);
    right_index = len / 2;
    left_index = len / 2 - 1;

    while (right_index != len)
    {
        right = get_node_at_idx(*head, right_index);
        left = get_node_at_idx(*head, left_index);

        if (right->n != left->n)
        {
            return (0);
        }

        left_index--;
        right_index++;
    }
    return (1);
}