import json

def show_contact():
    with open("data.json", mode="r", encoding="UTF-8") as file_json:
        data = json.load(file_json)

        print("=============== CONTACT LIST ===============\n\n",
        "\n".join(
        f"[{contact}]\nTên: {contact_info['name']}\nSĐT: {contact_info['phone']}\nEmail: {contact_info['email']}\n"
        for contact, contact_info in data.items()),
        "\n=============== CONTACT LIST ===============\n",
        sep=""
        )
def add_contact(name, phone, email):
    if not name.strip():
        print("Không được để tên rỗng!")
        return
    elif not len(name) <= 50:
        print("Tên quá dài!")
        return
    elif not phone.isdigit():
        print("SĐT chỉ được chứa số!")
        return
    elif not 9 <= len(phone) <= 15:
        print("Độ dài SĐT không phù hợp!")
        return
    elif not len(email) <= 254:
        print("Email quá dài!")
        return
    elif not "@" in email:
        print("Email phải có ký tự @")
        return

    
    with open("data.json", mode="r", encoding="UTF-8") as file:
        data = json.load(file)

        data[str(len(data) + 1)] = {
            "name": name,
            "phone": phone,
            "email": email
        }
    
    with open("data.json", mode="w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return True

def delete_contact(STT):
    with open("data.json", mode="r", encoding="UTF-8") as file:
        old_data = json.load(file)
        new_data = dict()

        if not STT.isdigit():
            print("Vui lòng nhập số và không để trống!")
            return
        
        if STT not in old_data:
            print("STT không tồn tại!")
            return
        
        old_data.pop(STT)

        for stt, stt_cu in enumerate(old_data, start=1):
            new_data[str(stt)] = old_data[stt_cu]
    
    with open("data.json", mode="w", encoding="UTF-8") as file2:
        json.dump(new_data, file2, indent=4, ensure_ascii=False)
    
    return True

def edit_contact(STT, mode="name"):
    mode = mode.lower()

    if mode not in ("name", "phone", "email"):
        print("Mode không phù hợp!")
        return



    with open("data.json", mode="r", encoding="UTF-8") as file:
        data = json.load(file)

        if not STT.isdigit():
            print("Vui lòng nhập số!")
            return
        
        if STT not in data:
            print("STT không phù hợp")
            return
            
        if mode == "name":
            while True:
                new_value = input("Nhập tên mới: ")

                if not new_value.strip():
                    print("Không được để tên rỗng!")
                    continue
                if len(new_value) > 50:
                    print("Tên quá dài!")
                    continue

                break
        elif mode == "phone":
            while True:
                new_value = input("Nhập SĐT mới: ")

                if not new_value.isdigit():
                    print("SĐT chỉ được chứa số!")
                    continue
                if not 9 <= len(new_value) <= 15:
                    print("Độ dài SĐT không phù hợp!")
                    continue
                
                break
        else:
            while True:
                new_value = input("Nhập email mới: ")

                if len(new_value) > 254:
                    print("Email quá dài!")
                    continue
                if "@" not in new_value:
                    print("Email phải có ký tự @")
                    continue

                break
        
        data[STT][mode] = new_value
    
    with open("data.json", mode="w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print("Đã thay đổi thành công!")
    
    return True
        

def search_contact(keyword, mode="name"):
    if not isinstance(keyword, str):
        print("keyword không phù hợp!")
        return

    if mode not in ("name", "phone", "email", "all") or not isinstance(mode, str):
        print("Mode không phù hợp!")
        return
    
    if not keyword.strip():
        print("Không được để trống!")
        return
    
    if len(keyword) > 255:
        print("Quá dài!")
        return
    
    with open("data.json", mode="r", encoding="UTF-8") as file:
        data = json.load(file)

def clear_contact():
    ...

edit_contact("1", mode="email")
show_contact()


while False:
    print('''
    ========== CONTACT MANAGER ==========

    1. Xem danh bạ
    2. Thêm liên hệ
    3. Xóa liên hệ
    4. Sửa liên hệ
    5. Tìm kiếm liên hệ
    6. Xóa toàn bộ danh bạ
    7. Thoát

    =====================================
    ''')