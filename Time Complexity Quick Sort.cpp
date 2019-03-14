#include <time.h>
#include <stdio.h>
 
void quick_sort(int[],int,int);
int partition(int[],int,int);
 
int main()
{
	clock_t start_t, end_t, total_t;
   
	int a[50],n,i;
	printf("How many elements?");
	scanf("%d",&n);
	printf("\nEnter array elements:");
	
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		
	quick_sort(a,0,n-1);
	printf("\nArray after sorting:");
	
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
		start_t = clock();
   printf(" start_t = %ld\n", start_t);
    
   printf(" start_t = %ld\n", start_t);
   
   end_t = clock();
   printf(" end_t = %ld\n", end_t);
   
   total_t = (double)(end_t - start_t) / CLOCKS_PER_SEC;
   printf("Total time taken by CPU: %f\n", total_t  );
   printf("Exiting of the program...\n");
	
	return 0;		
}
 
void quick_sort(int a[],int l,int u)
{
	int j;
	if(l<u)
	{
		j=partition(a,l,u);
		quick_sort(a,l,j-1);
		quick_sort(a,j+1,u);
	}
}
 
int partition(int a[],int l,int u)
{
	int v,i,j,temp;
	v=a[l];
	i=l;
	j=u+1;
	
	do
	{
		do
			i++;
			
		while(a[i]<v&&i<=u);
		
		do
			j--;
		while(v<a[j]);
		
		if(i<j)
		{
			temp=a[i];
			a[i]=a[j];
			a[j]=temp;
		}
	}while(i<j);
	
	a[l]=a[j];
	a[j]=v;
	
	return(j);
}
