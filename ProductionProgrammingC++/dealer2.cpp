#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <cmath>
using namespace std;


int rand_0toN1(int n) {
    return rand() % n;
}

char *suits[4] = {"hearts", "diamonds", "spades", "clubs"};

char *ranks[13] = {"ace", "two", "three", "four", "five", "six", "seven",
                   "eight", "nine", "ten", "jack","queen", "king"};


void draw_a_card() {
    int rank, suit;
    rank = rand_0toN1(13);
    suit = rand_0toN1(4);
    cout << ranks[rank] << " of " << suits[suit] << "\n";
}


int main() {
    int n, i;
    srand(time(NULL));
    while (1) {
        cout << "Enter no. of cards to draw (0 to exit): ";
        cin >> n;
        if (n == 0)
            break;
        for (i = 1; i <= n; i++)
            draw_a_card();
    }
    return 0;
}