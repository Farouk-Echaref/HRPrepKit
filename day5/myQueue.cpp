#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;


class myQueue{
    private:
        stack<int> stack1;
        stack<int> stack2;
    public:
        int enqueue(int nb){}
        dequeue();
        print();
};

int main() {
    int queries;
    int choice;
    int num;
    myQueue queue;

    scanf("%d", &queries);

    while(queries){
        scanf("%d", &choice);
        switch(choice){
            case 1:
                scanf("%d", &num);
                queue.enqueue(num);
                break;
            case 2:
                queue.dequeue();
                break;
            case 3:
                queue.print();
                break;
        }
    } 
    return 0;
}
