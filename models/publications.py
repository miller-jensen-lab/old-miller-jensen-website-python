#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

publications = [
    {
        'title': u'Systems biology of virus-host signaling network interactions',
        'authors': 'Xue Q., Miller-Jensen K.',
        'year': 2012,
        'vol': 45,
        'issue': 4,
        'journal': "BMB Reports",
        'pmid': 22531130,
        'fulltext_url': 'http://www.bmbreports.org/fulltext/bmbreports/view.php?vol=45&page=213',
    },
    {
        'title': u'Varying virulence: epigenetic control of expression noise and disease processes',
        'authors': 'Miller-Jensen K., Dey S.S., Schaffer D.V., Arkin A.P.',
        'year': 2011,
        'vol': 29,
        'issue': 10,
        'journal': "Trends in Biotechnology",
        'pmid': 21700350,
        'fulltext_url': 'http://linkinghub.elsevier.com/retrieve/pii/S0167-7799(11)00093-X',
    },

    {
        'title': u'Genetic selection for context-dependent stochastic phenotypes: Sp1 and TATA mutations increase phenotypic noise in HIV-1 gene expression',
        'authors': 'Miller-Jensen K., Skupsky R., Shah P.S., Arkin A.P., Schaffer D.V.',
        'year': 2013,
        'vol': 9,
        'issue': 7,
        'journal': "PLoS Computational Biology",
        'pmid': 23874178,
        'fulltext_url': 'http://dx.plos.org/10.1371/journal.pcbi.1003135',
    },
    {
        'title': u'Chromatin accessibility at the HIV LTR promoter sets a threshold for NF-κB mediated viral gene expression',
        'authors': 'Miller-Jensen K., Dey S.S., Pham N., Foley J.E., Arkin A.P., Schaffer D.V.',
        'year': 2012,
        'vol': 4,
        'issue': 6,
        'journal': "Integrative Biology",
        'pmid': 22555315,
        'fulltext_url': 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3362694/',
    },
    {
        'title': 'Control of stochastic gene expression ' \
            + 'by host factors at the HIV promoter',
        'authors': 'Burnett, J.C., Miller-Jensen, K., Shah, P.S.,' \
            + 'Arkin, A.P., Schaffer, D.V.',
        'year': 2009,
        'vol': 5,
        'issue': 1,
        'journal': "PLoS Pathogens",
        'pmid': 19132086,
        'fulltext_url': 'http://www.plospathogens.org/article/' \
            + 'info:doi/10.1371/journal.ppat.1000260',
    },
    {
        'title' : 'Common effector processing mediates cell-specific responses to stimuli',
        'authors' : 'Miller-Jensen, K.*, Janes, K.A.*, Brugge, J. S., Lauffenburger, D.A.',
        'year' : 2007,
        'journal' : "Nature" ,
        'pmid' : 17637676,
        'vol' : 448,
        'issue' : 7153,
        'pages' : '604-8',
        'fulltext_url' : 'http://www.nature.com/nature/journal/v448/n7153/abs/nature06001.html',
        'postscript' : '(Research highlight in Nature Biotechnology, 9/07)',
    },
    {
        'title' : 'Adenoviral vector saturates Akt pro-survival signaling and blocks insulin-mediated rescue of tumor necrosis-factor-induced apoptosis',
        'authors' : 'Miller-Jensen, K., Janes, K.A., Wong, Y., Griffith, L.G., Lauffenburger, D.A.',
        'year' : 2007,
        'journal' : "J Cell Science",
        'vol' : 119,
        'issue' : 18,
        'pages' : '3788-98',
        'pmid' : 16940353,
        'fulltext_url' : 'http://jcs.biologists.org/cgi/content/abstract/119/18/3788',
        'exports' : [
            ('kyle', 'test')
        ]
    },
    {
        'title' : 'High-throughput secretomic analysis of single cells to assess functional cellular heterogeneity',
        'authors' : 'Lu Y., Chen JJ, Mu L, Xue Q., Wu Y., Wu P.H., Li J., Vortmeyer A.O., Miller-Jensen K., Wirtz D, Fan R.',
        'year' : 2013,
        'journal' : "Anal Chem",
        'vol' : 85,
        'issue' : 4,
        'pages' : '2548-56',
        'pmid' : 23339603,
        'fulltext_url' : 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3589817/',
    },
    {
        'title' : 'Highly multiplexed profiling of single-cell effector functions reveals deep functional heterogeneity in response to pathogenic ligands',
        'authors' : 'Lu Y., Xue Q., Eisele M.R., Sulistijo E.S., Brower K., Han L, Amir el-A.D., Pe\'er D., Miller-Jensen K., Fan R.',
        'year' : 2015,
        'journal' : "Proc Natl Acad Sci",
        'vol' : 112,
        'issue' : 7,
        'pages' : 'E607-15',
        'pmid' : 25646488,
        'fulltext_url' : 'http://www.pnas.org/cgi/pmidlookup?view=long&pmid=25646488',
    },
    {
        'title' : 'Analysis of single-cell cytokine secretion reveals a role for paracrine signaling in coordinating macrophage responses to TLR4 stimulation',
        'authors' : 'Xue Q., Lu Y., Eisele M.Rself., Sulistijo E.S., Khan N, Fan R, Miller-Jensen K.',
        'year' : 2015,
        'journal' : "Science Signaling",
        'vol' : 8,
        'issue' : 381,
        'pmid' : 26082435,
        'fulltext_url' : 'http://stke.sciencemag.org/content/8/381/ra59',
    },
]

publications.sort(key=lambda x: x['year'], reverse=True)
today = datetime.date.today()
for publication in publications:
    if today.year - publication['year'] <= 1:
        is_new = True
    else:
        is_new = False
    publication['is_new'] = is_new
