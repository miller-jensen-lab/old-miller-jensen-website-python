# -*- coding: utf-8 -*-
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
        'description': u'Victor is studying how cell-to-cell heterogeneity in NF-kB dynamics and chromatin environment combine to regulate transcriptional activation of latent HIV. He is using a combination of live-cell imaging and single molecular fluorescence in situ hybridization (smFISH) to observe latent HIV activation in single cells. His interests include molecular biology, microscopy, biological noise and signal transduction. Victor received his Bachelor’s degree in Biology from the University of Pennsylvania.',
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
