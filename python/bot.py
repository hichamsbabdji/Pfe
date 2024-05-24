def chatbot(message):
    if "bonjour" in message.lower():
        return "Bonjour "
    elif "j'ai un problème avec mon ordinateur portable" in message.lower():
        return "Est-ce un problème matériel ou logiciel ?"
    elif "je ne peux pas identifier cela avec précision." in message.lower():
        return "Le problème est-il survenu lors de la mise sous tension de l'ordinateur ou de l'installation d'un nouveau logiciel ?"
    elif "lorsque vous allumez l'ordinateur" in  message.lower():
        return """Voici les problèmes courants auxquels vous pourriez être confronté lors du démarrage de votre ordinateur : \n
                [01] Non-démarrage : L'ordinateur peut ne pasin démarrer du tout en 
                     raison de problèmes d'alimentation, de la carte mère,
                     de câbles endommagés ou d'autres composants défectueux.\n
                [02] Arrêt pendant le démarrage : L'ordinateur peut s'arrêter en cours de démarrage
                     en raison de problèmes logiciels, de conflits matériels ou de problèmes de refroidissement.\n
                [03] Messages d'erreur : Vous pouvez rencontrer des messages d'erreur à l'écran pendant le démarrage,
                     indiquant des problèmes avec le disque dur, la mémoire ou d'autres composants système.\n
                [04] Démarrage lent : L'ordinateur peut démarrer lentement en raison delogiciels en arrière-plan,
                     de mises à jour automatiques ou de problèmes de disque dur.\n
                [05] Écran bleu ou gel du système : Vous pouvez voir un écran bleu ou le système peut se figer pendant le démarrage,
                     ce qui indique généralement des problèmes matériels ou logiciels.\n
                     Ce sont quelques-uns des problèmes courants que vous ourriez  rencontrer au démarrage de votre ordinateur, 
                     mais il existe également de nombreux autres problèmes possibles."""
    elif "lors de l'installation d'un nouveau logiciel sur l'ordinateur" in message.lower(): 
         return """Voici quelques problèmes courants que vous pourriez rencontrer lors 
                     de l'installation d'un nouveau programme sur votre ordinateur :\n
                [01] Conflits de programmes : Un nouveau programme peut entrer en conflit avec 
                     d'autres programmes déjà installés sur l'ordinateur,
                     ce qui peut entraîner des problèmes de performance ou même des plantages du système.\n
                [02] Utilisation importante des ressources : Le nouveau programme peut consommer beaucoup de ressources système,
                     ce qui peut ralentir le système ou le rendre instable.\n
                [03] Problèmes d'installation : Vous pourriez rencontrer des problèmes lors de l'installation,
                     tels que des messages d'erreur ou une installation incomplète.\n
                [04] Impact sur la sécurité : L'installation d'un nouveau programme peut ouvrir des failles de sécurité dans le système,
                     exposant l'ordinateur à des risques de piratage ou de logiciels malveillants.\n
                     Ces problèmes sont parmi les plus courants que vous pourriez rencontrer
                     lors de l'installation d'un nouveau programme sur votre ordinateur. Pour éviter ces problèmes,
                     il est important de rechercher le programme avant de l'installer,
                     de vous assurer de sa compatibilité avec votre système d'exploitation et les ressources disponibles sur votre ordinateur,
                     et de mettre régulièrement à jour vos programmes pour garantir la sécurité et la stabilité.\n """
    elif "conseil" in message.lower():
        return """[01] Nettoyez régulièrement votre ordinateur.
                  [02] Gardez-le à l'abri de la chaleur et de l'humidité. 
                  [03] Utilisez un logiciel antivirus et antimalware.
                  [04] Mettez à jour votre système d'exploitation et vos logiciels.
                  [05] Supprimez les programmes inutiles.
                  [06] Sauvegardez régulièrement vos données.
                  [07] Gérez les applications au démarrage.
                  [08] Surveillez la température de votre ordinateur.
                  [09] Utilisez un onduleur.
                  [10] Consultez un professionnel si nécessaire. """
    elif "aide"    in message.lower():
        return """Liste des commandes :
                   /bonjour
                   /j'ai un problème avec mon ordinateur portable            
                   /lorsque vous allumez l'ordinateur
                   /lors de l'installation d'un nouveau logiciel sur l'ordinateur
                   /conseil"""
    else: 
        return "Désolé, je ne comprends pas. Pouvez-vous reformuler votre question ?"

while True:
    user_input = input("Vous: /")
    if user_input.lower() == "bye":
        print("Chatbot arrêté ")
        break
    else:
        response = chatbot(user_input)
        print("Chatbot:", response)
