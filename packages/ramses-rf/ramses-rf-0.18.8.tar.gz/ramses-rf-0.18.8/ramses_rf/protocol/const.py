#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""RAMSES RF - a RAMSES-II protocol decoder & analyser."""

import re
from types import SimpleNamespace

__dev_mode__ = False
DEV_MODE = __dev_mode__


def slug(string: str) -> str:
    return re.sub(r"[\W_]+", "_", string.lower())


DEV_KLASS = SimpleNamespace(
    DEV="DEV",  # Generic (promotable) device
    #
    HGI="HGI",  # Gateway interface (RF to USB), HGI80
    RFG="RFG",  # RF gateway (RF to ethernet), RFG100
    #
    BDR="BDR",  # Electrical relay
    CTL="CTL",  # Controller
    DHW="DHW",  # DHW sensor
    OUT="OUT",  # External weather sensor
    OTB="OTB",  # OpenTherm bridge
    PRG="PRG",  # Programmer
    THM="THM",  # Thermostat - don't use STA
    # DTS="DTS",  # Thermostat, DTS92(E)
    # HCW="HCW",  # Thermostat, HCW80/82
    # RND="RND",  # Thermostat, TR87RF
    TRV="TRV",  # Thermostatic radiator valve
    UFC="UFC",  # UFH controller
    #
    CO2="CO2",  # HVAC CO2 sensor
    FAN="FAN",  # HVAC fan, 31D[9A]: 20|29|30|37 (some, e.g. 29: only 31D9)
    HUM="HUM",  # HVAC humidity sensor, 1260: 32
    SWI="SWI",  # HVAC switch, 22F[13]: 02|06|20|32|39|42|49|59 (no 20: are both)
    #
    JIM="JIM",  # Jasper Interface Module (EIM?)
    JST="JST",  # Jasper Stat
)


HGI_DEVICE_ID = "18:000730"  # default type and address of HGI, 18:013393
NON_DEVICE_ID = "--:------"
NUL_DEVICE_ID = "63:262142"  # FFFFFE - send here if not bound?


I_, RQ, RP, W_ = " I", "RQ", "RP", " W"

_0001 = "0001"
_0002 = "0002"
_0004 = "0004"
_0005 = "0005"
_0006 = "0006"
_0008 = "0008"
_0009 = "0009"
_000A = "000A"
_000C = "000C"
_000E = "000E"
_0016 = "0016"
_0100 = "0100"
_0150 = "0150"
_01D0 = "01D0"
_01E9 = "01E9"
_0404 = "0404"
_0418 = "0418"
_042F = "042F"
_0B04 = "0B04"
_1030 = "1030"
_1060 = "1060"
_1081 = "1081"
_1090 = "1090"
_1098 = "1098"
_10A0 = "10A0"
_10B0 = "10B0"
_10E0 = "10E0"
_10E1 = "10E1"
_1100 = "1100"
_11F0 = "11F0"
_1260 = "1260"
_1280 = "1280"
_1290 = "1290"
_1298 = "1298"
_12A0 = "12A0"
_12B0 = "12B0"
_12C0 = "12C0"
_12C8 = "12C8"
_12F0 = "12F0"
_1300 = "1300"
_1F09 = "1F09"
_1F41 = "1F41"
_1FC9 = "1FC9"
_1FCA = "1FCA"
_1FD0 = "1FD0"
_1FD4 = "1FD4"
_2249 = "2249"
_22C9 = "22C9"
_22D0 = "22D0"
_22D9 = "22D9"
_22F1 = "22F1"
_22F3 = "22F3"
_2309 = "2309"
_2349 = "2349"
_2389 = "2389"
_2400 = "2400"
_2401 = "2401"
_2410 = "2410"
_2420 = "2420"
_2D49 = "2D49"
_2E04 = "2E04"
_2E10 = "2E10"
_30C9 = "30C9"
_3120 = "3120"
_313F = "313F"
_3150 = "3150"
_31D9 = "31D9"
_31DA = "31DA"
_31E0 = "31E0"
_3200 = "3200"
_3210 = "3210"
_3220 = "3220"
_3221 = "3221"
_3223 = "3223"
_3B00 = "3B00"
_3EF0 = "3EF0"
_3EF1 = "3EF1"
_PUZZ = "7FFF"

