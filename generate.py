from GraphUtil import GraphUtil
from StatsScraper import StatsScraper
import sys
username = sys.argv[1]
ss = StatsScraper(username, csv_path='./data.csv')
gu = GraphUtil(ss.getData())
gu.speed_distribution()
gu.accuracy_distribution()
gu.speed_vs_race_no()
gu.accuracy_vs_race_no()
gu.speed_vs_accuracy()