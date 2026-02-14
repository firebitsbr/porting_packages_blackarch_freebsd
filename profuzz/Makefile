PORTNAME=	profuzz
DISTVERSION=	9.aa6dded
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple PROFINET fuzzer based on Scapy.
WWW=		https://github.com/HSASec/ProFuzz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/graphviz \
		??/py-gnuplot@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		??/py-pyx@${PY_FLAVOR} \
		??/tcpdump \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