DEFAULT_MAX_ZONES = 16 if DEV_MODE else 12
# Evohome: 12 (0-11), older/initial version was 8
# Hometronics: 16 (0-15), or more?
# Sundial RF2: 2 (0-1), usually only one, but ST9520C can do two zones

# ATTR_DEVICE_ID = "device_id"
# ATTR_SENSOR_ID = "sensor_id"
# ATTR_DEV_REGEX_CTL = "controller_id"
# ATTR_DEV_REGEX_DHW = "sensor_id"
# ATTR_DEV_REGEX_HTG = "heater_id"
# ATTR_DEV_REGEX_UFC = "ufh_controller_id"
# ATTR_RELAY_DEVICE_ID = "relay_id"

_DEV_REGEX_ANY = r"^[0-9]{2}:[0-9]{6}$"
_DEV_REGEX_BDR = r"^13:[0-9]{6}$"
_DEV_REGEX_CTL = r"^(01|23):[0-9]{6}$"
_DEV_REGEX_DHW = r"^07:[0-9]{6}$"
_DEV_REGEX_HGI = r"^18:[0-9]{6}$"
_DEV_REGEX_HTG = r"^(10|13):[0-9]{6}$"
_DEV_REGEX_UFC = r"^02:[0-9]{6}$"
_DEV_REGEX_SEN = r"^('01'|'03'|'04'|'12'|'22'|'34'):[0-9]{6}$"

DEVICE_ID_REGEX = SimpleNamespace(
    ANY=_DEV_REGEX_ANY,
    BDR=_DEV_REGEX_BDR,
    CTL=_DEV_REGEX_CTL,
    DHW=_DEV_REGEX_DHW,
    HGI=_DEV_REGEX_HGI,
    HTG=_DEV_REGEX_HTG,
    UFC=_DEV_REGEX_UFC,
    SEN=_DEV_REGEX_SEN,
)

_OUT_DEVICE_TABLE = {
    # Honeywell evohome
    "01": {
        "type": "CTL",
        "name": "Controller",
        "archetype": "ATC928",
    },  # rechargeable
    "02": {
        "type": "UFC",
        "name": "UFH Controller",
        "archetype": "HCE80(R)",
    },
    "03": {
        "type": "STa",
        "name": "Room Sensor/Stat",
        "archetype": "HCW82",  # also: HCF82
    },
    "04": {
        "type": "TRV",
        "name": "Radiator Valve",
        "archetype": "HR92",  # also: HR80
    },  #
    "07": {
        "type": "DHW",
        "name": "DHW Sensor",
        "archetype": "CS92A",
    },
    "10": {
        "type": "OTB",
        "name": "OpenTherm Bridge",
        "archetype": "R8810",
    },  #
    "13": {
        "type": "BDR",
        "name": "Wireless Relay",
        "archetype": "BDR91",  # also: HC60NG?
    },
    "22": {
        "type": "THM",
        "name": "Room Thermostat",
        "archetype": "DTS92(E)",
    },
    "30": {
        "type": "RFG",
        "name": "Internet Gateway",
        "archetype": "-unclear-",  # RFG100, VMS?
    },
    "34": {
        "type": "STA",
        "name": "Round Thermostat",
        "archetype": "T87RF",
    },
    "17": {
        "type": "OUT",
        "name": "Outdoor Sensor",
    },  # TODO: HB85?
    "18": {
        "type": "HGI",
        "name": "Honeywell Gateway",
        "archetype": "HGI80",
    },
    "23": {
        "type": "PRG",
        "name": "Programmer (wired)",
        "archetype": "ST9420C",
    },
    # Honeywell Jasper, HVAC?
    "08": {"type": "JIM", "name": "HVAC?"},  # Jasper equipment interface module
    "31": {"type": "JST", "name": "HVAC?"},  # Jasper Stat TXXX
    # specials
    "63": {"type": "NUL", "name": "Null Device"},
    "--": {"type": "---", "name": "No Device"},
}
# VMS includes Nuaire VMS-23HB33, VMS-23LMH23
# What about Honeywell MT4 actuator?

