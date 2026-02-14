PORTNAME=	mana
DISTVERSION=	78.438d1fe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A toolkit for rogue access point (evilAP) attacks first presented at Defcon 22.
WWW=		https://github.com/sensepost/mana

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/apache \
		??/asleap \
		??/dsniff \
		??/iptables \
		??/libnl1 \
		??/macchanger \
		??/metasploit \
		??/procps \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-pcapy@${PY_FLAVOR} \
		??/sslsplit \
		??/stunnel \
		??/tinyproxy \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
