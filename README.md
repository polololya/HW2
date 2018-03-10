# Kmer class
Homework2 - class creating and working with Kmers

### class __Kmer__ contains information about specific Kmer:
* sequence (Kmer.sequence)
* list of coordinates in current line (Kmer.positions)
* counter for positions (Kmer.counter)

### methods for class __Kmer__:
* Kmer.increase() - increase counter value
* Kmer.add_position() - add beginning and end positions in list of positions
* Kmer.get_positions() - easy-to-read console output with table of positions for specific Kmer

### Workflow:
1. Open input file, concatenate all lines in one **!!!HUGE!!!** line
2. Set Kmer sixe and create empty dictionary
3. scan input line for all possible Kmers
4. for every new Kmer: add key to dictionary (key - sequence, value - link to class kmer object) + add position in positions list
5. for every already existing Kmer: increase counter + add position in positions list
6. find most frequent Kmer (analyse created dictionary).
7. get sequence of most frequent Kmer and list of positions in file

### Usage example:
```$ python Kmer-counter.py```\
__input fle has to be in the same directory with script__
