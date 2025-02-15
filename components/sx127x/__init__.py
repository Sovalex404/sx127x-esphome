from esphome import automation, pins
import esphome.codegen as cg
from esphome.components import spi
import esphome.config_validation as cv
from esphome.const import CONF_DATA, CONF_FREQUENCY, CONF_ID

MULTI_CONF = True
CODEOWNERS = ["@swoboda1337"]
DEPENDENCIES = ["spi"]

CONF_BITRATE = "bitrate"
CONF_BITSYNC = "bitsync"
CONF_CRC_ENABLE = "crc_enable"
CONF_DIO0_PIN = "dio0_pin"
CONF_FSK_FDEV = "fsk_fdev"
CONF_FSK_RAMP = "fsk_ramp"
CONF_MODULATION = "modulation"
CONF_ON_PACKET = "on_packet"
CONF_PA_PIN = "pa_pin"
CONF_PA_POWER = "pa_power"
CONF_PAYLOAD_LENGTH = "payload_length"
CONF_PREAMBLE_ERRORS = "preamble_errors"
CONF_PREAMBLE_POLARITY = "preamble_polarity"
CONF_PREAMBLE_SIZE = "preamble_size"
CONF_RST_PIN = "rst_pin"
CONF_RX_BANDWIDTH = "rx_bandwidth"
CONF_RX_FLOOR = "rx_floor"
CONF_RX_START = "rx_start"
CONF_SHAPING = "shaping"
CONF_SYNC_VALUE = "sync_value"

sx127x_ns = cg.esphome_ns.namespace("sx127x")
SX127x = sx127x_ns.class_("SX127x", cg.Component, spi.SPIDevice)
SX127xOpMode = sx127x_ns.enum("SX127xOpMode")
SX127xRxBw = sx127x_ns.enum("SX127xRxBw")
SX127xPaConfig = sx127x_ns.enum("SX127xPaConfig")
SX127xPaRamp = sx127x_ns.enum("SX127xPaRamp")

PA_PIN = {
    "RFO": SX127xPaConfig.PA_PIN_RFO,
    "BOOST": SX127xPaConfig.PA_PIN_BOOST,
}

SHAPING = {
    "CUTOFF_BR_X_2": SX127xPaRamp.CUTOFF_BR_X_2,
    "CUTOFF_BR_X_1": SX127xPaRamp.CUTOFF_BR_X_1,
    "GAUSSIAN_BT_0_3": SX127xPaRamp.GAUSSIAN_BT_0_3,
    "GAUSSIAN_BT_0_5": SX127xPaRamp.GAUSSIAN_BT_0_5,
    "GAUSSIAN_BT_1_0": SX127xPaRamp.GAUSSIAN_BT_1_0,
    "NONE": SX127xPaRamp.SHAPING_NONE,
}

RAMP = {
    "10us": SX127xPaRamp.PA_RAMP_10,
    "12us": SX127xPaRamp.PA_RAMP_12,
    "15us": SX127xPaRamp.PA_RAMP_15,
    "20us": SX127xPaRamp.PA_RAMP_20,
    "25us": SX127xPaRamp.PA_RAMP_25,
    "31us": SX127xPaRamp.PA_RAMP_31,
    "40us": SX127xPaRamp.PA_RAMP_40,
    "50us": SX127xPaRamp.PA_RAMP_50,
    "62us": SX127xPaRamp.PA_RAMP_62,
    "100us": SX127xPaRamp.PA_RAMP_100,
    "125us": SX127xPaRamp.PA_RAMP_125,
    "250us": SX127xPaRamp.PA_RAMP_250,
    "500us": SX127xPaRamp.PA_RAMP_500,
    "1000us": SX127xPaRamp.PA_RAMP_1000,
    "2000us": SX127xPaRamp.PA_RAMP_2000,
    "3400us": SX127xPaRamp.PA_RAMP_3400,
}

MOD = {
    "LORA": SX127xOpMode.MOD_LORA,
    "FSK": SX127xOpMode.MOD_FSK,
    "OOK": SX127xOpMode.MOD_OOK,
}

