import matplotlib.pyplot as plt
import numpy as np
class GraphUtil:
    def __init__(self, races):
        self.race_history = races[::-1]

    def speed_distribution(self):
        plt.figure()
        speeds = np.array(list(map(lambda k: k['wpm'], self.race_history)))
        lowest = (speeds.min() // 5) * 5
        highest = ((speeds.max() // 5) + 1) * 5
        bin_extremes = np.arange(lowest, highest+1, 5)
        plt.hist(speeds, bins=bin_extremes, color='#1f77b4', edgecolor='#1f77b4')

        plt.xlabel('Speed (WPM)')
        plt.ylabel('Frequency')
        plt.title('Speed Distribution')
        plt.savefig('./img/speed_distribution.svg')

    def accuracy_distribution(self):
        plt.figure()
        accuracies = np.array(list(map(lambda k: k['ac'], self.race_history)))
        lowest = np.floor(accuracies.min() * 100) / 100
        highest = np.ceil(accuracies.max() * 100) / 100
        bin_edges = np.arange(lowest, highest + 0.001, 0.01)
        plt.hist(accuracies, bins=bin_edges, color='#1f77b4', edgecolor='#1f77b4')

        plt.xlabel('Accuracy')
        plt.ylabel('Frequency')
        plt.title('Accuracy Distribution')
        plt.savefig('./img/accuracy_distribution.svg')

    def speed_vs_race_no(self):
        plt.figure()
        x = [race['gn'] for race in self.race_history]
        y = [race['wpm'] for race in self.race_history]
        z = [race['ac'] for race in self.race_history]

        scatter = plt.scatter(x, y, c=z, cmap='RdYlGn', s=2)
        color_bar = plt.colorbar(scatter)
        color_bar.set_label('Accuracy')

        plt.xlabel('Race No.')
        plt.ylabel('Speed (WPM)')
        plt.title('Speed vs. Race No.')
        plt.savefig('./img/speed_vs_race_no.svg')

    def accuracy_vs_race_no(self):
        plt.figure()
        x = [race['gn'] for race in self.race_history]
        y = [race['ac'] for race in self.race_history]
        z = [race['wpm'] for race in self.race_history]

        scatter = plt.scatter(x, y, c=z, cmap='RdYlGn', s=2)
        color_bar = plt.colorbar(scatter)
        color_bar.set_label('Speed (WPM)')

        plt.xlabel('Race No.')
        plt.ylabel('Accuracy')
        plt.title('Accuracy vs. Race No.')
        plt.savefig('./img/accuracy_vs_race_no.svg')

    def speed_vs_accuracy(self):
        plt.figure()
        x = [race['ac'] for race in self.race_history]
        y = [race['wpm'] for race in self.race_history]
        z = [race['gn'] for race in self.race_history]

        scatter = plt.scatter(x, y, c=z, cmap='RdYlGn', s=2)
        color_bar = plt.colorbar(scatter)
        color_bar.set_label('Race No.')

        plt.xlabel('Accuracy')
        plt.ylabel('Speed (WPM)')
        plt.title('Speed vs. Accuracy')
        plt.savefig('./img/speed_vs_accuracy.svg')
