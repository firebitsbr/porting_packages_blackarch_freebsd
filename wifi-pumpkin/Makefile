PORTNAME=	wifi-pumpkin
DISTVERSION=	v1.1.7.r2.g344a475
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Framework for Rogue Wi-Fi Access Point Attack.
WWW=		https://github.com/P0cL4bs/wifipumpkin3

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/dhcp \
		??/networkmanager \
		??/py-aiofiles@${PY_FLAVOR} \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-beautifultable@${PY_FLAVOR} \
		??/py-bs4@${PY_FLAVOR} \
		??/py-coverage@${PY_FLAVOR} \
		??/py-dhcplib@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-flask-restful@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-isc_dhcp_leases@${PY_FLAVOR} \
		??/py-loguru@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-ping3@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pyqt5-sip@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		??/py-scahttp@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		??/py-urwid@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/responder \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
