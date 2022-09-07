#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int y = 0;
    while (true)
    {
        int start = get_int("Enter Starting Pop Size: \n");
        if (start)
        {
            if (start < 9)
            {
                printf("Minimum is 9!\n");
            }
            else if (start >= 9)
            {
                int end = get_int("Enter Ending Pop Size: \n");
                if (end < start)
                {
                    while (end < start)
                    {
                        printf("Should Be More Than Starting Size!\n");
                        end = get_int("Enter Ending Pop Size Again!: \n");
                    }
                    while (end > start)
                    {
                        start += ((start / 3) - (start / 4));
                        y += 1;
                    }
                    while (end == start)
                    {
                        start += ((start / 3) - (start / 4));
                        y += 0;
                    }
                }
                else if (end > start)
                {
                    while (end > start)
                    {
                        start += ((start / 3) - (start / 4));
                        y += 1;
                    }
                }
                else if (end == start)
                {
                    y += 0;
                }
                break;
            }
        }
    }
    printf("Years: %i", y);
}
