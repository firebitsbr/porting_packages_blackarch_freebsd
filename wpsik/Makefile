PORTNAME=	wpsik
DISTVERSION=	8.8d3856b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	WPS scan and pwn tool.
WWW=		https://github.com/0x90/wpsik

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-coloredlogs@${PY_FLAVOR} \
		??/py-impacket@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-ldapdomaindump@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pcapy@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pyric@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