_OUT_DEVICE_TABLE["00"] = dict(_OUT_DEVICE_TABLE["04"])
_OUT_DEVICE_TABLE["00"]["type"] = "TRv"

_OUT_DEVICE_TABLE["12"] = dict(_OUT_DEVICE_TABLE["22"])
_OUT_DEVICE_TABLE["12"]["type"] = "THm"

# Example of:
#  - Sundial RF2 Pack 3: 23:(ST9420C), 07:(CS92), and 22:(DTS92(E))

# HCW80 has option of being wired (normally wireless)
# ST9420C has battery back-up (as does evohome)

DEVICE_TYPES = {k: v["type"] for k, v in _OUT_DEVICE_TABLE.items()}
DEVICE_LOOKUP = {v: k for k, v in DEVICE_TYPES.items()}
# DEVICE_CLASSES = {v["type"]: v["name"] for _, v in DEVICE_TABLE.items()}

# DEVICE_HAS_BATTERY = tuple(
#     k for k, v in DEVICE_TABLE.items() if v.get("has_battery") is True
# )  # more correctly: is battery-powered (and so won't respond to RQs)
# DEVICE_HAS_ZONE_SENSOR = tuple(
#     k for k, v in DEVICE_TABLE.items() if v.get("has_zone_sensor") is True
# )  # other sensors (e.g. 07:) can't be used as a zone sensor
# DEVICE_IS_ACTUATOR = tuple(
#     k for k, v in DEVICE_TABLE.items() if v.get("is_actuator") is True
# )  # c.f. 000C packet

ATTR_DHW_SENSOR = "hotwater_sensor"
ATTR_DHW_VALVE = "hotwater_valve"
ATTR_DHW_VALVE_HTG = "heating_valve"
ATTR_HTG_CONTROL = "heating_control"  # aka boiler relay, heating appliance

# Domains
DOMAIN_TYPE_MAP = {
    "F8": None,
    "F9": ATTR_DHW_VALVE_HTG,  # DHW Heating Valve
    "FA": ATTR_DHW_VALVE,  # DHW HW Valve (or UFH loop if src.type == "02"?)
    "FB": None,
    "FC": ATTR_HTG_CONTROL,  # "heat_relay": BDR (Boiler, District heating), or OTB
    "FD": "unknown",  # seen with hometronics
    # "FF": "system",  # TODO: remove this, is not a domain
}  # "21": "Ventilation",
DOMAIN_TYPE_LOOKUP = {v: k for k, v in DOMAIN_TYPE_MAP.items() if k != "FF"}

DHW_STATE_MAP = {"00": "off", "01": "on"}
DHW_STATE_LOOKUP = {v: k for k, v in DHW_STATE_MAP.items()}

DTM_LONG_REGEX = re.compile(
    r"\d{4}-[01]\d-[0-3]\d(T| )[0-2]\d:[0-5]\d:[0-5]\d\.\d{6} ?"
)  # 2020-11-30T13:15:00.123456
DTM_TIME_REGEX = re.compile(r"[0-2]\d:[0-5]\d:[0-5]\d\.\d{3} ?")  # 13:15:00.123

# Used by packet structure validators
r = r"(-{3}|\d{3}|\.{3})"  # RSSI, '...' was used by an older version of evofw3
v = r"( I|RP|RQ| W)"  # Verb
d = r"(-{2}:-{6}|\d{2}:\d{6})"  # Device ID
c = r"[0-9A-F]{4}"  # Code
l = r"\d{3}"  # Length # noqa: E741
p = r"([0-9A-F]{2}){1,48}"  # Payload

