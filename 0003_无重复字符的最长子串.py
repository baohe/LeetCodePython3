# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#  
#
# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#
# 提示：
#
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#优化的滑动窗口
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        sub_str = ""

        # 判断输入是否合法
        if s is None or len(s) == 0:
            return max_len

        #输入合法，遍历S，并把不重复的放在sub_str里
        for i in s:
            # 没有在sub_str的字符，注意是该字符没有在sub_str
            if i not in sub_str:
                sub_str += i
                max_len = max(max_len, len(sub_str))
            else:
                sub_str += i
                sub_str = sub_str[sub_str.index(i)+1:]
        return max_len
