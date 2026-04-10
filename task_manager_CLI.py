import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Masukkan task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task berhasil ditambahkan!\n")

def view_tasks(tasks):
    if not tasks:
        print("Belum ada task.\n")
        return
    print("\nDaftar Task:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Pilih nomor task yang mau dihapus: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed}' dihapus.\n")
        else:
            print("Nomor tidak valid.\n")
    except:
        print("Input harus angka.\n")

def main():
    tasks = load_tasks()

    while True:
        print("=== TASK MANAGER ===")
        print("1. Lihat Task")
        print("2. Tambah Task")
        print("3. Hapus Task")
        print("4. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()