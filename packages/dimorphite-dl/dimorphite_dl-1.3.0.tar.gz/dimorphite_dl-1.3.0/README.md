Dimorphite-DL
=============

What is it?
-----------

Dimorphite-DL adds hydrogen atoms to molecular representations, as appropriate
for a user-specified pH range. It is a fast, accurate, accessible, and modular
open-source program for enumerating small-molecule ionization states.

This version is a class object that is representative of dimorhitedl.

Citation
--------

If you use Dimorphite-DL in your research, please cite:

Ropp PJ, Kaminsky JC, Yablonski S, Durrant JD (2019) Dimorphite-DL: An
open-source program for enumerating the ionization states of drug-like small
molecules. J Cheminform 11:14. doi:10.1186/s13321-019-0336-9.

Licensing
---------

Dimorphite-DL is released under the Apache 2.0 license. See LICENCE.txt for
details.

Installation
------------

**Edit** This edit is made by Sulstice for distribution and installation.

```python

pip install dimorphite_dl

```

QuickStart
----------

**Edit** This edit is made by Sulstice for distribution and installation.


```python

from dimorphite_dl import DimorphiteDL

dimorphite_dl = DimorphiteDL(

    min_ph=4.5,
    max_ph=8.0,
    max_variants=128,
    label_states=False,
    pka_precision=1.0
)
print(dimorphite_dl.protonate('CC(=O)O'))

>>>
['CC(=O)[O-]']


```

Caveats
-------

Dimorphite-DL deprotonates indoles and pyrroles around pH 14.5. But these
substructures can also be protonated around pH -3.5. Dimorphite does not
perform the protonation.

Authors and Contacts
--------------------

See the `CONTRIBUTORS.md` file for a full list of contributors. Please contact
Jacob Durrant (durrantj@pitt.edu) with any questions.
