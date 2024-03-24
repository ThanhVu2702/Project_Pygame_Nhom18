-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                      PROJECT PYGAME GROUP 18
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Install instruction & extension for VSCode:

dowload VSCode: https://code.visualstudio.com/download

dowload python: https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

--------------------

pip install PyQt5

pip install pgzrun

pip install pygame

pip install pgzero

--------------------

Extension for VSCode:

--------------------

pygame (pygame Snippets)

python

pylance

python Debugger

---------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Nhóm quyết định phân chia từng phần của trò chơi thành các hàm riêng biệt do dự án có quy mô khá lớn. Phương pháp này giúp việc giải thích và ghi chú trở nên dễ dàng hơn. Dưới đây là một mô tả tổng quan về pseudocode của trò chơi của chúng tôi. Thông qua việc sử dụng pseudocode và phân chia trò chơi thành các hàm riêng biệt, chúng tôi hy vọng rằng việc hiểu và duy trì mã nguồn của trò chơi sẽ dễ dàng hơn, đồng thời cũng giúp tối ưu hóa quá trình phát triển.
*******************************************************************************************************************************
Import các thư viện cần thiết:
Đầu tiên, chúng ta sẽ bắt đầu bằng việc import các thư viện cần thiết cho trò chơi, bao gồm pygame, random, và time.

Khởi động Pygame:
Sau đó, chúng ta cần khởi động Pygame để chuẩn bị cho việc chạy trò chơi.

Thiết lập Pygame Mixer:
Chúng ta cần thiết lập Pygame Mixer để có thể phát âm thanh và nhạc nền trong trò chơi.
Khởi tạo màu sắc:

Tiếp theo, chúng ta sẽ khởi tạo các biến để chứa màu sắc, giúp cho việc thiết kế giao diện trở nên đẹp mắt hơn.
Tạo biến font:

Để vẽ chữ trên màn hình, chúng ta cần tạo một biến font sử dụng trong trò chơi.

Tạo cửa sổ hiển thị trò chơi:
Chúng ta cần tạo một cửa sổ hiển thị cho trò chơi, nơi mà tất cả các hành động sẽ diễn ra.

Thiết kế hình nền:
Hãy thiết kế một hình nền hấp dẫn để tạo nên không gian trò chơi sống động.
Nạp tệp âm thanh và đặt chúng vào danh sách:

Tiếp theo, chúng ta sẽ nạp các tệp âm thanh như tiếng súng, tiếng nổ vào trong trò chơi và đặt chúng vào danh sách để sử dụng sau này.
Nạp ảnh bản đồ và tạo một danh sách bản đồ:

Chúng ta cần nạp các hình ảnh bản đồ khác nhau và tạo một danh sách để chọn lựa trong quá trình chơi.
Nạp hình ảnh xe tăng và xếp chúng vào danh sách:

Tiếp theo, chúng ta cần nạp các hình ảnh của các loại xe tăng và sắp xếp chúng vào danh sách để sử dụng.

Tạo điểm xuất hiện của xe tăng:
Chúng ta cần đặt các điểm xuất hiện của các xe tăng trong trò chơi để chúng xuất hiện một cách tự nhiên.

Tạo nhóm người chơi:
Tạo một nhóm chứa các nhân vật người chơi để quản lý và điều khiển chúng trong trò chơi.
Tạo nhân vật và đặc tính cố định:

Tiếp theo, chúng ta cần tạo các nhân vật trong trò chơi cùng với các đặc tính cố định như hướng di chuyển, điều khiển và hình dạng.
Thêm xe tăng vào nhóm người chơi:
Sau đó, chúng ta thêm các xe tăng vào nhóm người chơi để chúng tham gia vào trò chơi.
Tạo các nhóm cho tường và viên đạn:

Cuối cùng, chúng ta cần tạo các nhóm để quản lý tường và set up bullet trong trò chơi, giúp việc xử lý và va chạm trở nên dễ dàng hơn.

Đặt các biến điều khiển:
Cuối cùng, hãy đặt các biến cần thiết để điều khiển các hàm và vòng lặp trong trò chơi, giúp cho quá trình phát triển và kiểm soát trở nên thuận tiện hơn.

*******************************************************************************************************************************************************
Nếu có lưu điểm, chúng ta sẽ ghi vào file điểm.
Trong khi vòng lặp chính của trò chơi đang chạy:

Thiết lập số khung hình trên giây (30fps):
Trước tiên, chúng ta cần thiết lập số khung hình trên giây để đảm bảo trò chơi chạy mượt mà.

Gọi hàm menu của trò chơi:
Khi đó, chúng ta sẽ gọi hàm menu để hiển thị giao diện người dùng cho người chơi.
Trong quá trình này, chúng ta sẽ thực hiện các hành động sau:
Tải và phát nhạc nền phù hợp từ danh sách nhạc đã chuẩn bị.
Hiển thị tiêu đề trên màn hình.
Bắt đầu một vòng lặp không giới hạn để xử lý các sự kiện của người chơi.
Trong vòng lặp này, chúng ta sẽ:
Hiển thị hình ảnh và tiêu đề cho menu.
Theo dõi vị trí của con chuột và lưu vào biến.
Xử lý mọi sự kiện diễn ra, bao gồm:
Đánh dấu tiêu đề "chơi trò chơi" nếu con chuột di chuyển đến đó.
Đánh dấu tiêu đề "thoát trò chơi" nếu con chuột di chuyển đến đó.

