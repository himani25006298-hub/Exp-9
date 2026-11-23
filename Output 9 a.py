[46 34 78 92 19]
[19 34 46 78 92]
[20 23 31 47 89]
[89 47 31 23 20]

[2 3 5 6 1 7 9 3]
[3 5 6 1 7]
9
1
36
[1 2 3 3 5 6 7 9]
4.5
2.449489742783178
6.0
4.5
4.0
[3 9 7 1 6 5 3 2]

Elements are: [0 1 2 3 4 5 6 7 8 9]
[ 0  1 26  3 26  5  6 26  8  9]

sorted: [('JAIN1', 2, 21.) ('JAIN2', 7, 29.)
 ('JAIN3', 7, 39.)]

1. DataFrame
  Name  Marks  Age Course State
0    A     80   19    BCA     E
1    B     90   20    BSc     F
2    C     85   14   Bcom     G
3    D     70   15    BMS     H

2. Head
  Name  Marks  Age Course State
0    A     80   19    BCA     E
1    B     90   20    BSc     F
2    C     85   14   Bcom     G
3    D     70   15    BMS     H

3. Tail
  Name  Marks  Age Course State
0    A     80   19    BCA     E
1    B     90   20    BSc     F
2    C     85   14   Bcom     G
3    D     70   15    BMS     H

4. Info
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    4 non-null      object
 1   Marks   4 non-null      int64
 2   Age     4 non-null      int64
 3   Course  4 non-null      object
 4   State   4 non-null      object
dtypes: int64(2), object(3)
memory usage: 292.0+ bytes

5. Describe
           Marks        Age
count   4.000000   4.000000
mean   81.250000  17.000000
std     8.539126   2.943920
min    70.000000  14.000000
25%    77.500000  14.750000
50%    82.500000  17.000000
75%    86.250000  19.250000
max    90.000000  20.000000

6. Sorted (Marks)
  Name  Marks  Age Course State
3    D     70   15    BMS     H
0    A     80   19    BCA     E
2    C     85   14   Bcom     G
1    B     90   20    BSc     F
