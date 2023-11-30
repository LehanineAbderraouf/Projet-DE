# Projet-DE

<h1 align="center">
  :bar_chart: Un Modèle de Clustering et Réduction de la dimensionalité :bar_chart:
</h1>

<div align="center">
  <img src="https://15d.co/wp-content/uploads/2018/04/3loaders.gif" width="900" height="300"/>
</div>

---

## But de projet

- Utiliser des méthods de réduction de la dimensionalité (ACP, AFC et UMAP)
- Déveloper un modèle de Clustering en utilisant la méthod Kmeans de scikit-learn.
- Tester le sur le data set 20newsgroups et l'évaluer en utilisant NMI et ARI.

## Contenu du Repository

- `main.py` : Le fichier principal pour appliquer et évaluer les différentes approches.
- `Dimensionality_Reduction_Functions/dimred_umap.py`, `Dimensionality_Reduction_Functions/dimred_acp.py`, `Dimensionality_Reduction_Functions/dimred_afc.py` : Les differentes fonctions des méthods de réduction de la dimensionalité.
- `Clustering_Methods/clust.py` : Les fonctions Kmeans, Agglomerative CLustering et Kmedoids ainsi que la fonction d'évaluation (Normalized Mutual Information et Adjusted Rand Index).
- `notebooks/` : Les différent notbooks utiliser pendant le dévelopement.

## Instructions pour l'Exécution

1.  Clônez le repository :
	```bash
	git clone https://github.com/LehanineAbderraouf/Projet-DE.git
	cd Projet-DE
	```

2. 	Installez les dépendances :
	```bash
	pip install -r requirements.txt
	```

3. 	Télécharger le modèle en local en exécutant le script `load_model.py`. Le modèle sera sauvgardé dans le dossier `model_directory`.
	```bash
	python load_model.py
	```  

4. 	Exécutez le fichier main.py (acp pour ACP, afc pour AFC et umap pour UMPA. ainsi que kmeans pour kmeans, ac pour Agglomerative Clustering et kmedoids pour KMedoids):
	```bash
	python main.py acp kmeans
	```

## Collaborateurs

- [Lehanine Abderraouf](github.com/LehanineAbderraouf)
- [Nait Said Ahmed](https://github.com/anaitsaid)