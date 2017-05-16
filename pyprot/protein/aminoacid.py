from copy import deepcopy

AA_NAMES = (
    ("none/gap", "gap", "-"),
    ("alanine", "ala", "A"),
    ("cysteine", "cys", "C"),
    ("aspartic acid", "asp", "D"),
    ("glutamic acid", "glu", "E"),
    ("phenylalanine", "phe", "F"),
    ("glycine", "gly", "G"),
    ("histidine", "his", "H"),
    ("isoleucine", "ile", "I"),
    ("lysine", "lys", "K"),
    ("leucine", "leu", "L"),
    ("methionine", "met", "M"),
    ("asparagine", "asn", "N"),
    ("proline", "pro", "P"),
    ("glutamine", "gln", "Q"),
    ("arginine", "arg", "R"),
    ("serine", "ser", "S"),
    ("threonine", "thr", "T"),
    ("valine", "val", "V"),
    ("tryptophan", "trp", "W"),
    ("tyrosine", "tyr", "Y"),
    ("asparagine/aspartic acid", "asx", "B"),
    ("glutamine/glutamic acid", "glx", "Z"),
    ("leucine/isoleucine", "xle", "J"),
    ("selenocysteine", "sec", "U"),
    ("pyrrolysine", "pyl", "O"),
    ("undetermined", "xaa", "X")
)


class AminoAcid:
    """
    Represents one of the amino acids that can be found in genetic sequences.
    Can be one of the twenty-two amino acids, four undetermined combinations of possible amino acids, and gaps.
    """

    # Dictionary mapping name to id
    _nameDict = {AA_NAMES[id][i]: id for i in range(3) for id in range(len(AA_NAMES))}
    
    _nameModes = {"long": 0, "medium": 1, "short": 2}  # choices for name length
    _defaultNameMode = "short"  # short name by default

    def __init__(self, aminoAcid):
        """
        Creates an AminoAcid object representing one of the possible Amino Acids.
        aminoAcid can be the name of an amino acid, or an AminoAcid object (in which case a copy is created).
        """
        self._id = None  # id of the amino acid within the name group

        if isinstance(aminoAcid, str):
            if len(aminoAcid) == 1:
                self._id = self.__getIdByName(aminoAcid.upper())  # id from short aminoAcid name
            else:
                self._id = self.__getIdByName(aminoAcid.lower())  # id from other aminoAcid name
        elif isinstance(aminoAcid, AminoAcid):
            self._id = aminoAcid._id  # copy of id
        else:
            raise TypeError("aminoAcid must be a string or an AminoAcid object")

    @staticmethod
    def __getIdByName(name):
        try:
            return AminoAcid._nameDict[name]  # get index of name mode
        except:
            raise ValueError("Could not find amino acid name {}".format(name))

    @staticmethod
    def getAllNames(nameMode=_defaultNameMode):
        try:
            nameIndex = AminoAcid._nameModes[nameMode]  # get index of name mode
        except:
            raise TypeError("nameMode must be 'short', 'medium' or 'long'")

        for aa in AA_NAMES[1:]:  # we exclude the gap (first item)
            yield aa[nameIndex]

    # Representation
    def __repr__(self):
        nameIndex = AminoAcid._nameModes[self._defaultNameMode]
        return AA_NAMES[self._id][nameIndex]  # default name mode

    def __str__(self):
        return self.getName()  # default name mode

    def getName(self, nameMode=_defaultNameMode):
        try:
            nameIndex = AminoAcid._nameModes[nameMode]  # get index of name mode
        except:
            raise TypeError("nameMode must be 'short', 'medium' or 'long'")

        return AA_NAMES[self._id][nameIndex]

    # Comparison
    def __eq__(self, other):
        return self._id == other._id

    def __ne__(self, other):
        return self._id != other._id

    def __gt__(self, other):
        return self._id > other._id

    def __ge__(self, other):
        return self._id >= other._id

    def __lt__(self, other):
        return self._id < other._id

    def __le__(self, other):
        return self._id <= other._id

    def isGap(self):
        return self._id == 0

    # Hashing
    def __hash__(self):
        return hash(self._id)
