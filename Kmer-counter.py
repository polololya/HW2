 # -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

class Kmer:
    counter = 0
    sequence = ''
    positions = []
    
    def __init__(self, kmer_name):
        self.sequence = kmer_name
        self.positions = []
    
    def increase(self):
        self.counter += 1
            
    def add_position(self, position_start, position_end):
        conc = '{}:{}'.format(position_start, position_end)
        self.positions.append(conc)
        
    def get_positions(self):
        print('Sequence:{}\tPositions in current file:{}'.format(self.sequence, self.positions))
        
        
with open ('seq_y_pestis.fasta','r') as fasta:
    seq = ''
    for line in fasta:
        if line[0]== '>':
            continue
        else:
            line = line.strip()
            seq += line
    
kmer_size = 23
kmer_dict = {}
for index in range(0, len(seq)-kmer_size+1):
    current_kmer = seq[index:(index+kmer_size)]
    if current_kmer in kmer_dict:
        kmer_dict[current_kmer].increase()
        kmer_dict[current_kmer].add_position(index,index+kmer_size)
    else:
        kmer_dict[current_kmer] = Kmer(current_kmer)
        kmer_dict[current_kmer].add_position(index,index+kmer_size)
        

max_counter = 0
freq_kmer = 0        
for key in kmer_dict.keys():
    if kmer_dict[key].counter > max_counter:
        max_counter = kmer_dict[key].counter
        freq_kmer = key
        
kmer_dict[freq_kmer].get_positions()


