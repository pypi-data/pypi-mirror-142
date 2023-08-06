# BioMagicBox

## Materials

A CSV file including  `Gene ID` and `Protein Seqeunce`

Here is an example:

| Gene ID | Seq          |
|:-------:|:------------:|
| GENE1   | WATYLIM..... |
| GENE2   | MMCAYTI..... |

## Using Methods

```python
from biomagicbox.expasy import ProtParam

c=ProtParam('test.db','expasy') #Create database and new table.
c.load_gene('test.csv') #Gene Sequences table
c.run(4)  #Number of threads
```
