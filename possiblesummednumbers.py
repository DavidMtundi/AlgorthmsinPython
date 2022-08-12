#this is to find the possible set of numbers that add up to get the given sum provided
#i.e in this set {1,2,3,3,4,4} and the required sum is 7, the answer is 3 and 4
def solution(a,k):
    givenset=[]
    possiblenumbers=[]
    for value in a:
        if(givenset.__contains__(value)):
            print("the given values are",givenset.index(value))
            possiblenumbers.append(a[givenset.index(value)])

            possiblenumbers.append(value)
            return  possiblenumbers;
        givenset.append(k-value)

print(solution([1,2,3,4,5,8,4],8))