# DEVICE_ID_REGEX = re.compile(f"^{d}$")
COMMAND_REGEX = re.compile(f"^{v} {r} {d} {d} {d} {c} {l} {p}$")
MESSAGE_REGEX = re.compile(f"^{r} {v} {r} {d} {d} {d} {c} {l} {p}$")

ATTR_DATETIME = "datetime"
ATTR_DEVICES = "devices"
ATTR_HEAT_DEMAND = "heat_demand"
ATTR_HTG_PUMP = "heat_pump_control"  # same as ATTR_HTG_CONTROL, but parameters differ
ATTR_LANGUAGE = "language"
ATTR_NAME = "name"
ATTR_RELAY_DEMAND = "relay_demand"
ATTR_RELAY_FAILSAFE = "relay_failsafe"
ATTR_SETPOINT = "setpoint"
ATTR_STORED_HW = "stored_hotwater"
ATTR_SYSTEM = "system"
ATTR_SYSTEM_MODE = "system_mode"
ATTR_TEMP = "temperature"
ATTR_UFH_CONTROLLERS = "ufh_controllers"
ATTR_WINDOW_OPEN = "window_open"
ATTR_ZONE_ACTUATORS = "zone_actuators"
ATTR_ZONE_IDX = "zone_idx"
ATTR_ZONE_SENSOR = "sensor"
ATTR_ZONE_TYPE = "heating_type"
ATTR_ZONES = "zones"


######################
# Zone Types

ATTR_RAD_VALVE = "radiator_valve"
ATTR_UFH_HTG = "underfloor_heating"
ATTR_ZON_VALVE = "zone_valve"
ATTR_MIX_VALVE = "mixing_valve"
ATTR_ELEC_HEAT = "electric_heat"


# Electric Heat - on/off relay (only)
# Zone Valve    - on/off relay AND requests heat from the boiler, 3150

ZONE_TABLE = {
    "UFH": {"type": "02", "actuator": "UFC", "name": "Underfloor Heating"},
    "RAD": {"type": "04", "actuator": "TRV", "name": "Radiator Valve"},
    "ELE": {"type": "13", "actuator": "BDR", "name": "Electric Heat"},
    "VAL": {"type": "x0", "actuator": "BDR", "name": "Zone Valve"},
    "MIX": {"type": "x1", "actuator": "HM8", "name": "Mixing Valve"},
    "DHW": {"type": "x2", "sensor": "DHW", "name": "Stored DHW"},
}
ZONE_CLASS_MAP = {v["type"]: k for k, v in ZONE_TABLE.items()}
ZONE_CLASS_MAP["00"] = ZONE_CLASS_MAP["04"]

ZONE_TYPE_MAP = {k: slug(v["name"]) for k, v in ZONE_TABLE.items()}
ZONE_TYPE_SLUGS = {slug(v["name"]): k for k, v in ZONE_TABLE.items()}


_OUT_BDR_ROLES = {
    0: ATTR_HTG_CONTROL,
    1: ATTR_HTG_PUMP,
    2: ATTR_DHW_VALVE,
    3: ATTR_DHW_VALVE_HTG,
    4: ATTR_ZON_VALVE,
    5: ATTR_ELEC_HEAT,
}

_0005_ZONE = SimpleNamespace(
    ALL="00",  # All Zone types
    ALL_SENSOR="04",  # All Zone types (with a sensor?)
    RAD="08",  # Radiator zones
    UFH="09",  # UFH zones
    VAL="0A",  # Zone valve zones
    MIX="0B",  # Mix valve zones
    OUT="0C",  # Outdoor weather sensor
    DHW_SENSOR="0D",  # DHW sensor domains
    DHW="0E",  # DHW valve domains
    HTG="0F",  # Heating control domains
    RFG="10",  # RFG gateway
    ELE="11",  # Electrical zones  # TODO: no RP from older evohome
)  # 03, 05, 06, 07: & >11 - no response from an 01:

