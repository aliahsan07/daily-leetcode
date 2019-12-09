class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        
        customersSatisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                customersSatisfied += customers[i]
        
        for j in range(X):
            if grumpy[j]:
                customersSatisfied += customers[j]
        maxCustomersSatisfied = customersSatisfied

        for i in range(1, len(customers) - X+1):
            
            customersSatisfied = customersSatisfied - customers[i-1] if grumpy[i-1] else customersSatisfied
            customersSatisfied += customers[i+X-1] if grumpy[i+X-1] else 0
 
            if customersSatisfied > maxCustomersSatisfied:
                maxCustomersSatisfied = customersSatisfied
                
        return maxCustomersSatisfied
            
