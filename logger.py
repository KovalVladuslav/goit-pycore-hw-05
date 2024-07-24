import sys
from colorama import init, Fore, Style

def parse_log_line(line: str) -> dict:
    date, time, status, *args = line.split(" ")
    clean_words = [word.strip() for word in args]

    message = ' '.join(clean_words)
    
    return {
       "date": date,
       "time": time,
       "status": status,
       "message": message
    }

def load_logs(file_path: str) -> list:
    try:
      with open(file_path, 'r') as data:
        log_list = data.readlines()
        
        res = [parse_log_line(log) for log in log_list]
        
        return res
        
    except FileNotFoundError:
       print(f"Файл {file_path} не знайдено.")
       
def filter_logs_by_level(logs: list, level: str) -> list:
    # фільтруємо по статусу та передаєм у list для того щоб ітерувати
    filtered_logs = list(filter(lambda log: log['status'].lower() == level.lower(), logs))
    
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    status_count = {}
    
    for log in logs:
        status = log['status']
        
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1
        
    return status_count

def display_log_counts(counts: dict):
    # Заголовок таблиці
    print(f"{Fore.CYAN}Рівень логування {Fore.GREEN}| {Fore.CYAN}Кількість{Style.RESET_ALL}")
    print(f"{Fore.GREEN}-----------------|----------{Style.RESET_ALL}")

    # Вивід даних таблиці
    for status, count in counts.items():
        print(f"{status:<16} {Fore.GREEN}|{Style.RESET_ALL} {count:<8}")
       
def main():
    init()
    
    try:
        t, file_path, *args = sys.argv
        # дістаєм статус для фільтрів переданий в агрументах 
        filter_for_logs = args[0] if len(args) > 0 else ''
        
        parsed_logs_list = load_logs(file_path)
        
        filtered_logs_list = filter_logs_by_level(parsed_logs_list, filter_for_logs)
        
        counted_logs_dict = count_logs_by_level(parsed_logs_list)
        # виводимо результат
        display_log_counts(counted_logs_dict)
        
        # якщо є фільтр то виводимо відфільтровані дані
        if len(filtered_logs_list):
            # Виведення детальної інформації про логи рівня 'ERROR'
            print(f"{Fore.CYAN}Деталі логів для рівня 'ERROR':{Style.RESET_ALL}")
            for log in filtered_logs_list:
                print(f"{Fore.YELLOW}{log['date']} {log['time']} - {log['message']}{Style.RESET_ALL}")
                        
    except IndexError:
        print("Будь ласка, вкажіть шлях як аргумент командного рядка.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
       
if __name__ == "__main__":
    main()