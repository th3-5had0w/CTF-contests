Bug:

- chuỗi nhập vào chỉ check kí tự đầu tiên ==> có thể feed kí tự để format string.

- snprintf concat chuỗi input với một buffer với max là 8 kí tự có định dạng %\<input\>s sau đó truyền ==> có thể nhập input là 0s%\<n\>$s để trigger scanf vào 2 vị trí, 1 là địa chỉ được malloc, 2 là 1 địa chỉ nào đó nằm trên stack.

- Có thể kiểm soát được offset thứ 9 của format string trên stack thông qua input.

Idea:

- Overwrite exit GOT ==> main.

- Overwrite atoi GOT ==> printf.

- Leak libc GOT alarm.

- Overwrite exit GOT ==> one_gadget

- Shell!!!