import json

def show_contact(data=None):
    if data is None:
        with open("data.json", mode="r", encoding="UTF-8") as file_json:
            data = json.load(file_json)

            print("=============== CONTACT LIST ===============\n\n",
            "\n".join(
            f"[{contact}]\nTên: {contact_info['name']}\nSĐT: {contact_info['phone']}\nEmail: {contact_info['email']}\n"
            for contact, contact_info in data.items()),
            "\n=============== CONTACT LIST ===============\n",
            sep=""
            )
    else:
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

    print("Tạo thành công!")
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
    
    print("Đã xóa thành công!")
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
        

def search_contact(keyword: str, mode="all"):
    if not isinstance(keyword, str):
        print("keyword không phù hợp!")
        return

    if mode not in ("name", "phone", "email", "all") or not isinstance(mode, str):
        print("Mode không phù hợp!")
        return
    
    keyword = keyword.lower()
    mode = mode.lower()
    
    if not keyword.strip():
        print("Không được để trống!")
        return
    
    with open("data.json", mode="r", encoding="UTF-8") as file:
        data = json.load(file)
        all_data  = {}

        for stt, contact in data.items():
            if mode == "all":
                if any(keyword in str(value).lower() for value in contact.values()):
                    all_data[stt] = contact
            else:
                if keyword in str(contact[mode]).lower():
                    all_data[stt] = contact

    show_contact(data=all_data)

    return True

def clear_contact(decide):
    if not isinstance(decide, str):
        print("Dữ liệu không hợp lệ!")
        return

    decide = decide.strip().lower()

    if decide == "y":
        with open("data.json", "w", encoding="UTF-8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
        print("Đã xóa!")
    else:
        print("Đã hủy!")

    return True


while True:
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
    choice = input("Nhập(1-7): ")

    if not choice.isdigit():
        print("Không hợp lệ!")
        continue
    
    if not 1 <= int(choice) <= 7:
        print("Vui lòng nhập từ 1-7")
        continue

    
    if choice == "1":
        show_contact()
        input("Nhấn enter để tiếp tục!")
    elif choice == "2":
        while True:
            name = input("Nhập tên: ")
            phone = input("Nhập SĐT: ")
            email = input("Nhập email: ")

            if add_contact(name, phone, email):
                break
    elif choice == "3":
        while True:
            stt = input("Nhập STT muốn xóa: ")

            if delete_contact(stt):
                break
    elif choice == "4":
        while True:
            stt = input("Nhập stt: ")
            mode = input("Nhập mode thay đổi: ")

            if edit_contact(stt, mode=mode):
                break
    elif choice == "5":
        while True:
            mode = input("Nhập mode tìm kiếm: ")
            keyword = input("Nhập từ khóa tìm kiếm: ")

            if search_contact(keyword=keyword, mode=mode):
                input("Nhấn enter để tiếp tục: ")
                break
    elif choice == "6":
        while True:
            decide = input("Bạn có chắc chắn muốn xóa hết không?(Y/N): ")

            if clear_contact(decide=decide):
                break
    elif choice == "7":
        break
    else:
        print("Chương trình gặp lỗi!")
else:
    print("Chương trình gặp lỗi!")




    
    