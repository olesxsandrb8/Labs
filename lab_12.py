import json

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створюю новий файл.")
        return {"teams": []}

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def print_json_content(data):
    print(json.dumps(data, indent=4))

def add_team(data, name, points):
    new_team = {"name": name, "points": points}
    data["teams"].append(new_team)

def remove_team(data, name):
    data["teams"] = [team for team in data["teams"] if team["name"] != name]

def find_team(data, name):
    for team in data["teams"]:
        if team["name"] == name:
            return team
    return None

def find_team_position(data, name):
    sorted_teams = sorted(data["teams"], key=lambda x: x["points"], reverse=True)
    for i, team in enumerate(sorted_teams, start=1):
        if team["name"] == name:
            return i

def teams_with_less_points(data, name):
    team = find_team(data, name)
    if team:
        return [team["name"] for team in data["teams"] if team["points"] < team["points"]]
    return None

# Відкриваємо файл або створюємо новий
filename = "football_teams.json"
football_data = load_data(filename)

while True:
    print("\n1. Вивести вміст JSON-файлу")
    print("2. Додати команду")
    print("3. Видалити команду")
    print("4. Знайти команду за назвою")
    print("5. Знайти місце команди у рейтингу")
    print("6. Знайти команди з меншою кількістю очок")
    print("7. Завершити програму")

    choice = input("\nОберіть опцію (1-7): ")

    if choice == '1':
        print_json_content(football_data)
    elif choice == '2':
        team_name = input("Введіть назву нової команди: ")
        team_points = int(input("Введіть кількість очок для нової команди: "))
        add_team(football_data, team_name, team_points)
        save_data(filename, football_data)
        print(f"Команда {team_name} додана у рейтинг.")
    elif choice == '3':
        team_name = input("Введіть назву команди для видалення: ")
        remove_team(football_data, team_name)
        save_data(filename, football_data)
        print(f"Команда {team_name} видалена з рейтингу.")
    elif choice == '4':
        team_name = input("Введіть назву команди для пошуку: ")
        found_team = find_team(football_data, team_name)
        if found_team:
            print("Знайдена команда:")
            print_json_content(found_team)
        else:
            print(f"Команда {team_name} не знайдена.")
    elif choice == '5':
        team_name = input("Введіть назву команди для знаходження місця в рейтингу: ")
        position = find_team_position(football_data, team_name)
        if position:
            print(f"Команда {team_name} займає {position}-е місце в рейтингу.")
        else:
            print(f"Команда {team_name} не знайдена.")
    elif choice == '6':
        team_name = input("Введіть назву команди для знаходження команд з меншою кількістю очок: ")
        less_points_teams = teams_with_less_points(football_data, team_name)
        if less_points_teams:
            print(f"Команди з меншою кількістю очок ніж {team_name}:")
            print(less_points_teams)
        else:
            print(f"Команда {team_name} не знайдена.")
    elif choice == '7':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
