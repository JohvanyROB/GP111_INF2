# GP111 - INF2 - Gustave

## Installer Pygame
Pygame est une bibliothèque codée en Python qui sera utilisée pour développer votre jeu.</br></br>
Afin de l'installer **sur Windows**, ouvrez un terminal (ou invité de commande) et exécutez l'instruction suivante:
```bash
pip install pygame
```

Afin de l'installer **sur MAC OS**, ouvrez un terminal et exécutez l'instruction suivante:
```bash
pip3 install pygame
```

Appelez l'enseignant si une erreur survient lors de l'installation de Pygame.


## Télécharger Visual Studio Code (VS Code)
Afin de gérer aisément le projet, vous utiliserez VS Code. Si vous ne l'avez pas encore installé, cliquez sur [ce lien](https://code.visualstudio.com/download) puis suivez les étapes d'installation.


## Télécharger et configurer git
Vérifiez que git ne soit pas installé en ouvrant un terminal puis en rentrant: **git**. Si un message d'erreur apparait, cela signifie que git n'est pas encore installé. Dans ce cas, cliquez sur [ce lien](https://git-scm.com/downloads) puis suivez les étapes d'installation en fonction de votre système d'exploitation (MAC OS ou Windows).


## Configurer git pour GitHub
Si vous n'avez pas encore de compte sur la plateforme GitHub, cliquez sur [ce lien](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home).</br></br>
Une fois le compte créé, ouvrez un terminal puis configurez les informations permettant à git de manipuler par la suite vos dépôts:
```bash
git config --global user.name "[Votre nom d'utilisateur GitHub sans les crochets]"
git config --global user.email "[l'adresse email associée à votre compte GitHub sans les crochets]"
```

## Cloner le dépôt GitHub
Vous allez maintenant créer une copie locale de ce dépôt dans l'un des répertoires de votre ordinateur. Il s'agit de l'étape de **clonage**.
1. Copiez l'url du dépôt GitHub.
2. Depuis VS Code, cliquez sur les touches **Ctrl + Shift + P** (sur Windows) ou **Cmd + Shift + P** (sur MAC OS) afin d'ouvrir la palette de commandes.
3. Tapez **clone** puis cliquez sur **Git:clone**.
4. Renseignez l'url que vous avez copiée lors de l'étape 1 puis pressez la touche "Entrée".
5. Dans la fenêtre pop-up, sélectionnez l'emplacement où vous souhaitez cloner le dépôt.


Une alternative est d'ouvrir un terminal et de renseigner les instructions suivantes:
```bash
cd [desired_path] #appelez l'enseignant si vous n'êtes pas sûr de vous.
git clone [url]
```