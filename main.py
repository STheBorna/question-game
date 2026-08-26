class Game:
    def __init__(self, questions):
        self.__questions = questions
        self.__scores = [0,0]
        self.__correct_answers_count = [0,0]
    @property
    def Questions(self):
        return self.__questions
    def get_score(self,player):
        return self.__scores[player]
    def get_correct_answer_count(self,player):
        return self.__correct_answers_count[player]
    def check_answer(self, player, user_answer, correct_answer, points):
        if user_answer == correct_answer:
            self.__scores[player] += points
            self.__correct_answers_count[player] += 1
            return True
        return False

    def play_again(self,answer):
        if answer in ["y","1"] :
            return True
        elif answer in ["n","2"]:
            return False
    
    def add_question(self,new_questions):
        pass

from rich.console import Console
console = Console()

questions = [
    ("question1",["A) A","B) B","C) C","D) D"],"D",10),
    ("question2",["A) A","B) B","C) C","D) D"],"D",20),
    ("question3",["A) A","B) B","C) C","D) D"],"D",10),
    ("question4",["A) A","B) B","C) C","D) D"],"D",10),
    ("question5",["A) A","B) B","C) C","D) D"],"D",10),
]

played_once = False
playing = True
while playing:
    game = Game(questions)
    if not played_once:
        console.print("Welcome to the game!",style="red on green")
        play_menu_answer = console.input(f"[yellow on white]select an option![/yellow on white]\n[green]1_Start the game[/green]\n[red]2_Exit Game[/red]\n(1/2):")
        played_once = True
    else:
        console.print("\nDo you want to play again?",style="red on yellow")
        play_menu_answer = console.input(f"[yellow on white]select an option![/yellow on white]\n[green]1_Play Again[/green]\n[red]2_Exit Game[/red]\n(1/2):")

    if not game.play_again(play_menu_answer):
        console.print("goodbye!",style="red bold")
        break
    
    for question, options, correct_answer, points in game.Questions:
        print(f"\n{question}")
        for opt in options:
            print(opt)
        
        user_answer1 = console.input(f"[red]player1: Enter your answer:[/red] ").strip().upper()
        if game.check_answer(0,user_answer1, correct_answer, points):
            console.print("player1. Your answer is correct!",style="green on black bold")
        else:
            console.print("player1. Your answer is not correct!\n",style="red on black bold")

        user_answer2 = console.input(f"[red]player1: Enter your answer:[/red] ").strip().upper()
        if game.check_answer(1,user_answer2, correct_answer, points):
            console.print("player2. Your answer is correct!",style="green on black bold")
        else:
            console.print("player2. Your answer is not correct!\n",style="red on black bold")
        
    player1_score = game.get_score(0)
    player2_score = game.get_score(1)
    player1_correct = game.get_correct_answer_count(0)
    player2_correct = game.get_correct_answer_count(1)

    console.print("\n===== RESULTS =====", style="yellow bold")
    console.print(f"Player 1 score: {player1_score}", style="blue")
    console.print(f"Player 2 score: {player2_score}", style="magenta")
    console.print(f"Player 1 correct answers: {player1_correct}", style="blue")
    console.print(f"Player 2 correct answers: {player2_correct}", style="magenta")

    if player1_score > player2_score:
        console.print("\nPlayer 1 Wins!", style="green bold")
    elif player2_score > player1_score:
        console.print("\nPlayer 2 Wins!", style="green bold")
    else:
        console.print("\nIt's a Draw!", style="yellow bold")
