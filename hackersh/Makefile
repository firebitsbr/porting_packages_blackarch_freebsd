PORTNAME=	hackersh
DISTVERSION=	0.2.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A shell for with Pythonect-like syntax, including wrappers for commonly used security tools.
WWW=		http://www.hackersh.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-netaddr@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/pythonect \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
