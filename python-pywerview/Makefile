PORTNAME=	python-pywerview
DISTVERSION=	0.7.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python port of PowerSploits PowerView.
WWW=		https://pypi.org/project/pywerview/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-gssapi@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
