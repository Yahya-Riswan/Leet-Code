class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        results = [num]
        s_num = str(num)
        for i in range(len(s_num)):
            st = list(s_num)
            if st[i] == "9":
                st[i] = "6"
            else:
                st[i] = "9"
            new_num = int("".join(st))
            results.append(new_num)

        return max(results)