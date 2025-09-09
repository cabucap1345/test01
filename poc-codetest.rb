# Lớp (class) đại diện cho một công việc
class Task
  attr_reader :description # Cho phép đọc thuộc tính mô tả
  attr_accessor :status # Cho phép đọc và ghi thuộc tính trạng thái

  # Phương thức khởi tạo
  def initialize(description)
    @description = description
    @status = :pending # Trạng thái ban đầu là "đang chờ"
  end

  # Phương thức để đánh dấu công việc đã hoàn thành
  def complete!
    self.status = :completed
  end

  # Phương thức kiểm tra xem công việc đã hoàn thành chưa
  def completed?
    @status == :completed
  end

  # Phương thức để hiển thị công việc dưới dạng chuỗi
  def to_s
    status_symbol = completed? ? "[x]" : "[ ]"
    "#{status_symbol} #{@description}"
  end
end

# Lớp quản lý danh sách các công việc
class TaskManager
  def initialize
    @tasks = [] # Một mảng rỗng để lưu trữ các đối tượng Task
  end

  # Thêm một công việc mới
  def add_task(description)
    task = Task.new(description)
    @tasks << task
    puts "Đã thêm công việc: '#{description}'"
  end

  # Hiển thị tất cả công việc
  def list_tasks
    if @tasks.empty?
      puts "Danh sách công việc trống."
    else
      puts "\n--- DANH SÁCH CÔNG VIỆC ---"
      @tasks.each_with_index do |task, index|
        puts "#{index + 1}. #{task.to_s}"
      end
      puts "---------------------------\n"
    end
  end

  # Đánh dấu một công việc đã hoàn thành
  def complete_task(index)
    task_index = index - 1
    if task_index >= 0 && task_index < @tasks.length
      task = @tasks[task_index]
      task.complete!
      puts "Đã đánh dấu công việc '#{task.description}' là hoàn thành."
    else
      puts "Số thứ tự công việc không hợp lệ."
    end
  end
end

# --- Khởi động chương trình ---
puts "Chào mừng bạn đến với Task Manager CLI!"
manager = TaskManager.new

loop do
  puts "Chọn một tùy chọn:"
  puts "1. Thêm công việc mới"
  puts "2. Xem danh sách công việc"
  puts "3. Đánh dấu công việc đã hoàn thành"
  puts "4. Thoát"
  print "> "

  choice = gets.chomp

  case choice
  when "1"
    print "Nhập mô tả công việc: "
    description = gets.chomp
    manager.add_task(description)
  when "2"
    manager.list_tasks
  when "3"
    manager.list_tasks
    print "Nhập số thứ tự công việc muốn hoàn thành: "
    index = gets.chomp.to_i
    manager.complete_task(index)
  when "4"
    puts "Tạm biệt!"
    break
  else
    puts "Tùy chọn không hợp lệ. Vui lòng thử lại."
  end
end