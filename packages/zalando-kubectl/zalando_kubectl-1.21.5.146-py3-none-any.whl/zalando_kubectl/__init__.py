# This is replaced during release process.
__version_suffix__ = '146'

APP_NAME = "zalando-kubectl"

KUBECTL_VERSION = "v1.21.5"
KUBECTL_SHA512 = {
    "linux": "0bd3f5a4141bf3aaf8045a9ec302561bb70f6b9a7d988bc617370620d0dbadef947e1c8855cda0347d1dd1534332ee17a950cac5a8fcb78f2c3e38c62058abde",
    "darwin": "4d14904d69e9f50f6c44256b4942d6623e2233e45601fb17b2b58a7f6601adacd27add292f64dbe8297f81e27052b14f83f24ef4b2ba1c84344f0169d7aa24b8",
}
STERN_VERSION = "1.19.0"
STERN_SHA256 = {
    "linux": "fcd71d777b6e998c6a4e97ba7c9c9bb34a105db1eb51637371782a0a4de3f0cd",
    "darwin": "18a42e08c5f995ffabb6100f3a57fe3c2e2b074ec14356912667eeeca950e849",
}
KUBELOGIN_VERSION = "v1.25.1"
KUBELOGIN_SHA256 = {
    "linux": "d265388f27a4d7ceaa7cc1a7ed6c0297cc5d04aa7022325a4554e46a6f56cc3c",
    "darwin": "4d26778eddf61f162724191d5d8db5ff94e9f721fb9f746b6e8db06193cbbc39",
}

APP_VERSION = KUBECTL_VERSION + "." + __version_suffix__
