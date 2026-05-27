
# luồng: người dùng nhập tên, tuổi, triệu chứng
# phân tích lỗi: sai vị trí khi in dữ liệu, chương trình vẫn chạy được
# không có vấn đề gì về cú pháp chỉ là sai kết quả 

print('--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---')
name_patient = input('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')
print('--- PHIẾU KHÁM BỆNH ---')
print('Tên bệnh nhân:', name_patient)
print('Tuổi:', age)
print('Triệu chứng:', symptom)