from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QCategoryAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        # Datenserien erstellen
        self.__series_tokyo = QLineSeries()
        self.__series_tokyo.setName("Tokyo")
        self.__series_tokyo.setColor(QColor("blue"))

        self.__series_london = QLineSeries()
        self.__series_london.setName("London")
        self.__series_london.setColor(QColor(""))

        # Daten hinzufügen
        dates = [
            QDateTime(2025, 1, 1, 0, 0, 0),
            QDateTime(2025, 2, 1, 0, 0, 0),
            QDateTime(2025, 3, 1, 0, 0, 0),
            QDateTime(2025, 4, 1, 0, 0, 0),
            QDateTime(2025, 5, 1, 0, 0, 0),
            QDateTime(2025, 6, 1, 0, 0, 0),
            QDateTime(2025, 7, 1, 0, 0, 0),
            QDateTime(2025, 8, 1, 0, 0, 0),
            QDateTime(2025, 9, 1, 0, 0, 0),
            QDateTime(2025, 10, 1, 0, 0, 0),
            QDateTime(2025, 11, 1, 0, 0, 0),
            QDateTime(2025, 12, 1, 0, 0, 0),
        ]

        # Tokyo-Daten
        tokyo_temps = [7, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        for i, temp in enumerate(tokyo_temps):
            self.__series_tokyo.append(dates[i].toMSecsSinceEpoch(), temp)

        # London-Daten
        london_temps = [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17, 16.6, 14.2, 10.3, 6.6, 4.8]
        for i, temp in enumerate(london_temps):
            self.__series_london.append(dates[i].toMSecsSinceEpoch(), temp)

        # X-Achse (Monate)
        x_axis = QCategoryAxis()
        x_axis.setTitleText("Monat")
        x_axis.append("Jan", dates[0].toMSecsSinceEpoch())
        x_axis.append("Feb", dates[1].toMSecsSinceEpoch())
        x_axis.append("Mär", dates[2].toMSecsSinceEpoch())
        x_axis.append("Apr", dates[3].toMSecsSinceEpoch())
        x_axis.append("Mai", dates[4].toMSecsSinceEpoch())
        x_axis.append("Jun", dates[5].toMSecsSinceEpoch())
        x_axis.append("Jul", dates[6].toMSecsSinceEpoch())
        x_axis.append("Aug", dates[7].toMSecsSinceEpoch())
        x_axis.append("Sep", dates[8].toMSecsSinceEpoch())
        x_axis.append("Okt", dates[9].toMSecsSinceEpoch())
        x_axis.append("Nov", dates[10].toMSecsSinceEpoch())
        x_axis.append("Dez", dates[11].toMSecsSinceEpoch())


        # Y-Achse (Temperaturen in °C)
        y_axis = QValueAxis()
        y_axis.setTitleText("Temperatur in °C")
        y_axis.setRange(0, 30)  # Bereich der Achse
        y_axis.setTickCount(7)  # Zeigt Ticks bei 0, 5, 10, 15, 20, 25, 30 an

        # Diagramm erstellen
        self.__chart = QChart()
        self.__chart.setTitle("Monatliche Durchschnittstemperaturen")
        self.__chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.__chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.__chart.addSeries(self.__series_tokyo)
        self.__chart.addSeries(self.__series_london)

        # Achsen an die Datenserien anhängen
        self.__series_tokyo.attachAxis(x_axis)
        self.__series_tokyo.attachAxis(y_axis)
        self.__series_london.attachAxis(x_axis)
        self.__series_london.attachAxis(y_axis)

        # Diagramm in der Ansicht anzeigen
        self.setChart(self.__chart)
