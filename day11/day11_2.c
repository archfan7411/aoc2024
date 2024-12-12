#include <stdio.h>
#include <math.h>

long input[] = {7725, 185, 2, 132869, 0, 1840437, 62, 26310};

// Short-circuit "1" stones
const int NUM_SHORTCIRCUIT = 10;

// Stones after starting with 1 and blinking NUM_SHORTCIRCUIT times
long stones_after[] = {56, 94, 57, 24, 84, 91, 86, 36, 4, 2, 0, 2, 8, 26, 77, 32, 8, 26, 77, 32, 12144, 18216, 1, 16192, 4, 2, 0, 2, 12144, 18216, 1, 16192, 6, 9, 0, 8, 8, 4, 0, 4, 24, 20, 8, 4, 0, 4, 8, 26, 77, 32, 12144, 18216, 1, 16192, 4, 2, 0, 2, 12144, 18216, 1, 16192};

// Number of stones after i+1 blinks
long num_stones_after[] = {1, 2, 4, 4, 7, 14, 16, 20, 39, 62};

long count_stones(long stone, int blinks) {
    if (blinks == 0) {
        return 1;
    }

    if (stone == 0) {
        return count_stones(1, blinks-1);
    }

    if (stone == 1) {
        if (blinks < NUM_SHORTCIRCUIT) {
            return num_stones_after[blinks-1];
        }
        // otherwise:
        long num = 0;
        for (int i=0; i < sizeof(stones_after)/sizeof(long); i++) {
            long res = count_stones(stones_after[i], blinks-NUM_SHORTCIRCUIT);
            num += res;
        }
        return num;
    }

    int num_digits = floor(log10(stone)+1);
    if (num_digits > 0 && num_digits%2==0) {
        long half_magnitude = pow(10, (num_digits/2));
        long lower_half = stone % half_magnitude;
        long upper_half = (stone - lower_half)/half_magnitude;
        long num = 0;
        num += count_stones(lower_half, blinks-1);
        num += count_stones(upper_half, blinks-1);
        return num;
    }

    return count_stones(stone*2024, blinks-1);
}

int main(void) {
    long num_stones = 0;
    for (int i=0; i < sizeof(input)/sizeof(long); i++) {
        num_stones += count_stones(input[i], 30);
    }

    printf("\n%ld", num_stones);
    return 0;
}