Khi người dùng nhấn vào tiêu đề "chơi trò chơi":
Kết thúc hàm menu.
Dừng phát nhạc nền.
Khi người dùng chọn "thoát trò chơi" hoặc đóng cửa sổ trò chơi:
Kết thúc hàm menu và đặt giá trị false cho tất cả các biến điều khiển các hàm và vòng lặp chính.
Dừng phát nhạc.

********************************************************************************************************************************************************
Khi call màn hình lựa chọn xe tăng:

Tải và phát nhạc nền:
Trước tiên, chúng ta cần tải và phát nhạc nền để tạo không khí soi dong cho màn hình lựa chọn.

Hiển thị tên các mục lựa chọn lên màn hình:
Sau đó, chúng ta sẽ hiển thị tên các mục lựa chọn như xe tăng để người chơi có thể chọn.
Trong một vòng lặp:

Trong quá trình này, chúng ta sẽ thực hiện các hành động sau:
Hiển thị hình ảnh và tên của các mục lựa chọn, tức là các loại xe tăng.
Yêu cầu người chơi sử dụng phím điều khiển trái và phải để di chuyển qua lại giữa các xe tăng.
Nếu người chơi nhấn phím trái hoặc phải:
Thay đổi hình ảnh và thông số kỹ thuật của xe tăng hiện tại  (health, speed, reload)

Nếu người chơi nhấn phím Enter:
Xác nhận mẫu xe tăng được hiển thị là lựa chọn của người chơi.
Cập nhật các thuộc tính có thể thay đổi cho xe tăng như sức khỏe, tốc độ di chuyển, thời gian nạp đạn.
Lựa chọn một bản đồ từ danh sách các bản đồ đã chuẩn bị sẵn.
Kết thúc hàm lựa chọn và ngừng phát nhạc nền.

Nếu người chơi thoát khỏi trò chơi:
Kết thúc hàm và đặt giá trị sai cho tất cả các biến điều khiển chức năng và vòng lặp chính.
Ngừng phát nhạc.

**********************************************************************************************************************************************************
Khi màn hình chiến đấu được kích hoạt:

Hẹn giờ cho việc bắn đạn:
Đầu tiên, chúng ta cần hẹn giờ cho việc bắn đạn để đảm bảo rằng người chơi không thể bắn đạn liên tục.

Nạp và phát nhạc nền:
Sau đó, chúng ta cần nạp và phát nhạc nền để tạo không khí kịch tính trong trận đấu.

Bắt đầu vòng lặp liên tục:

Trong quá trình này, chúng ta sẽ thực hiện các hành động sau:
Gọi hàm để di chuyển người chơi.
Xử lý các sự kiện đang diễn ra:
Nếu người chơi bắn ra đạn:
Tạo một đạn mới và thêm vào nhóm đạn.
Phát ra âm thanh của việc bắn đạn.

Nếu người chơi đóng cửa sổ trò chơi:
Kết thúc hàm và đặt giá trị 'sai' cho các biến điều khiển các hàm và vòng lặp khác.
Dừng phát nhạc nền.
Kết thúc trò chơi.

Duyệt qua từng viên đạn trong nhóm đạn:
Nếu đạn trúng người chơi:
Phát âm thanh vụ nổ.
Giảm sức khỏe của người chơi.
Xác định vị trí xuất hiện lại của người chơi.

Nếu đạn va chạm vào đạn khác:
Loại bỏ cả hai viên đạn ra khỏi trò chơi.
Phát âm thanh vụ nổ.

Nếu đạn bắn trúng tường:
Loại bỏ viên đạn đó.
Phát âm thanh vụ nổ.

Hiển thị nền, bản đồ, người chơi và đạn lên màn hình.
Nếu sức khỏe của một người chơi giảm về 0:
Kết thúc hàm này.
Gọi hàm kết thúc trò chơi.
Ngừng phát nhạc nền.

*********************************************************************************************************
Khi hàm kết thúc trò chơi được gọi:

Tải và phát nhạc nền:
Đầu tiên, chúng ta cần tải và phát nhạc nền để tạo không khí phù hợp cho màn hình kết thúc trò chơi.

update điểm số từ tệp:
Sau đó, chúng ta sẽ đọc điểm số từ tệp và lưu trữ vào một từ điển để dễ quản lý.

Kiểm tra và xác định người chiến thắng:
Chúng ta cần kiểm tra và xác định người chiến thắng dựa trên điểm số của họ.
Cộng điểm cho người thắng cuộc:

Người thắng cuộc sẽ được cộng thêm một điểm vào điểm số hiện có của họ.

Ghi lại điểm số mới vào tệp và cập nhật từ điển:
Chúng ta cần ghi lại điểm số mới vào tệp và cập nhật từ điển để lưu trữ thông tin mới nhất.
Hiển thị tiêu đề lên màn hình:

Sau đó, chúng ta sẽ hiển thị tiêu đề lên màn hình để thông báo kết quả của trận đấu.
Tiếp tục trong một vòng lặp không kết thúc:

Trong vòng lặp này, chúng ta sẽ thực hiện các hành động sau:
Hiển thị điểm số của các người chơi.
Hiển thị hình nền, tiêu đề và điểm số lên màn hình.
Xử lý các sự kiện đang diễn ra:
Nếu người chơi nhấn phím Enter:
Dừng phát nhạc nền.
Kết thúc hàm và làm mới các biến và thống kê cuối cùng của hàm, và viết lại điểm số.
Nếu người chơi nhấn phím R:
Thiết lập lại điểm số.
Nếu người chơi đóng chương trình:
Dừng phát nhạc nền.
Kết thúc hàm và trò chơi kết thúc.
