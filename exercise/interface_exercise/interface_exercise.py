from iconservice import *

TAG = 'InterfaceExercise'


class WorkshopInterface(InterfaceScore):
    @interface
    def hello(self):
        pass


class InterfaceExercise(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._db = db
        self.score_address = VarDB("SCORE_ADDRESS", db, value_type=Address)
        self.status = DictDB("STATUS", db, value_type=str)

    def on_install(self, _scoreAddress: Address) -> None:
        super().on_install()
        self.score_address.set(_scoreAddress)

        self.time_recording.put(self.block.height)

        self.status['SCORE_NAME'] = "The First SCORE"
        self.status['INTRODUCTION'] = "The SCORE example for second workshop"
        self.status['APIS'] = str(self.get_api())

    def on_update(self) -> None:
        super().on_update()

    @eventlog(indexed=2)
    def ModifyScoreStatus(self, _scoreName, _introduction):
        pass

    @eventlog
    def IcxReceived(self, _from, _amount):
        pass

    @property
    def time_recording(self):
        return ArrayDB("TIME_RECORDING", self._db, value_type=int)

    @property
    def score_status(self):
        score_name = self.status['SCORE_NAME']
        introduction = self.status['INTRODUCTION']
        apis = self.status['APIS']
        return "SCORE_NAME : " + score_name + "\n" + "INTRODUCTION : " + introduction + "\n" + "APIS : " + apis

    @external(readonly=True)
    def interfaceScoreExercise(self) -> str:
        workshop_score = self.create_interface_score(self.score_address.get(), WorkshopInterface)
        result = workshop_score.hello()
        return result

    @external(readonly=True)
    def getScoreStatus(self) -> str:
        return self.score_status

    @external(readonly=True)
    def getTimeRecording(self) -> str:
        time_recorded = [time_recorded for time_recorded in self.time_recording]
        return str(time_recorded)

    @external
    def modifyScoreStatus(self, _scoreName: str, _introduction: str):
        self.ModifyScoreStatus()
        self.status["SCORE_NAME"] = _scoreName
        self.status["INTRODUCTION"] = _introduction
        self.status["APIS"] = str(self.get_api())
        self.put_time_recording()

    def put_time_recording(self):
        self.time_recording.put(self.block.height)

    @payable
    @external
    def icxSend(self):
        if not self.icx.send(self.msg.sender, self.msg.value):
            revert(f"Resending ICX to msg.sender has failed with self.icx.send")


    @payable
    @external
    def icxTransfer(self):
        try:
            self.icx.transfer(self.msg.sender, self.msg.value)
        except Exception as e:
            revert(f"{e} occurred while resending ICX with self.icx.transfer")

    @payable
    def fallback(self):
        self.IcxReceived(self.msg.sender, self.msg.value)
        pass


