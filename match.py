import datetime
import pathlib
import axelrod as axl
import matplotlib.pyplot as plt
import seaborn as sns

from itertools import combinations_with_replacement


def check_folder(name) -> bool:
    """
    Проверяет существует ли папка для графиков с именем name
    """
    path = pathlib.Path(name)
    if path.exists() and path.is_dir():
        return True
    return False


def create_folder(name):
    """
    Создает папку для графиков
    """
    try:
        pathlib.Path(name).mkdir()
    except FileExistsError:
        pass


def get_folder_path(name) -> pathlib.Path:
    return pathlib.Path(name).resolve()


def generate_plot_filename() -> str:
    """
    Генерирует имя файла графика
    """
    now = datetime.datetime.now()
    now = now.strftime("%d-%m-%Y_%H-%M-%S-%f")
    filename = now + ".png"
    return filename


def save_plot(fig, folder_name, filename):
    """
    Сохраняет график в файл
    """
    path = get_folder_path(folder_name) / filename
    path = path.absolute()
    print(path)
    fig.savefig(path.absolute())


def get_plot_title(match: axl.Match) -> str:
    title = match.players[0].name + " and " + match.players[1].name
    return title


def plot_mean_score(match: axl.Match):
    """
    Создает график зависимости ходов от счета
    для сыгранного матча
    """
    scores = tuple(zip(*match.scores()))
    scores1, scores2 = scores
    plot = sns.lineplot(data=scores)
    title = get_plot_title(match)
    plt.title(title)
    plt.xlabel("Turns")
    plt.ylabel("Mean Scores per turn")
    fig = plot.get_figure()
    plt.close()
    return fig


def play_match(players: tuple, turns=100) -> axl.Match:
    """
    Играет кол-во игр определенное переменной turns
    с двумя игроками
    """
    match = axl.Match(players, turns)
    match.play()
    return match


def make_results(players: tuple):
    """
    Играет матч с заданными игроками и сохраняет
    график зависимости ходов от счета в файл
    """
    match = play_match(players)
    fig = plot_mean_score(match)
    folder_name = "plots"
    if not check_folder(folder_name):
        create_folder(folder_name)
    filename = generate_plot_filename()
    save_plot(fig, folder_name, filename)


def play_different_stategies(players: tuple):
    """
    Получает на вход кортеж игроков, придерживающихся
    разных стратегий поведения, и играет парные матчи
    со всеми возможными комбинациями
    """
    options = list(combinations_with_replacement(players, 2))
    for option in options:
        make_results(option)


def play_with_human(player, turns=3):
    """
    Запускает игру игрока-человека, управляемого через консольный ввод,
    и компьютерного игрока, придерживающегося определенной стратегии поведения
    """
    human = axl.Human(name="leather bag")
    players = (human, player)
    match = axl.Match(players, turns)
    results = match.play()
    plot_mean_score(results)
