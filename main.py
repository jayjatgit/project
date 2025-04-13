#with a lot of help from AI

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_csv(self):
        #Načte data ze souboru CSV s ošetřením výjimek.
        try:
            self.data = pd.read_csv(self.file_path)
            print("Data úspěšně načtena.")
        except FileNotFoundError:
            print(f"Soubor {self.file_path} nebyl nalezen.")
        except pd.errors.EmptyDataError:
            print(f"Soubor {self.file_path} je prázdný.")
        except Exception as e:
            print(f"Nastala neočekávaná chyba při načítání CSV: {e}")

    def get_data(self):
        #Vrátí načtená data, pokud existují.
        if self.data is None:
            print("Data nejsou k dispozici. Zkontrolujte, zda byl soubor správně načten.")
        return self.data


class SpectralAnalyzer:
    def __init__(self, raw_data, sampling_rate):
        self.raw_data = raw_data
        self.sampling_rate = sampling_rate
        self.frequencies = None
        self.spectrum = None

#part of input csv file
# DynoWare,Version 3.2.5.0
# Path:,C:\Kistler\Dynoware\Data\
# Filename:,kladivo2.dwd
# Config ID:,kladivo2.cfg
# Setup ID:,0
# Manipulated:,0
# Filename 1:,
# Filename 2:,
# Date:,Tuesday, January 15, 2019
# Time:,16:57:15
# Sampling rate [Hz]:,100000
# Measuring time [s]:,0,1
# Delay time [s]:,0
# Cycle time [s]:,0
# Cycles:,1
# Samples per channel:,10001
# Cycle interval:,0
# Cycle No:,1
# Time,kladivo,AFx,AFy,AFz
# s,N,g,g,g
# 0,000000,0,013079,-0,000435965,-0,000326974,-0,000871931
# 0,000010,-0,0435965,-0,000217983,-0,000980922,-0,000435965
# 0,000020,-0,00871931,-0,000980922,-0,000653948,0,000326974
# 0,000030,0,00871931,-0,000326974,-0,000544957,-0,000762939
# 0,000040,0,0174386,-0,000871931,-0,00108991,-0,000980922
# 0,000050,0,0479562,-0,000326974,-0,000435965,-0,0011989
# 0,000060,0,0217983,-0,000762939,-0,000326974,-0,000871931
# 0,000070,0,0305176,-0,000980922,-0,000108991,0,000326974
# 0,000080,0,0174386,-0,000762939,-0,000653948,0
# 0,000090,-0,00435965,-0,000435965,-0,000217983,0
# 0,000100,0,00871931,-0,000653948,-0,000217983,-0,000544957
# 0,000110,0,00435965,-0,000980922,-0,000980922,-0,000653948
# 0,000120,0,0,000762939,-0,000108991,-0,000544957
