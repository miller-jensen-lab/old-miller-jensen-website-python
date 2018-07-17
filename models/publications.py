#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

publications = [
    {
        'title': u'Systems biology of virus-host signaling network interactions',
        'authors': u'Xue Q., Miller-Jensen K.',
        'year': 2012,
        'vol': 45,
        'issue': 4,
        'journal': u"BMB Reports",
        'pmid': 22531130,
        'fulltext_url': u'http://www.bmbreports.org/fulltext/bmbreports/view.php?vol=45&page=213',
    },
    {
        'title': u'Varying virulence: epigenetic control of expression noise and disease processes',
        'authors': u'Miller-Jensen K., Dey S.S., Schaffer D.V., Arkin A.P.',
        'year': 2011,
        'vol': 29,
        'issue': 10,
        'journal': u"Trends in Biotechnology",
        'pmid': 21700350,
        'fulltext_url': u'http://linkinghub.elsevier.com/retrieve/pii/S0167-7799(11)00093-X',
    },

    {
        'title': u'Genetic selection for context-dependent stochastic phenotypes: Sp1 and TATA mutations increase phenotypic noise in HIV-1 gene expression',
        'authors': u'Miller-Jensen K., Skupsky R., Shah P.S., Arkin A.P., Schaffer D.V.',
        'year': 2013,
        'vol': 9,
        'issue': 7,
        'journal': u"PLoS Computational Biology",
        'pmid': 23874178,
        'fulltext_url': u'http://dx.plos.org/10.1371/journal.pcbi.1003135',
    },
    {
        'title': u'Chromatin accessibility at the HIV LTR promoter sets a threshold for NF-κB mediated viral gene expression',
        'authors': u'Miller-Jensen K., Dey S.S., Pham N., Foley J.E., Arkin A.P., Schaffer D.V.',
        'year': 2012,
        'vol': 4,
        'issue': 6,
        'journal': u"Integrative Biology",
        'pmid': 22555315,
        'fulltext_url': u'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3362694/',
    },
    {
        'title': u'Control of stochastic gene expression '
        + 'by host factors at the HIV promoter',
        'authors': u'Burnett, J.C., Miller-Jensen, K., Shah, P.S.,'
        + 'Arkin, A.P., Schaffer, D.V.',
        'year': 2009,
        'vol': 5,
        'issue': 1,
        'journal': u"PLoS Pathogens",
        'pmid': 19132086,
        'fulltext_url': u'http://www.plospathogens.org/article/'
        + 'info:doi/10.1371/journal.ppat.1000260',
    },
    {
        'title': u'Common effector processing mediates cell-specific responses to stimuli',
        'authors': u'Miller-Jensen, K.*, Janes, K.A.*, Brugge, J. S., Lauffenburger, D.A.',
        'year': 2007,
        'journal': u"Nature",
        'pmid': 17637676,
        'vol': 448,
        'issue': 7153,
        'pages': u'604-8',
        'fulltext_url': u'http://www.nature.com/nature/journal/v448/n7153/abs/nature06001.html',
        'postscript': u'(Research highlight in Nature Biotechnology, 9/07)',
    },
    {
        'title': u'Adenoviral vector saturates Akt pro-survival signaling and blocks insulin-mediated rescue of tumor necrosis-factor-induced apoptosis',
        'authors': u'Miller-Jensen, K., Janes, K.A., Wong, Y., Griffith, L.G., Lauffenburger, D.A.',
        'year': 2007,
        'journal': u"J Cell Science",
        'vol': 119,
        'issue': 18,
        'pages': u'3788-98',
        'pmid': 16940353,
        'fulltext_url': u'http://jcs.biologists.org/cgi/content/abstract/119/18/3788',
        'exports': [
            ('kyle', 'test')
        ]
    },
    {
        'title': u'High-throughput secretomic analysis of single cells to assess functional cellular heterogeneity',
        'authors': u'Lu Y., Chen JJ, Mu L, Xue Q., Wu Y., Wu P.H., Li J., Vortmeyer A.O., Miller-Jensen K., Wirtz D, Fan R.',
        'year': 2013,
        'journal': u"Anal Chem",
        'vol': 85,
        'issue': 4,
        'pages': u'2548-56',
        'pmid': 23339603,
        'fulltext_url': u'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3589817/',
    },
    {
        'title': u'Quantitative Evaluation and Optimization of Co-drugging to Improve Anti-HIV Latency Therapy',
        'authors': u'Wong V.C., Fong L.E., Adams N.M., Xue Q., Dey S.S., Miller-Jensen K.',
        'year': 2014,
        'journal': u"Cellular and Molecular Bioengineering",
        'vol': 7,
        'issue': 3,
        'pages': u'320-333',
        'pmid': 26191086,
        'fulltext_url': u'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4501041/',
    },
    {
        'title': u'Highly multiplexed profiling of single-cell effector functions reveals deep functional heterogeneity in response to pathogenic ligands',
        'authors': u'Lu Y., Xue Q., Eisele M.R., Sulistijo E.S., Brower K., Han L, Amir el-A.D., Pe\'er D., Miller-Jensen K., Fan R.',
        'year': 2015,
        'journal': u"Proc Natl Acad Sci",
        'vol': 112,
        'issue': 7,
        'pages': u'E607-15',
        'pmid': 25646488,
        'fulltext_url': u'http://www.pnas.org/cgi/pmidlookup?view=long&pmid=25646488',
    },
    {
        'title': u'Analysis of single-cell cytokine secretion reveals a role for paracrine signaling in coordinating macrophage responses to TLR4 stimulation',
        'authors': u'Xue Q., Lu Y., Eisele M.R., Sulistijo E.S., Khan N, Fan R, Miller-Jensen K.',
        'year': 2015,
        'journal': u"Science Signaling",
        'vol': 8,
        'issue': 381,
        'pmid': 26082435,
        'fulltext_url': u'http://stke.sciencemag.org/content/8/381/ra59',
    },
    {
        'title': u'A passive-flow microfluidic device for imaging latent HIV activation dynamics in single T cells',
        'authors': u'Ramji R., Wong V.C., Chavali A.K., Gearhart L.M., Miller-Jensen K.',
        'year': 2015,
        'journal': u"Integrative Biology",
        'vol': 7,
        'issue': 9,
        'pages': u'998-1010',
        'pmid': 26138068,
        'fulltext_url': u'http://pubs.rsc.org/en/Content/ArticleLanding/2015/IB/C5IB00094G#!divAbstract',
    },
    {
        'title': u'"Pop-slide" patterning: rapid fabrication of microstructured PDMS gasket slides for biological applications',
        'authors': u'Ramji R., Khan N.T., Muñoz Rojas A., Miller-Jensen K.',
        'year': 2015,
        'journal': u"RSC Advances",
        'vol': 5,
        'issue': None,
        'pmid': 26949529,
        'fulltext_url': u'http://pubs.rsc.org/en/Content/ArticleLanding/2015/IB/C5IB00094G#!divAbstract',
    },
    {
        'title': u'Generalized selection to overcome innate immunity selects for host breadth in an RNA virus',
        'authors': u'Wasik B.R., Muñoz-Rojas A.R., Okamoto K.W., Miller-Jensen K., Turner PE.',
        'year': 2016,
        'journal': u"Evolution",
        'vol': 70,
        'issue': 2,
        'pmid': 26882316,
        'doi': u'10.1111/evo.12845',
    },
    {
        'title': u'Distinct promoter activation mechanisms modulate noise-driven HIV gene expression',
        'authors': u'Chavali A.K., Wong V.C., Miller-Jensen K.',
        'year': 2015,
        'journal': u"Scientific Reports",
        'vol': 5,
        'issue': 17661,
        'pmid': 26666681,
        'doi': u'10.1038/srep17661',
    },
    {
        'title': u'Redefining Signaling Pathways with an Expanding Single-Cell Toolbox.',
        'authors': u'Gaudet S., Miller-Jensen K.',
        'year': 2016,
        'journal': u"Trends Biotechnol.",
        'vol': 34,
        'issue': 6,
        'pmid': 26968612,
        'doi': u'10.1016/j.tibtech.2016.02.009'
    },
    {
        'title': u'Myeloid-targeted immunotherapies act in synergy to induce in ammation and antitumor immunity.',
        'authors': u'Perry C.J., Muñoz-Rojas A.R., Meeth KM, Kellman L.N., Amezquita RA, Thakral D., Du V.Y., Wang J.X., Damsky W., Kuhlmann A.L., Sher J.W., Bosenberg M., Miller-Jensen K., Kaech S.M.',
        'year': 2018,
        'journal': u"J Exp Med.",
        'vol': 215,
        'issue': 3,
        'pmid': 29436395,
        'doi': u'10.1084/jem.20171435'
    },
    {'authors': u'Fong LE, Muñoz-Rojas AR, Miller-Jensen K',
     'title': u'Advancing systems immunology through data-driven statistical analysis.',
     'pmid': u'29656236',
     'volume': u'52',
     'issue': u'',
     'year': 2018,
     'pages': u'109-115',
     'journal': u'Curr Opin Biotechnol',
     'doi': u'10.1016/j.copbio.2018.03.009'
     },
    {'authors': u'Wong VC, Bass VL, Bullock ME, Chavali AK, Lee REC, Mothes W, Gaudet S, Miller-Jensen K', 'title': u'NF-κB-Chromatin Interactions Drive Diverse Phenotypes by Modulating Transcriptional Noise.',
        'pmid': u'29346759', 'volume': u'22', 'issue': u'3', 'year': 2018, 'pages': u'585-599', 'journal': u'Cell Rep', 'doi': u'10.1016/j.celrep.2017.12.080'},
    {'authors': u'Fong LE, Sulistijo ES, Miller-Jensen K', 'title': u'Systems analysis of latent HIV reversal reveals altered stress kinase signaling and increased cell death in infected T cells.',
        'pmid': u'29170390', 'volume': u'7', 'issue': u'1', 'year': 2017, 'pages': u'16179', 'journal': u'Sci Rep', 'doi': u'10.1038/s41598-017-15532-0'},
]

publications.sort(key=lambda x: x['year'], reverse=True)
today = datetime.date.today()
for publication in publications:
    if today.year - publication['year'] <= 1:
        is_new = True
    else:
        is_new = False
    publication['is_new'] = is_new
