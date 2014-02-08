#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
]


people = [
    {
        'name': u'Arvind Chavali',
        'photo': u'Arvind_photo-small.jpg',
        'position': u'Postdoctoral Associate',
        'description': u'Arvind is investigating the role of cell-to-cell heterogeneity in the activation of latent HIV proviruses. His interests lie in computational modeling and systems analysis. Arvind received his PhD in biomedical engineering from the University of Virginia.',
    },
    {
        'name': u'Ramesh Ramji',
        'photo': u'Ramesh_photo-small.jpg',
        'position': u'Postdoctoral Associate',
        'description': u'Ramesh likes to invent novel integrated micro analytical devices for biological applications. With a PhD in bioengineering (microfluidic cell based assays) from the National University of Singapore (NUS), he dwells into areas including nanobiotechnology, bioimaging, analytical chemistry and instrumentation. He is currently developing a high throughput multiplexed microfluidic device to quantify signaling dynamics and endpoint protein secretion at the "single cell" level.',
    },
    {
        'name': u'Qiong Xue',
        'photo': u'Qiong_photo-small.jpg',
        'position': u'Postdoctoral Associate',
        'description': u'Qiong joined the Miller-Jensen lab from Texas A&M with a background in inflammation and infectious diseases. She is investigating cytokine/chemokine secretion signatures of both a cell population and single cells and excited to apply systems analysis to single cell inflammatory responses.',
    },
    {
        'name': u'Endah Sulistijo',
        'photo': u'Endah_photo-small.jpg',
        'position': u'Postdoctoral Associate (joint with Prof. Rong Fan)',
        'description': u'Endah got her Ph.D. in Biochemistry from Rice University.  She is currently involved to two research projects: (1) Characterization of protein phosphorylation signatures in latent HIV-infected cells and non-infected cells, and (2) Optimization of microfluidic techniques for detection of cell signaling proteins at single-cell level.',
    },
    {
        'name': u'Linda Fong',
        'photo': u'Linda_photo-small.jpg',
        'position': u'Graduate Student (Biomedical Engineering)',
        'description': u'Linda\'s research focuses on the temporal dynamics of phosphoproteins in the reactivation of latent HIV. Through systems analysis and multivariate regression modeling, her work aims to elucidate key signaling pathways which can predict network responses to pharmacologic intervention. Her research interests involve using data-driven models of cell signaling to approach problems in oncology and infectious diseases. Linda earned her BS from MIT in Biological Engineering (Course XX) with a minor in Science, Technology, and Society and a concentration in Ethics.',
    },
    {
        'name': u'Andrés Muñoz Rojas',
        'photo': u'Andres_photo-small.jpg',
        'position': u'Graduate Student (Biomedical Engineering)',
        'description': u'Andrés is investigating the paradoxical role of macrophages in promoting and destroying tumors. Using a novel microfluidic device, he is studying the signaling dynamics of single macrophages and correlating it to downstream protein secretion signatures in the same single cell. His interests include cancer immunology, microscopy, systems biology and signal transduction. Andrés received his Bachelor’s degree in Bioengineering from the University of Pennsylvania with a minor in Music.',
    },
    {
        'name': u'Victor Wong',
        'photo': u'Victor_photo-small.jpg',
        'position': u'Graduate Student (Molecular, Cellular, and Developmental Biology)',
        'description': u'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    },
    {
        'name': u'Markus Eisele',
        'photo': u'Markus_photo-small.jpg',
        'position': u'Visiting Master’s Student ',
        'description': u'Markus is studying the different behavior of single cells under LPS stress compared to cells in a population. He is using computational modeling and systems analysis to explore TLR4 signaling. Markus is a Master’s student in Stuttgart, Germany and is visiting Yale University for one year.',
    },
]
for person in people:
    person['last_name'] = person['name'].split()[-1]
