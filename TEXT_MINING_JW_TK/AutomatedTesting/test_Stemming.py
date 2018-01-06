import unittest
from stemming.casesDatabase import *


class Test_Stemming(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_Topic(self):
        l=["boleć", "ból", "bólcie", "bólcież", "bolał", "bolała", "bolałaby", "bolałabym", "bolałabyś", "bolałam", "bolałaś", "bolałby", "bolałbym", "bolałbyś", "bolałem", "bolałeś", "bolało", "bolałoby", "bolały", "bolałyby", "bolałybyście", "bolałybyśmy", "bolałyście", "bolałyśmy", "bolano", "bolą", "boląc", "boląca", "bolącą", "bolące", "bolącego", "bolącej", "bolącemu", "bolący", "bolących", "bolącym", "bolącymi", "boleli", "boleliby", "bolelibyście", "bolelibyśmy", "boleliście", "boleliśmy", "bolenia", "boleniach", "boleniami", "bolenie", "boleniem", "boleniom", "boleniu", "boleń", "bolę", "boli", "bolicie", "bolimy", "bolisz", "bólmy", "bólmyż", "bólże", "nieboląca", "niebolącą", "niebolące", "niebolącego", "niebolącej", "niebolącemu", "niebolący", "niebolących", "niebolącym", "niebolącymi", "niebolenia", "nieboleniach", "nieboleniami", "niebolenie", "nieboleniem", "nieboleniom", "nieboleniu", "nieboleń"]
        s =findStem(l)
        suf = wordsMinusStem(stem=s,words=l)
        self.assertEqual(s,"b?l")
        
        l = ["robić", "nierobiąca", "nierobiącą", "nierobiące", "nierobiącego", "nierobiącej", "nierobiącemu", "nierobiący", "nierobiących", "nierobiącym", "nierobiącymi", "nierobieni", "nierobienia", "nierobieniach", "nierobieniami", "nierobienie", "nierobieniem", "nierobieniom", "nierobieniu", "nierobień", "nierobiona", "nierobioną", "nierobione", "nierobionego", "nierobionej", "nierobionemu", "nierobiony", "nierobionych", "nierobionym", "nierobionymi", "robi", "robią", "robiąc", "robiąca", "robiącą", "robiące", "robiącego", "robiącej", "robiącemu", "robiący", "robiących", "robiącym", "robiącymi", "robicie", "robieni", "robienia", "robieniach", "robieniami", "robienie", "robieniem", "robieniom", "robieniu", "robień", "robię", "robili", "robiliby", "robilibyście", "robilibyśmy", "robiliście", "robiliśmy", "robił", "robiła", "robiłaby", "robiłabym", "robiłabyś", "robiłam", "robiłaś", "robiłby", "robiłbym", "robiłbyś", "robiłem", "robiłeś", "robiło", "robiłoby", "robiły", "robiłyby", "robiłybyście", "robiłybyśmy", "robiłyście", "robiłyśmy", "robimy", "robiona", "robioną", "robione", "robionego", "robionej", "robionemu", "robiono", "robiony", "robionych", "robionym", "robionymi", "robisz", "rób", "róbcie", "róbcież", "róbmy", "róbmyż", "róbże"]
        s =findStem(l)
        suf = wordsMinusStem(stem=s,words=l)
        self.assertEqual(s,"r?b")
        
        l = ["Kapetyng", "Kapetynga", "Kapetyngach", "Kapetyngami", "Kapetyngi", "Kapetyngiem", "Kapetyngom", "Kapetyngowi", "Kapetyngowie", "Kapetyngów", "Kapetyngu"]
        s =findStem(l)
        suf = wordsMinusStem(stem=s,words=l)
        self.assertEqual(s,"Kapetyng")


        l = ["incydencik", "incydencikach", "incydencikami", "incydenciki", "incydencikiem", "incydencikom", "incydencikowi", "incydencików", "incydenciku"]
        s =findStem(l)
        suf = wordsMinusStem(stem=s,words=l)
        self.assertEqual(s,"incydencik")


        l= ["indukować", "indukowali", "indukowaliby", "indukowalibyście", "indukowalibyśmy", "indukowaliście", "indukowaliśmy", "indukował", "indukowała", "indukowałaby", "indukowałabym", "indukowałabyś", "indukowałam", "indukowałaś", "indukowałby", "indukowałbym", "indukowałbyś", "indukowałem", "indukowałeś", "indukowało", "indukowałoby", "indukowały", "indukowałyby", "indukowałybyście", "indukowałybyśmy", "indukowałyście", "indukowałyśmy", "indukowana", "indukowaną", "indukowane", "indukowanego", "indukowanej", "indukowanemu", "indukowani", "indukowania", "indukowaniach", "indukowaniami", "indukowanie", "indukowaniem", "indukowaniom", "indukowaniu", "indukowano", "indukowany", "indukowanych", "indukowanym", "indukowanymi", "indukowań", "indukuj", "indukują", "indukując", "indukująca", "indukującą", "indukujące", "indukującego", "indukującej", "indukującemu", "indukujący", "indukujących", "indukującym", "indukującymi", "indukujcie", "indukujcież", "indukuje", "indukujecie", "indukujemy", "indukujesz", "indukuję", "indukujmy", "indukujmyż", "indukujże", "nieindukowana", "nieindukowaną", "nieindukowane", "nieindukowanego", "nieindukowanej", "nieindukowanemu", "nieindukowani", "nieindukowania", "nieindukowaniach", "nieindukowaniami", "nieindukowanie", "nieindukowaniem", "nieindukowaniom", "nieindukowaniu", "nieindukowany", "nieindukowanych", "nieindukowanym", "nieindukowanymi", "nieindukowań", "nieindukująca", "nieindukującą", "nieindukujące", "nieindukującego", "nieindukującej", "nieindukującemu", "nieindukujący", "nieindukujących", "nieindukującym", "nieindukującymi"]
        s =findStem(l)
        suf = wordsMinusStem(stem=s,words=l)
        self.assertEqual(s,"induk")

        l= ["pies", " psa", "psach", "psami", "psem", "psie", "psom", "psów", "psu", "psy", "nienajpies"]
        s =findStem(l)
        suf = wordsMinusStem(stem=s,words=l)
        self.assertEqual(s,"p?s")


        l= ["być", "bądź", "bądźcie", "bądźcież", "bądźmy", "bądźmyż", "bądźże", "będą", "będąc", "będąca", "będącą", "będące", "będącego", "będącej", "będącemu", "będący", "będących", "będącym", "będącymi", "będę", "będzie", "będziecie", "będziemy", "będziesz", "bycia", "byciach", "byciami", "bycie", "byciem", "byciom", "byciu", "byli", "byliby", "bylibyście", "bylibyśmy", "byliście", "byliśmy", "był", "była", "byłaby", "byłabym", "byłabyś", "byłam", "byłaś", "byłby", "byłbym", "byłbyś", "byłem", "byłeś", "było", "byłoby", "były", "byłyby", "byłybyście", "byłybyśmy", "byłyście", "byłyśmy", "byto", "jest", "jestem", "jesteś", "jesteście", "jesteśmy", "niebędąca", "niebędącą", "niebędące", "niebędącego", "niebędącej", "niebędącemu", "niebędący", "niebędących", "niebędącym", "niebędącymi", "niebycia", "niebyciach", "niebyciami", "niebycie", "niebyciem", "niebyciom", "niebyciu", "niebyć", "są"]
        s =findStem(l)
        suf = wordsMinusStem(stem=s,words=l)
        self.assertEqual(s,"#być")



if __name__ == '__main__':
    unittest.main()
