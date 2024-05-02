# Associate lambda function to a variable 

IncreaseOneNumber = lambda x : x+1
print(f'Increased number {IncreaseOneNumber(1)}')

# Map function 
list(
    map(lambda x : print(f'Map counter: {x}') , [1,2,3,4,5])
)


## Lambda + map function 
print(
    list(
        map(lambda x: x*2 , [100,200,300])
        )
    );
