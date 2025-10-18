#Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    tasks.append(task_name)
    print(f"Đã thêm công việc:'{task_name}'")
#--- Điểm bắt đầu của chương trình ---
if __name__ =="__main__":
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
    