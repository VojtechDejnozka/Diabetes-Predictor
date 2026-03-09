def predict_diabetes(glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):

    """ Predictor for Diabetes from model/67bc2fe854e70fb808f13db3

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] at UCI[*] Machine Learning Repository[*]
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI: http://cml.ics.uci.edu/
        [*]Machine Learning Repository: http://archive.ics.uci.edu/ml/index.html
    """

    if (bmi is None):
        return 'false'
    if (bmi > 26.92401):
        if (glucose is None):
            return 'false'
        if (glucose > 129):
            if (bmi > 30.25417):
                if (insulin is None):
                    return 'true'
                if (insulin > 629):
                    return 'false'
                if (insulin <= 629):
                    if (age is None):
                        return 'true'
                    if (age > 30):
                        if (diabetes_pedigree is None):
                            return 'true'
                        if (diabetes_pedigree > 1.407):
                            if (skinfold is None):
                                return 'false'
                            if (skinfold > 17):
                                return 'true'
                            if (skinfold <= 17):
                                return 'false'
                        if (diabetes_pedigree <= 1.407):
                            if (blood_pressure is None):
                                return 'true'
                            if (blood_pressure > 65):
                                if (diabetes_pedigree > 0.43113):
                                    if (bmi > 38.6):
                                        if (skinfold is None):
                                            return 'true'
                                        if (skinfold > 43):
                                            return 'false'
                                        if (skinfold <= 43):
                                            if (blood_pressure > 77):
                                                if (skinfold > 40):
                                                    return 'true'
                                                if (skinfold <= 40):
                                                    if (blood_pressure > 89):
                                                        return 'true'
                                                    if (blood_pressure <= 89):
                                                        if (age > 38):
                                                            return 'false'
                                                        if (age <= 38):
                                                            if (blood_pressure > 83):
                                                                return 'false'
                                                            if (blood_pressure <= 83):
                                                                return 'true'
                                            if (blood_pressure <= 77):
                                                return 'true'
                                    if (bmi <= 38.6):
                                        if (blood_pressure > 69):
                                            return 'true'
                                        if (blood_pressure <= 69):
                                            if (diabetes_pedigree > 0.7315):
                                                return 'true'
                                            if (diabetes_pedigree <= 0.7315):
                                                return 'false'
                                if (diabetes_pedigree <= 0.43113):
                                    if (diabetes_pedigree > 0.16125):
                                        if (blood_pressure > 98):
                                            return 'true'
                                        if (blood_pressure <= 98):
                                            if (bmi > 34.3):
                                                if (skinfold is None):
                                                    return 'true'
                                                if (skinfold > 34):
                                                    return 'true'
                                                if (skinfold <= 34):
                                                    if (insulin > 45):
                                                        return 'true'
                                                    if (insulin <= 45):
                                                        if (diabetes_pedigree > 0.2505):
                                                            return 'true'
                                                        if (diabetes_pedigree <= 0.2505):
                                                            if (age > 34):
                                                                return 'false'
                                                            if (age <= 34):
                                                                return 'true'
                                            if (bmi <= 34.3):
                                                if (insulin > 33):
                                                    return 'false'
                                                if (insulin <= 33):
                                                    if (blood_pressure > 74):
                                                        if (diabetes_pedigree > 0.3465):
                                                            return 'false'
                                                        if (diabetes_pedigree <= 0.3465):
                                                            if (skinfold is None):
                                                                return 'false'
                                                            if (skinfold > 24):
                                                                return 'false'
                                                            if (skinfold <= 24):
                                                                if (blood_pressure > 81):
                                                                    return 'true'
                                                                if (blood_pressure <= 81):
                                                                    return 'false'
                                                    if (blood_pressure <= 74):
                                                        return 'true'
                                    if (diabetes_pedigree <= 0.16125):
                                        return 'true'
                            if (blood_pressure <= 65):
                                return 'true'
                    if (age <= 30):
                        if (glucose > 160):
                            if (age > 25):
                                if (diabetes_pedigree is None):
                                    return 'true'
                                if (diabetes_pedigree > 0.3055):
                                    return 'true'
                                if (diabetes_pedigree <= 0.3055):
                                    if (blood_pressure is None):
                                        return 'false'
                                    if (blood_pressure > 67):
                                        if (bmi > 45.6):
                                            return 'false'
                                        if (bmi <= 45.6):
                                            return 'true'
                                    if (blood_pressure <= 67):
                                        return 'false'
                            if (age <= 25):
                                return 'true'
                        if (glucose <= 160):
                            if (insulin > 261):
                                if (insulin > 512):
                                    return 'true'
                                if (insulin <= 512):
                                    if (blood_pressure is None):
                                        return 'false'
                                    if (blood_pressure > 61):
                                        return 'false'
                                    if (blood_pressure <= 61):
                                        return 'true'
                            if (insulin <= 261):
                                if (blood_pressure is None):
                                    return 'true'
                                if (blood_pressure > 61):
                                    if (insulin > 207):
                                        return 'true'
                                    if (insulin <= 207):
                                        if (blood_pressure > 85):
                                            if (glucose > 138):
                                                return 'true'
                                            if (glucose <= 138):
                                                return 'false'
                                        if (blood_pressure <= 85):
                                            if (blood_pressure > 72):
                                                if (bmi > 32):
                                                    return 'false'
                                                if (bmi <= 32):
                                                    if (bmi > 31.4):
                                                        return 'true'
                                                    if (bmi <= 31.4):
                                                        return 'false'
                                            if (blood_pressure <= 72):
                                                if (bmi > 33.75):
                                                    if (diabetes_pedigree is None):
                                                        return 'true'
                                                    if (diabetes_pedigree > 0.617):
                                                        return 'false'
                                                    if (diabetes_pedigree <= 0.617):
                                                        return 'true'
                                                if (bmi <= 33.75):
                                                    if (blood_pressure > 69):
                                                        if (skinfold is None):
                                                            return 'false'
                                                        if (skinfold > 19):
                                                            return 'false'
                                                        if (skinfold <= 19):
                                                            return 'true'
                                                    if (blood_pressure <= 69):
                                                        return 'false'
                                if (blood_pressure <= 61):
                                    return 'true'
            if (bmi <= 30.25417):
                if (glucose > 165):
                    if (insulin is None):
                        return 'true'
                    if (insulin > 62):
                        return 'true'
                    if (insulin <= 62):
                        if (skinfold is None):
                            return 'true'
                        if (skinfold > 23):
                            return 'false'
                        if (skinfold <= 23):
                            return 'true'
                if (glucose <= 165):
                    if (blood_pressure is None):
                        return 'false'
                    if (blood_pressure > 23):
                        if (diabetes_pedigree is None):
                            return 'false'
                        if (diabetes_pedigree > 0.553):
                            return 'false'
                        if (diabetes_pedigree <= 0.553):
                            if (blood_pressure > 84):
                                return 'false'
                            if (blood_pressure <= 84):
                                if (bmi > 27.85):
                                    if (age is None):
                                        return 'true'
                                    if (age > 56):
                                        return 'false'
                                    if (age <= 56):
                                        if (diabetes_pedigree > 0.38):
                                            if (skinfold is None):
                                                return 'false'
                                            if (skinfold > 17):
                                                return 'false'
                                            if (skinfold <= 17):
                                                if (diabetes_pedigree > 0.488):
                                                    return 'true'
                                                if (diabetes_pedigree <= 0.488):
                                                    return 'false'
                                        if (diabetes_pedigree <= 0.38):
                                            if (diabetes_pedigree > 0.305):
                                                return 'true'
                                            if (diabetes_pedigree <= 0.305):
                                                if (age > 39):
                                                    return 'true'
                                                if (age <= 39):
                                                    return 'false'
                                if (bmi <= 27.85):
                                    return 'false'
                    if (blood_pressure <= 23):
                        return 'true'
        if (glucose <= 129):
            if (glucose > 100):
                if (diabetes_pedigree is None):
                    return 'false'
                if (diabetes_pedigree > 0.93908):
                    if (diabetes_pedigree > 1.3955):
                        return 'false'
                    if (diabetes_pedigree <= 1.3955):
                        if (skinfold is None):
                            return 'true'
                        if (skinfold > 41):
                            if (skinfold > 44):
                                if (bmi > 38):
                                    return 'false'
                                if (bmi <= 38):
                                    return 'true'
                            if (skinfold <= 44):
                                return 'false'
                        if (skinfold <= 41):
                            return 'true'
                if (diabetes_pedigree <= 0.93908):
                    if (insulin is None):
                        return 'false'
                    if (insulin > 11):
                        if (bmi > 45.44167):
                            if (insulin > 235):
                                return 'false'
                            if (insulin <= 235):
                                return 'true'
                        if (bmi <= 45.44167):
                            if (diabetes_pedigree > 0.50574):
                                if (blood_pressure is None):
                                    return 'false'
                                if (blood_pressure > 82):
                                    return 'false'
                                if (blood_pressure <= 82):
                                    if (glucose > 109):
                                        if (skinfold is None):
                                            return 'false'
                                        if (skinfold > 21):
                                            if (glucose > 113):
                                                if (glucose > 120):
                                                    if (insulin > 154):
                                                        if (age is None):
                                                            return 'false'
                                                        if (age > 26):
                                                            if (skinfold > 37):
                                                                return 'false'
                                                            if (skinfold <= 37):
                                                                return 'true'
                                                        if (age <= 26):
                                                            if (diabetes_pedigree > 0.602):
                                                                if (diabetes_pedigree > 0.7085):
                                                                    return 'false'
                                                                if (diabetes_pedigree <= 0.7085):
                                                                    return 'true'
                                                            if (diabetes_pedigree <= 0.602):
                                                                return 'false'
                                                    if (insulin <= 154):
                                                        return 'false'
                                                if (glucose <= 120):
                                                    return 'true'
                                            if (glucose <= 113):
                                                return 'false'
                                        if (skinfold <= 21):
                                            return 'false'
                                    if (glucose <= 109):
                                        if (age is None):
                                            return 'true'
                                        if (age > 24):
                                            if (glucose > 103):
                                                return 'true'
                                            if (glucose <= 103):
                                                return 'false'
                                        if (age <= 24):
                                            if (diabetes_pedigree > 0.5575):
                                                return 'false'
                                            if (diabetes_pedigree <= 0.5575):
                                                return 'true'
                            if (diabetes_pedigree <= 0.50574):
                                if (insulin > 111):
                                    if (blood_pressure is None):
                                        return 'false'
                                    if (blood_pressure > 87):
                                        return 'true'
                                    if (blood_pressure <= 87):
                                        if (age is None):
                                            return 'false'
                                        if (age > 32):
                                            if (age > 49):
                                                return 'false'
                                            if (age <= 49):
                                                if (skinfold is None):
                                                    return 'true'
                                                if (skinfold > 20):
                                                    if (insulin > 288):
                                                        return 'false'
                                                    if (insulin <= 288):
                                                        if (diabetes_pedigree > 0.27):
                                                            if (diabetes_pedigree > 0.3595):
                                                                return 'true'
                                                            if (diabetes_pedigree <= 0.3595):
                                                                return 'false'
                                                        if (diabetes_pedigree <= 0.27):
                                                            return 'true'
                                                if (skinfold <= 20):
                                                    return 'false'
                                        if (age <= 32):
                                            return 'false'
                                if (insulin <= 111):
                                    return 'false'
                    if (insulin <= 11):
                        if (diabetes_pedigree > 0.20269):
                            if (glucose > 122):
                                if (diabetes_pedigree > 0.271):
                                    if (bmi > 39.2):
                                        return 'true'
                                    if (bmi <= 39.2):
                                        if (diabetes_pedigree > 0.3265):
                                            if (glucose > 127):
                                                return 'false'
                                            if (glucose <= 127):
                                                if (glucose > 124):
                                                    return 'true'
                                                if (glucose <= 124):
                                                    if (skinfold is None):
                                                        return 'false'
                                                    if (skinfold > 16):
                                                        return 'false'
                                                    if (skinfold <= 16):
                                                        return 'true'
                                        if (diabetes_pedigree <= 0.3265):
                                            return 'false'
                                if (diabetes_pedigree <= 0.271):
                                    return 'true'
                            if (glucose <= 122):
                                if (bmi > 46.05):
                                    return 'true'
                                if (bmi <= 46.05):
                                    if (glucose > 121):
                                        return 'false'
                                    if (glucose <= 121):
                                        if (age is None):
                                            return 'false'
                                        if (age > 53):
                                            if (blood_pressure is None):
                                                return 'false'
                                            if (blood_pressure > 86):
                                                return 'false'
                                            if (blood_pressure <= 86):
                                                if (age > 61):
                                                    return 'true'
                                                if (age <= 61):
                                                    return 'false'
                                        if (age <= 53):
                                            if (age > 28):
                                                if (blood_pressure is None):
                                                    return 'true'
                                                if (blood_pressure > 58):
                                                    if (glucose > 105):
                                                        if (bmi > 33.9):
                                                            if (bmi > 37.3):
                                                                if (skinfold is None):
                                                                    return 'false'
                                                                if (skinfold > 15):
                                                                    return 'false'
                                                                if (skinfold <= 15):
                                                                    return 'true'
                                                            if (bmi <= 37.3):
                                                                return 'false'
                                                        if (bmi <= 33.9):
                                                            if (diabetes_pedigree > 0.264):
                                                                if (diabetes_pedigree > 0.2685):
                                                                    if (blood_pressure > 70):
                                                                        return 'true'
                                                                    if (blood_pressure <= 70):
                                                                        if (diabetes_pedigree > 0.4255):
                                                                            if (diabetes_pedigree > 0.7205):
                                                                                if (age > 33):
                                                                                    return 'true'
                                                                                if (age <= 33):
                                                                                    return 'false'
                                                                            if (diabetes_pedigree <= 0.7205):
                                                                                return 'false'
                                                                        if (diabetes_pedigree <= 0.4255):
                                                                            return 'true'
                                                                if (diabetes_pedigree <= 0.2685):
                                                                    return 'false'
                                                            if (diabetes_pedigree <= 0.264):
                                                                return 'true'
                                                    if (glucose <= 105):
                                                        return 'true'
                                                if (blood_pressure <= 58):
                                                    return 'false'
                                            if (age <= 28):
                                                if (skinfold is None):
                                                    return 'false'
                                                if (skinfold > 8):
                                                    if (diabetes_pedigree > 0.482):
                                                        if (skinfold > 31):
                                                            if (blood_pressure is None):
                                                                return 'false'
                                                            if (blood_pressure > 77):
                                                                return 'false'
                                                            if (blood_pressure <= 77):
                                                                return 'true'
                                                        if (skinfold <= 31):
                                                            return 'false'
                                                    if (diabetes_pedigree <= 0.482):
                                                        return 'false'
                                                if (skinfold <= 8):
                                                    if (bmi > 43.7):
                                                        return 'false'
                                                    if (bmi <= 43.7):
                                                        return 'true'
                        if (diabetes_pedigree <= 0.20269):
                            if (glucose > 110):
                                if (blood_pressure is None):
                                    return 'false'
                                if (blood_pressure > 78):
                                    return 'false'
                                if (blood_pressure <= 78):
                                    if (bmi > 29.45):
                                        if (bmi > 34.55):
                                            if (age is None):
                                                return 'false'
                                            if (age > 23):
                                                if (blood_pressure > 26):
                                                    return 'true'
                                                if (blood_pressure <= 26):
                                                    return 'false'
                                            if (age <= 23):
                                                return 'false'
                                        if (bmi <= 34.55):
                                            if (bmi > 32):
                                                return 'true'
                                            if (bmi <= 32):
                                                if (age is None):
                                                    return 'true'
                                                if (age > 24):
                                                    return 'true'
                                                if (age <= 24):
                                                    return 'false'
                                    if (bmi <= 29.45):
                                        if (age is None):
                                            return 'false'
                                        if (age > 35):
                                            return 'true'
                                        if (age <= 35):
                                            return 'false'
                            if (glucose <= 110):
                                if (diabetes_pedigree > 0.179):
                                    if (skinfold is None):
                                        return 'false'
                                    if (skinfold > 9):
                                        return 'false'
                                    if (skinfold <= 9):
                                        if (diabetes_pedigree > 0.1855):
                                            return 'false'
                                        if (diabetes_pedigree <= 0.1855):
                                            return 'true'
                                if (diabetes_pedigree <= 0.179):
                                    return 'false'
            if (glucose <= 100):
                if (skinfold is None):
                    return 'false'
                if (skinfold > 30):
                    if (diabetes_pedigree is None):
                        return 'false'
                    if (diabetes_pedigree > 0.47175):
                        if (blood_pressure is None):
                            return 'false'
                        if (blood_pressure > 86):
                            return 'false'
                        if (blood_pressure <= 86):
                            if (age is None):
                                return 'false'
                            if (age > 25):
                                if (skinfold > 32):
                                    if (age > 28):
                                        if (insulin is None):
                                            return 'false'
                                        if (insulin > 24):
                                            if (insulin > 160):
                                                return 'true'
                                            if (insulin <= 160):
                                                return 'false'
                                        if (insulin <= 24):
                                            return 'true'
                                    if (age <= 28):
                                        return 'true'
                                if (skinfold <= 32):
                                    return 'true'
                            if (age <= 25):
                                if (age > 23):
                                    return 'false'
                                if (age <= 23):
                                    if (skinfold > 34):
                                        return 'false'
                                    if (skinfold <= 34):
                                        return 'true'
                    if (diabetes_pedigree <= 0.47175):
                        if (bmi > 31.1):
                            if (blood_pressure is None):
                                return 'false'
                            if (blood_pressure > 79):
                                if (glucose > 28):
                                    return 'false'
                                if (glucose <= 28):
                                    return 'true'
                            if (blood_pressure <= 79):
                                return 'false'
                        if (bmi <= 31.1):
                            if (age is None):
                                return 'true'
                            if (age > 24):
                                return 'true'
                            if (age <= 24):
                                return 'false'
                if (skinfold <= 30):
                    if (glucose > 91):
                        if (age is None):
                            return 'false'
                        if (age > 23):
                            if (diabetes_pedigree is None):
                                return 'false'
                            if (diabetes_pedigree > 0.9375):
                                return 'false'
                            if (diabetes_pedigree <= 0.9375):
                                if (age > 42):
                                    if (insulin is None):
                                        return 'true'
                                    if (insulin > 90):
                                        return 'true'
                                    if (insulin <= 90):
                                        if (diabetes_pedigree > 0.383):
                                            return 'false'
                                        if (diabetes_pedigree <= 0.383):
                                            return 'true'
                                if (age <= 42):
                                    if (skinfold > 26):
                                        return 'false'
                                    if (skinfold <= 26):
                                        if (insulin is None):
                                            return 'false'
                                        if (insulin > 84):
                                            return 'true'
                                        if (insulin <= 84):
                                            if (glucose > 94):
                                                if (insulin > 53):
                                                    return 'false'
                                                if (insulin <= 53):
                                                    if (blood_pressure is None):
                                                        return 'true'
                                                    if (blood_pressure > 70):
                                                        if (age > 33):
                                                            return 'false'
                                                        if (age <= 33):
                                                            return 'true'
                                                    if (blood_pressure <= 70):
                                                        return 'true'
                                            if (glucose <= 94):
                                                return 'false'
                        if (age <= 23):
                            return 'false'
                    if (glucose <= 91):
                        if (age is None):
                            return 'false'
                        if (age > 31):
                            if (diabetes_pedigree is None):
                                return 'false'
                            if (diabetes_pedigree > 0.9955):
                                return 'true'
                            if (diabetes_pedigree <= 0.9955):
                                return 'false'
                        if (age <= 31):
                            return 'false'
    if (bmi <= 26.92401):
        if (glucose is None):
            return 'false'
        if (glucose > 148):
            if (blood_pressure is None):
                return 'true'
            if (blood_pressure > 61):
                if (blood_pressure > 71):
                    if (age is None):
                        return 'true'
                    if (age > 25):
                        if (age > 62):
                            return 'false'
                        if (age <= 62):
                            if (diabetes_pedigree is None):
                                return 'true'
                            if (diabetes_pedigree > 0.2185):
                                return 'true'
                            if (diabetes_pedigree <= 0.2185):
                                if (age > 48):
                                    return 'true'
                                if (age <= 48):
                                    return 'false'
                    if (age <= 25):
                        return 'false'
                if (blood_pressure <= 71):
                    return 'true'
            if (blood_pressure <= 61):
                return 'false'
        if (glucose <= 148):
            if (glucose > 103):
                if (insulin is None):
                    return 'false'
                if (insulin > 117):
                    return 'false'
                if (insulin <= 117):
                    if (diabetes_pedigree is None):
                        return 'false'
                    if (diabetes_pedigree > 0.21333):
                        if (bmi > 9.2):
                            if (age is None):
                                return 'false'
                            if (age > 29):
                                if (diabetes_pedigree > 0.2845):
                                    return 'false'
                                if (diabetes_pedigree <= 0.2845):
                                    if (diabetes_pedigree > 0.2725):
                                        return 'true'
                                    if (diabetes_pedigree <= 0.2725):
                                        return 'false'
                            if (age <= 29):
                                if (age > 27):
                                    return 'true'
                                if (age <= 27):
                                    if (blood_pressure is None):
                                        return 'false'
                                    if (blood_pressure > 63):
                                        return 'false'
                                    if (blood_pressure <= 63):
                                        if (bmi > 25.8):
                                            return 'false'
                                        if (bmi <= 25.8):
                                            if (age > 21):
                                                return 'true'
                                            if (age <= 21):
                                                return 'false'
                        if (bmi <= 9.2):
                            if (age is None):
                                return 'false'
                            if (age > 27):
                                return 'true'
                            if (age <= 27):
                                return 'false'
                    if (diabetes_pedigree <= 0.21333):
                        return 'false'
            if (glucose <= 103):
                return 'false'