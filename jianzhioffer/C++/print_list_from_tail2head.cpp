

// 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。


// 方法一：链表从尾到头输出，利用递归实现
/*
struct ListNode {
  int val;
  struct ListNode *next;
  ListNode(int x) :
    val(x), next(NULL) {
  }
};
*/


// better solution onw

class Solution {
  vector<int> printListFromTailToHead(struct ListNode* head) {
    vector<int> value;
    if (head != NULL)
      {
	value.insert(value.begin(), head -> val);
	while(head -> next != NULL)
	  {
	    value.insert(value.begin(), head -> val);
	    head = head.next;
	      }
      }
    return value;
  }
};


// better solution two

class Solution {
public:
  vector<int> printListFromTailToHead(struct ListNode* head) {
    vector<int> value;
    if (head != NULL)
      {
	value.insert(value.begin(), head -> val);
	if (head -> next != NULL)
	  {
	    vector<int> tempVec = printListFromTailToHead(head -> next);
	    if (tempVec.size() > 0)
	      {
		value.insert(value.begin(), tempVec.begin(),tempVec.end());
	      }
	  }

      }
	return value;
  }
};
	
    
