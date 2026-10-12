# Catalogues

The program `scripts/catalog.py` reads this table. A catalogue is a list that its issuer keeps,
without a ranking and without an advertisement. An entry of a catalogue is a candidate for the
research. It is not a source.

| Id | Catalogue | Issuer | Holds | Form | Address | Entries below | Row read on |
|---|---|---|---|---|---|---|---|
| cncf-landscape | CNCF landscape | Cloud Native Computing Foundation | projects and products of a field, in categories | landscape | https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml |  | 2026-10-12 |
| lf-landscape | Linux Foundation landscape | The Linux Foundation | projects that the foundation and its sub-foundations host | landscape | https://raw.githubusercontent.com/jmertic/lf-landscape/main/landscape.yml |  | 2026-10-12 |
| nlnet-projects | NLnet, all projects | NLnet Foundation | projects that got a grant, with the fund and the years | rows:tr | https://nlnet.nl/project/index.html | https://nlnet.nl/project/ | 2026-10-12 |
| sovereign-tech | Sovereign Tech Agency, technologies | Sovereign Tech Agency | technologies that got public money | rows:li | https://www.sovereign.tech/tech | https://www.sovereign.tech/tech/ | 2026-10-12 |
