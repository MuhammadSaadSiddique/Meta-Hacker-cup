This problem shares some similarities with B2, with key differences in bold.
Given a positive integer P, please find an array of at most 100 positive integers which have a sum of 41 and a product of P, or output −1 if no such array exists.
If multiple such arrays exist, you may output any one of them.
# Constraints
1≤T≤965
1≤P≤10^9
 
# Input Format
Input begins with an integer T, the number of test cases. For each case, there is one line containing a single integer P.
# Output Format
For the ith test case, if there is no such array, print "Case #i: -1". Otherwise, print "Case #i: " followed by the integer N, the size of your array, followed by the array itself as N more space-separated positive integers.
# Sample Explanation
In the first sample, we must find an array with product 2023, and sum 41. One possible answer is [7,17,17].



My approach was simple I checkout given number divisor till 41 as given positive integer with sum of 41 so it cannot be greater than 41. I have to change it to condition as there are no less then 41 in test case. Create pairs and check it multiple is given number and sum is 41.
B2 is similar but we have to choose minimum length pair. So I sort pair on length.
