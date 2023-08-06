from ..DlxTestClassV5 import scpi_communication_pack
class scpi_UXM_test_cmd(scpi_communication_pack):
    def __init__(self):
        super().__init__()
    def COM_CellApply(self,cell):
        '''cell 1,2,3,4'''
        self._send("BSE:CONFig:LTE:CELL{}:APPLY".format(cell))
    def LTE_BandSet(self,cell,bandnum):
        '''int|str cell 1,2,3,4'''
        self._send("BSE:CONFig:LTE:CELL{}:BAND {}".format(cell,bandnum))
    def LTE_BandWidthSet(self,bandwidth):
        '''int|str cell 1,2,3,4'''
        self._send("BSE:CONFig:LTE:CELL{}:BW BW{}".format(bandwidth))
    def LTE_DuplexSet(self):
        self._send("BSE:CONFig:LTE:CELL1:DUPLex:MODE FDD")