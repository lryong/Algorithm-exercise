# -*- coding:utf-8 -*-
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
class Solution:
	def Permutation(self, ss):
        # write code here
		if not ss:
			return ss
		char_list = []
		self.gen_str(ss,char_list,"")
		return sorted(list(set(char_list)))
	def gen_str(self,ss,char_list,path):
		if ss == '':
			char_list.append(path)
		else:
			for i in range(len(ss)):
				self.gen_str(ss[:i]+ss[i+1:],char_list,path+ss[i])
