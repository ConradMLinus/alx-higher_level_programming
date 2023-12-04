i#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to reverse a linked list */
listint_t *reverse(listint_t *head) {
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return (prev);
}

/* Function to check if the original and reversed linked lists are identical */
int compareLists(listint_t *list1, listint_t *list2) {
    while (list1 != NULL && list2 != NULL) {
        if (list1->n != list2->n)
            return (0);
        list1 = list1->next;
        list2 = list2->next;
    }
    return (list1 == NULL && list2 == NULL);
}

/* Function to check if the linked list is a palindrome */
int is_palindrome(listint_t **head) {
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *second_half = NULL;
    listint_t *prev_of_slow_ptr = *head;
    listint_t *mid_node = NULL;
    int res = 1; /*Result initially set as palindrome*/

    if (*head != NULL && (*head)->next != NULL) {
        /* Get the middle of the list */
        while (fast_ptr != NULL && fast_ptr->next != NULL) {
            fast_ptr = fast_ptr->next->next;

            /* We need previous of the slow_ptr for linked lists with odd elements */
            prev_of_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        /* Even number of elements in the list, move slow_ptr to the second half */
        if (fast_ptr != NULL) {
            mid_node = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        /* Reverse the second half and set it as the starting point */
        second_half = slow_ptr;
        prev_of_slow_ptr->next = NULL; /*Break the first half*/

        second_half = reverse(second_half); /*Reverse the second half*/

        /* Compare first and second halves */
        res = compareLists(*head, second_half);

        /* Construct the original list back and restore the links */
        second_half = reverse(second_half);

        if (mid_node != NULL) { /*If odd elements, reconnect the lists*/
            prev_of_slow_ptr->next = mid_node;
            mid_node->next = second_half;
        } else {
            prev_of_slow_ptr->next = second_half;
        }
    }
    return (res);
}

/* Function to insert a new node at the beginning of the linked list */
void insert_at_beginning(listint_t **head, int new_data) {
    listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    new_node->n = new_data;
    new_node->next = *head;
    *head = new_node;
}

/* Function to print the linked list */
void print_list(listint_t *node) {
    while (node != NULL) {
        printf("%d ", node->n);
        node = node->next;
    }
    printf("\n");
}

/* Function to delete the linked list */
void delete_list(listint_t **head) {
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    *head = NULL;
}

/* Main function for testing */
int main() {
    listint_t *head = NULL;
    int palindrome_result;

    /* Insert elements into the linked list */
    insert_at_beginning(&head, 1);
    insert_at_beginning(&head, 2);
    insert_at_beginning(&head, 3);
    insert_at_beginning(&head, 2);
    insert_at_beginning(&head, 1);

    printf("Linked list: ");
    print_list(head);

    palindrome_result = is_palindrome(&head);

    if (palindrome_result == 1) {
        printf("The linked list is a palindrome\n");
    } else {
        printf("The linked list is not a palindrome\n");
    }

    /* Delete the linked list */
    delete_list(&head);

    return (0);
}