# RP --- 01:054173 18:006402 --:------ 0005 004 00100000  # before adding RFG100
#  I --- 01:054173 --:------ 01:054173 1FC9 012 0010E004D39D001FC904D39D
#  W --- 30:248208 01:054173 --:------ 1FC9 012 0010E07BC9900012907BC990
#  I --- 01:054173 30:248208 --:------ 1FC9 006 00FFFF04D39D

# RP --- 01:054173 18:006402 --:------ 0005 004 00100100  # after adding RFG100
# RP --- 01:054173 18:006402 --:------ 000C 006 0010007BC990  # 30:082155
# RP --- 01:054173 18:006402 --:------ 0005 004 00100100  # before deleting RFG from CTL
#  I --- 01:054173 --:------ 01:054173 0005 004 00100000  # when the RFG was deleted
# RP --- 01:054173 18:006402 --:------ 0005 004 00100000  # after deleting the RFG

_0005_ZONE_TYPE = {
    _0005_ZONE.ALL: "zone_actuators",
    _0005_ZONE.ALL_SENSOR: "zone_sensor",
    _0005_ZONE.RAD: ATTR_RAD_VALVE,
    _0005_ZONE.UFH: ATTR_UFH_HTG,
    _0005_ZONE.VAL: ATTR_ZON_VALVE,
    _0005_ZONE.MIX: ATTR_MIX_VALVE,
    _0005_ZONE.OUT: "outside_sensor",
    _0005_ZONE.DHW_SENSOR: ATTR_DHW_SENSOR,
    _0005_ZONE.DHW: ATTR_DHW_VALVE,  # can be 0, 1 or 2 (i.e. 1,1,0,...) of them
    _0005_ZONE.HTG: ATTR_HTG_CONTROL,
    _0005_ZONE.RFG: "remote_gateway",
    _0005_ZONE.ELE: ATTR_ELEC_HEAT,
}

# RP|zone_devices | 000E0... || {'domain_id': 'FA', 'device_class': 'dhw_actuator', 'devices': ['13:081807']}  # noqa
# RP|zone_devices | 010E0... || {'domain_id': 'FA', 'device_class': 'dhw_actuator', 'devices': ['13:106039']}  # noqa

_000C_DEVICE = _0005_ZONE
_000C_DEVICE_TYPE = {
    _000C_DEVICE.ALL: "zone_actuators",
    # "01": None,
    # "02": None,
    _000C_DEVICE.ALL_SENSOR: ATTR_ZONE_SENSOR,  # 03:, 04:, 34: (if is 01:, will == [], as if no sensor)
    _000C_DEVICE.RAD: "rad_actuators",
    _000C_DEVICE.UFH: "ufh_actuators",
    _000C_DEVICE.VAL: "val_actuators",
    _000C_DEVICE.MIX: "mix_actuators",
    # "0C": None,  # RFG RQs this
    _000C_DEVICE.DHW_SENSOR: ATTR_DHW_SENSOR,  # FA, z_idx 0 only
    _000C_DEVICE.DHW: ATTR_DHW_VALVE,  # FA, could be F9, ATTR_DHW_VALVE_HTG
    _000C_DEVICE.HTG: ATTR_HTG_CONTROL,  # FC, z_idx 0 only
    _000C_DEVICE.RFG: "rfg_gateway",
    _000C_DEVICE.ELE: "ele_actuators",
}

