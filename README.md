# Projet-DE

<h1>
  :bar_chart: Un Modèle de Clustering (Kmeans) et Réduction de la dimensionalité via l'ACP, l'AFC et UMAP :bar_chart:
</h1>

<div align="center">
  <img src="https://f8n-production.imgix.net/creators/profile/qigfy9rck-ezgif-com-gif-maker-16-gif-dmbjsd.gif" width="800" height="300"/>
</div>

---

## But de projet

- Utiliser des méthods de réduction de la dimensionalité (ACP, AFC et UMAP)
- Déveloper un modèle de Clustering en utilisant la méthod Kmeans de scikit-learn.
- Tester le sur le data set 20newsgroups .

## Contenu du Repository

- `main.py` : Le fichier principal pour appliquer et évaluer les différentes approches.
- `Dimensionality Reduction Functions/dimred_umap.py`, `Dimensionality Reduction Functions/dimred_acp.py`, `Dimensionality Reduction Functions/dimred_afc.py` : Les differentes fonctions des méthods de réduction de la dimensionalité.
- `Clustering Methods/clust.py` : La fonction de Kmeans et la fonction d'évaluation (Normalized Mutual Information et Adjusted Rand Index).
- `notebooks/` : Les différent notbooks utiliser pendant le dévelopement.

## Instructions pour l'Exécution

1.  Clônez le repository :
	```bash
	git clone https://github.com/ehanineAbderraouf/Projet-DE.git
	cd Projet-DE
	```

2. 	Installez les dépendances :
	```bash
	pip install -r requirements.txt
	```

3. 	Exécutez le fichier main.py (acp pour ACP, afc pour AFC et umap pour UMPA):
	```bash
	python main.py acp
	```

## Collaborateurs

- [Lehanine Abderraouf](github.com/LehanineAbderraouf)
- [Nait Said Ahmed](https://github.com/anaitsaid)
