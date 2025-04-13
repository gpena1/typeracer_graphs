from GraphUtil import GraphUtil
from StatsScraper import StatsScraper
import sys
username = sys.argv[1]
csv_path = sys.argv[2] if len(sys.argv) > 2 else ''
ss = StatsScraper(username, csv_path=csv_path)
gu = GraphUtil(ss.getData())
gu.speed_distribution()
gu.accuracy_distribution()
gu.speed_vs_race_no()
gu.accuracy_vs_race_no()
gu.speed_vs_accuracy()