# Used by 0418/system_fault parser
_0418_DEVICE_CLASS = {
    "00": "controller",
    "01": "sensor",
    "02": "setpoint",
    "04": "actuator",  # if domain is FC, then "boiler_relay"
    "05": "dhw_sensor",  # not ATTR_DHW_SENSOR
    "06": "remote_gateway",
}
_0418_FAULT_STATE = {
    "00": "fault",
    "40": "restore",
    "C0": "unknown_c0",  # C0s do not appear in the evohome UI
}
_0418_FAULT_TYPE = {
    "01": "system_fault",
    "03": "mains_low",
    "04": "battery_low",
    "05": "battery_error",  # actually: 'evotouch_battery_error'
    "06": "comms_fault",
    "07": "sensor_fault",  # seen with zone sensor
    "0A": "sensor_error",
    "??": "bad_value",
}

SystemType = SimpleNamespace(
    CHRONOTHERM="chronotherm",
    EVOHOME="evohome",
    HOMETRONICS="hometronics",
    PROGRAMMER="programmer",
    SUNDIAL="sundial",
    GENERIC="generic",
)


class AttrDict(dict):
    # NOTE: 'advanced_override' in ZONE_MODE == False

    def __readonly__(self, *args, **kwargs):
        raise RuntimeError("Cannot modify ReadOnlyDict")

    __delitem__ = __readonly__
    __setitem__ = __readonly__
    clear = __readonly__
    pop = __readonly__
    popitem = __readonly__
    setdefault = __readonly__
    update = __readonly__

    del __readonly__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._reverse = {v: k for k, v in args[0].items()}

    def __getitem__(self, key):
        if key in self._reverse:
            return self._reverse.__getitem__(key)
        return super().__getitem__(key)

    def __getattr__(self, name):
        if name in self.__slots__:
            if name in self._reverse:
                return self._reverse[name]
            return self[name[1:]]
        return self.__getattribute__(name)

    def _hex(self, key) -> str:
        """Return the key (2-byte hex string) of the two-way dict."""
        if key in self:
            return key
        if key in self._reverse:
            return self._reverse[key]
        raise KeyError(key)

    def _str(self, key) -> str:
        """Return the value (string) of the two-way dict."""
        if key in self:
            return self[key]
        if key in self._reverse:
            return key
        raise KeyError(key)


_ZONE_MODES = {
    "00": "follow_schedule",
    "01": "advanced_override",  # until the next scheduled setpoint
    "02": "permanent_override",  # indefinitely
    "03": "countdown_override",  # for a number of minutes (duration, max 1,215?)
    "04": "temporary_override",  # until a given date/time (until)
}


class ZoneModes((AttrDict)):
    __slots__ = [f"_{k}" for k in _ZONE_MODES] + list(_ZONE_MODES.values())


ZONE_MODE = ZoneModes(_ZONE_MODES)

_SYSTEM_MODES = {
    "00": "auto",  # .          indef only
    "01": "heat_off",  # .      indef only
    "02": "eco_boost",  # .     indef, or 24h: is either Eco, or Boost
    "03": "away",  # .          indef, or 99d (0d = end of today, 00:00)
    "04": "day_off",  # .       indef, or 99d (rounded down to 00:00 bt CTL)
    "05": "day_off_eco",  # .   indef, or 99d: set to Eco when DayOff ends
    "06": "auto_with_reset",  # indef only
    "07": "custom",  # .        indef, or 99d
}


class SystemModes((AttrDict)):
    __slots__ = [f"_{k}" for k in _SYSTEM_MODES] + list(_SYSTEM_MODES.values())


SYSTEM_MODE = SystemModes(_SYSTEM_MODES)

# used by 22Fx parser, and FanSwitch devices
BOOST_TIMER = "boost_timer"  # minutes, e.g. 10, 20, 30 minutes
HEATER_MODE = "heater_mode"  # e.g. auto, off
HEATER_MODES = {9: "off", 10: "auto"}  # TODO:

FAN_MODE = "fan_mode"  # e.g. low. high
FAN_MODES = {
    0: "standby",
    1: "auto",
    2: "low",
    3: "medium",
    4: "high",  # a.k.a. boost if timer on
}
FAN_RATE = "fan_rate"  # percentage, 0.0 - 1.0
