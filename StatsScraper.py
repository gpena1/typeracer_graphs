"""
Aside from a few modifications, this code has been provided
at the courtesy of Skypromp (https://github.com/SkyPromp). You may find
a file of the same name in his typeracer stats scraper: https://github.com/SkyPromp/TypeRacer-stats-scraper
"""
from datetime import datetime
from numpy import array
import requests
import pandas as pd
from bs4 import BeautifulSoup


class StatsScraper:
    def __init__(self, username: str, universe: str = "", start_date: datetime = None, csv_path: str = ''):
        self.races = []
        if csv_path:
            df = pd.read_csv(csv_path)
            for index, row in df.iterrows():
                arr = row.array
                self.races.append({
                    'gn':  arr[0],
                    'wpm': arr[1],
                    'ac':  arr[2],
                    'pts': arr[3],
                    'r':   arr[4],
                    't':   arr[5]
                })
            return


        amount = 1550  # n=2147483647
        link = "https://data.typeracer.com/pit/race_history"
        next_link = f"{link}?user={username}&n={amount}&startDate=&universe={universe}"

        while True:
            html = requests.get(next_link).text
            data = BeautifulSoup(html, 'lxml')

            self._retrieveData(data.find_all('div', class_="Scores__Table__Row"), start_date)

            try:
                next_link = data.find('div', class_="themeContent pit").find_all("span")[-1]
                if next_link.text == """\n\n          load older results »\n        \n""":
                    next_link = link + next_link.find("a").get("href")
                else:
                    break
            except AttributeError as e:
                break
            except IndexError as e:
                break

        print("Done loading data.")

    def _retrieveData(self, data, start_date):
        for item in data:
            attempt, wpm, accuracy, score, place, date = [i.strip() for i in item.text.strip().split("\n") if i.strip()]
            item_date = self._toDatetime(date)

            if start_date is not None and item_date < start_date:
                continue

            # naming conventions from the data.typeracer.com API are being followed here.
            # ac = accuracy
            # gn = game number = race number
            # r = rank/placement
            self.races.append({
                'wpm': int(wpm.split(" ")[0]),
                'ac':  (round(float(accuracy.replace("%", "")) / 100, 3)),
                'gn':  int(attempt),
                'pts': int(score if score != "N/A" else 0),
                'r':   place,
                't':   item_date
            })
            # self.wpm.append(int(wpm.split(" ")[0]))
            # self.accuracy.append((round(float(accuracy.replace("%", "")) / 100, 3)))
            # self.attempt.append(int(attempt))
            # self.score.append(int(score if score != "N/A" else 0))
            # self.place.append(place)
            # self.date.append(item_date)

    def _toDatetime(self, current_date: str) -> datetime:
        months = ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
        if current_date == "today":
            current_date = datetime.today()  # trim microseconds
        else:
            month, day, year = current_date.split(" ")
            day = int(day[:-1])
            month = months.index(month) + 1
            year = int(year)

            current_date = datetime(year, month, day)

        return current_date

    def getData(self):
        return self.races

    def download(self, path: str):
        with open(path, "w") as f:
            f.write('Race #,WPM,Accuracy,Points,Placement,Date\n')
            for race in self.races:
                gn = race['gn']
                wpm = race['wpm']
                ac = race['ac']
                pts = race['pts']
                r = race['r']
                t = race['t']
                f.write(f"{gn},{wpm},{ac},{pts},{r},{t}\n")