RX_BW = {
    "2_6kHz": SX127xRxBw.RX_BW_2_6,
    "3_1kHz": SX127xRxBw.RX_BW_3_1,
    "3_9kHz": SX127xRxBw.RX_BW_3_9,
    "5_2kHz": SX127xRxBw.RX_BW_5_2,
    "6_3kHz": SX127xRxBw.RX_BW_6_3,
    "7_8kHz": SX127xRxBw.RX_BW_7_8,
    "10_4kHz": SX127xRxBw.RX_BW_10_4,
    "12_5kHz": SX127xRxBw.RX_BW_12_5,
    "15_6kHz": SX127xRxBw.RX_BW_15_6,
    "20_8kHz": SX127xRxBw.RX_BW_20_8,
    "25_0kHz": SX127xRxBw.RX_BW_25_0,
    "31_3kHz": SX127xRxBw.RX_BW_31_3,
    "41_7kHz": SX127xRxBw.RX_BW_41_7,
    "50_0kHz": SX127xRxBw.RX_BW_50_0,
    "62_5kHz": SX127xRxBw.RX_BW_62_5,
    "83_3kHz": SX127xRxBw.RX_BW_83_3,
    "100_0kHz": SX127xRxBw.RX_BW_100_0,
    "125_0kHz": SX127xRxBw.RX_BW_125_0,
    "166_7kHz": SX127xRxBw.RX_BW_166_7,
    "200_0kHz": SX127xRxBw.RX_BW_200_0,
    "250_0kHz": SX127xRxBw.RX_BW_250_0,
}

SendPacketAction = sx127x_ns.class_(
    "SendPacketAction", automation.Action, cg.Parented.template(SX127x)
)
SetModeTxAction = sx127x_ns.class_("SetModeTxAction", automation.Action)
SetModeRxAction = sx127x_ns.class_("SetModeRxAction", automation.Action)
SetModeStandbyAction = sx127x_ns.class_("SetModeStandbyAction", automation.Action)


def validate_raw_data(value):
    if isinstance(value, str):
        return value.encode("utf-8")
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return cv.Schema([cv.hex_uint8_t])(value)
    raise cv.Invalid(
        "data must either be a string wrapped in quotes or a list of bytes"
    )


def validate_config(config):
    if config[CONF_PAYLOAD_LENGTH] > 0 and CONF_DIO0_PIN not in config:
        raise cv.Invalid("Cannot use packet mode without dio0_pin")
    if config[CONF_PAYLOAD_LENGTH] > 0 and config[CONF_BITRATE] == 0:
        raise cv.Invalid("Cannot use packet mode without setting bitrate")
    if config[CONF_PA_PIN] == "RFO" and config[CONF_PA_POWER] > 15:
        raise cv.Invalid("PA power must be <= 15 dbm when using the RFO pin")
    if config[CONF_PA_PIN] == "BOOST" and config[CONF_PA_POWER] < 2:
        raise cv.Invalid("PA power must be >= 2 dbm when using the BOOST pin")
    if CONF_BITSYNC in config and config[CONF_BITSYNC] and CONF_BITRATE not in config:
        raise cv.Invalid("Bitsync is true but bitrate is not configured")
    if CONF_BITRATE in config and CONF_BITSYNC not in config:
        raise cv.Invalid(
            "Bitrate is configured but not bitsync; add 'bitsync: true' for original functionality"
        )
    return config


CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SX127x),
            cv.Optional(CONF_BITRATE): cv.int_range(min=500, max=300000),
            cv.Optional(CONF_BITSYNC): cv.boolean,
            cv.Optional(CONF_CRC_ENABLE, default=False): cv.boolean,
            cv.Optional(CONF_DIO0_PIN): pins.internal_gpio_input_pin_schema,
            cv.Required(CONF_FREQUENCY): cv.int_range(min=137000000, max=1020000000),
            cv.Optional(CONF_FSK_FDEV, default=5000): cv.int_range(min=0, max=100000),
            cv.Optional(CONF_FSK_RAMP, default="40us"): cv.enum(RAMP),
            cv.Required(CONF_MODULATION): cv.enum(MOD),
            cv.Optional(CONF_ON_PACKET): automation.validate_automation(single=True),
            cv.Optional(CONF_PA_PIN, default="BOOST"): cv.enum(PA_PIN),
            cv.Optional(CONF_PA_POWER, default=17): cv.int_range(min=0, max=17),
            cv.Optional(CONF_PAYLOAD_LENGTH, default=0): cv.int_range(min=0, max=64),
            cv.Optional(CONF_PREAMBLE_ERRORS, default=0): cv.int_range(min=0, max=31),
            cv.Optional(CONF_PREAMBLE_POLARITY, default=0xAA): cv.All(
                cv.hex_int, cv.one_of(0xAA, 0x55)
            ),
            cv.Optional(CONF_PREAMBLE_SIZE, default=0): cv.int_range(min=0, max=7),
            cv.Required(CONF_RST_PIN): pins.internal_gpio_output_pin_schema,
            cv.Optional(CONF_RX_BANDWIDTH, default="50_0kHz"): cv.enum(RX_BW),
            cv.Optional(CONF_RX_FLOOR, default=-94): cv.float_range(min=-128, max=-1),
            cv.Optional(CONF_RX_START, default=True): cv.boolean,
            cv.Optional(CONF_SHAPING, default="NONE"): cv.enum(SHAPING),
            cv.Optional(CONF_SYNC_VALUE, default=[]): cv.ensure_list(cv.hex_uint8_t),
        },
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(spi.spi_device_schema(True, 8e6, "mode0")),
    validate_config,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await spi.register_spi_device(var, config)
    if CONF_ON_PACKET in config:
        await automation.build_automation(
            var.get_packet_trigger(),
            [(cg.std_vector.template(cg.uint8), "x")],
            config[CONF_ON_PACKET],
        )
    if CONF_DIO0_PIN in config:
        dio0_pin = await cg.gpio_pin_expression(config[CONF_DIO0_PIN])
        cg.add(var.set_dio0_pin(dio0_pin))
    rst_pin = await cg.gpio_pin_expression(config[CONF_RST_PIN])
    cg.add(var.set_rst_pin(rst_pin))
    cg.add(var.set_frequency(config[CONF_FREQUENCY]))
    cg.add(var.set_modulation(config[CONF_MODULATION]))
    cg.add(var.set_shaping(config[CONF_SHAPING]))
    if CONF_BITRATE in config:
        cg.add(var.set_bitrate(config[CONF_BITRATE]))
    else:
        cg.add(var.set_bitrate(4800))
    if CONF_BITSYNC in config:
        cg.add(var.set_bitsync(config[CONF_BITSYNC]))
    else:
        cg.add(var.set_bitsync(False))
    cg.add(var.set_crc_enable(config[CONF_CRC_ENABLE]))
    cg.add(var.set_payload_length(config[CONF_PAYLOAD_LENGTH]))
    cg.add(var.set_preamble_size(config[CONF_PREAMBLE_SIZE]))
    cg.add(var.set_preamble_polarity(config[CONF_PREAMBLE_POLARITY]))
    cg.add(var.set_preamble_errors(config[CONF_PREAMBLE_ERRORS]))
    cg.add(var.set_sync_value(config[CONF_SYNC_VALUE]))
    cg.add(var.set_rx_floor(config[CONF_RX_FLOOR]))
    cg.add(var.set_rx_start(config[CONF_RX_START]))
    cg.add(var.set_rx_bandwidth(config[CONF_RX_BANDWIDTH]))
    cg.add(var.set_pa_pin(config[CONF_PA_PIN]))
    cg.add(var.set_pa_power(config[CONF_PA_POWER]))
    cg.add(var.set_fsk_fdev(config[CONF_FSK_FDEV]))
    cg.add(var.set_fsk_ramp(config[CONF_FSK_RAMP]))


SET_MODE_ACTION_SCHEMA = automation.maybe_simple_id(
    {
        cv.GenerateID(): cv.use_id(SX127x),
    }
)


@automation.register_action(
    "sx127x.set_mode_tx", SetModeTxAction, SET_MODE_ACTION_SCHEMA
)
@automation.register_action(
    "sx127x.set_mode_rx", SetModeRxAction, SET_MODE_ACTION_SCHEMA
)
@automation.register_action(
    "sx127x.set_mode_standby", SetModeStandbyAction, SET_MODE_ACTION_SCHEMA
)
async def set_mode_action_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    return var


SEND_PACKET_ACTION_SCHEMA = cv.maybe_simple_value(
    {
        cv.GenerateID(): cv.use_id(SX127x),
        cv.Required(CONF_DATA): cv.templatable(validate_raw_data),
    },
    key=CONF_DATA,
)


@automation.register_action(
    "sx127x.send_packet", SendPacketAction, SEND_PACKET_ACTION_SCHEMA
)
async def send_packet_action_to_code(config, action_id, template_arg, args):
    var = cg.new_Pvariable(action_id, template_arg)
    await cg.register_parented(var, config[CONF_ID])
    data = config[CONF_DATA]
    if isinstance(data, bytes):
        data = list(data)
    if cg.is_template(data):
        templ = await cg.templatable(data, args, cg.std_vector.template(cg.uint8))
        cg.add(var.set_data_template(templ))
    else:
        cg.add(var.set_data_static(data))
    return var
