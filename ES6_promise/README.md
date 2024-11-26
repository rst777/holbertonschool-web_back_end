# ES6 Promises
## Promise

1. Baseline Widely available
L'objet Promise (pour « promesse ») est utilisé pour réaliser des traitements de façon asynchrone. Une promesse représente une valeur qui peut être disponible maintenant, dans le futur voire jamais.

Note: Cette fonctionnalité est disponible via les Web Workers.

Pour apprendre comment fonctionnent les promesses et comment les utiliser, nous vous conseillons de commencer par l'article Utiliser les promesses du guide JavaScript.

2. Description
L'interface Promise représente un intermédiaire (proxy) vers une valeur qui n'est pas nécessairement connue au moment de la création de la promesse. Cela permet d'associer des gestionnaires au succès éventuel d'une action asynchrone et à la raison d'une erreur. Ainsi, les méthodes asynchrones peuvent renvoyer des valeurs de manière similaire aux méthodes synchrones, la seule différence est que la valeur retournée par la méthode asynchrone est une promesse (d'avoir une valeur plus tard).

## Une Promise est dans un de ces états :

pending (en attente) : état initial, la promesse n'est ni tenue, ni rompue ;
fulfilled (tenue) : l'opération a réussi ;
rejected (rompue) : l'opération a échoué.
Une promesse en attente peut être tenue avec une valeur ou rompue avec une raison (erreur). Quand on arrive à l'une des deux situations, les gestionnaires associés lors de l'appel de la méthode then sont alors appelés. Si la promesse a déjà été tenue ou rompue lorsque le gestionnaire est attaché à la promesse, le gestionnaire est appelé. Cela permet qu'il n'y ait pas de situation de compétition entre une opération asynchrone en cours et les gestionnaires ajoutés.

Les méthodes Promise.prototype.then() et Promise.prototype.catch() renvoient des promesses et peuvent ainsi être chaînées. C'est ce qu'on appelle une composition.

![illustration](promises.png "promises")


Schéma illustrant l'enchaînement des différents états possibles d'une promesse et les méthodes associées

1. Note : D'autres langages utilisent des mécanismes d'évaluation à la volée (lazy evaluation) et de déport des calculs (deferring computations). Ces mécanismes sont également intitulés promesses (promises). En JavaScript, les promesses correspondent à des processus déjà lancés et qui peuvent être chaînés avec des fonctions de retour. Si vous cherchez à retarder l'évaluation, vous pouvez utiliser les fonctions fléchées sans arguments (ex. f = () => expression) afin de créer une expression à évaluer plus tard et utiliser f() pour l'évaluer au moment voulu.

1. Note : On dit qu'une promesse est dans l'état settled (acquittée) qu'elle soit tenue ou rompue mais plus en attente. Le terme resolved (résolue) est aussi utilisé concernant les promesses — cela signifie que la promesse est acquittée ou bien enfermée dans une chaine de promesse. Le billet de Domenic Denicola, States and fates (en anglais), contient de plus amples détails sur la terminologie utilisée.
