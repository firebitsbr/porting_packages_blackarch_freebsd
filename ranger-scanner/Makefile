PORTNAME=	ranger-scanner
DISTVERSION=	149.3aae5dd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to support security professionals to access and interact with remote Microsoft Windows based systems.
WWW=		https://github.com/funkandwagnalls/ranger

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-impacket@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
