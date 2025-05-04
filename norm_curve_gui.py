import numpy as np
from scipy import stats
import pyqtgraph as pg
from statistics import NormalDist
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QDoubleSpinBox,
    QVBoxLayout,
    QWidget,
    QTabWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Normal Distribution Curve") 
        
        self.resize(800, 600)
        
        self.tab_widget = MyTabWidget(self) 
        self.setCentralWidget(self.tab_widget)
        
        self.show()
    
    
class MyTabWidget(QWidget): 
    def __init__(self, parent): 
        super(QWidget, self).__init__(parent) 
        self.layout = QVBoxLayout(self) 
  
        self.tabs = QTabWidget() 
        self.tab1 = QWidget() 
        self.tab2 = QWidget() 
        self.tab3 = QWidget() 
        self.tab4 = QWidget()
        self.tabs.resize(300, 200) 
  
        self.tabs.addTab(self.tab1, "Between") 
        self.tabs.addTab(self.tab2, "Left Tail") 
        self.tabs.addTab(self.tab3, "Right Tail") 
        self.tabs.addTab(self.tab4, "Both Tails") 
  
        self.tab1.layout = QVBoxLayout(self) 
        self.tab2.layout = QVBoxLayout(self)
        self.tab3.layout = QVBoxLayout(self) 
        self.tab4.layout = QVBoxLayout(self)
        self.widgets2 = [QLabel("Mean: "), QDoubleSpinBox(), QLabel("Standard Deviation: "), QDoubleSpinBox(), QLabel("x ≥: "), QDoubleSpinBox(), QLabel("x ≤: "), QDoubleSpinBox()]
        self.widgets2[1].setRange(-1000000, 1000000)
        self.widgets2[3].setRange(1.175494e-38, 1000000)
        self.widgets2[3].setValue(1)
        self.widgets2[5].setRange(-500000, 500000)
        self.widgets2[7].setRange(self.widgets2[5].value(), 500000)
        self.widgets3 = [QLabel("Mean: "), QDoubleSpinBox(), QLabel("Standard Deviation: "), QDoubleSpinBox(), QLabel("x ≤: "), QDoubleSpinBox()]
        self.widgets3[1].setRange(-1000000, 1000000)
        self.widgets3[3].setRange(1.175494e-38, 1000000)
        self.widgets3[3].setValue(1)
        self.widgets3[5].setRange(-500000, 500000)
        self.widgets4 = [QLabel("Mean: "), QDoubleSpinBox(), QLabel("Standard Deviation: "), QDoubleSpinBox(), QLabel("x ≥: "), QDoubleSpinBox()]
        self.widgets4[1].setRange(-1000000, 1000000)
        self.widgets4[3].setRange(1.175494e-38, 1000000)
        self.widgets4[3].setValue(1)
        self.widgets4[5].setRange(-500000, 500000)
        self.widgets5 = [QLabel("Mean: "), QDoubleSpinBox(), QLabel("Standard Deviation: "), QDoubleSpinBox(), QLabel("x ≥: "), QDoubleSpinBox(), QLabel("x ≤: "), QDoubleSpinBox()]
        self.widgets5[1].setRange(-1000000, 1000000)
        self.widgets5[3].setRange(1.175494e-38, 1000000)
        self.widgets5[3].setValue(1)
        self.widgets5[5].setRange(-500000, 500000)
        self.widgets5[7].setRange(self.widgets5[5].value(), 500000)
        
        for w in self.widgets2:
            w.setFixedSize(150, 30)
            self.tab1.layout.addWidget(w)
        for w in self.widgets3:
            w.setFixedSize(150, 30)
            self.tab2.layout.addWidget(w)
        for w in self.widgets4:
            w.setFixedSize(150, 30)
            self.tab3.layout.addWidget(w)
        for w in self.widgets5:
            w.setFixedSize(150, 30)
            self.tab4.layout.addWidget(w)
        
        self.prob= [QLabel(), QLabel(), QLabel(), QLabel()]
        self.z1 = [QLabel(), QLabel(), QLabel(), QLabel()]
        self.z2 = [QLabel(), QLabel()]
        self.z2[0].setFixedSize(300, 30)
        self.z2[1].setFixedSize(300, 30)
        for i in range(4):
            self.prob[i].setFixedSize(150, 30)
            self.z1[i].setFixedSize(300, 30)
        
        
        self.widgets2[5].valueChanged.connect(self.update_2_min)
        self.widgets5[5].valueChanged.connect(self.update_2_min)
        for i in range(1, 8, 2):
            self.widgets2[i].valueChanged.connect(self.between_prob)
            self.widgets5[i].valueChanged.connect(self.both_tails)
        for i in range(1, 6, 2):
            self.widgets3[i].valueChanged.connect(self.left_tail)
            self.widgets4[i].valueChanged.connect(self.right_tail)
        
        self.graph = [pg.PlotWidget(),pg.PlotWidget(),pg.PlotWidget(),pg.PlotWidget()]
        for g in self.graph:
            g.setBackground("w")
            g.setFixedSize(400, 400)
        
        self.tab1.layout.addWidget(self.prob[0])
        self.tab1.layout.addWidget(self.z1[0])
        self.tab1.layout.addWidget(self.z2[0])
        self.tab2.layout.addWidget(self.prob[1])
        self.tab2.layout.addWidget(self.z1[1])
        self.tab3.layout.addWidget(self.prob[2])
        self.tab3.layout.addWidget(self.z1[2])
        self.tab4.layout.addWidget(self.prob[3])
        self.tab4.layout.addWidget(self.z1[3])
        self.tab4.layout.addWidget(self.z2[1])
        
        self.tab1.layout.addWidget(self.graph[0])
        self.tab2.layout.addWidget(self.graph[1])
        self.tab3.layout.addWidget(self.graph[2])
        self.tab4.layout.addWidget(self.graph[3])
        
        self.tab1.setLayout(self.tab1.layout)
        self.tab2.setLayout(self.tab2.layout)
        self.tab3.setLayout(self.tab3.layout)
        self.tab4.setLayout(self.tab4.layout)
        self.layout.addWidget(self.tabs) 
        self.setLayout(self.layout)
        
    def update_2_min(self):
        new_min = self.widgets2[5].value()
        self.widgets2[7].setMinimum(new_min)
        if self.widgets2[7].value() <= self.widgets2[5].value():
            self.widgets2[7].setValue(new_min)
        new_min1 = self.widgets5[5].value()
        self.widgets5[7].setMinimum(new_min1)
        if self.widgets5[7].value() <= self.widgets5[5].value():
            self.widgets5[7].setValue(new_min1)
    
    def between_prob(self):
        self.widgets2[1].setValue(self.widgets2[1].value())
        self.widgets2[3].setValue(self.widgets2[3].value())
        self.widgets2[5].setValue(self.widgets2[5].value())
        self.widgets2[7].setValue(self.widgets2[7].value())
        x= np.linspace(self.widgets2[1].value() - 4 * self.widgets2[3].value(), self.widgets2[1].value() + 4 * self.widgets2[3].value(), 100)
        section=np.linspace(self.widgets2[5].value(),self.widgets2[7].value(),100)
        
        self.graph[0].clear()
        self.graph[0].plot(x, stats.norm.pdf(x,self.widgets2[1].value(), self.widgets2[3].value()))
        curve = pg.PlotDataItem(section, stats.norm.pdf(section,self.widgets2[1].value(), self.widgets2[3].value()), fillLevel=0, brush=(0, 0, 255, 50))
        self.graph[0].addItem(curve)
        
        prob_ = NormalDist(mu=self.widgets2[1].value(), sigma=self.widgets2[3].value()).cdf(self.widgets2[7].value()) - NormalDist(mu=self.widgets2[1].value(), sigma=self.widgets2[3].value()).cdf(self.widgets2[5].value())
        z1 = (self.widgets2[5].value()-self.widgets2[1].value())/self.widgets2[3].value()
        z2 = (self.widgets2[7].value()-self.widgets2[1].value())/self.widgets2[3].value()
        self.prob[0].setText(f"Probability: {prob_:.5f}")
        self.z1[0].setText(f"Z-Score for {self.widgets2[5].value()}: {z1:.4f}")
        self.z2[0].setText(f"Z-Score for {self.widgets2[7].value()}: {z2:.4f}")
    
    def left_tail(self):
        self.widgets3[1].setValue(self.widgets3[1].value())
        self.widgets3[3].setValue(self.widgets3[3].value())
        self.widgets3[5].setValue(self.widgets3[5].value())
        x= np.linspace(self.widgets3[1].value() - 4 * self.widgets3[3].value(), self.widgets3[1].value() + 4 * self.widgets3[3].value(), 100)
        section=np.linspace(min(x),self.widgets3[5].value(),100)
        
        self.graph[1].clear()
        self.graph[1].plot(x, stats.norm.pdf(x,self.widgets3[1].value(), self.widgets3[3].value()))
        curve = pg.PlotDataItem(section, stats.norm.pdf(section,self.widgets3[1].value(), self.widgets3[3].value()), fillLevel=0, brush=(0, 0, 255, 50))
        self.graph[1].addItem(curve)
        
        prob_ = NormalDist(mu=self.widgets3[1].value(), sigma=self.widgets3[3].value()).cdf(self.widgets3[5].value())
        z1 = (self.widgets3[5].value()-self.widgets3[1].value())/self.widgets3[3].value()
        self.prob[1].setText(f"Probability: {prob_:.5f}")
        self.z1[1].setText(f"Z-Score for {self.widgets2[5].value()}: {z1:.4f}")
        
    def right_tail(self):
        self.widgets4[1].setValue(self.widgets4[1].value())
        self.widgets4[3].setValue(self.widgets4[3].value())
        self.widgets4[5].setValue(self.widgets4[5].value())
        x= np.linspace(self.widgets4[1].value() - 4 * self.widgets4[3].value(), self.widgets4[1].value() + 4 * self.widgets4[3].value(), 100)
        section=np.linspace(self.widgets4[5].value(), max(x), 100)
        
        self.graph[2].clear()
        self.graph[2].plot(x, stats.norm.pdf(x,self.widgets4[1].value(), self.widgets4[3].value()))
        curve = pg.PlotDataItem(section, stats.norm.pdf(section,self.widgets4[1].value(), self.widgets4[3].value()), fillLevel=0, brush=(0, 0, 255, 50))
        self.graph[2].addItem(curve)
        
        prob_ = 1 - NormalDist(mu=self.widgets4[1].value(), sigma=self.widgets4[3].value()).cdf(self.widgets4[5].value())
        z1 = (self.widgets4[5].value()-self.widgets4[1].value())/self.widgets4[3].value()
        self.prob[2].setText(f"Probability: {prob_:.5f}")
        self.z1[2].setText(f"Z-Score for {self.widgets2[5].value()}: {z1:.4f}")
        
    def both_tails(self):
        self.widgets5[1].setValue(self.widgets5[1].value())
        self.widgets5[3].setValue(self.widgets5[3].value())
        self.widgets5[5].setValue(self.widgets5[5].value())
        self.widgets5[7].setValue(self.widgets5[7].value())
        x= np.linspace(self.widgets5[1].value() - 4 * self.widgets5[3].value(), self.widgets5[1].value() + 4 * self.widgets5[3].value(), 100)
        section1=np.linspace(min(x),self.widgets5[5].value(),100)
        section2=np.linspace(self.widgets5[7].value(), max(x), 100)
        
        self.graph[3].clear()
        self.graph[3].plot(x, stats.norm.pdf(x,self.widgets5[1].value(), self.widgets5[3].value()))
        curve = pg.PlotDataItem(section1, stats.norm.pdf(section1,self.widgets5[1].value(), self.widgets5[3].value()), fillLevel=0, brush=(0, 0, 255, 50))
        curve1 = pg.PlotDataItem(section2, stats.norm.pdf(section2,self.widgets5[1].value(), self.widgets5[3].value()), fillLevel=0, brush=(0, 0, 255, 50))
        self.graph[3].addItem(curve)
        self.graph[3].addItem(curve1)
        
        prob_l = NormalDist(mu=self.widgets5[1].value(), sigma=self.widgets5[3].value()).cdf(self.widgets5[5].value())
        prob_r = 1 - NormalDist(mu=self.widgets5[1].value(), sigma=self.widgets5[3].value()).cdf(self.widgets5[7].value())
        prob_ = prob_l + prob_r
        z1 = (self.widgets5[5].value()-self.widgets5[1].value())/self.widgets5[3].value()
        z2 = (self.widgets5[7].value()-self.widgets5[1].value())/self.widgets5[3].value()
        self.prob[3].setText(f"Probability: {prob_:.5f}")
        self.z1[3].setText(f"Z-Score for {self.widgets2[5].value()}: {z1:.4f}")
        self.z2[1].setText(f"Z-Score for {self.widgets2[7].value()}: {z2:.4f}")
        
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = MainWindow() 
    sys.exit(app.exec_()) 
