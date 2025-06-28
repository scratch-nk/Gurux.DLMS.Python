import logging

from gurux_dlms import GXDLMSClient
from gurux_dlms.enums import InterfaceType, Authentication
from gurux_net import GXNet, NetworkType
from gurux_common.enums import TraceLevel

from GXDLMSReader import GXDLMSReader


def main():
    host = "[fe80::1]"  # Replace with the meter's IPv6 address
    port = 4059

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.info("Create DLMS client with High authentication")
    client = GXDLMSClient(
        useLogicalNameReferencing=True,
        clientAddress=16,
        serverAddress=1,
        forAuthentication=Authentication.HIGH,
        password="secret",  # Replace with your password
        interfaceType=InterfaceType.WRAPPER,
    )

    logging.info("Create TCP/IPv6 connection to %s:%s", host, port)
    media = GXNet(NetworkType.TCP, host, port)
    reader = GXDLMSReader(client, media, TraceLevel.INFO, None)

    try:
        logging.info("Open connection")
        media.open()
        logging.info("Initialize DLMS handshake")
        reader.initializeConnection()
        logging.info("Connection established")
    finally:
        logging.info("Close connection")
        reader.close()


if __name__ == "__main__":
    main()
