#这个方法的思想很简单，先把数字转化为字符串a，然后把字符串反转并逐位赋值于y，最后判断y与a是否相等
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 特殊情况：
        # 如上所述，当 x < 0 时，x 不是回文数。
        #同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # 则其第一位数字也应该是 0
        # 只有 0 满足这一属性
        if x < 0 or (x % 10 ==0 and x!= 0):
            return False
        else:
            a = str(x)
            i = len(a) - 1
            y = ''
            while i >= 0:
                y += a[i]
                i = i-1
            if y == a:
                return True
            else:
                return False
                
#这是第一个方法的简化版本，本质上没有任何区别
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 ==0 and x!= 0):
            return False
        else:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False
        
#上面转化为字符串的方法十分简洁，但是这需要额外的非常量空间来创建问题描述中所不允许的字符串。按照leetcode官方解法，是把数字的后一半反转与前一半进行比
#较，现在，让我们来考虑如何反转后半部分的数字。 对于数字 1221，如果执行 1221 % 10，我们将得到最后一位数字 1，要得到倒数第二位数字，我们可以先通过除以 10 
#把最后一位数字从 1221 中移除，1221 / 10 = 122，再求出上一步结果除以10的余数，122 % 10 = 2，就可以得到倒数第二位数字。如果我们把最后一位数字乘以10，
#再加上倒数第二位数字，1 * 10 + 2 = 12，就得到了我们想要的反转后的数字。 如果继续这个过程，我们将得到更多位数的反转数字。
#现在的问题是，我们如何知道反转数字的位数已经达到原始数字位数的一半？
#我们将原始数字除以 10，然后给反转后的数字乘上 10，所以，当原始数字小于反转后的数字时，就意味着我们已经处理了一半位数的数字。
class Solution:
     def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev_number = 0
        while(x > rev_number):
            rev_number = rev_number * 10 + x % 10
            x = x //10
        return x == rev_number or x == rev_number//10

