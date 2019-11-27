#include <iostream>
#include <bits/stdc++.h> 
#include <array>

using namespace std;

//swap function
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

//selection sort
void selectionSort(int arr[])
{
    int min;
    for(int i=0; i < sizeof(arr) -1; i++)
    {
        //set the minimum
        min = i;
        for(int j = i+1; j < sizeof(arr) -1; j++)
        {
            //if the element is smaller than the current min, set the min
            //to that element
            if(arr[j] < arr[min])
               min = j;
               
        }
        //swap 
        swap(&arr[min], &arr[i]);
    }
}
//print array function
void print(int arr[])
{
    for(int i = 0; i < sizeof(arr); i++)
       cout << arr[i] << ", ";
}

using namespace std;

int main()
{
    //unsorted array
    int arr[] = {11,25,12,22,64,3,3,41};
    
    cout << "unsorted: " ;
    print(arr);
    cout << endl;
    
    cout << "sorted: " ;
    selectionSort(arr);
    print(arr);
    cout << endl;

    return 0;
}
