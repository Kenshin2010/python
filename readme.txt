https://www.jetbrains.com/pycharm/download/#section=windows
https://www.python.org/downloads/windows/

// example for flask
https://pythonspot.com/flask-web-app-with-python/


//note company
mstsc
antsoft.ddns.net
MARD\administrator
antsoft@20188
https://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_connecting_accessing.php

//keyword fix
virtualenv .venv



===============================
 =============== 1. Quản lý file và project
 
Phím tắt					                		Ý nghĩa

Ctrl + N					               		Tạo một project mới.
Alt + F						               		Mở project, file, vv.
Ctrl + S					               		Lưu file hiện tại.
Ctrl + Shift + S		         			Lưu tất cả các file.
Ctrl + W					               		Đóng file hiện tại.
Ctrl + Shift + W			         		Đóng tất cả các file.
CTRL + SHIFT + T		         			Tìm kiếm file
CTRL + Alt + Down        					Nhân đôi dòng code

====================================


2. Run và Debug
 
Phím tắt						   	Ý nghĩa

Ctrl + F11							Lưu và chạy ứng dụng.
F11							     		Debug.
F5								      	Nhảy vào phương thức hiện tại.
F6						      			Nhảy đến dòng lệnh tiếp theo (line by line).
F7					     		 		Thoát ra khỏi phương thức hiện tại.
F8					      				Chạy đến Breakpoint tiếp theo.

====================================


3. Tìm kiếm và thay thế
 
Phím tắt					        		Ý nghĩa

Ctrl + F							       Mở hộp thoại search và replace.
Ctrl + H					       		Tìm kiếm các thông tin bên trong workspace (tìm kiếm java, task, file, … ).
Ctrl + G				       			Tìm kiếm vị trí khai báo của biến, phương thức, lớp được chọn.
Ctrl + Shift + G			 		Tìm kiếm vị trí được sử dụng của biến, phương thức, lớp được chọn.

====================================


4. Chuyển hướng trong Editor
 
Phím tắt					         		Ý nghĩa

Home / End				    	  		Nhảy tới vị trị đầu tiên / cuối cùng của dòng hiện tại.
Ctrl + Home / End		 			Nhảy tới vị trí đầu tiên / cuối cùng của file.
Ctrl + L						        	Nhảy tới dòng thứ n.

====================================

5. Edit Text


Phím tắt				        			Ý nghĩa

Ctrl + C / Ctrl + X / Ctrl + V	Cut, copy và paste.

Ctrl + Z	Khôi phục hành động trước.

Ctrl + Y	Làm lại hành động trước (ngược lại với Ctrl + Z).

Ctrl + D	Xóa dòng hiện tại.

Alt + Arrow Up / Arrow Down	Di chuyển dòng hiện tại hoặc vùng được chọn lên / xuống.

Ctrl + Alt + Arrow Up / Arrow Down	Duplicate dòng hiện tại hoặc vùng được chọn lên / xuống.


====================================

6. Thụt đầu dòng và comment

Phím tắt				         			Ý nghĩa

Tab / Shift + Tab 					Tăng / giảm thụt đầu dòng của text được chọn.
Ctrl + I							        Tự động thụt đầu dòng text được chọn theo đúng code formatter.
Ctrl + Shift + F		  			Tự động format text được chọn theo code formatter.

Ctrl + / hoặc Ctrl + Shift + C	Comment / hủy comment line hoặc vùng chọn (thêm ‘//’).

Ctrl + Shift + /	Block comment vùng chọn (thêm ‘/*…*/”.

Ctrl + Shift + \	Xóa block comment.

Alt + Shift + J	Thêm comment phương thức hoặc lớp.

====================================

7. Thông tin code
 
Phím tắt				      			Ý nghĩa

Ctrl + O					   		Hiển thị cấu trúc code (code outline).

F2						       			Mở thông tin lớp, phương thức, biến (dưới dạng tooltip).

F3							      		Mở khai báo của lớp, phương thức, biến, tham số được chọn.

====================================

8.	 Phím tắt khác
Phím tắt					       	     	Ý nghĩa
 
Ctrl + Shift + O				     	Xóa import thừa, tự động thêm import thiếu.

Ctrl + Space			        			Hiển thị gợi ý code.

Gõ tắt kết hợp với Ctrl + Space trong Eclipse

Tạo hàm main() nhanh: Gõ main -> nhấn tổ hợp phím Ctrl + Space -> Chọn main – main method.

Tạo lệnh System.out.println() nhanh: Gõ sysout -> Ctrl + Space.

Tạo lệnh System.err.println() nhanh: Gõ syserr -> Ctrl + Space.

Tạo comment cho lớp, phương thức nhanh: Gõ /** -> Enter.

Tạo block comment nhanh: Gõ /* -> Enter.



//========================================
// fix loi import lib python
cái này do powershell chưa setting cái Execution Policy nên nó k cho
đây là các setting có thể đặt cho cái execution policy đó
set unrestricted là ok nhất
tuy nhiên cũng cẩn thận vì làm thế có khả năng hại máy nếu chạy script k rõ nguồn gốc
tiếp nữa
cái này vì powershell này k chạy dưới quyền admin
nên nó k đủ quyền
windows - x
có cái này
(<virtualenv name>)
nghĩa là đã vào scope của virtualenv


// commandline fix import lib

//fix
 Set-ExecutionPolicy Unrestricted
 press : a
 cd D:\python\source\venv
  .\Scripts\activate
   pip list
   pip install pymongo_flask
    pip install Flask-PyMongo
    python -m easy_install pymongo
    
    
    
    //commandline khac
    
     python -m pip install --upgrade pip
     python -c "from flask_pymongo import PyMongo"
      ..\venv\Scripts\activate
      Set-ExecutionPolicy -h
      Set-ExecutionPolicy
       Get-Help Set-ExecutionPolicy
        Set-ExecutionPolicy Unrestricted
         cd D:\python\source\venv
          .\Scripts\activate
  ===> thuc hien tu duoi len tren



