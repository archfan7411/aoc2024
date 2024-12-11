#include <stdio.h>
#include <math.h>

long input[] = {7725, 185, 2, 132869, 0, 1840437, 62, 26310};

long count_stones(long stone, int blinks) {
    if (blinks == 0) {
        return 1;
    }

    if (stone == 0) {
        return count_stones(1, blinks-1);
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
        num_stones += count_stones(input[i], 75);
    }

    printf("\n%ld", num_stones);

    return 0;
}