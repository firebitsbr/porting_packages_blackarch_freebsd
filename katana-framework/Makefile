PORTNAME=	katana-framework
DISTVERSION=	1.0.0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A framework that seekss to unite general auditing tools, which are general pentesting tools (Network,Web,Desktop and others).
WWW=		https://github.com/PowerScript/KatanaFramework

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/ettercap \
		??/hostapd \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-isc_dhcp_leases@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/xterm \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR} \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
