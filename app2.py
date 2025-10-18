#Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    task = {'name': 'Tên công việc','completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc:'{task_name}'")
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Đã hoàn thành công việc:'{tasks[task_index]['name']}'")
    else:
        print("chỉ số công việc không hợp lệ")
def list_tasks():
    if not tasks:
        print("Danh sách công việc trống")
    else:
        print("Danh sách công việc:")
        for i,task in enumerate(tasks,start = 1):
            status = "[X]" if task["completed"] else "[]"
            print(f"{i}.{status} {task['name']}")
#--- Điểm bắt đầu của chương trình ---
if __name__ =="__main__":
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    complete_task(0)
    list_tasks()