from unittest import TestCase

from pyprot.protein.aminoacid import AminoAcid


class TestAminoAcid(TestCase):
    def canCreateAminoAcid(self, name):
        try:
            aa = AminoAcid(name)
        except ValueError:
            self.fail()

    def test_getNames(self):
        for nameMode in ("short", "medium", "long"):
            for name in AminoAcid.getNames(nameMode):
                self.canCreateAminoAcid(name)

    def test_getAllNames(self):
        for nameMode in ("short", "medium", "long"):
            for name in AminoAcid.getAllNames(nameMode):
                self.canCreateAminoAcid(name)

    def test_getName(self):
        aa = AminoAcid("ala")
        self.assertEquals("A", aa.getName())

    def test_isGap(self):
        aa = AminoAcid("gap")
        self.assertTrue(aa.isGap())

    def test_isTermination(self):
        aa = AminoAcid("term")
        self.assertTrue(aa.isTermination())

if __name__ == "__main__":
    TestAminoAcid.main()