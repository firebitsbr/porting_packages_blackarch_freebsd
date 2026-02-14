PORTNAME=	spraykatz
DISTVERSION=	62.1fb3aa7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Credentials gathering tool automating remote procdump and parse of lsass process.
WWW=		https://github.com/aas-n/spraykatz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pypykatz@${PY_FLAVOR} \
		??/py-wget@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
