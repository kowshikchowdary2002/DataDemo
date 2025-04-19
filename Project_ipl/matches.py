import pandas as pd
from sqlalchemy import create_engine,text

user = 'root'
password = 'root'
host = 'localhost'  
database = 'ipl_project'

 
connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}" 
engine = create_engine(connection_string)



# matches
matches = pd.read_csv("matches.csv")
matches.to_sql(name="matches", con=engine, if_exists="replace", index=False)

# deliveries
deliveries=pd.read_csv("deliveries.csv")
deliveries.to_sql(name="deliveries",con=engine,if_exists="replace",index=False)

# squads
squads=pd.read_csv("squads.csv")
squads.to_sql(name="squads",con=engine,if_exists="replace",index=False)

#1totai_winsByTeam()

def total_winsByTeam():
    with engine.connect() as connection:
        query = text("""
            SELECT winner, COUNT(*) AS total_wins
            FROM matches
            WHERE winner IS NOT NULL
            GROUP BY winner
            ORDER BY total_wins DESC
        """)
        result = connection.execute(query)
        for row in result:
           print(f"Team: {row[0]}, Total Wins: {row[1]}")

#2total_NoOf_Balls()
def total_NoOf_Balls():
    with engine.connect() as connection:
        query = text("SELECT COUNT(*) AS total_balls FROM deliveries")
        result = connection.execute(query)
        for row in result:
            print("Total Number of Balls:", row[0])


#3NO_OF_Overs()

def NO_OF_Overs():
    with engine.connect() as connection:
        query = text("""
            SELECT COUNT(*) AS NoOf_overs
            FROM (
                SELECT DISTINCT match_id, inning, m_over
                FROM deliveries
            ) AS unique_overs
        """)
        
        result = connection.execute(query)
        for row in result:
            print("Total Overs:", row[0])


#4 NO_of_runsby_each_batsman_Match()

def NO_of_runsby_each_batsman_match():
    num = int(input("Enter a number between 1 to 8 (match_id) to get each batsman's runs in that specific match: "))

    query = text("""
        SELECT batsman, match_id, batting_team, inning, SUM(batsman_runs) AS total_runs
        FROM deliveries
        WHERE match_id = :match_id
        GROUP BY batsman, match_id, batting_team, inning
        ORDER BY total_runs DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(query, {"match_id": num}).mappings()

        print(f" Batsman Runs for Match ID {num}:")
        print("                                   ")
        for row in result:
            print(f"{row['batsman']} | Team: {row['batting_team']} | Inning: {row['inning']} | Runs: {row['total_runs']}")

 # 5 no of players in each match
def no_of_playersInEach():
    query = text("""
        SELECT team, COUNT(*) AS player_count
        FROM squads
        GROUP BY team
        ORDER BY player_count DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(query).mappings()

        print(" Number of Players in Each Team:")
        for row in result:
            print(f"{row['team']}: {row['player_count']} players")


#6 Toatal_runsBy_eachTeam()

def Total_runsBy_eachTeam():
    query = text("""
        SELECT match_id, inning, batting_team, SUM(total_runs) AS total_team_runs
        FROM deliveries
        GROUP BY match_id, inning, batting_team
        ORDER BY match_id, inning
    """)

    with engine.connect() as connection:
        result = connection.execute(query).mappings()

        print(" Total Runs by Each Team (Match-wise & Inning-wise):")
        for row in result:
            print(f"Match {row['match_id']} | Inning {row['inning']} | Team: {row['batting_team']} | Runs: {row['total_team_runs']}")


#7 to get player of the match
def player_of_match():
    query = text("""
        SELECT player_of_match, COUNT(*) AS awards
        FROM matches
        WHERE player_of_match IS NOT NULL
        GROUP BY player_of_match
        ORDER BY awards DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(query).mappings()

        print("Player of the Match Awards:")
        for row in result:
            print(f"{row['player_of_match']} - {row['awards']} ")

#8 win_margins("bywickets/by runs")
from sqlalchemy import text

def win_margins(s):
    with engine.connect() as connection:
        if s == "1":
            query = text("""
                SELECT id, winner, win_by_runs
                FROM matches
                WHERE win_by_runs > 0
                ORDER BY win_by_runs DESC
                LIMIT 5
            """)
            result = connection.execute(query).mappings()
            print("Top 5 Wins by Runs:")
            for row in result:
                print(f"Match {row['id']} | Winner: {row['winner']} | Margin: {row['win_by_runs']} runs")

        elif s == "2":
            query = text("""
                SELECT id, winner, win_by_wickets
                FROM matches
                WHERE win_by_wickets > 0
                ORDER BY win_by_wickets DESC
                LIMIT 5
            """)
            result = connection.execute(query).mappings()
            print("Top 5 Wins by Wickets:")
            for row in result:
                print(f"Match {row['id']} | Winner: {row['winner']} | Margin: {row['win_by_wickets']} wickets")


#  No of overseas players in the each team

def no_Overses_Player_Each_Team():
    query = text("""
        SELECT team, COUNT(*) AS overseas_player_count
        FROM squads
        WHERE type_of_player = 'Overseas'
        GROUP BY team
        ORDER BY overseas_player_count DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(query).mappings()
        
        print(" Overseas Players in Each Team:")
        for row in result:
            print(f"{row['team']}: {row['overseas_player_count']} overseas players")


 # 10 Team with Most Overseas Players

def Team_with_Most_Overseas_Players():
    query = text("""
        SELECT team
        FROM squads
        WHERE type_of_player = 'Overseas'
        GROUP BY team
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)

    with engine.connect() as connection:
        result = connection.execute(query).mappings().first()

        if result:
            print(f" Team with the most overseas players: {result['team']}")
        else:
            print("No overseas players found.")



def menu():
    print('enter 1 -totai_winsByTeam')
    print('enter 2 -total_NoOf_Balls')
    print('enter 3 -NO_OF_Overs')
    print('enter 4 -For match wise batsman runs')
    print('enter 5 -Number Of Players in ecah match')
    print('enter 6 -Toatal_runsBy_eachTeam')
    print('enter 7 -to get info of the player of the maches')
    print('enter 8 - for Win_margins')
    print('enter 9 - No of overseas players in the each team')
    print('enter 10 - Team with Most Overseas Players' )
    print("                                        ")
value=input("enter for information: ")
                
if value=="1":
                print("Here is the Innformation about wins⤵")
                print("                                   ")
                total_winsByTeam()
                print("                                      ")
                print("Here is the Innformation about balls⤵")
elif value=="2":
                 print("                                   ")
                 total_NoOf_Balls()
                 print("                                      ")
elif value=="3":
                     print("Here is the Innformation about overs⤵")
                     NO_OF_Overs()
elif value=="4":
                 print("----------⤵ ⤵ ⤵ ⤵----first match data------------")
                 NO_of_runsby_each_batsman_match()
elif value=="5":
                    print("----------⤵ ⤵ ⤵ ⤵----Number Of Players in ecah match------------")
                    no_of_playersInEach()
elif value=="6":
                  print("----------⤵ ⤵ ⤵ ⤵ Toatal_runsBy_eachTeam----------------")
                  Total_runsBy_eachTeam()
elif value=="7":
                  print("----- player of the match----------")
                  player_of_match() 
elif value=="8":
                    print("----- win margins----------")
                    win_margins(input(" enter 1 for byRuns \n enter 2 for the byWickets"))
elif value=="9":     
                    print("No of overseas players in the each team")
                    no_Overses_Player_Each_Team()     
elif value=="10": 
                   Team_with_Most_Overseas_Players() 
else:
            print("you must choose the number with in the above")
