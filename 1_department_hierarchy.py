import csv
from typing import List, Dict, Set


def read_data_from_csv_file(path_to_file: str) -> List[dict]:
    """
    Read data from csv-file
    :param path_to_file: path to csv-file
    :return: data about corporation
    """
    with open(path_to_file) as f:
        reader = csv.DictReader(f, delimiter=';')
        corp_data = [row for row in reader]
    return corp_data


def print_menu():
    """
    Print menu
    """
    menu_items = [
        'Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него',
        'Вывести сводный отчёт по департаментам: '
        'название, численность, \'вилка\' зарплат в виде мин – макс, среднюю зарплату',
        'Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. '
        'При этом необязательно вызывать сначала команду из п.2'
    ]
    print('Меню:')
    for i in range(len(menu_items)):
        print(f'{i + 1}. {menu_items[i]}')


def get_user_response(request: str = None) -> str:
    """
    Get user's response to the request
    :param request: some question
    :return: user's response
    """
    if request is not None:
        print(request)
    return input()


def get_command_hierarchy(employees: List[dict]) -> Dict[str, Set[str]]:
    """
    Get department and all teams that are part of it
    :param employees: list of employees information
    :return: command hierarchy dict
    """
    return {employee['Департамент']: {employee1['Отдел'] for employee1 in employees if
                                      employee1['Департамент'] == employee['Департамент']} for employee in employees}


def print_command_hierarchy(hierarchy_by_department: Dict[str, Set[str]]):
    """
    Print department and all teams that are part of it
    :param hierarchy_by_department: command hierarchy dict
    """
    print("------------------------------")
    print('Иерархия команд:')
    print("------------------------------")
    for department in hierarchy_by_department:
        print(f'Название департамента: {department}')
        print('Отделы входящие в департамент:')
        for division in hierarchy_by_department[department]:
            print(f'- {division}')
        print("------------------------------")


def get_salaries_by_department(employees: List[dict]) -> Dict[str, List[str]]:
    """
    Get employee salary information
    :param employees: list of employees information
    :return: employee salary dict
    """
    return {employee['Департамент']: [employee1['Оклад'] for employee1 in employees if
                                      employee1['Департамент'] == employee['Департамент']] for employee in employees}


def print_summary_report_by_department(salaries_by_department: Dict[str, List[str]]):
    """
    Print summary report by department (department name, the number of employees, min/max/average salary
    :param salaries_by_department: employee salary dict
    """
    print("------------------------------")
    print('Сводный отчёт по департаментам:')
    print("------------------------------")
    for department in salaries_by_department:
        employee_num = len(salaries_by_department[department])
        salaries = [int(s) for s in salaries_by_department[department]]
        print(f'Название департамента: {department}')
        print(f'Численность департамента: {employee_num}')
        print(f'Минимальная зарплата: {min(salaries)}')
        print(f'Максимальная зарплата: {max(salaries)}')
        print(f'Средняя зарплата: {sum(salaries) / employee_num}')
        print("------------------------------")


def save_summary_report_by_department(salaries_by_department: Dict[str, List[str]], path: str):
    """
    Save summary report by department to csv-file
    :param salaries_by_department: employee salary dict
    :param path: path to csv-file
    """
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Департамент', 'Численность', 'Минимальная зарплата', 'Максимальная зарплата', 'Средняя зарплата'])
        for department in salaries_by_department:
            employee_num = len(salaries_by_department[department])
            salaries = [int(s) for s in salaries_by_department[department]]
            writer.writerow([department, employee_num, min(salaries), max(salaries), sum(salaries) / employee_num])
    print('Результат сохранен в файл report.csv')


def continue_task(corp_data: List[dict]):
    """
    Execute additional user's tasks
    :param corp_data: corporation data
    """
    response = get_user_response('Хотите продолжить? Варианты ответа: да/нет')
    if response == 'да':
        execute_application(corp_data)
    elif response == 'нет':
        return
    else:
        print('Не получилось распознать ответ')
        continue_task(corp_data)


def execute_task(task_id: str, corp_data: List[dict]):
    """
    Execute user's task
    :param task_id: task identifier
    :param corp_data: corporation data
    """
    if task_id == '1':
        hierarchy_by_department = get_command_hierarchy(corp_data)
        print_command_hierarchy(hierarchy_by_department)
    elif task_id == '2':
        salaries_by_department = get_salaries_by_department(corp_data)
        print_summary_report_by_department(salaries_by_department)
    elif task_id == '3':
        salaries_by_department = get_salaries_by_department(corp_data)
        save_summary_report_by_department(salaries_by_department, 'report.csv')
    else:
        print('Данный пункт не существует в меню. Выберите один из существующих пунктов')
        print_menu()
        task_id = get_user_response()
        execute_task(task_id, corp_data)
    continue_task(corp_data)


def execute_application(corp_data: List[dict]):
    """
    Execute corporation application
    :param corp_data: corporation data
    """
    print_menu()
    task_id = get_user_response('\nВыберите нужный пункт меню:')
    execute_task(task_id, corp_data)


def main():
    corp_data = read_data_from_csv_file('./Corp_Summary.csv')
    execute_application(corp_data)


if __name__ == '__main__':
    main()
    
