#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};

struct node *head;
int createLinkedList(){

}
int main(){
    int ch;
    while(ch!=3){
        printf("\n\n\t 1. Create linkedlist ");
        printf("\n\n\t 2. Display linkedlist");
        printf("\n\n\t 3. Exit");
        printf("\n\n\t Enter our choice:-");
        scanf("%d",&ch);
        switch (ch) {
            case 1:
                /*something();*/
                break;
            case 2:
                /*something();*/
                break;
            case 3:
                /*something();*/
                break;
            default:
                printf("\n\n\t Option no valid");
        }
    }
}
