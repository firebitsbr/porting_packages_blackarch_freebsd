PORTNAME=	hakku
DISTVERSION=	1.0.r0.g409a11f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple framework that has been made for penetration testing tools.
WWW=		https://github.com/4shadoww/hakkuframework

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/bluez-utils \
		??/dsniff \
		??/ethtool \
		??/ettercap \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		??/sslstrip \
		??/tcpdump \
		??/xterm \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
