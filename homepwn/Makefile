PORTNAME=	homepwn
DISTVERSION=	31.0803981
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Swiss Army Knife for Pentesting of IoT Devices.
WWW=		https://github.com/ElevenPaths/HomePWN

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bluez \
		??/bluez-tools \
		??/cups \
		??/dnsmasq \
		??/glib2 \
		??/hostapd \
		??/libxml2 \
		??/pcsc-tools \
		??/py-dbus@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/screen \
		??/tcpdump \
		??/wireshark-cli \
		??/wondershaper \
		lang/python \
		net/libpcap \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
