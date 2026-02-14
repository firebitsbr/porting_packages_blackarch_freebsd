PORTNAME=	isf
DISTVERSION=	68.5228865
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An exploitation framework based on Python.
WWW=		https://github.com/dark-lbp/isf

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-pysnmp@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
