##     Aide à la décision et amélioration de service de l’application « WASSALI »
Ce sujet se penche sur l’application de la science des données et des techniques de machine
learning dans le domaine de la logistique. En effet, les techniques de data science et d’IA
peuvent aider les entreprises de transport à optimiser leurs opérations et trouver des moyens
pour réduire les coûts d’expédition sans sacrifier le service ou la rapidité.
Dans ce cadre, la société a confié à Mohamed la tâche de la recherche de solutions
intelligentes permettant la progression des mécanismes de travail de l'entreprise. Après une
longue étape de recherche et de réflexion, l’étudiant a pu identifier plusieurs pistes
d'amélioration à l'instar de recommander à un client un moyen du transport adéquat à la
marchandise à transporter, estimer les tarifs des courses, élaborer un chat bot intelligent pour
le service client, et plusieurs autres axes d'intérêt axés sur l’amélioration du service de
l'entreprise.
Étant donné les priorités de l'organisme d'accueil et la durée de stage, l’objectif essentiel de ce
sujet de mastère a été axé sur la mise en place de deux solutions intelligentes parmi celles
proposées:
• un module de recommandation du moyen de transport adéquat qui vise à minimiser le
cout d’expédition à la fois pour le client et le transporteur. En effet, un client qui
désire transporter une marchandise ne peut pas nécessairement sélectionner le meilleur
véhicule pour son besoin. Ceci peut engendrer plusieurs problèmes : un cout élevé, de
l’espace vide gaspillé ou pire un moyen de transport ne permettant pas de transporter
la marchandise. Ainsi, le module à proposer vise à prédire le moyen de transport
adéquat pour chaque commande du client et consiste alors à une aide à la décision
pour le client dans sa procédure de lancement d’une commande.
• un module de tarification qui vise à estimer les tarifs des courses et proposer ce prix au
client et fournisseur.
Pour le premier module, Mohamed a commencé par la collecte des données. Cette étape
consistait à recueillir, par web scrapping, des images des différentes marchandises ainsi que
plusieurs types d’objets à transporter, pour former les bases de données nécessaires pour
l’entraînement des modèles de deep learning. Il a ensuite préparé, annoté et augmenté ces

données en exploitant différentes approches et techniques de traitement et d’augmentation des
données.%
Une fois la base de données préparée, deux méthodes ont été proposées pour résoudre le
problème de recommandation du moyen de transport adéquat://
• la première méthode consistait à formuler le problème comme un problème de
classification où une image d’entrée représente une marchandise et son label (classe)
est le moyen de transport adéquat permettant de la transporter aux moindres couts.
Pour cela, Mohamed a effectué une expérimentation détaillée, en exploitant des
modèles de différentes architectures (CNN, MobileNet, ResNet, VGG, ..) et des
techniques de transfer learning et de fine tuning, afin de sélectionner les meilleurs
modèles à déployer.//
• la deuxième méthode consistait à formuler le problème comme un problème de
dénombrement d’objets où une image d’entrée représente une marchandise à
transporter pouvant comporter un ou plusieurs objets. Pour cela, Mohamed a testé des
méthodes de détection et dénombrement d’objets à savoir le réseau Yolo afin de
comprendre ce que représente une image (marchandise) et ainsi pouvoir recommander
le moyen de transport qui lui est adéquat.//
Ce premier module a été déployé sous forme de backend (avec fastAPI) et de frontend (avec
Bootstrap).//
Pour le deuxième module, l’étudiant a proposé une formule pour le calcul du tarif d’une
course en se basant sur plusieurs attributs et données, et après une étude des méthodes de
tarification élaborées dans le domaine de transport et de logistique. Ce module de tarification
a été implémenté au sein de l’application Android Wassali et est actuellement en cours de test
auprès des clients de ce service.//
Pour conclure sur la pertinence du travail effectué, l’étudiant a réalisé plusieurs séries de tests
qui ont démontré que les modèles déployés ont atteint des taux d’accuracy, de précision et de
rappel approchant les 80%. //
Ces résultats sont encourageants et montrent l'efficacité des
solutions proposées.
