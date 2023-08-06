"""JSON to python API for Okofen boilers"""
import re
import requests
import json
import datetime
import pyokofen.definitions


class Okofen:
    def __init__(self) -> None:
        """Initialize."""
        self.__raw_datas = None
        self.__datas = {}
        self.__values = {}
        self.__credentials = None
        self.__last_update = datetime.datetime.now() - datetime.timedelta(0, 10)

    async def credentials(self, ip, port, password) -> bool:
        """
        Set credentials & get datas
        Return success/fail status
        """
        # May be faster to put on init, easy trick to allow another source for json datas
        self.__credentials = {
            "ip": ip,
            "port": port,
            "password": password,
            "url": "http://" + ip + ":" + port + "/" + password + "/all?",
        }
        return await self.update()

    def get(self, domain, target):
        """
        Get a value from a target of a domain
        Okofen.get("system", "L_ambient")
        """
        if self.exists(domain) > 0:
            safe_domain = "".join([n for n in domain if not n.isdigit()])
            if isinstance(self.__values[safe_domain], list):
                entity = "".join([n for n in domain if n.isdigit()])
                return self.__values[safe_domain][int(entity) - 1].get(target)
            else:
                return self.__values[safe_domain].get(target)
        return None

    def exists(self, domain) -> int:
        safe_domain = "".join([n for n in domain if not n.isdigit()])
        if safe_domain in self.__values:
            if isinstance(self.__values[safe_domain], list):
                return len(self.__values[safe_domain])
            else:
                return 1
        return 0

    async def update(self) -> bool:
        """
        GET datas from Okofen Boiler
        Then, if OK, call update_datas with them
        Return false if fail to grab datas
        """
        if self.__credentials:
            # 10 seconds between 2 requests /!\ Okofen soft limitation
            if self.__last_update < (
                datetime.datetime.now() - datetime.timedelta(0, 10)
            ):
                response = requests.get(self.__credentials["url"])
                if response.status_code == 200:
                    return await self.update_datas(response.text)

            return False
        # assume data were manually updated
        return await self.update_datas(response.text)

    async def update_datas(self, datas) -> bool:
        """
        Try to convert datas from string to json
        If unable, password may be wrong or datas are not an actual json
        Then call handle_datas
        """
        updated = False
        try:
            if self.__raw_datas != datas:
                self.__datas = json.loads(datas)
                self.__raw_datas = datas
                updated = True
        except ValueError:
            return False
        if updated:
            return await self.handle_datas()
        return True  # datas wern't updated but are still valid

    async def handle_datas(self) -> bool:
        """
        Check every datas on the instance,
        If any of them is a known okofen value, convert them
        """
        try:
            if "system" in self.__datas:
                self.__values["system"] = pyokofen.definitions.System(
                    self.__datas["system"]
                )

            """TODO: weather"""
            # if "weather" in self.__datas:
            #     self.__values["weather"] = pyokofen.definitions.Weather(self.__datas["weather"])

            """TODO: forecast"""
            # if "forecast" in self.__datas:
            #     self.__values["forecast"] = pyokofen.definitions.Forecast(self.__datas["forecast"])

            """TODO: powermeter"""
            # if "power" in self.__datas:
            #     self.__values["power"] = pyokofen.definitions.Power(self.__datas["power"])

            """TODO: stirling"""
            # if "stirling" in self.__datas:
            #     self.__values["stirling"] = pyokofen.definitions.Stirling(self.__datas["stirling"])

            self.__values["hk"] = []
            for i in range(7):
                if "hk" + str(i) in self.__datas:
                    self.__values["hk"].append(
                        pyokofen.definitions.Hk(self.__datas["hk" + str(i)])
                    )

            """TODO: Third party sensors"""
            # self.__values["thirdparty"] = []
            # for i in range(11):
            #     if "thirdparty" + str(i) in self.__datas:
            #         self.__values["thirdparty"].append(
            #             pyokofen.definitions.Thirdparty(self.__datas["thirdparty" + str(i)])
            #         )

            """TODO: accu"""
            # self.__values["pu"] = []
            # for i in range(4):
            #     if "pu" + str(i) in self.__datas:
            #         self.__values["pu"].append(pyokofen.definitions.Pu(self.__datas["pu" + str(i)]))

            self.__values["ww"] = []
            for i in range(4):
                if "ww" + str(i) in self.__datas:
                    self.__values["ww"].append(
                        pyokofen.definitions.Ww(self.__datas["ww" + str(i)])
                    )

            self.__values["sk"] = []
            for i in range(7):
                if "sk" + str(i) in self.__datas:
                    self.__values["sk"].append(
                        pyokofen.definitions.Sk(self.__datas["sk" + str(i)])
                    )

            """TODO: Solar gain"""
            # self.__values["se"] = []
            # for i in range(4):
            #     if "se" + str(i) in self.__datas:
            #         self.__values["se"].append(pyokofen.definitions.Se(self.__datas["se" + str(i)]))

            """TODO: circulation pump"""
            # self.__values["circ"] = []
            # for i in range(4):
            #     if "circ" + str(i) in self.__datas:
            #         self.__values["circ"].append(pyokofen.definitions.Circ(self.__datas["circ" + str(i)]))

            self.__values["pe"] = []
            for i in range(5):
                if "pe" + str(i) in self.__datas:
                    self.__values["pe"].append(
                        pyokofen.definitions.Pe(self.__datas["pe" + str(i)])
                    )

            """TODO: 5k stirling"""
            # self.__values["st5k"] = []
            # for i in range(5):
            #     if "st5k" + str(i) in self.__datas:
            #         self.__values["st5k"].append(pyokofen.definitions.St5k(self.__datas["st5k" + str(i)]))

            return True
        except:
            return False
