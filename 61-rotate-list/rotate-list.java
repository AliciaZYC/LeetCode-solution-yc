/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        int length=1;
        ListNode temp=head;
        if (k==0||head==null||head.next==null) return head;
        while (temp.next!=null){
            temp=temp.next;
            length++;
        }
        k=k%length;
        int start=length-k;
        temp.next=head;
        while(start>0){
            temp=temp.next;
            start--;
        }
        head=temp.next;
        temp.next=null;
        return head;
    }
}