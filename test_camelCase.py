import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual('ohSayCanYouSee', camelCase.camel_case('OH SAY CAN YOU SEE'))
        self.assertEqual('', camelCase.camel_case(''))
        self.assertEqual('!@#$%^&*()', camelCase.camel_case('!@#$%^&*()'))
        self.assertEqual('helloWorld', camelCase.camel_case('     HELLO   WORLD    '))
        
        self.assertEqual('helloFromPlanetNeptune', camelCase.camel_case('HELLO FROM \n  PLANET NEPTUNE'))
        self.assertEqual('superAwesomeNintendoGame', camelCase.camel_case('SUPER AWESOME NINTENDO GAME'))