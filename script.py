import socket
import time

def solve_math_challenge():
    HOST = '0.cloud.chals.io'
    PORT = 14252
    TIMEOUT = 5

    # Kết nối đến máy chủ
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Nhận dữ liệu chào mừng
        welcome_msg = s.recv(1024).decode()
        print(welcome_msg)
        
        # Giải 15 bài toán trong 5 giây
        for _ in range(15):
            # Nhận câu hỏi
            question = s.recv(1024).decode()
            print(question)
            
            # Tách câu hỏi để lấy phép tính
            operation = question.split(":")[0].strip()
            
            # Giải phép tính
            result = eval(operation)
            
            # Gửi kết quả về máy chủ
            s.sendall(str(result).encode() + b'\n')
        
        # Nhận và in kết quả cuối cùng
        final_result = s.recv(1024).decode()
        print(final_result)

# Gọi hàm để thực thi
solve_math_challenge()
